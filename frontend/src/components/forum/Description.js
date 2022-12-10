/* eslint-disable prettier/prettier */
import React from 'react';

const Descripton = ({ category }) => {
  if (!category.description) return null;

  return (
    <div
      className="category-description"
      dangerouslySetInnerHTML={{
        __html: category.description.html,
      }}
    />
  );
};
export default Descripton;
