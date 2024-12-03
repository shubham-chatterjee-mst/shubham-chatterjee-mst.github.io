# Personal Website


A modern, responsive, and dynamic website for showcasing course materials and academic content. Built using the [al-folio](https://github.com/alshedivat/al-folio) theme with custom modifications for course management.

## ✨ Features

- **Course Management**: Organized structure for multiple courses
- **Interactive Syllabus**: Dynamic syllabus pages with detailed course information
- **Assignment Tracking**: Clear presentation of weekly and quick assignments
- **Resource Library**: Easy access to lecture slides, assignments, and course materials
- **Responsive Design**: Optimized for all devices and screen sizes
- **Coming Soon Pages**: Elegant placeholder pages for upcoming courses
- **Modern UI**: Clean and professional interface with animations

## 🚀 Quick Start

1. Clone the repository
```bash
git clone https://github.com/yourusername/teaching-website.git
cd teaching-website
```

2. Install dependencies
```bash
bundle install
```

3. Start the development server
```bash
bundle exec jekyll serve
```

4. Visit `http://localhost:4000`

## 📁 Directory Structure

```
.
├── _courses/           # Course-specific content
├── _includes/         # Reusable components
├── _layouts/          # Page layouts
├── assets/           # Static files
│   ├── img/         # Images
│   ├── pdf/         # Course materials
│   └── css/         # Stylesheets
└── pages/           # Main pages
```

## 🔧 Customization

### Adding a New Course

1. Create a new directory in `_courses/`
2. Add course metadata in the front matter
3. Create course-specific pages (syllabus, assignments, etc.)

Example:
```yaml
---
layout: page
title: "Course Title"
description: "Course Description"
img: assets/img/course-image.jpg
---
```

### Modifying Styles

- Edit `assets/css/main.scss` for global styles
- Course-specific styles can be added inline or in separate CSS files

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Based on the [al-folio](https://github.com/alshedivat/al-folio) theme
- Inspired by modern academic websites
- Thanks to all contributors

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Your Name - [shubham.chatterjee94@gmail.com](mailto:shubham.chatterjee94@gmail.com)

Project Link: [https://github.com/shubham-chatterjee-mst/shubham-chatterjee-mst.github.io](https://github.com/shubham-chatterjee-mst/shubham-chatterjee-mst.github.io)

---

⭐ Star this repo if you find it helpful!