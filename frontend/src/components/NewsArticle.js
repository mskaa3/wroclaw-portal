/* eslint-disable prettier/prettier */
import React from 'react';

function NewsArticle({ data }) {
  const openInNewTab = (url) => {
    const newWindow = window.open(url, '_blank', 'noopener,noreferrer')
    if (newWindow) newWindow.opener = null
  }

  return (
    <div className="news" onClick={() => openInNewTab(data.url)}>
      <h1 className="news__title">{data.title}</h1>
      <p className="news__desc">{data.description}</p>
      <span className="image" img src={data.image}></span>
      <span className="news__published">{data.date}</span>
      {/* <span className="news__source">{data.source}</span> */}
      
    </div>
  );
}

export default NewsArticle;
