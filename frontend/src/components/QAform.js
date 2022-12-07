/* eslint-disable prettier/prettier */
import Button from 'react-bootstrap/Button';
import React from 'react';
import Form from 'react-bootstrap/Form';
import Badge from 'react-bootstrap/Badge';
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
        console.log(decodeURIComponent(escape((data[1].context))));
        setAnswers(data);
        setIsPending(false);
        setIsAnswered(true);
      });
    });
  };
  return (
    <div className="QaComponents">
       <Card className='qa-submit'>

        <Card.Body>
          <center>
          <Card.Title>Have any questions? We will try to answer them!</Card.Title>
          </center>
          <Card.Text>
          <Form
        name="QAform"
        onSubmit={handleSubmit}
        action="http://localhost:5000/qa"
        method="post"
      >
        <center>
          <div className="col-sm-6">
            <Form.Group className="mb-3 mt-4" controlId="question" >
              
              <Form.Control
                type="question"
                placeholder="Type your question..."
                onChange={(e) => setQuestion(e.target.value)}
                value={question}
              />
            </Form.Group>
          </div>
          <div>
          <Badge bg="primary">#Culture</Badge>{' '}
          <Badge bg="secondary">#Transport</Badge>{' '}
          <Badge bg="success">#Legal stay</Badge> {' '}
          <Badge bg="danger">#Work</Badge>{' '}
          <Badge bg="warning" text="dark">
            #Studies
          </Badge>{' '}
          <Badge bg="info">#Costs</Badge>{' '}
          <Badge bg="light" text="dark">
            #Accomodation
          </Badge>{' '}
          <Badge bg="dark">#Others</Badge>

        </div>
        <br /><br />
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
          </Card.Text>
          
        </Card.Body>
      </Card>
      {/* <Form
        name="QAform"
        onSubmit={handleSubmit}
        action="http://localhost:5000/qa"
        method="post"
      >
        <center>
          <div className="col-sm-6">
            <Form.Group className="mb-3 mt-4" controlId="question" >
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
      </Form> */}

      <div className="answers-component">
        {isAnswered && <h2>Most relevant results:</h2>}
        <ListGroup>
          {answers.map((answ) => {
            return (
              <div className="single-answer">
                <Card key={answ.id}>
                  <Card.Body>
                    <Card.Title>{decodeURIComponent(escape(answ.answer))}</Card.Title>
                    <Card.Text>...{decodeURIComponent(escape(answ.context))}...</Card.Text>
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
