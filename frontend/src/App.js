//import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Container } from 'react-bootstrap';
import Header from './components/Header';
import Footer from './components/Footer';
import HomeScreen from './screens/HomeScreen';
import UniversityScreen from './screens/UniversityScreen';
import CurrencyScreen from './screens/CurrencyScreen';
import DocumentsScreen from './screens/DocumentsScreen';
import ForumScreen from './screens/ForumScreen';
import MapScreen from './screens/MapScreen';
import NewsScreen from './screens/NewsScreen';
import QaScreen from './screens/QaScreen';
import LoginScreen from './screens/LoginScreen';

const App = () => {
  return (
    <Router>
      <HomeScreen />
      <Header title="Wroclaw Portal" />

      <main>
        <Container>
          <Routes>
            <Route exact path="/currency" element={<CurrencyScreen />} />
            <Route exact path="/uni" element={<UniversityScreen />} />
            <Route exact path="/news" element={<NewsScreen />} />
            <Route exact path="/map" element={<MapScreen />} />
            <Route exact path="/forum" element={<ForumScreen />} />
            <Route exact path="/docs" element={<DocumentsScreen />} />
            <Route exact path="/qa" element={<QaScreen />} />
            <Route exact path="/login" element={<LoginScreen />} />
          </Routes>
        </Container>
      </main>

      <Footer />
    </Router>
  );
};

export default App;
