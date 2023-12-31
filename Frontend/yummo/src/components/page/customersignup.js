import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import axios from "axios";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import usePasswordToggle from "../../hooks/usePasswordToggle";
import "./customersignup.css";

function Customer_Signup() {
  const [username, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const [PasswordInputType, ToggleIcon] = usePasswordToggle();

  const url = "http://localhost:8000/auth/users/";

  const user = {
    username: username,
    password: password,
    email: email,
    group_name: "Customers",
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post(url, user);
      alert("Account created successfully!");
      console.log(response.data);
      navigate("/");
    } catch (error) {
      console.error(error);
      alert("Error! Try Again.");
    }
  };

  const handleUserNameChange = (event) => {
    setUserName(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };
  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  return (
    <div className="wholepg">
      <div className="navbar-signup">
        <nav>
          <img
            src="/yummo_logo.png"
            alt="Yummo logo"
            width="8%"
            style={{ paddingLeft: "3rem" }}
          />
        </nav>
      </div>

      <div className="below-nav-bar">
        <div className="form-container">
          <div className="signup-text">
            <h2>SignUp</h2>
          </div>
          <form className="customer-signup-personal-info-form">
            <div className="signup-txt-field">
              <label>
                Username:<br></br>
                <input
                  type="text"
                  onChange={handleUserNameChange}
                  placeholder="UserName"
                />
              </label>
            </div>

            <div className="signup-txt-field">
              <label>
                Email:<br></br>
                <input
                  type="text"
                  onChange={handleEmailChange}
                  value={email}
                  placeholder="Email"
                />
                <br></br>
              </label>
            </div>
            {/*
                    <div className="txt-field">
                            <label>
                                Password:<br></br>
                                <input
                                type="text"
                                onChange={handlePasswordChange}
                                placeholder="Password" />
                            </label>
                            <span className="password-toogle-icon">
                                        {ToggleIcon}
                            </span>
                    </div> */}
            <div className="signup-txt-field">
              <div className="input-group-prepend">
                <span className="input-group-text">
                  <FontAwesomeIcon icon="lock" />
                </span>
              </div>
              <label className="pass-text">
                Password:<br></br>
                <input
                  className="form-control"
                  placeholder="Create password"
                  type={PasswordInputType}
                  value={password}
                  // onFocus={() => setPasswordFocused(true)}
                  onChange={handlePasswordChange}
                />
              </label>
              <span className="password-toogle-icon">{ToggleIcon}</span>
            </div>

            <div className="buttons-container">
              <button onClick={handleSubmit}>Submit</button>
            </div>
          </form>
        </div>
      </div>

      <div className="img-container">
        <img src="/mediacust_signup.png" alt="signup_img" width="35%" />
      </div>
    </div>
  );
}

export default Customer_Signup;