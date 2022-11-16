import 'C:/7SEMESTER/wroclaw-portal/frontend/src/css/Currency.css';

import { useEffect, useState } from 'react';
import Axios from 'axios';
import React from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Dropdown from 'react-dropdown';
//import Dropdown from 'react-bootstrap/Dropdown';

import '../css/Currency.css';
//import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

function CurrencyCalculator() {
  /*const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs((values) => ({ ...values, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setInputs(() => '5');
    console.log(inputs);
  };*/

  /*return (
    <center>
      <form onSubmit={handleSubmit}>
        <label>
          Enter your name:
          <input
            type="text"
            name="username"
            value={inputs.username || ''}
            onChange={handleChange}
          />
        </label>
        <br></br>
        <label>
          Enter your age:
          <input
            type="number"
            name="age"
            value={inputs.age || ''}
            onChange={handleChange}
          />
        </label>
        <br></br>
        <input type="submit" />
      </form>
    </center>
  );*/

  // Initializing all the state variables
  const [info, setInfo] = useState([]);
  const [input, setInput] = useState(0);
  const [from, setFrom] = useState('usd');
  const [to, setTo] = useState('eur');
  const [options, setOptions] = useState([]);
  const [output, setOutput] = useState(0);

  // Calling the api whenever the dependency changes
  useEffect(() => {
    Axios.get(
      `https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/${from}.json`
    ).then((res) => {
      setInfo(res.data[from]);
    });
  }, [from]);

  // Calling the convert function whenever
  // a user switches the currency
  useEffect(() => {
    setOptions(Object.keys(info));

    convert();
  }, [info]);

  // Function to convert the currency
  function convert() {
    var rate = info[to];

    setOutput(input * rate);
  }

  // Function to switch between two currency
  function flip() {
    var temp = from;

    setFrom(to);

    setTo(temp);
  }

  return (
    <center>
      <Form.Group className="mb-3 w-25 mt-5" controlId="formBasicCurrencyFrom">
        <Form.Label>Currency From</Form.Label>
        <div className="container" style={{ display: 'inherit' }}>
          <Dropdown
            className="sample-container-2"
            options={options}
            onChange={(e) => {
              setFrom(e.value);
            }}
            value={from}
            placeholder="From"
          />
        </div>

        <br />
        <div>
          <Form.Control
            type="Currency From"
            placeholder="Enter currency"
            onChange={(e) => setInput(e.target.value)}
          />
        </div>
        <br />
      </Form.Group>
      <Form.Group className="mb-3 w-25" controlId="formBasicCurrencyTo">
        <Form.Label>Currency To</Form.Label>
        <div>
          <Dropdown
            options={options}
            onChange={(e) => {
              setTo(e.value);
            }}
            value={to}
            placeholder="To"
          />
        </div>
        <br />
      </Form.Group>
      <button
        onClick={() => {
          convert();
        }}
      >
        Convert
      </button>
      <h2>Result of Convertion:</h2>

      <p>{input + ' ' + from + ' = ' + output.toFixed(2) + ' ' + to}</p>
    </center>
  );
}

export default CurrencyCalculator;
