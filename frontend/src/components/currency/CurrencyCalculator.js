/* eslint-disable prettier/prettier */
import React, { useEffect, useState } from 'react';
import Axios from 'axios';
import Form from 'react-bootstrap/Form';
import Dropdown from 'react-dropdown';

import '../../css/Currency.css';
import DropdownButton from 'react-bootstrap/DropdownButton';

function CurrencyCalculator() {
  // Initializing all the state variables
  const [currencyNames, setCurrencyNames] = useState([]);
  const [info, setInfo] = useState([]);
  const [input, setInput] = useState(0);
  const [from, setFrom] = useState();
  const [to, setTo] = useState();
  const [options, setOptions] = useState([]);
  const [output, setOutput] = useState();

  // Calling the api whenever the dependency changes
  useEffect(() => {
    Axios.get(
      'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json'
    ).then((res) => {
      setCurrencyNames(
        Object.entries(res.data).map((item) => {
          return { value: item[0], label: item[1] };
        })
      );
    });
  }, []);

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

    //convert();
  }, [info]);

  // Function to convert the currency
  function convert() {
    if (!from || !to) {
      return;
    }
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
        <div style={{ display: 'inherit' }}>
          {currencyNames && (
            <Form.Select
              onChange={(e) => {
                console.log(e.target.value);
                setFrom(e.target.value);
              }}
            >
              {!from && <option value="">Select currency from</option>}

              {currencyNames &&
                currencyNames.map((item) => {
                  return (
                    <option key={item.value} value={item.value}>
                      {item.label}
                    </option>
                  );
                })}
            </Form.Select>
          )}
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
          <Form.Select
            //value="Choose Currency To"
            onChange={(e) => {
              setTo(e.target.value);
            }}
          >
            {!to && <option value="">Select currency to</option>}

            {currencyNames &&
              currencyNames.map((item) => {
                return (
                  <option key={item.value} value={item.value}>
                    {item.label}
                  </option>
                );
              })}
          </Form.Select>
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
      {output && (
        <div>
          <br />
          <h2>Result of Convertion:</h2>

          <p>{input + ' ' + from + ' = ' + output.toFixed(2) + ' ' + to}</p>
        </div>
      )}
    </center>
  );
}

export default CurrencyCalculator;
