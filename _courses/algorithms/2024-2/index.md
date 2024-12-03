---
layout: page
title: "CS 2500: Algorithms"
description: Introduction to Algorithm Design and Analysis
img: assets/img/algorithms.webp
course: "CS 2500: Algorithms"
semester: "2024-2"
permalink: /courses/algorithms/2024-2/
syllabus: /courses/algorithms/2024-2/syllabus/
---

<div style="text-align: justify;">
<h2 style="font-weight: bold;">Course Description</h2>
<hr>
  <p>
    This course is designed to equip undergraduate students with the foundational skills needed to solve basic computational problems through the effective use of algorithms. Throughout the course, students will develop a solid understanding of how to design, analyze, and implement algorithms to address a wide range of computational challenges.
    Students will learn to evaluate the efficiency of algorithms, focusing on both memory usage and runtime complexity. Key analytical tools such as asymptotic notation, recurrence relations, and mathematical proof techniques will be employed to rigorously assess algorithmic performance. In addition, students will gain practical experience in programming algorithms, reinforcing their understanding through hands-on application.
  </p>

  <p>
    The course will cover a variety of algorithm design techniques. Below is a tentative list of topics:
  </p>

  <ul>
    <li>
      <strong>Recursion:</strong> A method of solving problems where the solution involves solving smaller instances of the same problem. This technique is foundational for many other algorithm design strategies, such as divide-and-conquer and dynamic programming.
    </li>
    <li>
      <strong>Divide-and-Conquer:</strong> Breaking down problems into smaller, more manageable sub-problems, solving each independently, and then combining their solutions to solve the original problem. Examples include merge sort and quicksort.
    </li>
    <li>
      <strong>Dynamic Programming:</strong> Optimizing recursive algorithms by storing solutions to overlapping sub-problems to avoid redundant calculations. This approach is particularly useful for problems with optimal substructure, like the knapsack problem and the Fibonacci sequence.
    </li>
    <li>
      <strong>Greedy Algorithms:</strong> Making the best local choices at each step with the hope of finding a global optimum. This technique works well for problems like finding the minimum spanning tree (e.g., Kruskal's and Prim's algorithms) or the shortest path in a graph (e.g., Dijkstra's algorithm).
    </li>
    <li>
      <strong>Basics of Computational Complexity:</strong> Understanding the inherent difficulty of computational problems by classifying them into complexity classes such as P, NP, and NP-complete. This will include discussions on the theoretical limits of algorithm efficiency, the significance of polynomial-time algorithms, and an introduction to the concept of intractable problems. These concepts are critical for evaluating the feasibility of algorithmic solutions in real-world applications.
    </li>
  </ul>

  <p>
    These design strategies will be applied to a broad spectrum of problems, ranging from fundamental tasks like sorting to more complex challenges like graph algorithms.
  </p>

  <p>
    By the end of the course, students will have developed both the theoretical and practical skills necessary to approach algorithmic problems with confidence. They will be well-prepared to tackle more advanced topics in computer science and apply their knowledge to real-world computational tasks.
  </p>

  <h2 style="font-weight: bold;">Course Goals</h2>
  <hr>
  <p>The course aims to achieve the following objectives:</p>
  <ul>
    <li>Develop proficiency in analyzing the correctness and runtime performance of algorithms.</li>
    <li>Gain fluency in key algorithm design paradigms, including recursion, divide-and-conquer, greedy algorithms, and dynamic programming.</li>
    <li>
      Enhance technical writing and communication skills within computer science, including the ability to clearly write algorithms using pseudocode and flowcharts, articulate complexity analysis with asymptotic notation, and present design approaches comprehensively.
    </li>
    <li>Acquire thorough knowledge of a core set of algorithms, such as sorting algorithms, graph algorithms, etc.</li>
    <li>Apply algorithmic techniques to solve real-world computational problems effectively.</li>
  </ul>

  <h2 style="font-weight: bold;">Course Prerequisites</h2>
  <hr>
  <p>
    This course is designed for undergraduate students enrolled in any science or engineering degree program who have a strong foundation in procedural programming, a solid understanding of data structures, and basic proficiency in calculus. If you are unsure about your readiness for this course, please contact the instructor for guidance.
  </p>

  <p>
    Python will be the primary programming language used in this course. Under exceptional circumstances, students may seek approval from the instructor to use an alternative programming language.
  </p>

  <p>The prerequisites for this course are as follows:</p>
  <ul>
    <li>A grade of “C” or better in both <strong>Comp Sci 1200</strong> and <strong>Comp Sci 1575</strong>.</li>
    <li>A grade of “C” or better in either <strong>Math 1208</strong> or <strong>Math 1214</strong>, or concurrent enrollment in <strong>Math 1208</strong> or <strong>Math 1214</strong>.</li>
  </ul>
  
  <h2 style="font-weight: bold;">Alignment with Bloom's Taxonomy</h2>
  <hr>
<p>
    This course leverages the cognitive framework of <a href='https://citt.ufl.edu/resources/the-learning-process/designing-the-learning-experience/blooms-taxonomy/'> Bloom's Taxonomy</a> to guide students through a structured progression of learning objectives. While AI tools can aid in achieving some of these objectives, this course emphasizes the distinctive human skills that are crucial for mastering algorithms and computational problem-solving. The focus is on equipping students with the ability to critically think, evaluate, and innovate, as these are the higher-order skills AI cannot fully replicate. These advanced skills are essential for solving complex computational problems and designing innovative algorithms. By the end of the course, students will have gained not only foundational knowledge but also the ability to apply, critically assess, and design algorithms in novel contexts.
</p>

<!-- Add the image of Bloom's Taxonomy -->
<div style="text-align: center; margin: 20px 0;">
  <img src="/assets/img/blooms-taxonomy-revisited.jpg" alt="Bloom's Taxonomy" style="width: 80%; max-width: 600px; height: auto;">
  <p style="font-style: italic; font-size: 0.9rem;">Figure: Bloom's Taxonomy - Levels of Cognitive Learning</p>
</div>

<ul>
  <li>
    <strong>Remember:</strong> Students will begin by recalling key concepts, definitions, and algorithmic paradigms. For example, they will memorize common algorithms (e.g., merge sort, Dijkstra’s algorithm) and foundational terminologies like asymptotic notation and complexity classes. This foundational knowledge ensures students can retrieve critical information during problem-solving, even in situations where no external aids are available.
  </li>
  <li>
    <strong>Understand:</strong> Students will demonstrate comprehension by explaining algorithmic concepts and principles. For instance, they will articulate how divide-and-conquer techniques reduce problem complexity or how dynamic programming avoids redundant calculations. Contextual understanding is essential for applying these techniques effectively to a wide range of computational challenges.
  </li>
  <li>
    <strong>Apply:</strong> By implementing algorithms in Python, students will translate theoretical knowledge into practical coding tasks, such as optimizing solutions for graph traversal or developing sorting algorithms. Through hands-on assignments, students will refine their ability to debug, test, and adapt their implementations to specific scenarios, emphasizing the importance of developing practical, independent programming skills.
  </li>
  <li>
    <strong>Analyze:</strong> Higher-order thinking begins with analyzing the trade-offs and efficiency of algorithms. Students will learn to break down problems into components, use recurrence relations to predict runtime, and assess memory usage. They will also compare different solutions to identify their strengths and limitations in specific scenarios, building a nuanced understanding of algorithmic performance.
  </li>
  <li>
    <strong>Evaluate:</strong> Students will critique and justify algorithmic choices for solving given problems. For instance, they will evaluate when to use a greedy algorithm versus dynamic programming, justifying their decisions based on problem characteristics like optimal substructure and overlapping subproblems. Evaluative skills ensure students can make informed, context-aware decisions in real-world applications.
  </li>
</ul>

<p>
    While the creation of original algorithms or adaptations of existing ones to solve novel computational challenges is undoubtedly important, the "Create" aspect of Bloom's Taxonomy is reserved for <strong>CS 5200</strong>, a more advanced algorithms course. By focusing on foundational skills in this course, students will build a strong base in algorithmic thinking, analysis, and implementation, which are critical prerequisites for tackling the creative and innovative aspects of algorithm design at a higher level. Excluding the "Create" stage from this course allows students to dedicate their efforts to mastering the essential building blocks of algorithmic problem-solving, such as understanding key paradigms (e.g., recursion, divide-and-conquer, dynamic programming, greedy strategies) and evaluating algorithm performance through rigorous analysis. These skills are invaluable for developing a deep understanding of computational thinking and preparing students for success in advanced courses like <strong>CS 5200</strong>. By leaving the "Create" stage for a more advanced course, this course remains focused on equipping students with the analytical and practical skills needed to effectively approach real-world computational problems. It ensures that students are not overwhelmed by overly complex tasks before they are ready, setting them up for greater success in their academic and professional pursuits.
</p>

<p>
  By the end of the course, students will have progressed through all (but one) levels of Bloom's Taxonomy, gaining not only foundational knowledge but also the higher-order thinking skills of analyzing, evaluating, and creating. These skills will enable them to solve complex computational problems independently and communicate their solutions effectively, ensuring they are well-prepared for advanced studies and professional roles in computer science.
</p>

<h3 style="font-weight: bold;">Developing Higher-Order Thinking Skills</h3>
<p>
  A significant focus of this course is on fostering higher-order thinking skills, specifically:
</p>

<ul>
  <li>
    <strong>Problem Analysis:</strong> Students will dissect complex problems, identifying patterns, breaking problems into subproblems, and analyzing the feasibility of various approaches.
  </li>
  <li>
    <strong>Critical Evaluation:</strong> Through in-depth discussions and assignments, students will evaluate different algorithmic strategies, examining their trade-offs and performance in terms of time and space complexity.
  </li>
  <li>
    <strong>Algorithm Design and Innovation:</strong> Students will be tasked with creating and optimizing algorithms for new challenges, requiring them to integrate knowledge, experiment with techniques, and propose innovative solutions.
  </li>
</ul>

<h3 style="font-weight: bold;">Do we still need this in the age of AI assistants?</h3>
<p>
  Yes, developing independent problem-solving and higher-order thinking skills remains essential, even in the age of AI assistants. While AI tools can assist in tasks like recalling facts, generating examples, or summarizing content, they are not a substitute for human creativity, critical thinking, and adaptability. These skills are indispensable in addressing complex, real-world challenges where human judgment, ethical reasoning, and innovation are required. 
</p>

<ul>
  <li>
    <strong>Critical Thinking:</strong> AI lacks the ability to fully understand and reason through the emotional, moral, and contextual dimensions of problems. Evaluating complex scenarios and proposing meaningful solutions requires human cognition, which goes beyond algorithmic outputs.
  </li>
  <li>
    <strong>Ethical Reflection:</strong> Decisions involving trade-offs or societal implications demand human judgment. While AI can highlight possible outcomes, it cannot weigh these against ethical considerations or make context-aware decisions.
  </li>
  <li>
    <strong>Creativity and Innovation:</strong> AI operates based on patterns and data it has been trained on. True originality and the ability to think outside the box—essential for creating novel algorithms or solving new problems—are uniquely human capabilities.
  </li>
  <li>
    <strong>Adaptability:</strong> AI models are limited to their training data and struggle with new or unique challenges. Humans, on the other hand, excel in adapting to unforeseen circumstances and crafting solutions that go beyond predefined models.
  </li>
</ul>

<h3 style="font-weight: bold;">Emphasis on Technical Writing</h3>
<p>
  Technical writing is a higher-order skill within Bloom's Taxonomy, falling under the levels of <strong>Analyze</strong>, <strong>Evaluate</strong>, and <strong>Create</strong>. It requires students not only to understand and apply algorithmic concepts but also to critically analyze trade-offs, evaluate design decisions, and communicate solutions effectively. This skill extends beyond recalling or applying knowledge—it challenges students to synthesize their understanding and present it in a professional, structured, and coherent manner. 
</p>

<p>
  In this course, technical writing serves as a bridge between theoretical knowledge and practical problem-solving. Students will:
</p>

<ul>
  <li>
    <strong>Analyze:</strong> Break down algorithms into components and use pseudocode or flowcharts to effectively communicate their structure and logic.
  </li>
  <li>
    <strong>Evaluate:</strong> Explain the trade-offs of algorithms, considering factors such as time complexity, space usage, and suitability for specific problems, using asymptotic notation and complexity analysis to justify their conclusions.
  </li>
  <li>
    <strong>Create:</strong> Articulate design decisions and justify their approaches through clear, well-documented assignments, mimicking the standards of professional research and technical communication.
  </li>
</ul>

<p>
  By emphasizing technical writing as a core component of this course, students develop the ability to convey complex ideas with precision and professionalism. This skill not only enhances their understanding of algorithms but also prepares them for advanced academic research, collaborative projects, and professional roles in the field of computer science. Through structured documentation and communication, students learn to make their algorithmic solutions accessible and understandable, a critical capability for success in real-world computational problem-solving.
</p>


  
  <h2 style="font-weight: bold;">Grading and Homeworks</h2>
  <hr>
  <p> Your performance in this course will be assessed through assignments and exams.</p>

  <ul>
  <li> 
    <strong>Assignments [50%]:</strong> These assignments consist of some problems requiring detailed answers. These aim to deepen your understanding of the material covered in class. Assignments are released every Tuesday and are due by midnight the following Tuesday. You will have 7 days to complete each assignment.
  </li>

  <li>
    <strong>Midterm Examination [25%]:</strong> The midterm examination will cover all the material discussed up until the midterm point of the course. It is designed to assess your understanding and application of the key concepts.
  </li>

  <li>
    <strong>Final Comprehensive Examination [25%]:</strong> The final exam is comprehensive, covering all the material discussed throughout the course. It will evaluate your overall understanding and integration of the topics covered.
  </li>
</ul>

  <h3 style="font-weight: bold;">Grading Scale</h3>
  <table style="width: 50%; border-collapse: collapse; margin-top: 10px; text-align: left; border: 1px solid #ddd;">
    <thead>
      <tr>
        <th style="padding: 8px; border: 1px solid #ddd;">Letter Grade</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Points</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">A</td>
        <td style="padding: 8px; border: 1px solid #ddd;">90 – 100 points</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">B</td>
        <td style="padding: 8px; border: 1px solid #ddd;">80 – 89 points</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">C</td>
        <td style="padding: 8px; border: 1px solid #ddd;">70 – 79 points</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">D</td>
        <td style="padding: 8px; border: 1px solid #ddd;">60 – 69 points</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">F</td>
        <td style="padding: 8px; border: 1px solid #ddd;">59 and below</td>
      </tr>
    </tbody>
  </table>
  <br>
  
  <h2 style="font-weight: bold;">Course Materials</h2>
  <hr>
  <ul>
    <li>
      <a href="/courses/algorithms/2024-2/materials/">Course Materials</a> - Lecture Notes, Slides, and Resources
    </li>
    <li>
      <a href="/courses/algorithms/2024-2/assignments/">Assignments</a> - Previous assignments and exams
    </li>
  </ul>
</div>


