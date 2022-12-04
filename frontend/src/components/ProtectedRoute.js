import React, { useContext } from 'react';
import { Outlet } from 'react-router-dom';
import AuthContext from '../context/auth/AuthContext';
import ProtectedModal from './auth/ProtectedModal';

function ProtectedRoute() {
  const { isAuthenticated } = useContext(AuthContext);

  return isAuthenticated ? <Outlet /> : <ProtectedModal />;
}

export default ProtectedRoute;
/*
return isAuthenticated ? (
    <Outlet />
  ) : (
    <Navigate to="/login" state={{ from: location }} />
  );
*/
/*
//const location = useLocation();
  //const handleLogin = () => {
  //  dispatch(showModal('LOGIN'), {});
  //};
return isAuthenticated ? <Outlet /> : <LoginModal />;
*/
