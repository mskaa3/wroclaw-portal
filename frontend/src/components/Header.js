import React from 'react';
import {
  Navbar,
  Container,
  Nav,
  Form,
  Button,
  NavDropdown,
} from 'react-bootstrap';

const Header = ({ title }) => {
  return (
    <>
      <Navbar bg="light" expand="lg">
        <Container fluid>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll">
            <Nav
              className="ms-auto my-2 my-lg-0"
              style={{ maxHeight: '100px' }}
              navbarScroll
            >
              <Form className="d-flex">
                <Form.Control
                  type="search"
                  placeholder="Search the website"
                  className="me-2"
                  aria-label="Search"
                />
                <Button variant="outline-success">Search</Button>
              </Form>
              &nbsp;&nbsp;
              <NavDropdown title="Language" id="navbarScrollingDropdown">
                <NavDropdown.Item href="#action3"> Action</NavDropdown.Item>
                <NavDropdown.Item href="#action4">
                  Another action
                </NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action5">
                  Something else here
                </NavDropdown.Item>
              </NavDropdown>
              &nbsp;&nbsp;
              <Nav.Link href="#action12">
                <i className="fa-solid fa-coins"></i> Currency
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <Navbar bg="light" expand="lg">
        <Container fluid>
          <Navbar.Brand href="/">{title}</Navbar.Brand>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll">
            <Nav
              className="ms-auto my-2 my-lg-0"
              style={{ maxHeight: '100px' }}
              navbarScroll
            >
              <Nav.Link href="#action1">
                <i className="fa-solid fa-house"></i> Home
              </Nav.Link>
              <Nav.Link href="#action6">
                <i className="fa-solid fa-square-rss"></i> News
              </Nav.Link>
              <Nav.Link href="#action7">
                <i className="fa-solid fa-building-columns"></i> Universities
              </Nav.Link>
              <Nav.Link href="#action8">
                <i className="fa-solid fa-map-location-dot"></i> Map
              </Nav.Link>
              <Nav.Link href="#action9">
                <i className="fa-solid fa-message"></i> Forum
              </Nav.Link>
              <Nav.Link href="#action10">
                <i className="fa-solid fa-file-invoice"></i> Documents
              </Nav.Link>
              <Nav.Link href="#action11">Translator</Nav.Link>

              <Nav.Link href="#" disabled>
                Link
              </Nav.Link>
              <Nav.Link href="#action13">
                <i className="fa-solid fa-user-graduate"></i> Sign In
              </Nav.Link>
            </Nav>
            <> </>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
};

export default Header;
