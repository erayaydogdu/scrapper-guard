# Dockerizing the Flask API - Plan

## 1. Gather Information
*   Completed.

## 2. Clarify Requirements
*   Completed.
    *   Base image: `python:3.9-slim-buster`
    *   Port: Specified as an environment variable in `.env`
    *   Other environment variables: `MONGODB_URI`, `MONGODB_DATABASE`

## 3. Create Dockerfile
*   Create a `Dockerfile` that specifies the base image, copies the application code, installs dependencies, defines the entry point for the container, and exposes the port, `MONGODB_URI`, and `MONGODB_DATABASE` from the environment variable.

## 4. Create .dockerignore
*   Create a `.dockerignore` file to exclude unnecessary files and directories from the Docker image, such as `.git` or `__pycache__`.

## 5. Create docker-compose.yml (Optional)
*   Show how to use envirnment parameters in docker-compose file

## 6. Test the Docker Image
*   Provide instructions on how to build and run the Docker image locally to ensure it works as expected and push it to docker hub.

## 7. Switch to Code Mode
*   Switch to code mode to implement the solution.