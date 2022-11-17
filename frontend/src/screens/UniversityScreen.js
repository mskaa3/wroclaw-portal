/* eslint-disable prettier/prettier */
import React from 'react';
import UniversitySearch from '../components/uni/UniversitySearch';
import UniversityResults from '../components/uni/UniversityResults';

//const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

const UniversityScreen = () => {
  //const { unis, loading, getUnis } = useContext(UnivercityContext);
  // const { unis, loading, handleSearchUni, unuSearchWord } =
  //   useContext(UnivercityContext);

  return (
    <>
      <UniversitySearch />
      <UniversityResults />
    </>
  );
};

export default UniversityScreen;
