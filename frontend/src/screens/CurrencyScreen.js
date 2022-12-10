/* eslint-disable prettier/prettier */
import React from 'react';
import CurrencyCalculator from '../components/currency/CurrencyCalculator';
import CurrencyTable from '../components/currency/CurrencyTable';


const CurrencyScreen = () => {
  return (
    <div>
      <CurrencyCalculator></CurrencyCalculator>
      <br></br>
      <CurrencyTable></CurrencyTable>
    </div>
  );
};

export default CurrencyScreen;
