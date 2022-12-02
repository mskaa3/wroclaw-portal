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
      <Button
        className="btn-sign-in"
        type="button"
        onClick={handleLoginOnClick}
      >
        Login
      </Button>

      <br />

      <Button
        className="btn-register"
        type="button"
        onClick={handleRegisterOnClick}
      >
        Register
      </Button>
    </div>
  );
};

export default GuestNav;
