/* eslint-disable prettier/prettier */

import axios from 'axios';
import Button from 'react-bootstrap/Button';
import docs from '../css/docs.css';
import { useEffect, useState ,useMemo} from 'react';
import { NewsContext } from "../NewsContext";
import NewsArticle from "./NewsArticle";
import React, { useContext } from "react";
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

function News() {
  const [sources,setSources]=useState([]);
  const [news,setNews]=useState([]);
  const [sourceID,setSourceID]=useState();
  /* eslint-disable prettier/prettier */
  const [filtered,setFiltered]=useState(false);

  const handleClick=(e)=>{
    setSourceID( parseInt(e.target.value));
    console.log(sourceID);
    setFiltered(true);
    
  };

  function getFilteredList() {
    if (!setSourceID) {
      return NaN;
    }
        
    return news.filter(news=>news.source===sourceID);
   
  }
  var filteredNews = useMemo(getFilteredList, [sourceID, news]);

  

  useEffect(()=>{
    const getData=async()=>{
      const {data}  = await axios.get(
        'http://localhost:5000/news'
      );
    
      setSources(data[0]);
      setFiltered(data[0]);
      setNews(data[1]);
      // console.log(documents[0])
      
    };
    getData();
  },[]);
  
  // const { data } = useContext(NewsContext);
  // console.log(data);

  return (
    <div>
      <center>
      <h1 className="head__text">News</h1>
      {/* <DropdownButton id="dropdown-item-button" title="Dropdown button"  value={sources}>
      {sources.map((source)=>{
          return (
             <Dropdown.Item as button
             action onClick={handleClick}
             value={source[0]} 
             >{source[1]}</Dropdown.Item>
            )
        })}
      </DropdownButton> */}
      </center>
      {!filtered && (
      
      <div className="all__news">
        {news
          ? news.map((single_news) => (
              <NewsArticle data={single_news} key={single_news.url} />
            ))
          : "Loading"}
      </div>
      )}
      {filtered && (
      
      <div className="all__news">
        {news
          ? news.map((single_news) => (
              <NewsArticle data={single_news} key={single_news.id} />
            ))
          : "Loading"}
      </div>
      )}
      <center><Button variant="primary" type="submit">
      Load more
      </Button></center>
    </div>

      
  );  
}

export default News;
