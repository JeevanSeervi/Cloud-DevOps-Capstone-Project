# Cloud & DevOps Capstone Project

A complete Cloud & DevOps capstone project demonstrating how to build, containerize, automate, deploy, and monitor a Python Flask REST API using Docker, GitHub Actions, AWS EC2, Nginx, SQLite, and CloudWatch.

---

## 🚀 Project Overview

This project is a Task Management REST API built with Python Flask.

The application is:

- Developed using Python and Flask
- Connected to a SQLite database
- Containerized using Docker
- Managed using Docker Compose
- Version controlled using Git and GitHub
- Automatically tested and built using GitHub Actions
- Automatically deployed to AWS EC2 using CI/CD
- Served through Nginx
- Monitored using AWS CloudWatch

---

## 🏗️ Architecture

```text
Developer
    |
    | git push
    v
GitHub Repository
    |
    | GitHub Actions
    v
+-------------------------+
| CI/CD Pipeline          |
|                         |
| CI:                     |
| - Checkout              |
| - Setup Python          |
| - Install dependencies  |
| - Validate application  |
| - Build Docker image    |
|                         |
| CD:                     |
| - SSH to EC2            |
| - Pull latest code      |
| - Build Docker image    |
| - Restart containers    |
+------------+------------+
             |
             v
       AWS EC2 Instance
             |
             v
          Nginx
          Port 80
             |
             v
      Docker Compose
             |
             v
      Flask Application
          Port 5000
             |
             v
       SQLite Database
             |
             v
       AWS CloudWatch
       Monitoring