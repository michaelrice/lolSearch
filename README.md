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
    source lolsearch/bin/activate

Next you need to check out the code from github

    git clone https://github.com/michaelrice/lolsearch.git
    cd lolsearch

Next install the required pip packages

    pip install -r requirements.txt

This should pull in Django, giphy_client, django-taggit, and PyYaml

Next you need to do some basic Django tasks to prep the app

    python manage.py makemigrations
    python manage.py migrate
    python manage.py test

This will setup the SQLite database and run the application tests

Next create a superuser for the app.

    python manage.py createsuperuser

Follow prompts to complete user creation.

Next add your API key to the `settings.yaml` file. Replace `YOUR_GIPHY_API_KEY` with your actual Giphy API key.
Quotes are not needed around the API key.

Now lolsearch is ready to be started

    python manage.py runserver

Open a web browser and visit: http://127.0.0.1:8000/