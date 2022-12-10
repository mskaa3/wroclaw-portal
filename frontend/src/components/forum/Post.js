/* eslint-disable prettier/prettier */
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Segment, Grid, Icon, Dropdown } from 'semantic-ui-react';
import RichEditor from './RichEditor';
import Avatar from './Avatar';
import './style.css';
import axios from 'axios';

//const Post = ({ post, isThread, threadPost }) => {
const Post = (props) => {
  const [isLoading, setIsLoading] = useState(false);
  //console.log('post_creator');
  //console.log(post.post_creator);
  const { deleteAction, id, threadID, isThread, dispatch } = props;
  /*
  const deleteThread = async (thread_id) => {
    const response = await axios.delete(
      `http://127.0.0.1:5000/forum/threads/${thread_id}`
    );

    return response.data;
  };
  */
  /*
  const deletePost = async (post_id) => {
    const response = await axios.delete(
      `http://127.0.0.1:5000/forum/posts/${post_id}`
    );

    return response.data;
  };
*/
  const onDelete = () => {
    //const { deleteAction, id, threadID, isThread } = this.props;
    if (isThread) {
      //deleteThread(threadID);
      deleteAction(dispatch, threadID);
    } else {
      //deletePost(id);
      deleteAction(dispatch, id);
    }
  };

  const {
    content,
    createdAt,
    creator,
    creator_name,
    avatar,
    authenticatedUser,
    //authenticatedUsername,
    //authenticatedIsStaff,
    //deletePostList,
  } = props;

  const color = isThread ? 'black' : null;
  const deleteText = isThread ? 'Delete Thread' : 'Delete Post';

  const actions = (
    <div className="post-dropdown">
      <Dropdown simple icon="caret down" direction="left">
        <Dropdown.Menu>
          <Dropdown.Item onClick={onDelete} icon="delete" text={deleteText} />
        </Dropdown.Menu>
      </Dropdown>
    </div>
  );

  //const isLoading = !isThread && deletePostList.indexOf(id) >= 0;

  return (
    <Segment loading={isLoading} color={color}>
      <Grid textAlign="left" padded="horizontally">
        <Grid.Column width={4}>
          <Grid.Row>
            <div className="post-row">
              <Avatar
                className="post-avatar"
                avatar={avatar}
                centered={false}
                link={`/users/${creator}`}
              />
              <div className="post-column">
                <div className="post-name">{creator_name}</div>
                <div className="post-username">
                  <Link to={`/users/${creator}`}>
                    <Icon name="user" />
                    {creator_name}
                  </Link>
                </div>
              </div>
            </div>
          </Grid.Row>
        </Grid.Column>
        <Grid.Column width={12}>
          <div className="post-time">{createdAt}</div>
          {actions}
          <RichEditor
            readOnly={true}
            content={content}
            wrapperClassName={false ? 'post-wrapper-edit' : 'post-wrapper-read'}
            editorClassName="post-editor"
            toolbarClassName="post-toolbar"
          />
        </Grid.Column>
      </Grid>
    </Segment>
  );
};

export default Post;

/*
<Grid.Column width={12}>
          <div className="post-time">
            {post.post_created_at}
            {(authenticatedUsername === creator.username) && actions}
          </div>
          <RichEditor
*/
