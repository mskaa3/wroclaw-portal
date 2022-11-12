import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function QAform() {
  return (
    <Form>
      <center>
        <div className="col-sm-6">
          <Form.Group className="mb-3" controlId="formQuestion">
            <Form.Label>
              Have any questions? We will try to answer them!
            </Form.Label>
            <Form.Control type="email" placeholder="Type your question..." />
          </Form.Group>
        </div>

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </center>
    </Form>
  );
}

export default QAform;
