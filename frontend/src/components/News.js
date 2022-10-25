/* eslint-disable prettier/prettier */
import { useState } from 'react';
import Form from 'react-bootstrap/Form';
import ListGroup from 'react-bootstrap/ListGroup';
import { Row, Col } from 'react-bootstrap';
import docs from '../css/docs.css';

const News = () => (
  <div>
    <center>
    <Form role="form" >
    <h1>What is New? </h1>
      <h2 className='h2 mb-5 mt-3'><span style={{ fontWeight: 'bold' }}>Wroclaw</span> | Poland</h2>  
      <h2 className='h1'> New NextBike stations in 2023</h2>
    <Form.Group>
    <Row>           
      {/* <Col lg={6} md={6} sm={12} xs={12}> */}
      <ListGroup variant="numbered" active className='line mb-3 w-25 mt-3'>
        <ListGroup.Item action href='#1'>Health</ListGroup.Item>
        <ListGroup.Item action href='#2'>Politics</ListGroup.Item>
        <ListGroup.Item action href='#3'>Education</ListGroup.Item>
        <ListGroup.Item action href='#4'>Law</ListGroup.Item>
        <ListGroup.Item action href='#6'>Business</ListGroup.Item>
        <ListGroup.Item action href='#5'>Entertainment</ListGroup.Item>
        <ListGroup.Item action href='#7'>Sport</ListGroup.Item>
        <ListGroup.Item action href='#8'>General</ListGroup.Item>
      </ListGroup>  
      {/* </Col>        */}
      
      <Col lg={6} md={6} sm={12} xs={12}>
        <img className='image mb-3'
          src='http://www.wroclaw.pl/en/files/news/13165/wroclawskirowermiejski.jpg'
          alt='example'/>           
          <div>"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"</div>                  
        </Col> 
       
      
      </Row>
      </Form.Group>        
    </Form>
    </center>
    </div>  
  )


export default News;
