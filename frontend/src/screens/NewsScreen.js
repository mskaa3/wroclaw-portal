import React from 'react';
import News from '../components/News';
import { NewsContextProvider } from '../NewsContext';

const NewsScreen = () => {
  return (
    <div>
      <NewsContextProvider>
        <News />
      </NewsContextProvider>
    </div>
  );
};

export default NewsScreen;
