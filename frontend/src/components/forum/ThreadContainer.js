import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './style.css';
import Thread from './Thread';
//import {createPost, fetchThread, deletePost, deleteThread} from '../../actions';
import { authHeader } from '../../context/auth/AuthActions';

const ThreadContainer = () => {
  const { id } = useParams();
  console.log('thread_id');
  console.log(id);

  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const [deleteError, setDeleteError] = useState(null);
  const [currentThread, setCurrentThread] = useState([]);
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchThread = async () => {
      const { data } = await axios.get(
        `http://127.0.0.1:5000/forum/threads/${id}/info`,
        { headers: authHeader() }
      );
      console.log('thread data');
      console.log(data);
      setCurrentThread(data);
    };

    fetchThread();
  }, [id]);

  useEffect(() => {
    const fetchThreadPosts = async () => {
      const { data } = await axios.get(
        `http://127.0.0.1:5000/forum/threads/${id}/posts`,
        { headers: authHeader() }
      );
      console.log('thread posts data');
      console.log(data);
      setPosts(data);
    };

    fetchThreadPosts();
  }, [id]);

  //console.log('before return');
  console.log(currentThread);

  return (
    <>
      <Thread
        thread={currentThread}
        //id={thread_id}
        //isLoading={isLoading}
        //name={thread.thread_name}
        //content={thread.thread_content}
        //pinned={thread.pinned}
        //creator={thread.thread_creator}
        //createdAt={thread.thread_created_at}
        posts={posts}
        //error={error}
        //isAuthenticated={isAuthenticated}
        //createPost={createPost}
        //newPostSuccess={newPostSuccess}
        //newPostLoading={newPostLoading}
        //newPostError={newPostError}
        //authenticatedUsername={authenticatedUsername}
        //authenticatedIsStaff={authenticatedIsStaff}
        //deletePostList={deletePostList}
        //deletePost={deletePost}
        isDeleting={isDeleting}
        deleteError={deleteError}
        //deleteThread={deleteThread}
      />
    </>
  );
};

export default ThreadContainer;
