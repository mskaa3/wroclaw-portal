import React, { useContext, useEffect } from 'react';
import Login from './Login';
import Modal from './Modal';
import AuthContext from '../../context/auth/AuthContext';
import { hideModal, showModal } from '../../context/auth/AuthActions';

const LoginModal = () => {
  const { isAuthenticated, dispatch } = useContext(AuthContext);

  const handleClose = () => {
    dispatch(hideModal);
    dispatch({ type: 'LOGIN_RESET' });
  };
  const showRegister = () => {
    dispatch(showModal('REGISTER', {}));
    dispatch({ type: 'LOGIN_RESET' });
  };
  useEffect(() => {
    if (isAuthenticated) {
      handleClose();
    }
  }, []);

  return isAuthenticated ? null : (
    <Modal onClose={handleClose}>
      <Login
        //handleLogin={handleLogin}
        showRegister={showRegister}
        //isLoading={isLoading}
        //error={error}
      />
    </Modal>
  );
};

export default LoginModal;
