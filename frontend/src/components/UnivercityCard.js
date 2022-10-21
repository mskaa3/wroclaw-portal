import React from 'react';
import { Container, Image, Card } from 'react-bootstrap';

const UnivercityCard = () => {
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="holder.js/100px180" />
      <Card.Body>
        <Card.Title>Univercity Title</Card.Title>
        <Card.Text>
          Institution Type: Univercity/ Higher Education Institution
        </Card.Text>

        <Card.Link href="#">View Courses</Card.Link>
        <Card.Link href="#">Visit Vebsite</Card.Link>
        <Card.Link href="#">Contact this institution</Card.Link>
      </Card.Body>
    </Card>
  );
};

export default UnivercityCard;
