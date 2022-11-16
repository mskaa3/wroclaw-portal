import React from 'react';
import CurrencyCalculator from '../components/CurrencyCalculator';
import CurrencyTable from '../components/CurrencyTable';

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
