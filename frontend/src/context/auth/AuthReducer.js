const authReducer = (state, action) => {
  switch (action.type) {
    case 'SET_IS_AUTHENTICATED':
      return {
        ...state,
        isAuthenticated: action.payload,
        isLoading: false,
      };
    case 'REQUEST_LOGIN':
      return {
        ...state,
        isLoading: true,
        error: null,
      };
    case 'LOGIN_SUCCESS':
      return {
        ...state,
        user: action.payload.user,
        token: action.payload.access_token,
        isAuthenticated: true,
        isLoading: false,
        error: null,
      };
    case 'LOGOUT':
      return {
        ...state,
        user: null,
        isLoading: false,
        isAuthenticated: false,
        token: null,
        error: null,
        isEditing: false,
        editError: null,
        editSuccess: false,
        registerError: false,
        modalType: null,
        modalProps: {},
      };
    case 'SET_LOADING':
      return {
        ...state,
        isLoading: true,
      };
    case 'LOGIN_ERROR':
      return {
        ...state,
        error: action.error,
        isLoading: false,
      };
    case 'LOGIN_RESET':
      return {
        ...state,
        isLoading: false,
        isAuthenticated: false,
        user: null,
        token: null,
        error: null,
      };
    case 'REGISTER_REQUEST':
      return {
        ...state,
        isLoading: true,
        registerError: null,
      };
    case 'REGISTER_SUCCESS':
      return {
        ...state,
        isLoading: false,
        registerError: null,
      };
    case 'REGISTER_ERROR':
      return {
        ...state,
        isLoading: false,
        registerError: action.error,
      };
    case 'REGISTER_RESET':
      return {
        ...state,
        isLoading: false,
        registerError: null,
      };
    case 'REQUEST_EDIT_PROFILE':
      return {
        ...state,
        isEditing: true,
        editError: null,
        editSuccess: false,
      };
    case 'EDIT_PROFILE_SUCCESS':
      return {
        ...state,
        isEditing: false,
        editError: null,
        editSuccess: true,
        user: action.payload.user,
      };
    case 'EDIT_PROFILE_FAILURE':
      return {
        ...state,
        isEditing: false,
        editSuccess: false,
        editError: action.error,
      };
    case 'EDIT_PROFILE_RESET':
      return {
        ...state,
        isEditing: false,
        editError: null,
        editSuccess: false,
      };
    case 'SHOW_MODAL':
      return {
        ...state,
        modalType: action.modalType,
        modalProps: action.modalProps,
      };
    case 'HIDE_MODAL':
      return {
        ...state,
        modalType: null,
        modalProps: {},
      };
    default:
      return state;
    //throw new Error(`Unhandled action type: ${action.type}`);
  }
};

export default authReducer;
