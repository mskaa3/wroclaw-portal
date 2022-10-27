/* eslint-disable prettier/prettier */

import React from 'react';
//import { Container } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import '../css/index.css';
import Image from 'react-bootstrap/Image';

const TopImage = () => {
  return (
    <div style={{ display: 'block', width: '100%', height: '300px' }}>
      <Image
        src="https://cdn.pixabay.com/photo/2016/05/25/15/05/poland-1415099_1280.jpg"
        className="image-top"
      />
    </div> 
  );
};

export default TopImage;
