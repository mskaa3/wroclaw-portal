import React from 'react';
import Description from './Description';
//import Icon from "./icon"

const Main = ({ category }) => {
  return (
    <div className="col-xs-12 col-sm-6 col-md-6 category-main">
      <div className="media">
        <div className="media-body">
          <h4 className="media-heading">
            <a href={category.url.index}>{category.name}</a>
          </h4>
          <Description category={category} />
        </div>
      </div>
    </div>
  );
};

export default Main;
