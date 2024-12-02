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

<div class="courses">
{%- if site.enable_course_categories and page.display_categories -%}
  {%- for category in page.display_categories -%}
    <h2 class="category" id="{{ category }}">{{ category }}</h2>
    {% assign categorized_courses = site.courses | where: "course", category %}
    {% assign sorted_courses = categorized_courses | sort: "semester" | reverse %}
    <div class="row row-cols-1 row-cols-md-3">
      {%- for course in sorted_courses -%}
        {% include courses.liquid %}
      {%- endfor -%}
    </div>
  {%- endfor -%}
{%- endif -%}
</div>
