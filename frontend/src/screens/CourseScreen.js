import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from 'react-bootstrap';
import UniversityDetailCard from '../components/uni/UniversityDetailCard';

//const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

const CourseScreen = ({ uni }) => {
  //const { unis, loading, dispatch, searchUniResults, city, level, discipline } =
  //  useContext(UnivercityContext);
  const navigate = useNavigate();

  return (
    <>
      <Button
        className="mt-3 w-40"
        variant="custom"
        type="submit"
        onClick={() => navigate(-1)}
      >
        <i className="fa-solid fa-left-long"></i> Back to search results
      </Button>

      <UniversityDetailCard uni={uni} />
    </>
  );

  //return <h2>Course</h2>;
  // <CourseCard />
};

export default CourseScreen;
