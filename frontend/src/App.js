//import './App.css';
import 'bootstrap/dist/css/bootstrap.css';

import { Container } from 'react-bootstrap';
import Header from './components/Header';
import Footer from './components/Footer';

const App = () => {
  return (
    <>
      <Header title="Wroclaw Portal" />

      <main>
        <Container>
          <h1>Wroclaw Portal</h1>
        </Container>
      </main>

      <Footer />
    </>
  );
};

export default App;
