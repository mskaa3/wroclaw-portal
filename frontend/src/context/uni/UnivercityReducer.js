/* eslint-disable prettier/prettier */
const univercityReducer = (state, action) => {
  switch (action.type) {
    case 'GET_UNIS':
      return {
        ...state,
        unis: action.payload,
        loading: false,
      };
    case 'SEARCH_UNIS_BY_FILTERS':
      return {
        ...state,
        searchUniResults: action.payload,
        loading: false,
      };
    case 'SET_LOADING':
      return {
        ...state,
        loading: true,
      };
    case 'SET_CITY_FILTER':
      return {
        ...state,
        city: action.payload,
      };
    case 'SET_LEVEL_FILTER':
      return {
        ...state,
        level: action.payload,
      };
    case 'SET_DISCIPLINE_FILTER':
      return {
        ...state,
        discipline: action.payload,
      };
    case 'SET_WORD_FILTER':
      return {
        ...state,
        search: action.payload,
      };
    case 'SET_WORD':
      return {
        ...state,
        search: action.payload,
      };
    case 'CLEAR_UNIS':
      return {
        ...state,
        unis: [],
      };
    case 'GET_STUDY_DISCIPLINES':
      return {
        ...state,
        disciplines: action.payload,
        loading: false,
      };
    default:
      return state;
  }
};

export default univercityReducer;
