import { useContext } from 'react';
import Spinner from './Spinner';
import UnivercityCard from './UnivercityCard';
import UnivercityContext from '../context/uni/UnivercityContext';

const UnivercityResults = (props) => {
  const { unis, loading } = useContext(UnivercityContext);

  if (!Array.isArray(unis)) {
    return <h3>There was an error loading your data!</h3>;
  }

  if (!loading) {
    return (
      <div>
        {props.unis.map((uni) => (
          <UnivercityCard key={uni.uni_id} uni={uni} />
        ))}
      </div>
    );
  } else {
    return <Spinner />;
  }
};

export default UnivercityResults;
