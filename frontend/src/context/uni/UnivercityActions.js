import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

// const univercity = axios.create({
//   baseURL: API_URL,
// });

export const searchUnis = async (uniSearchWord) => {
  const params = new URLSearchParams({
    q: uniSearchWord,
  });

  const response = await axios.get(`${API_URL}/search/unis?${params}`);

  return response.data;
};

export const getStudyDisciplines = async (e) => {
  //const params = new URLSearchParams({
  //  q: uniSearchWord,
  //});

  const response = await axios.get(`${API_URL}/study_disciplines`);

  return response.data;
};
