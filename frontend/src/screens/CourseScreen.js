import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from 'react-bootstrap';
import UniversityDetailCard from '../components/uni/UniversityDetailCard';

const CourseScreen = ({ uni }) => {
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

      <UniversityDetailCard />
    </>
  );
};

export default CourseScreen;
