import React from 'react';
import { Container, Card, Col, Row } from 'react-bootstrap';
import '../../css/index.css';
import { Link } from 'react-router-dom';

const UniversityCard = ({ uni, uni_key }) => {
  return (
    <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 mt-3 mb-2">
      <Card border="info" className="w-100">
        <Card.Body>
          <Container>
            <Row className="d-flex align-items-baseline mb-3">
              <Col lg={2} md={2} sm={2} xs={2}>
                <Card.Img variant="top" src={uni.logo} />
              </Col>
              <Col>
                <Card.Title>{uni.uni_name}</Card.Title>
              </Col>
            </Row>

            <Row>
              <Col className="text-left ">
                <Link to={`/courses/uni/${uni_key}`}>View Courses</Link>
              </Col>
              <Col className="text-align-center">
                <Card.Link href={uni.www}>Visit Vebsite</Card.Link>
              </Col>
              <Col className="text-align-center">
                <Card.Link href="#">Contact this institution</Card.Link>
              </Col>
            </Row>
          </Container>
        </Card.Body>
      </Card>
    </div>
  );
};

export default UniversityCard;
