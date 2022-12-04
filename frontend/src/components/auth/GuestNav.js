/* eslint-disable prettier/prettier */
import React, { useContext } from 'react';
import Button from '../forum/Button';
import AuthContext from '../../context/auth/AuthContext';
import './style.css';
import { showModal } from '../../context/auth/AuthActions';

const GuestNav = () => {
  const { dispatch } = useContext(AuthContext);

  const handleLoginOnClick = () => {
    dispatch(showModal('LOGIN'), {});
  };
  const handleRegisterOnClick = () => {
    dispatch(showModal('REGISTER'), {});
  };

  return (
    <div className="guestMenu">
      <p
        className="btn-sign-in"
        style={{ opacity: 0.6}}
        onClick={handleLoginOnClick}
      >
        Login
      </p>

      <br />

      <p
        className="btn-register"
        style={{ opacity: 0.6}}
        onClick={handleRegisterOnClick}
      >
        Register
      </p>
    </div>
  );
};

export default GuestNav;
