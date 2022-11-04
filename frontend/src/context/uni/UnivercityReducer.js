const univercityReducer = (state, action) => {
  switch (action.type) {
    case 'GET_UNIS':
      return {
        ...state,
        unis: action.payload,
        loading: false,
      };
    case 'SET_LOADING':
      return {
        ...state,
        loading: true,
      };
    case 'CLEAR_UNIS':
      return {
        ...state,
        unis: [],
      };
    case 'GET_STUDY_DISCIPLINES':
      return {
        ...state,
        study_disciplines: action.payload,
        loading: false,
      };
    default:
      return state;
  }
};

export default univercityReducer;
