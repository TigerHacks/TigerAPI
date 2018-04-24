# How to Set Up Local Virtual Environment (and server) 
----------------------------
### Requirements 
1. Make sure Python 3 installed 
.a. Check to see if it is installed run `python --version`
.b. Python 3.6.5
2. Make sure pip 10 is installed
.a. Type `pip --version` 
.b. pip 10
.c. If pip 10 is not the current version on your computer, **upgrade**by using the following command `python -m pip install --upgrade pip`

Pip is a Package manager for python which we will use to load in modules/libraries into our environments.
An example of one of these libraries is VirtualEnv which will help us keep our environments clean from other Libraries. This sounds really confusing but as you start using it you’ll begin to understand how valuable this encapsulation of modules/libraries can be.

## Install the Virtual Environment 
run `pip install virtualenv` then 
Install virtual environment wrapper 
`pip install virtualenvwrapper-win`

## Implement your own server 
 
### Create VE 
### Make Your VE 
### Connect project to VE 
### Set project directory 
### Deactivate 
### Workon
### Pip install
### Flask


Make a Virtual Environemt:
Lets call it HelloWold. All we do in a command prompt is enter `mkvirtualenv HelloWold`
This will create a folder with python.exe, pip, and setuptools all ready to go in its own little environment. It will also activate the Virtual Environment which is indicated with the (HelloWold) on the left side of the prompt.

Anything we install now will be specific to this project. And available to the projects we connect to this environment.
Connect our project with our Environment:
Now we want our code to use this environment to install packages and run/test code.
First lets create a directory with the same name as our virtual environment in our preferred development folder. In this case mine is ‘dev’
See here:

HelloWold will be the root folder of our first project!
Set Project Directory:
Now to bind our virtualenv with our current working directory we simply enter ‘setprojectdir .’
Like so:

Now next time we activate this environment we will automatically move into this directory!
Deactivate:
Let say you’re content with the work you’ve contributed to this project and you want to move onto something else in the command line. Simply type ‘deactivate’ to deactivate your environment.
Like so:

Notice how the parenthesis disappear.
You don’t have to deactivate your environment. Closing your command prompt will deactivate it for you. As long as the parenthesis are not there you will not be affecting your environment. But you will be able to impact your root python installation.
Workon:
Now you’ve got some work to do. Open up the command prompt and type ‘workon HelloWold’ to activate the environment and move into your root project folder.
Like so:

Pretty sweet! Lets get working.
Pip Install:
To use flask we need to install the packages and to do that we can use pip to install it into our HelloWold virtual environment.
Make sure (HelloWold) is to the left of your prompt and enter ‘pip install flask’
Like so:

This will bring in all the tools required to write your first web server!
Flask:
Now that you have flask installed in your virtual environment you can start coding!
Open up your favorite text editor and create a new file called hello.py and save it in your HelloWold directory.
I’ve simply taken the sample code from Flask’s website to create a very basic ‘Hello World!’ server.
I’ve named the file hello.py.
Once the code is in place I can start the server using ‘python hello.py’ this will run the python instance from your virtual environment that has flask.
See here:

You can now navigate with your browser to http://127.0.0.1:5000/ and see your new site!
Sweet. You have everything you need to start working through tutorials on Flask without worrying about gunking up your Python installations.
Let me know if you have any questions! Happy Developing!


----------------------------------------
#### Reference 
For more detailed guide: http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/

https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask


