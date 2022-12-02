import React from 'react';

import { Container, Card, Col, Row } from 'react-bootstrap';
import '../../css/index.css';

const CourseCard = ({ course }) => {
  return (
    <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 mt-3 mb-3">
      <Card border="info" className="w-100">
        <Card.Body>
          <Container>
            <Row className="d-flex align-items-baseline text-center">
              <Col>
                <Card.Title>{course.course_name}</Card.Title>
              </Col>
            </Row>
            <Row>
              <Col>
                <Card.Text>
                  <strong>Course form:</strong>
                </Card.Text>
              </Col>
              <Col>
                <Card.Text>{course.form}</Card.Text>
              </Col>
            </Row>
            <Row>
              <Col>
                <Card.Text>
                  <strong>Course title:</strong>
                </Card.Text>
              </Col>
              <Col>
                <Card.Text>{course.title}</Card.Text>
              </Col>
            </Row>
            <Row>
              <Col>
                <Card.Text>
                  <strong>Course level:</strong>
                </Card.Text>
              </Col>
              <Col>
                <Card.Text>{course.level}</Card.Text>
              </Col>
            </Row>
            <Row>
              <Col>
                <Card.Text>
                  <strong>Course ECTS:</strong>
                </Card.Text>
              </Col>
              <Col>
                <Card.Text>{course.ects}</Card.Text>
              </Col>
            </Row>
            <Row>
              <Col>
                <Card.Text>
                  <strong>Number of semesters:</strong>
                </Card.Text>
              </Col>
              <Col>
                <Card.Text>{course.semesters_number}</Card.Text>
              </Col>
            </Row>
            <Row>
              <Col>
                <Card.Text>
                  <strong>Course language:</strong>
                </Card.Text>
              </Col>
              <Col>
                <Card.Text>{course.language}</Card.Text>
              </Col>
            </Row>
          </Container>
        </Card.Body>
      </Card>
    </div>
  );
};

export default CourseCard;
