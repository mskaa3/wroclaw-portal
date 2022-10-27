import React from 'react';
import { Form, Button } from 'react-bootstrap';

const Univercity = ({ handleSubmit, uniSearchWord, setUniSearchWord }) => {
  return (
    <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 align-left ">
      <h2 className="mt-4">Explore study options</h2>

      <Form onSubmit={handleSubmit}>
        <Form.Control
          type="text"
          value={uniSearchWord}
          onChange={(e) => setUniSearchWord(e.target.value)}
          placeholder="Enter search keywords"
          className="mt-4 "
          aria-label="SearchUni"
        />
        <Form.Text id="orText" className="mt-1 mb-1 text-center">
          or
        </Form.Text>

        <Form.Select>
          <option>Select field of study</option>
          <option value="1">One</option>
          <option value="2">Two</option>
          <option value="3">Three</option>
        </Form.Select>

        <Form.Select className="mt-2">
          <option>Select level of study</option>
          <option value="1">One</option>
          <option value="2">Two</option>
          <option value="3">Three</option>
        </Form.Select>

        <Form.Select className="mt-2">
          <option>Select city of study in Poland</option>
          <option value="1">One</option>
          <option value="2">Two</option>
          <option value="3">Three</option>
        </Form.Select>

        <Button className="mt-2 w-100" variant="custom" type="submit">
          Search
        </Button>
      </Form>
    </div>
  );
};

export default Univercity;
