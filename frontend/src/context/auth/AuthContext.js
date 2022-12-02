import { createContext, useReducer } from 'react';
import authReducer from '../auth/AuthReducer';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const initialState = {
    //isLogin: null,
    isAuthenticated: false,
    user: null,
    isLoading: false,
    error: null,
    isEditing: false,
    editError: null,
    editSuccess: false,
    registerError: false,
    modalType: null,
    modalProps: {},
  };

  const [state, dispatch] = useReducer(authReducer, initialState);

  // const getUnis = async (e) => {
  //   //e.preventDefault();
  //   //console.log(uniSearchWord);

  //   setLoading();
  //   try {
  //     const res = await axios.get(`${API_URL}/unis`);
  //     console.log([res.data]);
  //     //setUnis([res.data, ...unis]);
  //     //setUnis(res.data || []);
  //     dispatch({
  //       type: 'GET_UNIS',
  //       payload: res,
  //     });

  //     //setLoading(false);
  //   } catch (error) {
  //     console.log(error);
  //   }

  //   //setUniSearchWord('');
  // };

  return (
    <AuthContext.Provider
      value={{
        ...state,
        dispatch,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
