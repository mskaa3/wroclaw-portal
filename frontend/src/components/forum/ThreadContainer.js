import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './style.css';
import Thread from './Thread';
//import {createPost, fetchThread, deletePost, deleteThread} from '../../actions';

const ThreadContainer = (props) => {
  const { thread_id } = useParams();
  console.log('thread_id');
  console.log(thread_id);

  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const [deleteError, setDeleteError] = useState(null);
  const [thread, setThread] = useState(null);
  /*
  const [newThreadState, setNewThreadState] = useState({
    newThreadLoading: false,
    newThreadSuccess: false,
    newThreadName: '',
    newThreadContent: '',
    newThreadId: null,
    newThreadError: null,
    newThreadShow: false,
  });
*/
  useEffect(() => {
    const fetchThread = async () => {
      console.log('thread data');
      const { data } = await axios.get(
        `http://127.0.0.1:5000/forum/threads/${thread_id}`
      );
      console.log('thread data');
      console.log(data);
      setThread(data);
    };

    fetchThread();
  }, [thread_id]);
  /*
  componentWillReceiveProps(newProps) {
    const {thread} = this.props.match.params;
    const {thread: newThread} = newProps.match.params;
    if (thread !== newThread) {
      this.props.fetchThread(newThread);
    }
  }
*/
  const isAuthenticated = () => {};

  const deleteThread = (thread_id) => {};

  const createPost = (newPost) => {};

  const deletePost = (post_id, thread_id) => {};

  return (
    <Thread
      id={thread_id}
      isLoading={isLoading}
      name={thread.thread_name}
      content={thread.thread_content}
      pinned={thread.pinned}
      creator={thread.thread_creator}
      createdAt={thread.thread_created_at}
      posts={thread.posts}
      error={error}
      isAuthenticated={isAuthenticated}
      createPost={createPost}
      //newPostSuccess={newPostSuccess}
      //newPostLoading={newPostLoading}
      //newPostError={newPostError}
      //authenticatedUsername={authenticatedUsername}
      //authenticatedIsStaff={authenticatedIsStaff}
      //deletePostList={deletePostList}
      deletePost={deletePost}
      isDeleting={isDeleting}
      deleteError={deleteError}
      deleteThread={deleteThread}
    />
  );
};

export default ThreadContainer;
