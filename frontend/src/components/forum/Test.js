import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import Thread from './Thread';

const Test = () => {
  const { id } = useParams();
  const [currentThread, setCurrentThread] = useState([]);
  console.log('thread_id from test');
  console.log(id);

  useEffect(() => {
    console.log('start');
    const fetchThread = async () => {
      console.log('thread data from test');
      const { data } = await axios.get(
        `http://127.0.0.1:5000/forum/threads/${id}`
      );
      console.log('thread data');
      console.log(data);
      setCurrentThread(data);
    };

    fetchThread();
  }, [id]);

  return (
    <div>
      <Thread currentThread={currentThread} />
    </div>
  );
};

export default Test;
