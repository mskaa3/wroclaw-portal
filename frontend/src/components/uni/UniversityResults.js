/* eslint-disable prettier/prettier */
import { useContext } from 'react';
import Spinner from '../Spinner';
import UniversityCard from './UniversityCard';
import UnivercityContext from '../../context/uni/UnivercityContext';

const UniversityResults = (props) => {
  const { loading, searchUniResults } = useContext(UnivercityContext);

  if (!Array.isArray(searchUniResults)) {
    return <h3>There was an error loading your data!</h3>;
  }

  if (!loading) {
    //if (searchUniResults.length === 0) {
    //  return <h3>No results found!</h3>;
    //} else {
    return (
      <div>
        {searchUniResults.map((uni) => (
          <UniversityCard key={uni.uni_uid} uni={uni} uni_key={uni.uni_uid} />
        ))}
      </div>
    );
    //}
  } else {
    return <Spinner />;
  }
};

export default UniversityResults;
