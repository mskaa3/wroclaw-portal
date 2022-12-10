/* eslint-disable prettier/prettier */
import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import Protected from './Protected';
import Modal from './Modal';
import AuthContext from '../../context/auth/AuthContext';
import { hideModal, showModal } from '../../context/auth/AuthActions';

const ProtectedModal = () => {
  const { isAuthenticated, dispatch } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleClose = () => {
    dispatch(hideModal());
    navigate('/');
  };
  const showRegister = () => {
    dispatch(showModal('REGISTER', {}));
    dispatch({ type: 'LOGIN_RESET' });
  };
  const showLogin = () => {
    dispatch(showModal('LOGIN', {}));
    dispatch({ type: 'REGISTER_RESET' });
  };

  return isAuthenticated ? null : (
    <Modal onClose={handleClose}>
      <Protected showLogin={showLogin} showRegister={showRegister} />
    </Modal>
  );
};

export default ProtectedModal;
