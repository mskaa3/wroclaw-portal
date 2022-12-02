import React, { useContext } from 'react';
import AuthContext from '../../context/auth/AuthContext';
import GuestNav from './GuestNav';
import UserNav from './UserNav';

const UserMenu = () => {
  const { isLogin, isAuthenticated, user, isLoading } = useContext(AuthContext);

  if (isAuthenticated) {
    return (
      <UserNav
        user={user}
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
