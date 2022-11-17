import Button from 'react-bootstrap/Button';
import React from 'react';
import Form from 'react-bootstrap/Form';
import { useState } from 'react';
import axios from 'axios';
function QAform() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('Some answer');
  const [isPending, setIsPending] = useState(false);
  const handleSubmit = async (e) => {
    e.preventDefault();
    setAnswer('');
    const query = { question };
    setIsPending(true);
    console.log(query);
    fetch('http://localhost:5000/qa', {
      method: 'POST',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify(query),
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setAnswer(data);
        console.log(answer);
        setIsPending(false);
      });

    // .then(res => res.json())
    // .then(res => console.log(res))
    // .then(res=>setAnswer(res))
    // .then(setIsPending(false));
  };
  return (
    <div className="QaComponents">
      <Form
        name="QAform"
        onSubmit={handleSubmit}
        action="http://localhost:5000/qa"
        method="post"
      >
        <center>
          <div className="col-sm-6">
            <Form.Group className="mb-3" controlId="question">
              <Form.Label>
                Have any questions? We will try to answer them!
              </Form.Label>
              <Form.Control
                type="question"
                placeholder="Type your question..."
                onChange={(e) => setQuestion(e.target.value)}
                value={question}
              />
            </Form.Group>
          </div>

          {!isPending && (
            <Button variant="primary" type="submit">
              Submit
            </Button>
          )}
          {isPending && (
            <Button disabled variant="primary" type="submit">
              Finding the answer, please wait...
            </Button>
          )}
        </center>
      </Form>
      <center>
        <div className="qa-answer">
          <p value={answer}>
            {' '}
            <br /> <br />
            {answer}
          </p>{' '}
        </div>
      </center>
    </div>
  );
}

export default QAform;
