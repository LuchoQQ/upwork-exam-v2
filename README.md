# Upwork - Entry Exam

## Goal
Working FastAPI API with a User and Profile models and schemas.

## Instructions
1. Fork this repository
2. Complete the tasks below adhering to the requirements
3. Submit a pull request with your solution in your forked repository
4. Deliver a GitHub repository with your solution (it can be private, just give access to @arielaco)

## Tasks
- [x] Create a [User](###User) and [Profile](###Profile) models and schemas 
- [x] Develop a REST API exposing CRUD endpoints for both models
- [x] Test at least 2 endpoints using pytest (with fixtures)
- [x] Point docs to root path
- [x] Create requirements file
- [x] Add a section on `README.md` with setup (venv), install (pip), run and testing instructions

### User
- Email as username
- Can have multiple profiles
- Can have a list of favorite profiles

### Profile
- It has a name and a description
- Belongs to a user

## Requirements
- Use English for all code, comments, commit messages, and documentation
- Delete dead code (unrelated to tasks)
- All responses must be JSON
- Implement proper folder structure
- Validation must be done using Pydantic
- Use multiple commits (when possible, use conventional commit messages)

## Setup

1. Create a new Anaconda environment with Python:
   ```bash
   conda create --upwork-exam-v2 python=3

2. Activate the Anaconda environment:
    ```bash
   conda activate upwork-exam-v2

3. Install project dependencies using pip:
    ```bash
   pip install -r requirements.txt

## Run

1. To run the project within the Anaconda environment for development in project root directory:
    ```bash
   uvicorn app.main:app --reload 

# Testing

1. You can run the test within Anaconda environment using pytest library:
    ```bash
    pytest