/* eslint-disable prettier/prettier */
import { useState } from 'react';
import Form from 'react-bootstrap/Form';
import ListGroup from 'react-bootstrap/ListGroup';
import {Col} from 'react-bootstrap'

const News = () => (
  <div>    
    <Form role="form" >
    <center>
    <h1>Documents </h1>
    <Form.Group>              
      <Col lg={6} md={6} sm={12} xs={12}>
      <ListGroup variant="flush active" active className='line mb-3 w-25 mt-3'>
        <ListGroup.Item action href='#1'>Health</ListGroup.Item>
        <ListGroup.Item action href='#2'>Politics</ListGroup.Item>
        <ListGroup.Item action href='#3'>Education</ListGroup.Item>
        <ListGroup.Item action href='#4'>Law</ListGroup.Item>
        <ListGroup.Item action href='#6'>Business</ListGroup.Item>
        <ListGroup.Item action href='#5'>Entertainment</ListGroup.Item>
        <ListGroup.Item action href='#7'>Sport</ListGroup.Item>
        <ListGroup.Item action href='#8'>General</ListGroup.Item>
      </ListGroup>  
      </Col>       
      </Form.Group>  
      </center>      
    </Form>   
    </div>  
  )
export default News;
