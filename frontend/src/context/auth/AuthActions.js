import axios from 'axios';
import { errorHandler } from '../../errorHandler';

const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

export async function loginUser(dispatch, loginPayload) {
  /*
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(loginPayload),
    //body: loginPayload,
  };
  console.log('request options');
  console.log(requestOptions);
  */

  dispatch({ type: 'REQUEST_LOGIN' });
  try {
    //let response = await axios(`${API_URL}/users/login`, requestOptions);

    let response = await axios.post(`${API_URL}/users/login`, loginPayload);
    //} catch (e) {
    //  console.log(e);
    //  console.log(e.response.status);
    //  console.log(e.response.data.message);

    console.log('response in actions');
    console.log(response);

    let data = await response.data;
    console.log('data in login actions');
    //console.log(typeof data);
    //console.log(typeof data.user);

    console.log(data);
    //if (data.user) {
    if (data.access_token) {
      dispatch({ type: 'LOGIN_SUCCESS', payload: data });
      localStorage.setItem('user', JSON.stringify(data.user));
      localStorage.setItem('access_token', JSON.stringify(data.access_token));
      //dispatch(hideModal());
      return data;
    }
  } catch (error) {
    const errorMessage = errorHandler(error);
    dispatch({ type: 'LOGIN_ERROR', error: errorMessage });
  }
}

export async function registerUser(dispatch, userData) {
  dispatch({ type: 'REGISTER_REQUEST' });

  await axios
    .post(`${API_URL}/users`, userData)
    .then((response) => {
      console.log('response from register user in actions');
      console.log(response);
      const data = response.data;
      console.log('register data in actions');
      console.log(data);

      if (data.user.user_id > 0) {
        //const registered_data = {
        //  user_name: data.user.user_name,
        //  password: data.user.password,
        //};
        const registered_data = {
          user_name: userData['user_name'],
          password: userData['password'],
        };
        //const registered_data = userData;
        console.log('registered_data');
        console.log(registered_data);
        dispatch({ type: 'REGISTER_SUCCESS' });
        console.log('after REGISTER_SUCCESS');
        dispatch(loginUser(dispatch, registered_data));
        console.log('after relogin');
        //dispatch(hideModal());
        //return data;
      }
    })
    .catch((error) => {
      const errorMessage = errorHandler(error);
      dispatch({ type: 'REGISTER_ERROR', error: errorMessage });
    });
}

export function logout(dispatch) {
  localStorage.removeItem('user');
  localStorage.removeItem('access_token');
  dispatch({ type: 'LOGOUT' });
}

export async function editProfile(dispatch, newProfile, user_id) {
  dispatch({ type: 'REQUEST_EDIT_PROFILE' });
  if (!user_id) {
    dispatch({ type: 'EDIT_PROFILE_FAILURE' }, 'Not authenticated');
  } else {
    console.log('before try');
    try {
      let response = await axios.put(
        `${API_URL}/users/${user_id}`,
        newProfile,
        { headers: authHeader() }
      );

      let data = await response.data;

      if (data.user) {
        localStorage.setItem('user', JSON.stringify(data.user));
        dispatch({ type: 'EDIT_PROFILE_SUCCESS', payload: data });
        //return data;
      }
    } catch (error) {
      console.log('in edit function error');
      const errorMessage = errorHandler(error);

      dispatch({ type: 'EDIT_PROFILE_FAILURE', errorMessage });
    }
  }
}

export const showModal = (modalType, modalProps) => ({
  type: 'SHOW_MODAL',
  modalType,
  modalProps,
});

export const hideModal = () => ({
  type: 'HIDE_MODAL',
});

export const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem('user'));
};
export const getAccessToken = () => {
  return JSON.parse(localStorage.getItem('access_token'));
};

export const authHeader = () => {
  const user = getCurrentUser();
  const access_token = getAccessToken();
  if (user && access_token) {
    return { Authorization: 'Bearer ' + access_token };
  } else {
    return {};
  }
};
