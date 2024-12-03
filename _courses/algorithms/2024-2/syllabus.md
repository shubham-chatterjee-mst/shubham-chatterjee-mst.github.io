---
layout: page
title: "Syllabus for CS 2500: Algorithms (Fall 2024)"
permalink: /courses/algorithms/2024-2/syllabus/
course: "CS 2500: Algorithms"
semester: "2024-2"
---

<div class="syllabus-container">
  <div class="topic-overview">
    <div class="topic-card">
      <h4>Course Format</h4>
      <p>4 credit hours<br> 3 LEC + 1 LAB per week</p>
    </div>
    <div class="topic-card">
      <h4>Prerequisites</h4>
      <p>CS 1200, CS 1575<br>Math 1208 or Math 1214</p>
    </div>
    <div class="topic-card">
      <h4>Assessment</h4>
      <p>Assignments: 50%<br>Midterm: 25%<br>Final: 25%</p>
    </div>
  </div>

  
  <div class="syllabus-section">
    <div class="section-header">
      <h2>1. Fundamentals of Algorithms</h2>
    </div>
    <ul>
      <li>Definition and examples of algorithms</li>
      <li>Algorithm analysis and complexity</li>
      <li>Asymptotic Notation: Big-O, Big-Omega, and Big-Theta</li>
      <li>Analysis of non-recursive algorithms</li>
      <li>Counting and rate of growth</li>
      <li>Tractable vs Intractable problems</li>
    </ul>
  </div>

  <div class="syllabus-section">
    <div class="section-header">
      <h2>2. Recursion and Mathematical Induction</h2>
    </div>
    
    <h3>2.1 Recursion Fundamentals</h3>
    <ul>
      <li>Introduction to recursion</li>
      <li>Simple recursive algorithms (factorial, Fibonacci)</li>
      <li>Tracing recursive calls</li>
      <li>Common pitfalls and debugging techniques</li>
    </ul>
    
    <h3>2.2 Mathematical Induction</h3>
    <ul>
      <li>Principles of mathematical induction</li>
      <li>Base case and inductive step</li>
      <li>Non-recursive examples and applications</li>
      <li>Common mistakes in inductive proofs</li>
    </ul>

    <h3>2.3 Recurrence Relations</h3>
    <ul>
      <li>Introduction to recurrence relations</li>
      <li>Linear vs non-linear recurrence relations</li>
      <li>Methods to solve recurrence relations:
        <ul>
          <li>Guess-and-verify (Substitution method)</li>
          <li>Iteration/Substitution method</li>
          <li>Recurrence-tree method</li>
          <li>Telescoping/Difference method</li>
          <li>Master theorem</li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="syllabus-section">
    <div class="section-header">
      <h2>3. Basic Sorting Algorithms</h2>
    </div>
    <ul>
      <li>Introduction to sorting and its importance</li>
      <li>Comparison-based sorting algorithms</li>
      <li>Bubble Sort: algorithm and analysis</li>
      <li>Selection Sort: algorithm and analysis</li>
      <li>Insertion Sort: algorithm and analysis</li>
      <li>Proof of correctness for sorting algorithms</li>
    </ul>
  </div>

  <div class="syllabus-section">
    <div class="section-header">
      <h2>4. Advanced Sorting and Divide-and-Conquer</h2>
    </div>
    <h3>4.1 Heap Sort</h3>
    <ul>
      <li>Introduction to heaps and heap properties</li>
      <li>Heap Sort algorithm and implementation</li>
      <li>Time complexity analysis</li>
    </ul>

    <h3>4.2 Divide-and-Conquer Strategy</h3>
    <ul>
      <li>Principles of divide-and-conquer</li>
      <li>Problem decomposition and solution combination</li>
      <li>Applications in sorting and searching</li>
    </ul>

    <h3>4.3 Merge Sort</h3>
    <ul>
      <li>Merge Sort algorithm and implementation</li>
      <li>Merging process analysis</li>
      <li>Recurrence relation and complexity</li>
      <li>Modified merge sort variants</li>
    </ul>

    <h3>4.4 Quick Sort</h3>
    <ul>
      <li>Quick Sort algorithm and implementation</li>
      <li>Partitioning strategies</li>
      <li>Time complexity analysis</li>
      <li>Practical considerations and optimizations</li>
    </ul>
  </div>

  <div class="syllabus-section">
    <div class="section-header">
      <h2>5. Order Statistics and Matrix Operations</h2>
    </div>
    <h3>5.1 Order Statistics</h3>
    <ul>
      <li>Finding maximum and minimum elements</li>
      <li>Selection algorithms for k-th smallest element</li>
      <li>QuickSelect algorithm</li>
    </ul>

    <h3>5.2 Matrix Multiplication</h3>
    <ul>
      <li>Standard matrix multiplication algorithm</li>
      <li>Strassen's algorithm</li>
      <li>Comparative analysis and applications</li>
    </ul>
  </div>

  <div class="syllabus-section">
    <div class="section-header">
      <h2>6. Greedy Algorithms</h2>
    </div>
    <ul>
      <li>Greedy algorithm principles</li>
      <li>Scheduling problems and solutions</li>
      <li>Huffman coding</li>
      <li>Fractional Knapsack problem</li>
      <li>Minimum Spanning Trees:
        <ul>
          <li>Prim's algorithm</li>
          <li>Kruskal's algorithm</li>
        </ul>
      </li>
      <li>Dijkstra's algorithm for shortest paths</li>
      <li>Optimal merge patterns</li>
    </ul>
  </div>

  <div class="syllabus-section">
    <div class="section-header">
      <h2>7. Dynamic Programming</h2>
    </div>
    <h3>7.1 Fundamentals</h3>
    <ul>
      <li>Principle of optimality</li>
      <li>Memoization and tabulation</li>
      <li>Basic examples: Binomial Coefficient, Making Change</li>
    </ul>

    <h3>7.2 Classical Problems</h3>
    <ul>
      <li>0/1 Knapsack and variations</li>
      <li>Subset Sum Problem</li>
      <li>Equal Sum Partition Problem</li>
      <li>Longest Common Subsequence</li>
      <li>Longest Common Substring</li>
      <li>String transformation problems</li>
      <li>Longest Palindromic Subsequence</li>
    </ul>

    <h3>7.3 Advanced Applications</h3>
    <ul>
      <li>Unbounded Knapsack</li>
      <li>Rod Cutting Problem</li>
      <li>Coin Change Problems</li>
      <li>Shortest Path Algorithms:
        <ul>
          <li>Bellman-Ford Algorithm</li>
          <li>Floyd-Warshall Algorithm</li>
        </ul>
      </li>
    </ul>
  </div>

