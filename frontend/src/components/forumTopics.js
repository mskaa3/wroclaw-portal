/* eslint-disable prettier/prettier */
import React from 'react';
import ListGroup from 'react-bootstrap/ListGroup';

function ForumTopics() {
  return (
    <div className="text-center">
      <h1>Choose the topic</h1>
      <ListGroup variant="flush active">
        <ListGroup.Item action href='#0'>Foodie</ListGroup.Item>
        <ListGroup.Item action href='#2'>
          International meetings </ListGroup.Item>

        <ListGroup.Item action href='#1'>Entertainment&events </ListGroup.Item>
        <ListGroup.Item action href='#2'>Shops</ListGroup.Item>
        <ListGroup.Item action href='#3'>Parties
      
        </ListGroup.Item>
        <ListGroup.Item action href='#4'>Help</ListGroup.Item>
        <ListGroup.Item action href='#5'>Off-topic</ListGroup.Item>
      </ListGroup>
    </div>
    
  );
}

export default ForumTopics;
