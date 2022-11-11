import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

const Footer = () => {
  return (
    <footer>
      <Container>
        <Row>
          <Col className="text-center py-3">
            <h6>Have any questions?</h6>
            <a href="mailto:sales@example.com" className="contact-link">
              sales@example.com
            </a>
          </Col>
          <Col className="text-center py-3">Copyright &copy; WroclawPortal</Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;
