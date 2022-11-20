/* eslint-disable prettier/prettier */
import './css/App.css';
import 'bootstrap/dist/css/bootstrap.css';
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from 'react-router-dom';
import { Container } from 'react-bootstrap';
//import axios from 'axios';
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
import HomeContentScreen from './screens/HomeContentScreen';
import CourseScreen from './screens/CourseScreen';
import ForumScreen2 from './screens/ForumScreen2';
import { UnivercityProvider } from './context/uni/UnivercityContext';
import TopicContainer from './components/forum/TopicContainer';
import ThreadContainer from './components/forum/ThreadContainer';
//import { useState, useEffect } from 'react';
import { NewsContextProvider } from './NewsContext';
import News from './components/News';
import SignupScreen from './screens/SignupScreen';
import HomeTextComponent from './components/HomeTextComponent';
//import Univercity from './components/Univercity';

//const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';



const App = () => {
  return (
    <UnivercityProvider>
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
              <Route exact path="/forum" element={<ForumScreen2 />} />
              <Route exact path="/docs" element={<DocumentsScreen />} />
              <Route exact path="/qa" element={<QaScreen />} />
              <Route exact path="/login" element={<LoginScreen />} />
              <Route exact path="/courses/uni/:id" element={<CourseScreen />} />
              
              <Route
                exact path="/forum/topics/:topic_id"
                element={<TopicContainer />}
              />
              <Route
                exact path="/threads/:thread_id"
                element={<ThreadContainer />}
              />
            </Routes>
          </Container>
        </main>

        <Footer />
      </Router>
    </UnivercityProvider>
  );
};

export default App;
