import React from 'react';
import Avatar from '../forum/Avatar';
import './style.css';

const Profile = (props) => {
  //class Profile extends Component {
  //formatDateTime(datetime) {
  //  return datetime.split('.')[0].replace('T', ' ');
  //}

  //render() {
  //const { name, username, avatar, bio, status, isStaff, dateJoined } =props;
  const { user_name, avatar, user_id, user_email } = props.user;

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
  //  }
};

export default Profile;
/*
return (
    <div className="profileContainer">
      <div>
        <Avatar className="profileAvatar" avatar={avatar} centered={false} />
      </div>
      <div className="profileInfo">
        <div className="name">{name}</div>
        <div className="username">
          <strong>@{username}</strong>
          <b className="staffStatus">{isStaff ? ' (Staff) ' : ''}</b>
        </div>
        <div className="status">
          <strong>Status: </strong>
          {status}
        </div>
        <div className="dateJoined">
          <strong>Joined: </strong>
          {dateJoined}
        </div>
        <div className="bio">
          <strong>Bio: </strong>
          {bio}
        </div>
      </div>
    </div>
  );
  //  }
};
*/
