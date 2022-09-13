# base image 
FROM  python:3.10-alpine

# sets the working directory inside the container
WORKDIR /rubot

# copies required files from the host machine into the container
COPY ./requirements.txt . 
COPY ./Twitter-Bot/rubot.py . 

# runs the command to install dependencies
RUN pip install -r requirements.txt

# command that will run when the container starts
CMD [ "python", "./rubot.py" ]
