import React, { useContext } from 'react';
import RegisterModal from './RegisterModal';
import LoginModal from './LoginModal';
import EditProfileModal from './EditProfileModal';
import AuthContext from '../../context/auth/AuthContext';

const ModalContainer = () => {
  const { modalType, modalProps } = useContext(AuthContext);

  switch (modalType) {
    case 'REGISTER':
      return <RegisterModal />;
    case 'LOGIN':
      return <LoginModal />;
    case 'EDIT_PROFILE':
      return <EditProfileModal />;
    default:
      return null;
  }
};

export default ModalContainer;
