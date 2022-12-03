import React, { useContext } from 'react';
import EditProfile from './EditProfile';
import Modal from './Modal';
import AuthContext from '../../context/auth/AuthContext';
import { hideModal } from '../../context/auth/AuthActions';

const EditProfileModal = (props) => {
  const { isAuthenticated, dispatch, editSuccess, editError, isEditing } =
    useContext(AuthContext);

  const handleClose = () => {
    dispatch(hideModal());
    dispatch({ type: 'EDIT_PROFILE_RESET' });
  };

  return !isAuthenticated ? null : (
    <Modal onClose={handleClose} dialogStyle={{ minWidth: '500px' }}>
      <EditProfile
        //handleEdit={editProfile}
        isLoading={isEditing}
        error={editError}
        editSuccess={editSuccess}
      />
    </Modal>
  );
};

export default EditProfileModal;
