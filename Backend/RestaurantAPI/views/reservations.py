from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Restaurant, Reservation
from ..serializers import ReservationSerializer
from Yummo.utilityfunctions import  AuthenticatedMerchantViewClass, IsMerchant, IsCustomer, AuthenticatedViewClass, isCustomerGroup, isMerchantGroup
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class ReservationsView(AuthenticatedViewClass):
    
    @swagger_auto_schema(tags=['reservations'], responses={200: ReservationSerializer(many=True), 400: "Bad Request", 403: "Forbidden", 404: "Not Found"})
    def get(self, request, resID):
        restaurant = get_object_or_404(Restaurant, pk=resID, merchant=request.user)
        reservations = restaurant.reservations
        serialized_reservations = ReservationSerializer(reservations, many=True)
        return Response(serialized_reservations.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(tags=['reservations'], 
                         request_body=ReservationSerializer,
                         responses={200: ReservationSerializer, 400: "Bad Request", 403: "Forbidden", 404: "Not Found"})
    def post(self, request, resID):
        data = request.data.copy()
        data['restaurant'] = resID
        data['customer'] = request.user.id
        serialized_reservation = ReservationSerializer(data=data)
        serialized_reservation.is_valid(raise_exception=True)
        serialized_reservation.save()
        return Response(serialized_reservation.data, status=status.HTTP_201_CREATED)
    
    # GET method requires Merchants access
    # POST method requires Customers access
    def get_permissions(self):
        permission_classes = super().permission_classes
        if self.request.method == 'GET':
            permission_classes.append(IsMerchant)
        elif self.request.method == 'POST':
            permission_classes.append(IsCustomer)
        return [permission() for permission in permission_classes]


class SingleReservationView(AuthenticatedViewClass):
    
    @swagger_auto_schema(tags=['reservations'], responses={200: ReservationSerializer, 400: "Bad Request", 403: "Forbidden", 404: "Not Found"})
    def get(self, request, resID, reservID):
        if isCustomerGroup(request):
            reservation = get_object_or_404(Reservation, pk=reservID, customer=request.user)
        elif isMerchantGroup(request):
            restaurant = get_object_or_404(Restaurant, pk=resID, merchant=request.user) #check that this restaurant belong to this merchant
            reservation = get_object_or_404(restaurant.reservations, pk=reservID) #find the reservation from the restaurant's list of reservations
        
        serialized_reservation = ReservationSerializer(reservation)
        return Response(serialized_reservation.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(tags=['reservations'], 
                         request_body=ReservationSerializer,
                         responses={201: ReservationSerializer, 400: "Bad Request", 403: "Forbidden", 404: "Not Found"})
    def put(self, request, resID, reservID):
        reservation = get_object_or_404(Reservation, pk=reservID, customer=request.user)
        data = request.data.copy()
        #Only reservation time and pax can be changed
        data['restaurant'] = reservation.restaurant.resID
        data['customer'] = reservation.customer.id
        serialized_reservation = ReservationSerializer(reservation, data=data, partial=True)
        serialized_reservation.is_valid(raise_exception=True)
        serialized_reservation.save()
        return Response(serialized_reservation.data,status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(tags=['reservations'], responses={200: 'OK', 400: "Bad Request", 403: "Forbidden", 404: "Not Found"})
    def delete(self, request, resID, reservID):
        reservation = get_object_or_404(Reservation, pk=reservID, customer=request.user) #ensure that the reservation is under the correct Customer
        reservation.delete()
        return Response({"message":"Reservation deleted"}, status=status.HTTP_200_OK)
    
    # GET method requires Customers, Merchants access
    # PUT, DELETE method requires Customers access
    def get_permissions(self):
        permission_classes = super().permission_classes
        if self.request.method != 'GET':
            permission_classes.append(IsCustomer)
        return [permission() for permission in permission_classes]


    