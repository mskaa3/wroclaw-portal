/* eslint-disable prettier/prettier */
import React, { useContext } from 'react';
import AuthContext from '../../context/auth/AuthContext';
import GuestNav from './GuestNav';
import UserNav from './UserNav';

const UserMenu = () => {
  const { isAuthenticated, isLoading } = useContext(AuthContext);

  if (isAuthenticated) {
    return (
      <UserNav
        //logout={logout}
        //showEditProfile={showEditProfile}
        isLoading={isLoading}
      />
    );
  } else {
    return <GuestNav />;
  }
};

export default UserMenu;
