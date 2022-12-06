import React, { useState, useContext } from 'react';
import { useParams } from 'react-router-dom';
import { Segment, Icon } from 'semantic-ui-react';
import StatusMessage from './StatusMessage';
import Post from './Post';
import NewPost from './NewPost';
import AuthContext from '../../context/auth/AuthContext';

const Thread = ({
  //isLoading,
  //error,
  isDeleting,
  deleteError,
  thread,
  posts,
}) => {
  const { dispatch, isAuthenticated, isLoading, error } =
    useContext(AuthContext);
  const {
    thread_id,
    thread_name,
    thread_content,
    thread_created_at,
    thread_creator,
    pinned,
    avatar,
    user_name,
    user_email,
  } = thread;

  const tread_creator = { avatar, user_name, user_email };
  const { newPost, setNewPost } = useState([]);
  const { postsList, setPostsList } = useState([]);

  if (error || deleteError || isLoading || isDeleting || !thread_name) {
    let loadingMessage = 'We are fetching the thread for you';
    if (isDeleting) {
      loadingMessage = 'We are deleting the thread for you';
    }
    return (
      <StatusMessage
        error={error || deleteError || !thread_name} // because a thread name cannot be empty
        errorClassName="thread-error"
        errorMessage={error || deleteError}
        loading={isLoading || isDeleting}
        loadingMessage={loadingMessage}
        nothing={!thread_name}
        nothingMessage={'Thread does not exist'}
        type="default"
      />
    );
  }

  const threadPost = (
    <Post
      id={thread_id}
      threadID={thread_id}
      isThread={true}
      content={thread_content}
      createdAt={thread_created_at}
      //creator={thread_creator}
      creator={user_name}
      avatar={avatar}
      //authenticatedUsername={authenticatedUsername}
      //authenticatedIsStaff={authenticatedIsStaff}
      //deleteAction={deleteThread}
    />
  );

  return (
    <div className="threadContainer">
      <div className="thread-title">
        <Icon name={pinned ? 'pin' : 'comment alternate outline'} />
        {thread_name}
      </div>
      <Segment.Group className="thread-list">
        {threadPost}
        {posts &&
          posts.map((post) => (
            <Post
              key={post.post_id}
              //post={post}
              threadID={thread_id}
              id={post.post_id}
              isThread={false}
              content={post.post_content}
              createdAt={post.post_created_at}
              creator={post.post_creator}
              //authenticatedUsername={authenticatedUsername}
              //authenticatedIsStaff={authenticatedIsStaff}
              //deletePostList={deletePostList}
              //deleteAction={deletePost}
            />
          ))}
      </Segment.Group>
      <NewPost
        isAuthenticated={isAuthenticated}
        threadID={thread_id}
        //createPost={createPost}
        //success={newPostSuccess}
        //isLoading={newPostLoading}
        //error={newPostError}
        maxLength={2000}
      />
    </div>
  );
};

export default Thread;
/*

*/
