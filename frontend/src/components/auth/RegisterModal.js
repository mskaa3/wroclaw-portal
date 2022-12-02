import React, { useContext, useEffect } from 'react';
import Register from './Register';
import Modal from './Modal';
import AuthContext from '../../context/auth/AuthContext';
import { hideModal, showModal } from '../../context/auth/AuthActions';

const RegisterModal = (props) => {
  const { isAuthenticated, dispatch, registerError, isLoading } =
    useContext(AuthContext);

  const handleClose = () => {
    dispatch(hideModal);
    dispatch({ type: 'REGISTER_RESET' });
  };
  const showLogin = () => {
    dispatch(showModal('LOGIN', {}));
    dispatch({ type: 'REGISTER_RESET' });
  };

  useEffect(() => {
    if (isAuthenticated) {
      handleClose();
    }
  }, []);

  return isAuthenticated ? null : (
    <Modal onClose={handleClose}>
      <Register
        //handleRegister={handleRegister}
        showLogin={showLogin}
        isLoading={isLoading}
        error={registerError}
        dispatch={dispatch}
      />
    </Modal>
  );
};

export default RegisterModal;
