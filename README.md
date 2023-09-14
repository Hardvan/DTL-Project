# DTL Project

Welcome to the DTL Project repository! This project is aimed at providing a platform for the RV College of Engineering community to stay updated about events, clubs, and various activities. Below, you'll find more information about the project and how you can contribute to it.

## [Link to the Website](https://dtl-project-rvce.onrender.com/) (Hosted on Render)

## Project Overview

The DTL Project is a web-based platform designed to serve the RV College of Engineering community. It offers the following features:

- **Events**: Stay informed about upcoming, ongoing, and completed events happening within the college. You can also view detailed event information.

- **Clubs**: Explore and learn more about the various clubs and departments operating within the college.

- **Chatbot**: Interact with the DTL Chatbot, which can provide information about events and assist you with various tasks related to the college.

## Project Structure

Here's a brief overview of the main project files and directories:

- `app.py`: Contains the Flask application code for the DTL Project, including routes for different sections of the website and the chatbot functionality.

- `PostHandler.py`: A module responsible for handling posts and formatting data for display on the website.

- `templates`: This directory contains HTML templates for different pages of the website, such as the dashboard and chatbot pages.

## Project Directory Structure

Click [here](./directory_structure.md) to view the project directory structure and learn more about the different files and directories involved in the project.

## Automation Scripts Used

- `DirecTracer.py`: Save the directory structure to text and Markdown files.
- `FileReader.py`: Reads selected files in a directory and writes the contents to a file.

## How to Contribute

1. Fork the repository by clicking on the `Fork` button on the top of the page. This will create a copy of this repository in your account.

2. Clone the repository to your local machine

   ```bash
   git clone https://github.com/Hardvan/DTL-Project
   ```

3. Create a new branch with a descriptive name

   ```bash
    git checkout -b <branch-name>
   ```

4. Make changes to the code base and push it to your remote repository

   ```bash
    git add .
    git commit -m "<your-commit-message>"
    git push origin <branch-name>
   ```

5. Create a Pull Request from your forked repository (Click on the `New Pull Request` button located at the top of your repo)

6. Wait for your PR review and merge approval!

## Some Important Notes

- Click anywhere on the website at the start to play the audio message from the chatbot. (This is because of Google Chrome's [autoplay policy](https://developer.chrome.com/blog/autoplay/))
