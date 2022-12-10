/* eslint-disable prettier/prettier */
import React, { useEffect, useState, useContext } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Button } from 'react-bootstrap';
import axios from 'axios';
import './style.css';
import Thread from './Thread';
import AuthContext from '../../context/auth/AuthContext';
//import {createPost, fetchThread, deletePost, deleteThread} from '../../actions';
import {
  authHeader,
  createPost,
  deletePost,
  deleteThread,
} from '../../context/auth/AuthActions';

const ThreadContainer = () => {
  const { id } = useParams();
  console.log('thread_id');
  console.log(id);
  const navigate = useNavigate();
  const {
    dispatch,
    isLoading,
    //name,
    //content,
    //pinned,
    //creator,
    //createdAt,
    posts,
    error,
    isAuthenticated,
    curThread,
    //createPost,
    //newPostLoading,
    //newPostError,
    //newPostSuccess,
    //authenticatedUsername,
    //authenticatedIsStaff,
    //deletePostList,
    //deletePost,
    //isDeleting,
    //deleteError,
    //deleteThread,
  } = useContext(AuthContext);

  //const [isLoading, setIsLoading] = useState(false);
  //const [error, setError] = useState(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const [deleteError, setDeleteError] = useState(null);
  const [currentThread, setCurrentThread] = useState([]);
  const [postss, setPostss] = useState([]);

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
      setPostss(data);
    };

    fetchThreadPosts();
  }, [id, curThread]);

  //console.log('before return');
  console.log(currentThread);

  return (
    <>
      <Button
        className="mt-3 w-40 mb-3"
        variant="custom"
        type="submit"
        onClick={() => navigate(-1)}
      >
        <i className="fa-solid fa-left-long"></i> &nbsp;Back to threads
      </Button>
      <Thread
        thread={currentThread}
        //id={thread_id}
        //isLoading={isLoading}
        //name={thread.thread_name}
        //content={thread.thread_content}
        //pinned={thread.pinned}
        //creator={thread.thread_creator}
        //createdAt={thread.thread_created_at}
        posts={postss}
        //error={error}
        //isAuthenticated={isAuthenticated}
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
    </>
  );
};

export default ThreadContainer;
