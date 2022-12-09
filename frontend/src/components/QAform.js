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
                placeholder='Type your question...'
                onChange={(e) => setQuestion(e.target.value)}
                value={question}
              />
            </Form.Group>
          </div>
          <div>
          <Button variant="primary" className="google p-0" onClick={() => setQuestion('Is there a cinema for foreigners?')}>#Culture</Button>{' '}
          <Button variant="secondary" onClick={() => setQuestion('How much is a bus ticket?')}>#Transport</Button>{' '}
          <Button variant="success" onClick={() => setQuestion('What is PESEL?')}>#Legal stay</Button> {' '}
          <Button variant="danger" onClick={() => setQuestion('Can I work legally as a student?')}>#Work</Button>{' '}
          <Button variant="info" onClick={() => setQuestion('What is the university cost in Poland?')} >
            #Studies
          </Button>{' '}
          <Button variant="help" onClick={() => setQuestion('How much are eggs?')}>#Costs</Button>{' '}
          <Button variant="success" onClick={() => setQuestion('Where can I look for a flat to rent?')}>
            #Accomodation
          </Button>{' '}
          <Button variant="primary" onClick={() => setQuestion('Are there any international groups?')}>#Others</Button>

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
