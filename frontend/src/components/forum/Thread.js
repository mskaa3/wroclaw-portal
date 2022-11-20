import React from 'react';
import StatusMessage from './StatusMessage';

const Thread = (props) => {
  if (
    props.error ||
    props.deleteError ||
    props.isLoading ||
    props.isDeleting ||
    !props.thread_name
  ) {
    let loadingMessage = 'We are fetching the thread for you';
    if (props.isDeleting) {
      loadingMessage = 'We are deleting the thread for you';
    }
    return (
      <StatusMessage
        error={props.error || props.deleteError || !props.thread_name} // because a thread name cannot be empty
        errorClassName="thread-error"
        errorMessage={props.error || props.deleteError}
        loading={props.isLoading || props.isDeleting}
        loadingMessage={loadingMessage}
        nothing={!props.thread_name}
        nothingMessage={'Thread does not exist'}
        type="default"
      />
    );
  }

  return <div>Thread</div>;
};

export default Thread;
