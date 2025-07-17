// src/pages/Home.jsx

import React from 'react';
import Hero from '../components/hero';
import About from '../components/about';
import CoreTopics from '../components/coreTopics';
import CallToAction from '../components/callToAction';

// CSS IMPORT
import '../assets/home.css';

const Home = () => {


  return (
    <main className='home-container'>
      <Hero/>
      <About />
      <CoreTopics/>
      <CallToAction />
    </main>
  );
};

export default Home;
