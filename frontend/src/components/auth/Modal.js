/* eslint-disable prettier/prettier */
import React from 'react';
import { Icon } from 'semantic-ui-react';
import './style.css';

const Modal = ({
  children,
  onClose,
  dialogStyle,
  overlayStyle,
  contentStyle,
}) => {
  const closeModal = () => {
    onClose();
  };

  const onDialogClick = (event) => {
    event.stopPropagation();
  };

  overlayStyle = overlayStyle ? overlayStyle : {};
  contentStyle = contentStyle ? contentStyle : {};
  dialogStyle = dialogStyle ? dialogStyle : {};

  return (
    <div>
      <div className="modal-overlay-div" style={overlayStyle} />
      <div
        className="modal-content-div"
        style={contentStyle}
        onClick={closeModal}
      >
        <div
          className="modal-dialog-div"
          style={dialogStyle}
          onClick={onDialogClick}
        >
          <Icon
            name="window close outline"
            size="large"
            className="modal-close-div"
            onClick={closeModal}
          />
          {children}
        </div>
      </div>
    </div>
  );
};

export default Modal;
