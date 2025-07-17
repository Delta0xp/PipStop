import React from 'react';
import '../assets/coreTopics.css'

const topics = [
    { emoji: '🤖', title: 'AI', desc: 'From neural networks to GenAI and everything in between.' },
    { emoji: '⚙️', title: 'Automation', desc: 'Scripts, bots, CI/CD pipelines, and intelligent agents.' },
    { emoji: '☁️', title: 'Cloud', desc: 'Master AWS, Azure, GCP, and hybrid cloud setups.' },
    { emoji: '📊', title: 'Data', desc: 'Big Data, analytics, ML pipelines, and business insights.' },
];

const CoreTopics = () => {
  return (
    <section className='topics-container'>
      <h2 className='topics-heading'>Our Core Topics</h2>
      <div className='topics-grid'>
        {topics.map((topic) => (
          <div key={topic.title} className='topic-card'>
            <span className='topic-emoji'>{topic.emoji}</span>
            <h3 className='topic-title'>{topic.title}</h3>
            <p className='topic-desc'>{topic.desc}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default CoreTopics;