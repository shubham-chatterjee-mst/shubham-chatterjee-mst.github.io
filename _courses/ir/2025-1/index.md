---
layout: page
title: "CS 5001: Information Retrieval"
description: Foundations of Information Retrieval Systems
img: assets/img/ir.webp
course: "CS 5001: Information Retrieval"
semester: "2025-1"
permalink: /courses/ir/2025-1/
syllabus: /courses/ir/2025-1/syllabus/
---

<style>
  .coming-soon-container {
    min-height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: linear-gradient(-45deg, #112233, #223344, #334455, #445566);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    padding: 2rem;
    border-radius: 1rem;
    margin: 2rem auto;
    max-width: 800px;
  }

  @keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }

  .coming-soon-content {
    text-align: center;
    color: #ffffff;
    padding: 2rem;
  }

  .coming-soon-title {
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 1rem;
    opacity: 0;
    animation: fadeIn 1s ease-in forwards;
  }

  .coming-soon-subtitle {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    opacity: 0;
    animation: fadeIn 1s ease-in 0.5s forwards;
  }

  .coming-soon-description {
    font-size: 1.1rem;
    line-height: 1.6;
    max-width: 600px;
    margin: 0 auto;
    opacity: 0;
    animation: fadeIn 1s ease-in 1s forwards;
  }

  .pulse {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    position: relative;
    margin: 2rem auto;
    animation: pulse 2s ease-out infinite;
  }

  @keyframes pulse {
    0% {
      transform: scale(0.95);
      box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.3);
    }
    70% {
      transform: scale(1);
      box-shadow: 0 0 0 60px rgba(255, 255, 255, 0);
    }
    100% {
      transform: scale(0.95);
      box-shadow: 0 0 0 0 rgba(255, 255, 255, 0);
    }
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .course-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    opacity: 0;
    animation: fadeIn 1s ease-in 1.5s forwards;
  }
</style>

<div class="coming-soon-container">
  <div class="coming-soon-content">
    <div class="pulse"></div>
    <div class="course-icon">📚</div>
    <h1 class="coming-soon-title">Coming Soon</h1>
    <h2 class="coming-soon-subtitle">Course Under Development</h2>
    <p class="coming-soon-description">
      We're working hard to bring you an exciting new learning experience. 
      This course is currently being developed and will be available soon. 
      Stay tuned for updates!
    </p>
  </div>
</div>
