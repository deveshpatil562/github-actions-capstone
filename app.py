from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

profile = {
    "name": "Devesh Patil",
    "title": "Infrastructure Analyst | Linux Administrator | DevOps Enthusiast",
    "about": "Linux Administrator with 3+ years of experience managing enterprise infrastructure, automation, and cloud environments. Passionate about DevOps, CI/CD, Docker, and Cloud.",
    "github": "devesh-github-username",
    "linkedin": "https://linkedin.com/in/YOUR_LINKEDIN"
}

skills = [
    "Linux", "Docker", "Kubernetes",
    "GitHub Actions", "AWS",
    "Python", "Bash",
    "Networking", "Terraform"
]

visitors = 0


@app.route("/")
def home():
    global visitors
    visitors += 1

    repos = []

    try:
        url = f"https://api.github.com/users/{profile['github']}/repos"
        response = requests.get(url)
        repos = response.json()[:6]
    except:
        repos = []

    return render_template(
        "index.html",
        profile=profile,
        skills=skills,
        repos=repos,
        visitors=visitors
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)