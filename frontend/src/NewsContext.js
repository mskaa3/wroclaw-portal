/* eslint-disable prettier/prettier */
import React, { createContext, useEffect, useState } from 'react';
import axios from 'axios';

export const NewsContext = createContext();

export const NewsContextProvider = (props) => {
  const [data, setData] = useState();
  //const apiKey = '35a4565a46f646e5a4304d38dec3646e';

  useEffect(() => {
    axios
      .get(
        `https://newsapi.org/v2/everything?q=Wrocław&language=pl&from=2022-10-10&sortBy=publishedAt&apiKey=35a4565a46f646e5a4304d38dec3646e`
      )
      .then((response) => setData(response.data))
      .catch((error) => console.log(error));
  }, []);

  return (
    <NewsContext.Provider value={{ data }}>
      {props.children}
    </NewsContext.Provider>
  );
};



