import React, { useContext } from 'react';
import RegisterModal from './RegisterModal';
import LoginModal from './LoginModal';
import EditProfileModal from './EditProfileModal';
import ProtectedModal from './ProtectedModal';
import AuthContext from '../../context/auth/AuthContext';

const ModalContainer = () => {
  const { modalType } = useContext(AuthContext);

  switch (modalType) {
    case 'REGISTER':
      return <RegisterModal />;
    case 'LOGIN':
      return <LoginModal />;
    case 'EDIT_PROFILE':
      return <EditProfileModal />;
    case 'PROTECTED_ROUTE':
      return <ProtectedModal />;
    default:
      return null;
  }
};

export default ModalContainer;
