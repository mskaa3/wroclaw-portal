/* eslint-disable prettier/prettier */
import React from 'react';
import Avatar from '../forum/Avatar';
import './style.css';

const Profile = (props) => {
  //formatDateTime(datetime) {
  //  return datetime.split('.')[0].replace('T', ' ');
  //}

  const { user_name, avatar } = props.user;

  return (
    <div className="profileContainer">
      <div>
        <Avatar className="profileAvatar" avatar={avatar} centered={false} />
      </div>
      <div className="profileInfo">
        <div className="username">
          <strong>@{user_name}</strong>
        </div>
      </div>
    </div>
  );
};

export default Profile;
