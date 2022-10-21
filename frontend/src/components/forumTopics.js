/* eslint-disable prettier/prettier */
import ListGroup from 'react-bootstrap/ListGroup';

function FlushExample() {
  return (
    <center>
      <h1>Choose the topic</h1>
      <ListGroup variant="flush" active>
        <ListGroup.Item>Food&Entertainment</ListGroup.Item>
        <ListGroup.Item>
          International meetings
         
        </ListGroup.Item>

        <ListGroup.Item>Bank</ListGroup.Item>
        <ListGroup.Item>Job</ListGroup.Item>
        <ListGroup.Item>
          Insurance
      
        </ListGroup.Item>
        <ListGroup.Item>Help</ListGroup.Item>
        <ListGroup.Item>General</ListGroup.Item>
      </ListGroup>
    </center>
  );
}

export default FlushExample;
