import React, { useState, useContext } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { Form, Icon, Message, Button } from 'semantic-ui-react';
import StatusMessage from '../forum/StatusMessage';
import AuthContext from '../../context/auth/AuthContext';
import { loginUser } from '../../context/auth/AuthActions';
import './style.css';

const Login = ({ showRegister }) => {
  const { dispatch, isAuthenticated, isLoading, error } =
    useContext(AuthContext);

  const navigate = useNavigate();
  const location = useLocation();

  const [values, setValues] = useState({
    username: '',
    password: '',
  });

  const handleChange = (e, { name, value }) => {
    setValues({ ...values, [name]: value });
  };

  const isFormValid = () => {
    let isFormValid = true;
    if (!values.username || !values.password) {
      isFormValid = false;
    }
    return isFormValid;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (isFormValid()) {
      const data = {
        user_name: values.username,
        //name: values.name,
        //user_email: values.email,
        password: values.password,
      };

      try {
        const response = await dispatch(loginUser(dispatch, data));
        //error = response.error;
        if (!response.user) return;

        //props.history.push('/dashboard') //navigate to dashboard on success
        if (location.state?.from) {
          navigate(location.state.from);
        }
      } catch (error) {
        console.log(error);
      }
    }
  };

  const statusMessage = (
    <StatusMessage
      error={error}
      errorMessage={error || 'Login Error'}
      loading={isLoading}
      loadingMessage={'Signing in'}
      type="modal"
    />
  );
  if (!isAuthenticated) {
    return (
      <div>
        <Message attached header="Login" />
        {statusMessage}
        <Form className="attached fluid segment">
          <Form.Input
            required
            label="Username"
            placeholder="Username"
            type="text"
            name="username"
            value={values.username}
            onChange={handleChange}
          />
          <Form.Input
            required
            label="Password"
            type="password"
            name="password"
            value={values.password}
            onChange={handleChange}
          />
          <Button
            color="blue"
            loading={isLoading}
            disabled={isLoading}
            onClick={handleSubmit}
          >
            Login
          </Button>
        </Form>
        <Message attached="bottom" warning>
          <Icon name="help" />
          New to this forum?&nbsp;
          <Link className="login-register" onClick={showRegister}>
            Register here
          </Link>
          &nbsp;instead.
        </Message>
      </div>
    );
  } else return null;
};

export default Login;
