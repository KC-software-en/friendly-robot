# Get Python in Container to have a runtime environment
FROM python:3.7.0

# Set environment variables
# By default, Python buffers its output when it is not connected to a terminal or when it's running in a non-interactive mode
# Buffering = Python collects some of the program's output in memory before displaying it -> This can lead to delayed output
# tell Python to run in unbuffered mode -> every line of output is immediately printed without waiting for a buffer
ENV PYTHONUNBUFFERED 1

# create a directory inside container from which to run the program 
RUN mkdir /app

# set a working directory & switch to it
# subsequent commands in the Dockerfile will be executed in working directory
WORKDIR /app

# copy contents from root directory to the current directory which will be /app
ADD . ./

# # Copy the requirements file into the container at /app/
COPY requirements.txt /app/

# run the command to install dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# run the command to run the container
CMD ["python", "Capstone Project I.py"]