import React from 'react';

import '../assets/callToAction.css'

const CallToAction = () => {
  return (
    <section className="cta-section">
      <h2 className="cta-heading"> Ready to Level up bruv? !!!</h2>
      <p className="cta=subheading">
        Join the PipStop community and become part of the movement shaping the future of tech. 
      </p>
      <div className="cta-buttons">
        <button className="cta-primary"> Get Started</button>
        <button className="cta-secondary"> Learn More </button>
      </div>
    </section>
  );

};

export default CallToAction;
