import React, { Component, useContext } from 'react';
//import { connect } from 'react-redux';
//import { useParams } from 'react-router-dom';
import AuthContext from '../../context/auth/AuthContext';
//import { fetchUserProfile } from '../../actions';
import StatusMessage from '../../components/forum/StatusMessage';
import Profile from '../../components/auth/Profile';
import './style.css';

const UserProfileContainer = () => {
  //const { id } = useParams();
  //console.log('user_id');
  //console.log(id);
  const { user, isLoading, error } = useContext(AuthContext);

  //  render() {
  //const { isLoading, error, profile } = this.props;

  //if (error || !profile || isLoading) {
  if (error || !user || isLoading) {
    return (
      <StatusMessage
        error={error || !user}
        errorClassName="userProfile-error"
        errorMessage={error}
        loading={isLoading}
        loadingMessage={`We are fetching the user profile for you`}
        type="default"
      />
    );
  }

  //const { name, username, status, bio, avatar, is_staff, date_joined } =profile;
  //const { user_name, avatar, user_id, user_email } = user;
  return (
    <Profile
      user={user}
      //username={user_name}
      //name={name}
      //avatar={avatar}
      //status={status}
      //bio={bio}
      //dateJoined={date_joined}
      //isStaff={is_staff}
    />
  );
};
//}
export default UserProfileContainer;
/*
const mapStateToProps = (state) => ({
  isLoading: state.userProfile.isLoading,
  profile: state.userProfile.profile,
  error: state.userProfile.error,
});

const mapDispatchToProps = (dispatch) => ({
  fetchUserProfile: (username) => {
    dispatch(fetchUserProfile(username));
  },
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(UserProfileContainer);

*/
/*
class UserProfileContainer extends Component {
  componentDidMount() {
    const { username } = this.props.match.params;
    this.props.fetchUserProfile(username);
  }

  componentWillReceiveProps(newProps) {
    const { username: oldUsername } = this.props.match.params;
    const { username: futureUsername } = newProps.match.params;
    if (oldUsername !== futureUsername) {
      this.props.fetchUserProfile(futureUsername);
    }
  }

*/
