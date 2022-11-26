import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

const Footer = () => {
  const footerYear = new Date().getFullYear();
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
          <Col className="text-center py-3">
            Copyright &copy;
            {footerYear} All rigts reserved
          </Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;
