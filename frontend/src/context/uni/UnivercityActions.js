import axios from 'axios';
import omitBy from 'lodash/omitBy';
import isEmpty from 'lodash/isEmpty';

const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

// const univercity = axios.create({
//   baseURL: API_URL,
// });

/*
export const searchUnisByWord = async (uniSearchWord) => {
  const params = new URLSearchParams({
    search: uniSearchWord,
  });

  const response = await axios.get(`${API_URL}/search/unis?${params}`);

  return response.data;
};
*/
export const searchUnisByFilters = async (
  discipline_name,
  level,
  city,
  search
) => {
  const params = new URLSearchParams(
    omitBy(
      {
        discipline_name: discipline_name,
        level: level,
        city: city,
        search: search,
      },
      isEmpty
    )
  );
  console.log('params after formatting');
  console.log(params.toString());

  //try {
  const response = await axios.get(`${API_URL}/search/unis?${params}`);
  //} catch (err) {
  //  console.log(err);
  //}

  return response.data;
};

export const getStudyDisciplines = async (e) => {
  //const params = new URLSearchParams({
  //  q: uniSearchWord,
  //});

  const response = await axios.get(`${API_URL}/disciplines`);

  return response.data;
};

export const getUnis = async (e) => {
  const response = await axios.get(`${API_URL}/unis`);

  return response.data;
};
