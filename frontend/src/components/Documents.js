/* eslint-disable prettier/prettier */
import { useEffect, useState } from 'react';
import ListGroup from 'react-bootstrap/ListGroup';
import {Col,Row} from 'react-bootstrap'
import DocumentCard from '../components/DocumentCard';
import axios from 'axios';
// import '..\\frontend\\src\\css\\doc_component.css';

const Documents = () => {
  const [categories,setCategories]=useState([]);
  const [documents,setDocuments]=useState([]);
  const [catID,setCatID]=useState();
  // useEffect(()=>{
  //   fetch("/docs").then(response=>{
  //       return response.json();
  //     }).then(data=>{
  //       setCategories(data);
  //       console.log(categories)
  //     })
  // },[]);
  const handleClick=(e)=>{
    console.log(catID);
    setCatID(e.target.value);
    console.log(catID);
    
  };

  useEffect(()=>{
    const getData=async()=>{
      const {data}  = await axios.get(
        'http://localhost:5000/docs'
      );
    
      setCategories(data[0]);
      setDocuments(data[1]);
      console.log(documents[0])
      console.log(categories[1][1])
    };
    getData();
  },[]);
  
  return (
  <div>    
  
    {/* <center>
    <h1 className='doc_title'>Documents </h1>
    </center> */}
    <Row>
      
      <Col lg={3} md={6} sm={10} xs={10} >
      <ListGroup variant="flush active"  className='line flex-column align-items-start active' 
      value={categories} >
         {categories.map((category_arr)=>{
          return(
             <ListGroup.Item  
             action onClick={handleClick}
             key={category_arr[0]} 
             value={category_arr[0]} 
             >{category_arr[1]}</ListGroup.Item>
          // <div>{category_arr[1]}</div>
            )
         })}
         
      </ListGroup>  
      
      </Col> 
      
      <Col >
      {/* <div className='doc_component'>
      <DocumentCard /> 
      </div> */}
      <ListGroup variant="flush active" value={documents}>
         {documents.map((documents_arr)=>{
           
          return(
            <div >
         
             <ListGroup.Item 
             role="tabpanel"
             aria-labelledby={documents_arr[3]}
             id={documents_arr[3]}
             action href={documents_arr[2]}
             >{documents_arr[1]}</ListGroup.Item>
         
          </div>
            )
         }
        )}
      </ListGroup>  
      </Col>  
      </Row>

    </div>  
  );
};
export default Documents;
