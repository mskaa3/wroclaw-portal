import React, { useState } from 'react';
import { Form, Icon, Message, Button } from 'semantic-ui-react';
import { Link } from 'react-router-dom';
import StatusMessage from '../forum/StatusMessage';
import './style.css';
import { registerUser } from '../../context/auth/AuthActions';

const Register = (props) => {
  const { showLogin, error, isLoading, dispatch } = props;
  const [values, setValues] = useState({
    username: '',
    //name: '',
    email: '',
    password: '',
    checked: true,
  });

  const handleChange = (e, { name, value }) => {
    setValues({ ...values, [name]: value });
  };

  const handleCheckbox = () => {
    setValues({ ...values, checked: !values.checked });
  };

  const isFormValid = () => {
    let isFormValid = true;
    if (
      !values.username ||
      //!values.name ||
      !values.email ||
      !values.password ||
      !values.checked
    ) {
      isFormValid = false;
    }
    return isFormValid;
  };

  const handleSubmit = (e) => {
    if (isFormValid()) {
      const data = {
        user_name: values.username,
        //name: values.name,
        user_email: values.email,
        password: values.password,
      };

      registerUser(dispatch, data);
    }
  };

  const statusMessage = (
    <StatusMessage
      error={error}
      errorMessage={error || 'Login Error'}
      loading={isLoading}
      loadingMessage={'Registering your account'}
      type="modal"
    />
  );

  return (
    <div>
      <Message
        attached
        header="Welcome to our forum!"
        content="Fill out the form below to sign-up for a new account"
      />
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
          label="Email"
          placeholder="Email"
          type="email"
          name="email"
          value={values.email}
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
        <Form.Checkbox
          inline
          required
          label="I agree to the terms and conditions"
          name="agreement"
          checked={values.checked}
          onChange={handleCheckbox}
        />
        <Button
          color="blue"
          loading={isLoading}
          disabled={isLoading}
          onClick={handleSubmit}
        >
          Submit
        </Button>
      </Form>
      <Message attached="bottom" warning>
        <Icon name="help" />
        Already signed up?&nbsp;
        <Link className="register-login" onClick={showLogin}>
          Login here
        </Link>
        &nbsp;instead.
      </Message>
    </div>
  );
};

export default Register;
