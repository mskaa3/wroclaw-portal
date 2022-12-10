/* eslint-disable prettier/prettier */
import React, { useContext } from 'react';
import Avatar from '../forum/Avatar';
import { Menu, Dropdown } from 'semantic-ui-react';
import './style.css';
import { useNavigate } from 'react-router-dom';
import AuthContext from '../../context/auth/AuthContext';
import { showModal, logout } from '../../context/auth/AuthActions';

const UserNav = () => {
  const { dispatch, user } = useContext(AuthContext);

  const navigate = useNavigate();

  const myProfile = () => {
    //history.push(`/user/${user.user_id}/profile`);
    navigate(`/users/${user.user_id}`);
  };

  const showEditProfile = () => {
    dispatch(showModal('EDIT_PROFILE', {}));
    navigate(`/users/${user.user_id}/edit`, { state: { user: { user } } });
  };

  const logoutHandler = () => {
    console.log('logout');
    logout(dispatch);
  };

  return (
    <div className="userMenu">
      <Menu fluid inverted borderless size="small" className="userMenu-menu">
        <Menu.Item disabled className="userMenu-avatar">
          <Avatar avatar={user.avatar} />
        </Menu.Item>
        <Dropdown item simple text={user.user_name} direction="left">
          <Dropdown.Menu>
            <Dropdown.Item onClick={myProfile} icon="user" text="My profile" />
            <Dropdown.Item
              onClick={showEditProfile}
              icon="setting"
              text="Edit profile"
            />
            <Dropdown.Item
              onClick={logoutHandler}
              icon="sign out"
              text="Logout"
            />
          </Dropdown.Menu>
        </Dropdown>
      </Menu>
    </div>
  );
};

export default UserNav;

/*
function withRouter(Component) {
  function ComponentWithRouterProp(props) {
    let location = useLocation();
    let navigate = useNavigate();
    let params = useParams();
    return <Component {...props} router={{ location, navigate, params }} />;
  }

  return ComponentWithRouterProp;
}
*/
