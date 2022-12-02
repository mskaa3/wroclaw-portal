import React, { useContext, useEffect } from 'react';
import EditProfile from './EditProfile';
import Modal from './Modal';
import AuthContext from '../../context/auth/AuthContext';
import { hideModal, editProfile } from '../../context/auth/AuthActions';

const EditProfileModal = (props) => {
  const {
    isAuthenticated,
    dispatch,
    editSuccess,
    editError,
    error,
    isEditing,
  } = useContext(AuthContext);

  const handleClose = () => {
    dispatch(hideModal);
    dispatch({ type: 'EDIT_PROFILE_RESET' });
  };

  useEffect(() => {
    if (isAuthenticated) {
      handleClose();
    }
  }, []);

  return !isAuthenticated ? null : (
    <Modal onClose={handleClose} dialogStyle={{ minWidth: '500px' }}>
      <EditProfile
        //avatar={user.avatar}
        //name={user.user_name}
        //handleEdit={editProfile}
        isLoading={isEditing}
        error={editError}
        editSuccess={editSuccess}
      />
    </Modal>
  );
};

export default EditProfileModal;
