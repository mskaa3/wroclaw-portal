import { createContext, useState, useReducer } from 'react';
import univercityReducer from '../UnivercityReducer';
import axios from 'axios';
import Select from 'react-select';

const UnivercityContext = createContext();

//const API_URL = process.env.REACT_APP_API_URL;
const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

export const UnivercityProvider = ({ children }) => {
  const initialState = {
    unis: [],
    uniSearchWord: '',
    loading: false,
  };

  const [state, dispatch] = useReducer(univercityReducer, initialState);
  //const [uniSearchWord, setUniSearchWord] = useState('');
  //const [unis, setUnis] = useState([]);
  //const [loading, setLoading] = useState(true);

  const getUnis = async (e) => {
    //e.preventDefault();
    //console.log(uniSearchWord);

    setLoading();
    try {
      const res = await axios.get(`${API_URL}/unis`);
      console.log([res.data]);
      //setUnis([res.data, ...unis]);
      //setUnis(res.data || []);
      dispatch({
        type: 'GET_UNIS',
        payload: res,
      });

      //setLoading(false);
    } catch (error) {
      console.log(error);
    }

    //setUniSearchWord('');
  };

  const handleSearchUni = async (uniSearchWord) => {
    //e.preventDefault();
    //console.log(uniSearchWord);
    setLoading();
    const params = new URLSearchParams({
      q: uniSearchWord,
    });
    try {
      const { unis } = await axios.get(`${API_URL}/search/unis?${params}`);
      //console.log([res.data]);
      //setUnis([res.data, ...unis]);
      //setUnis(res.data || []);
      dispatch({
        type: 'GET_UNIS',
        payload: unis,
      });
      //setLoading(false);
    } catch (error) {
      console.log(error);
    }

    setUniSearchWord('');
  };

  //set loading
  const setLoading = () => dispatch({ type: 'SET_LOADING' });
  const setUniSearchWord = () => dispatch({ type: 'SET_UNI_SEARCH_WORD' });

  return (
    <UnivercityContext.Provider
      value={{
        unis: state.unis,
        loading: state.loading,
        getUnis,
        handleSearchUni,
        uniSearchWord: state.uniSearchWord,
      }}
    >
      {children}
    </UnivercityContext.Provider>
  );
};

export default UnivercityContext;
