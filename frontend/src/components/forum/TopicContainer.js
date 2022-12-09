import React, { useEffect, useState, useContext } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Button } from 'react-bootstrap';
import axios from 'axios';
import TopicThreadList from './TopicThreadList';
import NewThread from './NewThread';
import AuthContext from '../../context/auth/AuthContext';
import './style.css';

import {
  createThreadSave,
  //fetchTopic,
  createThread,
} from '../../context/auth/AuthActions';

const TopicContainer = () => {
  const { topic_id } = useParams();
  console.log(topic_id);
  const navigate = useNavigate();
  const {
    dispatch,
    isAuthenticated,
    newThreadShow,
    newThreadError,
    newThreadId,
    newThreadName,
    newThreadContent,
    newThreadLoading,
    newThreadSuccess,
    user,
  } = useContext(AuthContext);

  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [threads, setThreads] = useState(null);
  const [topic, setTopic] = useState(null);

  //const [newThreadState, setNewThreadState] = useState({
  //newThreadLoading: false,
  //newThreadSuccess: false,
  //newThreadName: '',
  //newThreadContent: '',
  //newThreadId: null,
  //newThreadError: null,
  //newThreadShow: false,
  //});

  useEffect(() => {
    const fetchTopic = async () => {
      const { data } = await axios.get(
        `http://127.0.0.1:5000/forum/topics/${topic_id}`
      );
      console.log('topic data');
      console.log(data);
      setTopic(data);
    };

    fetchTopic();
  }, [topic_id]);

  useEffect(() => {
    const fetchThreads = async () => {
      const { data } = await axios.get(
        `http://127.0.0.1:5000/forum/topics/${topic_id}/threads`
      );
      console.log('threads data');
      console.log(data);
      setThreads(data);
    };

    fetchThreads();
  }, [topic_id, newThreadId]);

  //const {
  //  isLoading,
  //  name,
  //  slug,
  //  description,
  //  threads,
  //  error,
  //newThreadLoading,
  //newThreadSuccess,
  //newThreadName,
  //newThreadContent,
  // newThreadId,
  //newThreadError,
  //newThreadShow,
  //} = this.props;

  //const { topic_name, slug, description } = topic;

  const createThreadToggle = () => {
    dispatch({ type: 'CREATE_THREAD_TOGGLE' });
  };
  return (
    <div>
      <NewThread
        topic={topic_id}
        isAuthenticated={isAuthenticated}
        isLoading={newThreadLoading}
        success={newThreadSuccess}
        thread_name={newThreadName}
        thread_content={newThreadContent}
        id={newThreadId}
        error={newThreadError}
        showEditor={newThreadShow}
        createThread={createThread}
        updateNewThread={createThreadSave}
        toggleShowEditor={createThreadToggle}
        maxLength={2000}
        user={user}
        dispatch={dispatch}
      />
      <Button
        className="mt-3 w-40 mb-3"
        variant="custom"
        type="submit"
        onClick={() => navigate(-1)}
      >
        <i className="fa-solid fa-left-long"></i> &nbsp;Back to topics
      </Button>
      <TopicThreadList
        isLoading={isLoading}
        threads={threads}
        error={error}
        topic={topic}
      />
    </div>
  );
};

export default TopicContainer;
