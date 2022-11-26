import React from 'react';

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
  const {
    isLoading,
    name,
    slug,
    description,
    threads,
    error,
    isAuthenticated,
    newThreadLoading,
    newThreadSuccess,
    newThreadName,
    newThreadContent,
    newThreadId,
    newThreadError,
    newThreadShow,
    createThread,
    createThreadSave,
    createThreadToggle,
  } = this.props;

  return (
    <div>
      <NewThread
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
      <TopicThreadList
        isLoading={isLoading}
        name={name}
        slug={slug}
        description={description}
        threads={threads}
        error={error}
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
