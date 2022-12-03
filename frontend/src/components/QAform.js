import Button from 'react-bootstrap/Button';
import React from 'react';
import Form from 'react-bootstrap/Form';
import { useState } from 'react';
import ListGroup from 'react-bootstrap/ListGroup';
import '../css/qa.css';
import Card from 'react-bootstrap/Card';

function QAform() {
  const [question, setQuestion] = useState('');
  const [answers, setAnswers] = useState([]);
  const [isPending, setIsPending] = useState(false);
  const [isAnswered, setIsAnswered] = useState(false);
  const handleSubmit = async (e) => {
    e.preventDefault();
    const query = { question };
    setIsPending(true);
    console.log(query);
    fetch('http://127.0.0.1:5000/qa', {
      method: 'POST',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify(query),
    }).then((response) => {
      response.json().then((data) => {
        console.log(data);
        setAnswers(data);
        setIsPending(false);
        setIsAnswered(true);
      });
    });
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
              <h3>Have any questions? We will try to answer them!</h3>
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

      <div className="answers-component">
        {isAnswered && <h2>Most relevant results:</h2>}
        <ListGroup>
          {answers.map((answ) => {
            return (
              <div className="single-answer">
                <Card key={answ.id}>
                  <Card.Body>
                    <Card.Title>{answ.answer}</Card.Title>
                    <Card.Text>...{answ.context}...</Card.Text>
                    <Card.Link href={answ.link}>Read more...</Card.Link>
                  </Card.Body>
                </Card>
              </div>
            );
          })}
        </ListGroup>
      </div>
    </div>
  );
}

export default QAform;
