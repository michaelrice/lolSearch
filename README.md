# LOLSearch

## Code Challenge

### POC Django App That Uses The Giphy API


### Running App

This application is currently only meant to be run in development mode of django using `python manage.py runserver`
It is configured to use a SQLite backend so no additional drivers are needed for test it out.

To setup an environment suitable for running the app you will need to get an API key from giphy. Visit https://developers.giphy.com/ for details.

Next you will need python 3.7 Older versions may work but this has only been tested on 3.7 With python3.7 installed setup 
a virtualenv

    mkdir $HOME/venvs
    cd $HOME/venvs
    virtualenv lolsearch

Next you need to check out the code from github

    git clone 