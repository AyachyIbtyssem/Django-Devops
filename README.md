# Django DevOps Mini Project

A simple Django backend project to demonstrate **CI/CD pipeline** with **GitLab** and **Docker**.  
This project focuses on testing, building, and deploying a Django backend using **GitLab CI/CD**.

---

## Technologies Used

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4-green?logo=django&logoColor=white)
![GitLab](https://img.shields.io/badge/GitLab-DevOps-orange?logo=gitlab&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker&logoColor=white)

---

## Project Overview

- Backend only: Django project without database for simplicity  
- Focus on **CI/CD workflow**: Test → Build → Deploy  
- Dockerized for easy deployment  
- Mirrored from GitHub to GitLab (optional)  

---

## CI/CD Pipeline

### 1. Test Stage

- GitLab runs:

```bash
pip install -r requirements.txt
python manage.py check

