import { createContext, useReducer } from 'react';
import univercityReducer from './UnivercityReducer';

const UnivercityContext = createContext();

export const UnivercityProvider = ({ children }) => {
  const initialState = {
    unis: [],
    uni: {},
    study_disciplines: [],
    //study_discipline: {},
    loading: false,
  };

  const [state, dispatch] = useReducer(univercityReducer, initialState);

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
    <UnivercityContext.Provider
      value={{
        ...state,
        //state,
        dispatch,
      }}
    >
      {children}
    </UnivercityContext.Provider>
  );
};

export default UnivercityContext;
