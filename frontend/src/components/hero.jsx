import React from 'react';

import '../assets/hero.css'

const Hero = ()=> {
  return (
   <section className="hero-container">
    <h1 className="hero-title"> PipStop One Stop Shop</h1>
    <p className="hero-subtitle">
        A Centre of Excellence for AI, Automation, Cloud, and Data.
        Join a thriving community of IT professionals pushing the boundaries of innovation.
    </p>

    <div className="hero-buttons">
      <button className="hero-btn-primary">Join</button>
      <button className="hero-btn-secondary">Explore the topics</button>
    </div>

   </section>
  );
};

export default Hero;