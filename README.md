### Start Machine Learning Project

### Software and Account Requirement

1. [Github account](https://github.com)
2. [Heroku account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation]()

Creating conda enviroment:  
conda create -p venv python==3.12.2 -y
...

Activating conda enviroment:
conda activate venv/ (command_prompt)
or
conda activate venv
...

Installing flask:
pip install -r requirements.txt
...

To add files to git:
git add file_name
...

To ignore file or folder we can write the name of that particular file or folder to the .gitignore file
...

To check the git status:
git status
...

To check all version maintained by git:
git log
...

To create version/commit all changes by git:
git commit -m "message"
...

To send versuin or changes to github:
git push origin main
...

To check remote url:
git remote -v
...

To setup CI/CD pipeline in Heroku we need 3 informations
1. Heroku_Email = 
2. Heroku_API_key = 
3. Heroku_app_name = 
...

Build DOCKER image
docker build -t <image name>:<tagname>
...

Note: Image name for docker must be in lowercase

To list docker images
docker images
...

Run docker image 
docker run -p 5000:5000 -e PORT=5000 (image id)

To check running container in docker
docker ps
...

To stop docker container
docker stop container_id
...

Automatically install all the libraries tha we have 
mentioned in requirements.txt
Python setup.py install
...