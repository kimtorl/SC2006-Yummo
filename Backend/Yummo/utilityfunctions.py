from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, BasePermission

#Put your utility functions here
MERCHANT = "Merchants"
CUSTOMER = "Customers"

OPERATION_DESCRIPTION_CUSTOMER = "\n\nAuthorization: `Customer`"
OPERATION_DESCRIPTION_MERCHANT = "\n\nAuthorization: `Merchant`"
OPERATION_DESCRIPTION_ALLOWANY = "\n\nAuthorization: `AllowAny`"

# Create permission class to check for customer
class IsCustomer(BasePermission):
    message = "Only Customers can access this function"

    def has_permission(self, request, view):
        return request.user.groups.filter(name=CUSTOMER).exists()
    
# Create permission class to check for merchant   
class IsMerchant(BasePermission):
    message = "Only Merchants can access this function"

    def has_permission(self, request, view):
        return request.user.groups.filter(name=MERCHANT).exists()
    

# Create base view class which require authentication
class AuthenticatedViewClass(APIView):
    permission_classes = [IsAuthenticated]

class AuthenticatedCustomerViewClass(AuthenticatedViewClass):
    permission_classes = AuthenticatedViewClass.permission_classes + [IsCustomer]

class AuthenticatedMerchantViewClass(AuthenticatedViewClass):
    permission_classes = AuthenticatedViewClass.permission_classes + [IsMerchant]


# Create Exception class that provides an exception message and a status code
# class ExceptionWithResponse(Exception):
#     def __init__(self, message: str, status_code: status):
#         super().__init__(message)
#         self.status_code = status_code

#     def get_status_code(self) -> status:
#         return self.status_code
    
    
#check if User is a Merchant
def isMerchantGroup(request) -> bool:
    return request.user.groups.filter(name=MERCHANT).exists()

# def is_merchant_or_403(request) -> bool:
#     if not isMerchantGroup(request):
#         raise ExceptionWithResponse("Only Merchants can access this function", status.HTTP_403_FORBIDDEN)
#     return True

#check if User is a Customer
def isCustomerGroup(request) -> bool:
    return request.user.groups.filter(name=CUSTOMER).exists()

# def is_customer_or_403(request) -> bool:
#     if not isCustomerGroup(request):
#         raise ExceptionWithResponse("Only Customers can access this function", status.HTTP_403_FORBIDDEN)
#     return True
