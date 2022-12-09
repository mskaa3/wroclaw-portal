/* eslint-disable prettier/prettier */
import React from 'react';

function NewsArticle({ data }) {
  return (
    <div className="news">
      <h1 className="news__title">{data.title}</h1>
      <p className="news__desc">{data.description}</p>
     
      <span className="news__published">{data.date}</span>
      <span className="news__source">{data.source}</span>
    </div>
  );
}

export default NewsArticle;
