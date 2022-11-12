import React, { useEffect, useState, useContext } from 'react';
import { Form, Button } from 'react-bootstrap';
import UnivercityContext from '../../context/uni/UnivercityContext';

import {
  searchUnisByWord,
  getStudyDisciplines,
  getUnis,
  searchUnisByFilters,
} from '../../context/uni/UnivercityActions';
import axios from 'axios';

const UniversitySearch = () => {
  const [uniSearchWord, setUniSearchWord] = useState('');

  const { unis, dispatch, city, level, discipline } =
    useContext(UnivercityContext);

  const [disciplines, setDisciplines] = useState([]);
  const [levels, setLevels] = useState([]);
  const [cities, setCities] = useState([]);
  /*
  const [values, setValues] = useState({
    discipline: '',
    level: '',
    city: '',
    results: [],
    searched: false,
  });
*/
  const handleWordChange = (e) => {
    setUniSearchWord(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    dispatch({ type: 'SET_LOADING' });
    //const unis = await searchUnis(uniSearchWord);
    const disciplines = await getStudyDisciplines();
    //console.log('from univercity try to print disciplines');
    //console.log(disciplines);
    if (!Array.isArray(disciplines)) {
      console.log(
        'From Univercity: Not an array There was an error loading your data!'
      );
    }

    dispatch({ type: 'GET_STUDY_DISCIPLINES', payload: disciplines });

    //setStudyDiscipline(event.target.value);

    //handleSearchUni(uniSearchWord);
    //getUnis();
    //setUniSearchWord('');
  };
  useEffect(() => {
    const fetchDisciplines = async () => {
      const { data } = await axios.get('http://127.0.0.1:5000/disciplines');

      setDisciplines(data);
    };

    const fetchLevels = async () => {
      const { data } = await axios.get('http://127.0.0.1:5000/courses/levels');
      setLevels(data);
    };

    const fetchCities = async () => {
      const { data } = await axios.get('http://127.0.0.1:5000/unis/cities');
      setCities(data);
    };

    fetchDisciplines();
    fetchLevels();
    fetchCities();
  }, []);

  const handleChange = (name) => (event) => {
    //setValues({ ...values, [name]: event.target.value });
    dispatch({
      type: 'SET_' + name.toUpperCase() + '_FILTER',
      payload: event.target.value,
    });
  };
  /*
  const handleSubmit1 = async (e) => {
    e.preventDefault();

    dispatch({ type: 'SET_LOADING' });
    //const unis = await searchUnis(uniSearchWord);
    const unis = await getUnis(uniSearchWord);
    //console.log('from univercity try to print unis');
    //console.log(unis);
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
*/
  //'http://127.0.0.1:5000/unis/search?' + query,
  /*
  const list = async (params) => {
    const query = queryString.stringify(params);
    //console.log(query);
    try {
      //let response = await axios.get('http://127.0.0.1:5000/unis?'+query, {
      let response = await axios.get(
        'http://localhost:5000/unis/search?' + query,
        {
          method: 'GET',
        }
      );
      //console.log(response.data);
      return response.data;
    } catch (err) {
      console.log(err);
    }
  };

  const search = () => {
    //if (values.search) {
    list({
      //search: values.search || undefined,
      discipline_name: values.discipline,
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
*/
  const handleSearch = async (e) => {
    e.preventDefault();

    dispatch({ type: 'SET_LOADING' });
    //const unis = await searchUnis(uniSearchWord);
    const searchResults = await searchUnisByFilters(discipline, level, city);
    //console.log('result from searchUnisByFilters');
    //console.log(searchResults);
    if (!Array.isArray(searchResults)) {
      console.log(
        'From Univercity after search: Not an array There was an error loading your data!'
      );
    }

    dispatch({ type: 'SEARCH_UNIS_BY_FILTERS', payload: searchResults });

    setUniSearchWord('');

    //handleSearchUni(uniSearchWord);
    //getUnis();
    //setUniSearchWord('');
  };
  /*
  const enterKey = (e) => {
    if (e.keyCode === 13) {
      e.preventDefault();
      search();
    }
  };
*/
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
          //onKeyDown={enterKey}
        />
        <Form.Text id="orText" className="mt-1 mb-1 text-center">
          or
        </Form.Text>

        <Form.Select
          id="disciplines"
          value={discipline}
          onChange={handleChange('discipline')}
        >
          {!discipline && <option value="">Select field of study</option>}

          {disciplines &&
            disciplines.map((item) => {
              return (
                <option key={item.discipline_id} value={item.discipline_id}>
                  {item.discipline_name}
                </option>
              );
            })}
        </Form.Select>

        <Form.Select
          id="levels"
          value={level}
          onChange={handleChange('level')}
          className="mt-2"
        >
          {!level && <option value="">Select level of study</option>}

          {levels &&
            levels.map((item) => {
              return (
                <option key={item.course_level_id} value={item.course_level_id}>
                  {item.course_level_name}
                </option>
              );
            })}
        </Form.Select>

        <Form.Select
          id="cities"
          value={city}
          onChange={handleChange('city')}
          className="mt-2"
        >
          {!city && <option value="">Select city of study in Poland</option>}

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
          //onClick={search}
        >
          Search - does not work yet
        </Button>

        <Button
          className="mt-2 w-100"
          variant="custom"
          type="submit"
          onClick={handleSearch}
        >
          Search by filters
        </Button>
      </Form>
    </div>
  );
};

export default UniversitySearch;
