/* eslint-disable prettier/prettier */

import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';
import '../css/index.css';
import Image from 'react-bootstrap/Image';


const TopImage = () => {

  return (
    <div style={{ display: 'block', width: '100%', height: '225px' }}>
      <Image
        // src="https://cdn.pixabay.com/photo/2016/05/25/15/05/poland-1415099_1280.jpg"
        // src="https://pickvisa.com/storage/public/articles/night-view-of-wroclaw.jpg"
        src="https://as1.ftcdn.net/jpg/01/46/71/02/1000_F_146710278_re8T8abkUPnGksMuxHcViGKd1KT1QKi7.jpg"
        className="image-top"
      />
    </div>
  
  );
};

export default TopImage;
