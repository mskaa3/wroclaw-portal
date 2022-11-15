/* eslint-disable prettier/prettier */
import { useEffect, useState } from 'react';
import Form from 'react-bootstrap/Form';
import ListGroup from 'react-bootstrap/ListGroup';
import {Col,Row} from 'react-bootstrap'
import DocumentCard from '../components/DocumentCard';
import axios from 'axios';
import '..\\frontend\\src\\css\\doc_component.css';

const News = () => {
  const [categories,setCategories]=useState([]);

  useEffect(()=>{
    fetch("/docs").then(
      resp=>resp.json()).then(
        data=>console.log(data))
      // data=>{
      //   setCategories(data);
      //   console.log(data)
      // }
    
  },[]);
  // useEffect(()=>{
  //   const getDocuments=async()=>{
  //     const { data } = await axios.get(
  //       '/docs'
  //     );
  //     setCategories(data);
  //     console.log(data)
  //   };
  //   getDocuments();
  // },[]);
  
  return (
  <div>    
  
    {/* <center>
    <h1 className='doc_title'>Documents </h1>
    </center> */}
    <Row>
      <Col lg={6} md={6} sm={12} xs={12}>
      <ListGroup variant="flush active" active className='line mb-3 w-25 mt-3' 
      value={categories}>
        <ListGroup.Item action href='#1'>Health</ListGroup.Item>
        <ListGroup.Item action href='#2'>Politics</ListGroup.Item>
        <ListGroup.Item action href='#3'>Education</ListGroup.Item>
        <ListGroup.Item action href='#4'>Law</ListGroup.Item>
        <ListGroup.Item action href='#6'>Business</ListGroup.Item>
        <ListGroup.Item action href='#5'>Entertainment</ListGroup.Item>
        <ListGroup.Item action href='#7'>Sport</ListGroup.Item>
        <ListGroup.Item action href='#8'>Genecral</ListGroup.Item>
         {/* {categories&&categories.map((item)=>{
          return(
            <ListGroup.Item key={item.id} value={item.category} action href='#8'>{item.category}</ListGroup.Item>
          )
         })} */}
         
      </ListGroup>  

      </Col> 
      <Col>
      <div className='doc_component'>
      <DocumentCard /> 
      </div>
      </Col>  
      </Row>

    </div>  
  );
};
export default News;
