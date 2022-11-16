import React, { useState, useEffect } from 'react';
import TopicList from '../components/forum/TopicList';
import { Header, Segment } from 'semantic-ui-react';
import axios from 'axios';
//import {fetchForums} from '../../actions';
import '../css/index.css';

//const mapStateToProps = state => ({
//  isLoading: state.home.isLoading,
//  forums: state.home.forums,
//  error: state.home.error,
//});

//const mapDispatchToProps = dispatch => ({
//  fetchForums: () => {
//   dispatch(fetchForums());
//  },
//});
/*
const topics = [
  {
    name: 'Topic 1',
    slug: 'topic_1 ',
    description: 'All about number 1',
    posts_count: 5,
    threads_count: 2,
    last_activity: null,
  },
  {
    name: 'Topic 2',
    slug: 'topic_2 ',
    description: 'All about pair things',
    posts_count: 10,
    threads_count: 3,
    last_activity: null,
  },
];
*/
const ForumScreen2 = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [topics, setTopics] = useState(null);
  useEffect(() => {
    const fetchTopics = async () => {
      const { data } = await axios.get('http://127.0.0.1:5000/forum/topics');

      setTopics(data);
    };

    fetchTopics();
  }, []);

  return (
    <>
      <Header size="huge" color="violet" className="forum-header">
        Wroclaw Portal Topics
      </Header>
      <TopicList isLoading={isLoading} error={error} topics={topics} />;
    </>
  );
};

export default ForumScreen2;
