# Project name
# Project description
*Importance of the project*
*What the project does*

# Installation section
*Tell other users how to install your project locally*

1. Open the Command Prompt (cmd)

1. Create a Virtual Environment:
    + in Command Prompt (powershell)
    + create a folder for new virtual env: `mkdir Virtual_env`
    + change directories: `cd Virtual_env`
    + create virtual env: `virtualenv appvenv`
    + you will see Scripts in appvenv
    + switch to Command Prompt (admin) 

1. Activate the Virtual Environment:
    + On Windows (Command Prompt):
        1. change directory to Scripts `cd "path\to\scripts\in\virtual\environment"`
        1. `activate.bat`
        1. change directory to app root directory: `cd "path\to\app"`

1. Install Python:   
    1. Download Python to run the program @ https://www.python.org/downloads/
    1. Run the Python Installer
    1. Check the Box for "Add Python to PATH"
    In cmd:
    1. Verify pip installation: `pip --version`

# Usage section

*Outline the steps necessary to build and run your application with venv and Docker:*
+ Install Docker desktop @ https://www.docker.com/products/docker-desktop
+ Open Docker Desktop

+ Use the Command Prompt
    1. Check that Docker desktop was successfully installed: `docker run hello-world`
    1. Build the docker image: `docker build -t bookshelf .` 
    1. Run the docker image: `docker run -it bookshelf`
    1. Deactivate the Virtual Environment: `deactivate`

+ Use Docker Playground
    1. create a repository
    1. Follow: https://labs.play-with-docker.com/
    1. Start a new instance
    In the terminal: 
        1. Copy command from Dockerhub @ https://hub.docker.com/repository/docker/kcse1/bookshelf-capstone/general: 
        `docker pull kcse1/bookshelf-capstone:latest`
        1. `docker run kcse1/bookshelf-capstone:latest`
    1. Close session

*Include screenshots of your project in action*

# Credits
*Highlights and links to the authors of your project if the project has been created by more than one person*
@KC-software-en

# Add a URL to your GitHub repository
https://github.com/KC-software-en/friendly-robot