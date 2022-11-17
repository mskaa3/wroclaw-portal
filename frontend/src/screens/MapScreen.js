import React from 'react';
import GoogleMapComponent from '../components/GoogleMapComponent';
import GooglePins from '../components/GooglePins';
import { useState, useEffect } from 'react';

const pinCategories = {
  uni: { key: 'uni', name: 'Universities' },
  gov: {
    key: 'gov',
    name: 'Governmental buildings',
    icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
  },
  dorm: { key: 'dorm', name: 'Dormentories' },
};

const pinData = [
  {
    id: 'pwrPosition',
    cat: pinCategories.uni.key,
    position: {
      lat: 51.1077,
      lng: 17.0625,
    },
  },
  {
    id: 'uniOfWroclaw',
    cat: pinCategories.uni.key,
    position: {
      lat: 51.114,
      lng: 17.0345,
    },
  },
  {
    id: 'uniOfEconomics',
    cat: pinCategories.uni.key,
    position: {
      lat: 51.0901,
      lng: 17.0278,
    },
  },
  {
    id: 'uniOfMedical',
    cat: pinCategories.uni.key,
    position: {
      lat: 51.1089,
      lng: 17.0689,
    },
  },
  {
    id: 'uniOfEnvironment',
    cat: pinCategories.uni.key,
    position: {
      lat: 51.1114,
      lng: 17.0643,
    },
  },
  {
    id: 'uniOfMilitary',
    cat: pinCategories.uni.key,
    position: {
      lat: 51.1501,
      lng: 17.0586,
    },
  },
  {
    id: 'uniOfArt',
    cat: pinCategories.uni.key,
    position: {
      lat: 51.11139,
      lng: 17.04361,
    },
  },
  {
    id: 'uniOfLogistics',
    cat: pinCategories.uni.key,
    position: {
      lat: 51.141261495243285,
      lng: 17.071594869314776,
    },
  },
  {
    id: 'uniOfFilology',
    cat: pinCategories.uni.key,
    position: {
      lat: 51.118106724596146,
      lng: 17.04895667616702,
    },
  },
  {
    id: 'uniOfMusic',
    cat: pinCategories.uni.key,
    position: {
      lat: 51.111224453329754,
      lng: 17.02138369445129,
    },
  },
  {
    id: 'wroclawMainHall',
    cat: pinCategories.gov.key,
    position: {
      lat: 51.109978082186494,
      lng: 17.04956507875505,
    },
  },
];

const MapScreen = () => {
  const [selectedPinCategories, setSelectedPinCategories] = useState([
    pinCategories.uni.key,
    pinCategories.gov.key,
    pinCategories.dorm.key,
  ]);
  console.log(pinData);
  return (
    <div>
      <center>
        <GoogleMapComponent
          pinCategories={selectedPinCategories}
          markerList={pinData}
        />
        <GooglePins
          pinCategories={pinCategories}
          selectedPinCategories={selectedPinCategories}
          onPinSelection={setSelectedPinCategories}
        />
      </center>
    </div>
  );
};

export default MapScreen;
