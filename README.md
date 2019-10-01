# Bigparser
This project is developed in python using 
BDD (Behavior Driven Development) frame work .
 Test cases flow is written in Feature Files
  in Gerkin Language which uses simple daily 
  use language and simple keywords like Given
   , Then etc.It make it easy to understand 
   the flow of execution.
#Built With  
•	Python – Language used for development 

•	Selenium – Web automation framework

•	Pycharm – Tool used for development

•	BDD – Development Approach used in Project 

#Prerequisites

•	python

•	behave 

•	selenium

•	git bash

#Setting up Environment and Running Project:

Steps to run the project:

1- Install Python:
If not installed, can be download from here: https://www.python.org/downloads/
In order to check if python is installed or not: python --version

2- Install Behave:
Install behave by "pip install behave" in CMD or power shell

3- Install Selenium:
Install selenium by "pip install selenium" in CMD or Shell

4- Clone Project repository “Bigparser”

 Steps: 

•	Install Git bash

•	 Open Git bash and go to location of your local machine where you want to clone repository through “cd” command (Location must be any empty folder not any Drive(C,D,E etc))

•	Run command “git clone clone_link_copied_from_repository” 

5- Setting download and upload file paths of project according to your local machine 

•	Go to Bigparser>src>features>pages

•	Open RenameParticularGridPageFile

•	Replace “E:\\Bigparser\\RenameTest.xlsx” with path of file you want to upload

•	Go to Bigparser>src>features>pages

•	Open DownloadPageFile

•	Replace “E:\\av2\\big\\automation\\Bigparser” with path of your cloned repository 

•	Replace “Rename.xlsx” with name of your uploaded file

5-Running cloned repository "Bigparser"
    Using “cd” command move to project repository Bigparser and run this command

    “behave .\src\features\featurefiles\BPMainFlow.feature"

#Versioning

We are using Git version control tool in this project.

Git is a distributed version-control system for tracking changes in source code during software development. It is designed for coordinating work among programmers, but it can be used to track changes in any set of files. Its goals include speed, data integrity, and support for distributed, non-linear workflows.
