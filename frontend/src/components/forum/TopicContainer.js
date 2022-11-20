import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import TopicThreadList from './TopicThreadList';
import NewThread from './NewThread';

import './style.css';

//import {
//  createThreadSave,
// createThreadToggle,
//  fetchForum,
//  createThread,
//} from '../../actions';

const TopicContainer = (props) => {
  const { topic_id } = useParams();
  console.log(topic_id);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [threads, setThreads] = useState(null);
  const [topic, setTopic] = useState(null);

  const [newThreadState, setNewThreadState] = useState({
    newThreadLoading: false,
    newThreadSuccess: false,
    newThreadName: '',
    newThreadContent: '',
    newThreadId: null,
    newThreadError: null,
    newThreadShow: false,
  });

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
  }, [topic_id]);
  //const {
  //  isLoading,
  //  name,
  //  slug,
  //  description,
  //  threads,
  //  error,
  //isAuthenticated,
  //newThreadLoading,
  //newThreadSuccess,
  //newThreadName,
  //newThreadContent,
  // newThreadId,
  //newThreadError,
  //newThreadShow,
  //createThread,
  //createThreadSave,
  //createThreadToggle,
  //} = this.props;

  //const { topic_name, slug, description } = topic;

  const isAuthenticated = () => {};

  const createThread = (newThread) => {};

  const createThreadSave = (newThread) => {};

  const createThreadToggle = () => {};
  return (
    <div>
      <NewThread
        topic={topic_id}
        isAuthenticated={isAuthenticated}
        isLoading={newThreadState.newThreadLoading}
        success={newThreadState.newThreadSuccess}
        name={newThreadState.newThreadName}
        content={newThreadState.newThreadContent}
        id={newThreadState.newThreadId}
        error={newThreadState.newThreadError}
        showEditor={newThreadState.newThreadShow}
        createThread={createThread}
        updateNewThread={createThreadSave}
        toggleShowEditor={createThreadToggle}
        maxLength={2000}
      />
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

//componentDidMount() {
//  const {forum} = this.props.match.params;
//  this.props.fetchForum(forum);
//}

//componentWillReceiveProps(newProps) {
//  const {forum: oldForum} = this.props.match.params;
//  const {forum: futureForum} = newProps.match.params;
//  if (oldForum !== futureForum) {
//    this.props.fetchForum(futureForum);
//  }
// }

/*
const mapStateToProps = state => ({
isLoading: state.forum.isLoading,
name: state.forum.name,
slug: state.forum.slug,
description: state.forum.description,
threads: state.forum.threads,
error: state.forum.error,
isAuthenticated: state.auth.isAuthenticated,
newThreadLoading: state.forum.newThreadLoading,
newThreadSuccess: state.forum.newThreadSuccess,
newThreadName: state.forum.newThreadName,
newThreadContent: state.forum.newThreadContent,
newThreadId: state.forum.newThreadId,
newThreadError: state.forum.newThreadError,
newThreadShow: state.forum.newThreadShow,
});

const mapDispatchToProps = dispatch => ({
fetchForum: forum => {
  dispatch(fetchForum(forum));
},
createThread: newThread => {
  dispatch(createThread(newThread));
},
createThreadSave: newThread => {
  dispatch(createThreadSave(newThread));
},
createThreadToggle: () => {
  dispatch(createThreadToggle());
},
});
*/

/*<NewThread
        forum={slug}
        isAuthenticated={isAuthenticated}
        isLoading={newThreadLoading}
        success={newThreadSuccess}
        name={newThreadName}
        content={newThreadContent}
        id={newThreadId}
        error={newThreadError}
        showEditor={newThreadShow}
        createThread={createThread}
        updateNewThread={createThreadSave}
        toggleShowEditor={createThreadToggle}
        maxLength={2000}
      />
      */
