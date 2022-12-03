import React, { useContext } from 'react';
import Login from './Login';
import Modal from './Modal';
import AuthContext from '../../context/auth/AuthContext';
import { hideModal, showModal } from '../../context/auth/AuthActions';

const LoginModal = () => {
  const { isAuthenticated, dispatch } = useContext(AuthContext);

  const handleClose = () => {
    dispatch(hideModal());
    dispatch({ type: 'LOGIN_RESET' });
  };
  const showRegister = () => {
    dispatch(showModal('REGISTER', {}));
    dispatch({ type: 'LOGIN_RESET' });
  };

  return isAuthenticated ? null : (
    <Modal onClose={handleClose}>
      <Login
        //handleLogin={handleLogin}
        showRegister={showRegister}
      />
    </Modal>
  );
};

export default LoginModal;
