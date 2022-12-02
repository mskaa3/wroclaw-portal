import React, { useContext } from 'react';
import { Outlet, Navigate, useLocation } from 'react-router-dom';

import AuthContext from '../context/auth/AuthContext';
import Login from './auth/Login';
import LoginModal from './auth/LoginModal';

import { showModal } from '../context/auth/AuthActions';

function ProtectedRoute() {
  const { isAuthenticated, dispatch } = useContext(AuthContext);
  const location = useLocation();
  const handleLogin = () => {
    //dispatch({
    //  type: 'SET_IS_LOGIN',
    //  payload: true,
    //});
    dispatch(showModal('LOGIN'), {});
  };
  return isAuthenticated ? <Outlet /> : <LoginModal />;
}

export default ProtectedRoute;
/*
return isAuthenticated ? (
    <Outlet />
  ) : (
    <Navigate to="/login" state={{ from: location }} />
  );
*/
