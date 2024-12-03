<!-- Main courses page (courses.md) -->
---
layout: page
title: Teaching
permalink: /teaching/
description: Courses I teach at the university.
nav: true
nav_order: 5
display_categories: ["CS 2500: Algorithms", "CS 3000: Systems"]
horizontal: false
---

<!-- pages/courses.md -->
<div class="courses">
{% if site.enable_course_categories and page.display_categories %}
  <!-- Display categorized courses -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_courses = site.courses | where: "course", category %}
  {% assign sorted_courses = categorized_courses | sort: "semester" | reverse %}
  <!-- Generate cards for each course offering -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for course in sorted_courses %}
      {% include courses_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for course in sorted_courses %}
      {% include courses.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}
{% else %}
<!-- Display courses without categories -->
{% assign sorted_courses = site.courses | sort: "semester" | reverse %}
  <!-- Generate cards for each course -->
{% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for course in sorted_courses %}
      {% include courses_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for course in sorted_courses %}
      {% include courses.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
