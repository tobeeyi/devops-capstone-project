# DevOps Capstone Project

![CI Build](https://github.com/tobeeyi/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)

## Project Description
This repository contains the Customer Accounts microservice developed as part of the DevOps Capstone Project. The project demonstrates the practical application of Agile planning methodologies, Test-Driven Development (TDD), Continuous Integration (CI) using GitHub Actions, security enforcement, and containerized deployment with Docker and Kubernetes.

## Features Implemented
* **Agile Planning:** Managed project requirements using a Kanban board with structured user stories, estimates, and sprints.
* **RESTful Account Service:** Developed a complete CRUD (Create, Read, Update, Delete) and List API using Python and Flask.
* **Test-Driven Development (TDD):** Achieved high test coverage using `nosetests` and automated code quality linting with `flake8`.
* **Continuous Integration:** Configured automatic testing, database initialization (PostgreSQL), and linting on every push or pull request to the main branch.
* **Application Security:** Integrated `Flask-Talisman` for secure headers and configured Cross-Origin Resource Sharing (CORS) policies.
* **Cloud Deployment:** Containerized the application using Docker and deployed the microservice to a Kubernetes cluster.

## How to Run the Tests
To run the automated test suite locally, execute the following command:
```bash
nosetests --with-spec --spec-color
