# 🚀 DevOps Portfolio Website (Flask)

![GitHub Repo stars](https://img.shields.io/github/stars/deveshpatil562/YOUR_REPO?style=social)
![GitHub forks](https://img.shields.io/github/forks/deveshpatil562/YOUR_REPO?style=social)

![CI/CD Pipeline](https://img.shields.io/github/actions/workflow/status/deveshpatil562/YOUR_REPO/main-pipeline.yml?label=CI%2FCD%20Pipeline)

![Docker](https://img.shields.io/badge/docker-ready-blue)
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

![GitHub last commit](https://img.shields.io/github/last-commit/deveshpatil562/YOUR_REPO)
![GitHub issues](https://img.shields.io/github/issues/deveshpatil562/YOUR_REPO)
![GitHub pull requests](https://img.shields.io/github/issues-pr/deveshpatil562/YOUR_REPO)

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=deveshpatil562.YOUR_REPO)

---

# 👨‍💻 About This Project

This is a **modern DevOps-style portfolio website built with Flask** that showcases my professional profile, skills, and GitHub projects.

The site includes:

* Animated DevOps background
* GitHub repository auto-fetch
* Terminal-style skills section
* Dark / Light mode
* Responsive UI
* Docker-ready architecture
* CI/CD pipeline compatibility

This project also serves as a **demonstration project for GitHub Actions CI/CD pipelines**.

---

# 👤 Author

**Devesh Patil**
Infrastructure Analyst | Linux Administrator | DevOps Enthusiast

🔗 LinkedIn
https://linkedin.com/in/YOUR_LINKEDIN

💻 GitHub
https://github.com/YOUR_GITHUB

---

# 🛠 DevOps Tech Stack

| Category         | Tools                 |
| ---------------- | --------------------- |
| Backend          | Flask, Python         |
| Frontend         | HTML, CSS, JavaScript |
| Containerization | Docker                |
| CI/CD            | GitHub Actions        |
| API Integration  | GitHub REST API       |

### Tech Stack Icons

![Python](https://img.shields.io/badge/Python-3776AB?logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux\&logoColor=black)

---

# 🏗 Architecture Diagram

```
                +--------------------+
                |   User Browser     |
                +---------+----------+
                          |
                          v
                +--------------------+
                |    Flask App       |
                |    (Portfolio)     |
                +---------+----------+
                          |
                          v
                +--------------------+
                |   GitHub API       |
                | Fetch Repositories |
                +--------------------+
```

### CI/CD Pipeline

```
Developer Push
      |
      v
GitHub Repository
      |
      v
GitHub Actions Workflow
      |
      v
Run Tests → Build Docker Image
      |
      v
Push Docker Image
      |
      v
Deploy Portfolio App
```

---

# 📁 Project Structure

```
portfolio-devops-site
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── static
│   ├── style.css
│   ├── script.js
│   └── devops-bg.js
│
├── templates
│   └── index.html
│
└── tests
    └── test_app.py
```

---

# ⚙️ Installation

### Clone Repository

```
git clone https://github.com/YOUR_GITHUB/portfolio-devops-site.git
cd portfolio-devops-site
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Run Application

```
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

# 🐳 Run with Docker

### Build Image

```
docker build -t portfolio-site .
```

### Run Container

```
docker run -p 5000:5000 portfolio-site
```

---

# 🔍 Application Endpoints

| Endpoint  | Description           |
| --------- | --------------------- |
| `/`       | Main portfolio page   |
| `/health` | Health check endpoint |

---

# 🧪 Run Tests

```
pytest
```

---

# 📸 Screenshots

### Portfolio Home Page

<img width="1877" height="791" alt="Screenshot 2026-03-17 045521" src="https://github.com/user-attachments/assets/54b58a53-5d90-4385-98de-cedbbd5f976b" />

```

### Projects Section

*Add screenshot here*

```
docs/screenshot-projects.png
```

---

# 🔮 Future Improvements

* GitHub contribution heatmap
* Contact form
* Resume download button
* Kubernetes deployment
* Slack deployment notifications
* Real visitor analytics

---

# ⭐ Support

If you like this project, please **star ⭐ the repository**.

---

# 📜 License

MIT License
