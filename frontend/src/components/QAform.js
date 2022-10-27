/* eslint-disable prettier/prettier */
import Button from 'react-bootstrap/Button';
import React from 'react';
import Form from 'react-bootstrap/Form';


function QAform() {

  return (
    <div className="QaComponents">
    <Form name="QAform">
     <center>
     <div className="col-sm-6">
      <Form.Group className="mb-3" controlId="formQuestion">
        <Form.Label>Have any questions? We will try to answer them!</Form.Label>
        <Form.Control type="email" placeholder="Type your question..." />

      </Form.Group>
    </div>
    
      <Button variant="primary" type="submit">
        Submit
      </Button>
      
       </center>
       
    </Form>
        <center>
          <div className="ga-answer"> <p> <br/> <br/> Just some generated answer</p> </div></center>
    
    </div>
    
    
  );
}

export default QAform;
