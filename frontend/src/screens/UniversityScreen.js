/* eslint-disable prettier/prettier */
import React from 'react';
import Univercity from '../components/Univercity';
import UnivercityCard from '../components/UnivercityCard';

const UniversityScreen = ({
  uniSearchWord,
  setUniSearchWord,
  handleSubmit,
  unis,
  setUnis,
}) => {
  return (
    <div>
      <Univercity
        handleSubmit={handleSubmit}
        uniSearchWord={uniSearchWord}
        setUniSearchWord={setUniSearchWord}
      />
      {unis.map((uni, i) => (
        <UnivercityCard key={i} uni={uni} />
      ))}
    </div>
  );
};

export default UniversityScreen;
