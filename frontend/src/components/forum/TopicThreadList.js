import React from 'react';

import { Segment } from 'semantic-ui-react';
import StatusMessage from './StatusMessage';

import './style.css';

//import {
//  createThreadSave,
// createThreadToggle,
//  fetchForum,
//  createThread,
//} from '../../actions';
//import ThreadList from '../../components/threadlist';
//import NewThread from '../../components/newthread';
import BaseThread from './BaseThread';

const TopicThreadList = ({ isLoading, error, threads, topic }) => {
  //const {isLoading, error, threads} = this.props;

  if (error || !threads || isLoading || threads.length === 0) {
    return (
      <StatusMessage
        error={error || !threads}
        errorClassName="forum-error"
        errorMessage={error}
        loading={isLoading}
        loadingMessage={`We are fetching the forum for you`}
        nothing={threads && threads.length === 0}
        nothingMessage={`No threads to display`}
        nothingClassName="forum-error"
        type="default"
      />
    );
  }

  return (
    <div className="forumContainer">
      <Segment.Group className="forum-list">
        {threads.map((thread) => {
          return <BaseThread key={thread.thread_id} thread={thread} />;
        })}
      </Segment.Group>
    </div>
  );
};

export default TopicThreadList;
