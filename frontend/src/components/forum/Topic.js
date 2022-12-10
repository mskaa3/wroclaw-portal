/* eslint-disable prettier/prettier */
import React from 'react';
import Main from '../components/forum/Main';
import Stats from '../components/forum/Stats';
import LastThread from '../components/forum/LastThread';

const Topic = ({ category, isFirst }) => {
  let className = 'list-group-item';
  if (category.description) {
    className += ' list-group-category-has-description';
  } else {
    className += ' list-group-category-no-description';
  }

  if (isFirst) {
    className += ' list-group-item-first';
  }
  if (category.css_class) {
    className += ' list-group-category-has-flavor';
    className += ' list-group-item-category-' + category.css_class;
  }
  return (
    <li className={className}>
      <div className="row">
        <Main category={category} />
        <Stats category={category} />
        <LastThread category={category} />
      </div>
    </li>
  );
};

export default Topic;
