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
    return (
      <div>
        {searchUniResults.map((uni) => (
          <UniversityCard key={uni.uni_uid} uni={uni} uni_key={uni.uni_uid} />
        ))}
      </div>
    );
  } else {
    return <Spinner />;
  }
};

export default UniversityResults;
