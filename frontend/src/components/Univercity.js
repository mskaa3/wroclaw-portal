import React, { useEffect } from 'react';
import { Form, Button } from 'react-bootstrap';
import UnivercityContext from '../context/uni/UnivercityContext';
import UnivercityResults from './UnivercityResults';
import { useState, useContext } from 'react';
import queryString from 'query-string';
import {
  searchUnis,
  getStudyDisciplines,
} from '../context/uni/UnivercityActions';
import axios from 'axios';
import Select from 'react-select';

const Univercity = () => {
  const [uniSearchWord, setUniSearchWord] = useState('');
  //const [study_discipline, setStudyDiscipline] = useState('');
  const [study_disciplines, setStudyDisciplines] = useState([]);
  //const { unis, dispatch, study_disciplines } = useContext(UnivercityContext);
  const { unis, dispatch } = useContext(UnivercityContext);
  //const { state, dispatch } = useContext(UnivercityContext);
  //const [level, setLevel] = useState('');
  const [levels, setLevels] = useState([]);
  //const [city, setCity] = useState('');
  const [cities, setCities] = useState([]);
  const [values, setValues] = useState({
    study_discipline: '',
    level: '',
    city: '',
    results: [],
    searched: false,
  });

  const handleWordChange = (e) => {
    setUniSearchWord(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    dispatch({ type: 'SET_LOADING' });
    //const unis = await searchUnis(uniSearchWord);
    const study_disciplines = await getStudyDisciplines();
    console.log('from univercity try to print study_disciplines');
    console.log(study_disciplines);
    if (!Array.isArray(study_disciplines)) {
      console.log(
        'From Univercity: Not an array There was an error loading your data!'
      );
    }

    dispatch({ type: 'GET_STUDY_DISCIPLINES', payload: study_disciplines });

    //setStudyDiscipline(event.target.value);

    //handleSearchUni(uniSearchWord);
    //getUnis();
    //setUniSearchWord('');
  };
  useEffect(() => {
    const fetchStudyDisciplines = async () => {
      const { data } = await axios.get(
        'http://127.0.0.1:5000/study_disciplines'
      );

      setStudyDisciplines(data);
    };

    fetchStudyDisciplines();
  }, []);

  useEffect(() => {
    const fetchStudyLevels = async () => {
      const { data } = await axios.get('http://127.0.0.1:5000/studies/levels');

      setLevels(data);
    };

    fetchStudyLevels();
  }, []);

  useEffect(() => {
    const fetchCities = async () => {
      const { data } = await axios.get('http://127.0.0.1:5000/unis/cities');

      setCities(data);
    };

    fetchCities();
  }, []);

  const handleChange = (name) => (event) => {
    setValues({ ...values, [name]: event.target.value });
  };

  const handleSubmit1 = async (e) => {
    e.preventDefault();

    dispatch({ type: 'SET_LOADING' });
    //const unis = await searchUnis(uniSearchWord);
    const unis = await searchUnis(uniSearchWord);
    console.log('from univercity try to print unis');
    console.log(unis);
    if (!Array.isArray(unis)) {
      console.log(
        'From Univercity: Not an array There was an error loading your data!'
      );
    }

    dispatch({ type: 'GET_UNIS', payload: unis });

    setUniSearchWord('');

    //handleSearchUni(uniSearchWord);
    //getUnis();
    //setUniSearchWord('');
  };
  //'http://127.0.0.1:5000/unis/search?' + query,
  const list = async (params) => {
    const query = queryString.stringify(params);
    try {
      let response = await axios.get('http://127.0.0.1:5000/unis', {
        method: 'GET',
      });
      console.log(response.data);
      return response.data;
    } catch (err) {
      console.log(err);
    }
  };

  const search = () => {
    //if (values.search) {
    list({
      //search: values.search || undefined,
      study_discipline: values.study_discipline,
      level: values.level,
      city: values.city,
    }).then((data) => {
      if (data.error) {
        console.log(data.error);
      } else {
        setValues({ ...values, results: data, searched: true });
      }
    });
    //}
  };

  const enterKey = (e) => {
    if (e.keyCode === 13) {
      e.preventDefault();
      search();
    }
  };

  return (
    <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 align-left ">
      <h2 className="mt-4">Explore study options</h2>
      <Form onSubmit={handleSubmit}>
        <Form.Control
          type="text"
          value={uniSearchWord}
          onChange={handleWordChange}
          placeholder="Enter search keywords"
          className="mt-4 "
          aria-label="SearchUni"
          onKeyDown={enterKey}
        />
        <Form.Text id="orText" className="mt-1 mb-1 text-center">
          or
        </Form.Text>

        <Form.Select
          id="study_disciplines"
          value={values.study_discipline}
          onChange={handleChange('study_discipline')}
        >
          <option selected>Select field of study</option>
          {study_disciplines &&
            study_disciplines.map((item) => {
              return (
                <option
                  key={item.study_discipline_id}
                  value={item.study_discipline_id}
                >
                  {item.study_discipline_name}
                </option>
              );
            })}
        </Form.Select>

        <Form.Select
          id="study_levels"
          value={values.level}
          onChange={handleChange('level')}
          className="mt-2"
        >
          <option>Select level of study</option>
          {levels &&
            levels.map((item, i) => {
              return (
                <option key={i} value={item.level}>
                  {item.level}
                </option>
              );
            })}
        </Form.Select>

        <Form.Select
          id="study_cities"
          value={values.city}
          onChange={handleChange('city')}
          className="mt-2"
        >
          <option>Select city of study in Poland</option>
          {cities &&
            cities.map((item, i) => {
              return (
                <option key={i} value={item.city}>
                  {item.city}
                </option>
              );
            })}
        </Form.Select>

        <Button
          className="mt-2 w-100"
          variant="custom"
          type="submit"
          onClick={search}
        >
          Search
        </Button>
        <Select
          onChange={handleChange('study_discipline')}
          //onLoad={fetchFor}
          options={study_disciplines}
          value={values.study_discipline}
          placeholder="Select field of study"
        />
      </Form>
      <UnivercityResults unis={values.results} searched={values.searched} />
    </div>
  );
};

export default Univercity;
