---
layout: page
title: Teaching
description: Courses I teach at Missouri S&T
permalink: /teaching/
nav: true
nav_order: 5
display_categories: ["CS 2500: Algorithms", "CS 5001: Information Retrieval", "CS 6001: Neural Information Retrieval"]
horizontal: true
---

<style>
.category-section {
  margin-bottom: 3rem;
}

.current-courses {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 20px;
}

.course-item {
  flex: 0 1 calc(33.333% - 20px);
  min-width: 300px;
}

.past-courses {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
}

.show-past {
  width: 100%;
  margin: 20px 0;
}

/* Ensure cards maintain consistent width */
.card {
  height: 100%;
  margin: 0;
}

/* Make sure images don't cause layout shifts */
.card-img-top {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.page-description {
  font-weight: bold;
  font-size: 1.5rem; /* Adjust size as needed */
  margin-bottom: 20px;
}

@media (max-width: 768px) {
  .course-item {
    flex: 0 1 100%;
  }
}
</style>

<!-- <div class="page-description">
  I teach the following courses at Missouri S&T
</div> -->

<div class="courses">
  {%- if site.enable_course_categories and page.display_categories -%}
    {%- for category in page.display_categories -%}
      <div class="category-section">
        <h2 class="category" id="{{ category }}">{{ category }}</h2>
        {% assign categorized_courses = site.courses | where: "course", category %}
        {% assign main_courses = categorized_courses | where_exp: "item", "item.path contains 'index.md'" %}
        {% assign sorted_courses = main_courses | sort: "semester" | reverse %}
        
        <div class="current-courses">
          {% assign current_course = sorted_courses | first %}
          {% assign course = current_course %}
          {% if course %}
            {% include courses.liquid %}
          {% endif %}
        </div>
        
        {% assign past_courses = sorted_courses | slice: 1, sorted_courses.size %}
        {% if past_courses.size > 0 %}
          <div class="show-past">
            <button class="btn btn-sm btn-outline-primary" onclick="togglePastOfferings('pastOfferings{{ forloop.index }}')">
              Show Past Offerings ({{ past_courses.size }})
            </button>
            
            <div class="collapse" id="pastOfferings{{ forloop.index }}">
              <div class="past-courses">
                {%- for course in past_courses -%}
                  {% include courses.liquid %}
                {%- endfor -%}
              </div>
            </div>
          </div>
        {% endif %}
      </div>
    {%- endfor -%}
  {%- endif -%}
</div>
<script>
function togglePastOfferings(id) {
  const element = document.getElementById(id);
  const button = event.target;
  
  if (element.classList.contains('show')) {
    element.classList.remove('show');
    button.textContent = `Show Past Offerings (${element.querySelectorAll('.course-item').length})`;
  } else {
    element.classList.add('show');
    button.textContent = `Hide Past Offerings (${element.querySelectorAll('.course-item').length})`;
  }
}
</script>
