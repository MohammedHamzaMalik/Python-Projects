'''
In this project-based tutorial, you’ll build a content aggregator from scratch using Python 
and the popular framework Django.

With so much content coming out online daily, it can be time consuming to go to multiple sites 
and sources to consume information about your favorite subjects. This is why content aggregators are so popular and powerful, as you can use them to view all the latest news and content in one place.

Whether you’re looking for a portfolio project or ways in which to extend future projects beyond
simple CRUD capabilities, this tutorial will have something for you.
'''

'''
Step 1: Setting Up Your Project
By the end of this step, you’ll have set up your environment, installed your dependencies, 
and finished getting Django up and running.

Begin by making your project directory and then changing directory into it:

$ mkdir pycasts
$ cd pycasts
'''

'''
Now that you’re inside your project directory, you should create your virtual environment and 
activate it. Use whatever tool makes you happiest to do this. This example uses venv:

$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python -m pip install --upgrade pip

With your environment now activated and pip upgraded, you’ll need to install the required 
dependencies to complete the project. You can find a requirements.txt file in the downloadable 
source code for this tutorial:

Get Source Code: Click here to get the source code you’ll use to build a content aggregator 
with Django and Python in this tutorial.

Open the source_code_setup/ folder and install the pinned dependencies. Be sure to replace the 
<path_to_requirements.txt> with the actual path of your downloaded file:

(.venv) $ python -m pip install -r <path_to_requirements.txt>
You should now have Django, feedparser, django-apscheduler, and their sub-dependencies installed.

Now that you have all the tools you need to get up and running, you can set up Django and start 
building. To complete this step of the build, you need to do the following four things:

Create your Django project in the current working directory, /pycasts
Create a podcasts Django app
Run initial migrations
Create a superuser
As you’re familiar with Django already, you won’t explore each of these steps in detail. 
You can go ahead and run the following commands:

(.venv) $ django-admin startproject content_aggregator .
(.venv) $ python manage.py startapp podcasts
(.venv) $ python manage.py makemigrations && python manage.py migrate
(.venv) $ python manage.py createsuperuser
'''

'''
Once you’ve followed Django’s prompts and finished creating your superuser account, you have one more change to make before testing that the app works. Although the application will run without it, don’t forget to add your new podcasts app to the settings.py file:

# content_aggregator/settings.py

# ...
'''

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # My Apps
    "podcasts.apps.PodcastsConfig",
]

'''
You listed your new app in INSTALLED_APPS as "podcasts.apps.PodcastsConfig".

The time has come to take your new Django project for a spin. Start the Django server:
(.venv) $ python manage.py runserver

Navigate to localhost:8000 in your browser and you should see Django’s default success page:
'''

'''
Step 2: Building Your Podcast Model
At this point, you should have your environment set up, your dependencies installed, and Django 
successfully running. By the end of this step, you’ll have defined and tested a model for podcast 
episodes and migrated the model to the database.

Your Episode model shouldn’t only reflect the information you’d like to capture as the developer. 
It should also reflect the information that the user would like to see. It’s tempting to jump 
into the code and start writing your model right away, but that could be a mistake. 
If you do that, you might soon forget about your user’s point of view. And after all, 
applications are meant for users—even users such as you or other developers.

Taking out a pen and paper can be useful at this point, but you should do whatever works for you. 
Ask yourself, “As a user, what would I like to do?” and answer that question over and over until 
you’ve exhausted all your ideas. Then you can ask yourself what’s missing by thinking about what 
you’d like as a developer.

This can be a good tactic when writing database models, and it can save you from needing to add 
extra fields later and running unnecessary migrations.

Note: You might have a list that’s different from the one below, and that’s okay. As the author 
of this tutorial, I’m sharing what I came up with, and that’s what you’ll use for the rest of 
this project.

But if there’s a field or attribute you feel is missing, then feel free to extend the application 
to add it at the end of this tutorial. This is your project, after all. Make it your own!

List your project’s requirements from a user’s perspective as well as a developer’s perspective:
'''

'''
You’ll see more of this last point in step 4 of this tutorial.

Given the requirements you listed, the Episode model in your podcasts app should look like this:
'''
# podcasts/models.py

from django.db import models

class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"

'''
One of the most powerful parts of Django is the built-in admin area. Having the episodes stored 
in the database is one thing, but you’ll also want to be able to interact with them in the admin 
area too. You can do this by replacing the code in your podcasts/admin.py file to tell the Django 
admin that you want to display your episode data:
'''
# podcasts/admin.py

from django.contrib import admin

from .models import Episode

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("podcast_name", "title", "pub_date")


'''
You can ensure that you don’t see this error by adding an extra line to the PodcastsConfig 
class in the app.py file:
'''
# podcasts/app.py

from django.apps import AppConfig

class PodcastsConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "podcasts"


'''
Now your app is configured to add a primary key to all your models automatically. 
You also have a picture of what your data should look like, and you have it represented in a model. 
You can now run the Django migrations to include your Episode table in the database:

(.venv) $ python manage.py makemigrations
(.venv) $ python manage.py migrate
'''

'''
Now that you have migrated the changes, it’s time to test it!

This tutorial is already covering a lot, so for simplicity, you’ll be using Django’s built-in 
testing framework for your unit tests. After completing the project in this tutorial, feel free 
to rewrite the unit tests with pytest or another testing framework if you’d prefer.

In your podcasts/tests.py file, you can add:
'''
# podcasts/tests.py

from django.test import TestCase
from django.utils import timezone
from .models import Episode

class PodCastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title="My Awesome Podcast Episode",
            description="Look mom, I made it!",
            pub_date=timezone.now(),
            link="https://myawesomeshow.com",
            image="https://image.myawesomeshow.com",
            podcast_name="My Python Podcast",
            guid="de194720-7b4c-49e2-a05f-432436d3fetr",
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.description, "Look mom, I made it!")
        self.assertEqual(self.episode.link, "https://myawesomeshow.com")
        self.assertEqual(
            self.episode.guid, "de194720-7b4c-49e2-a05f-432436d3fetr"
        )

    def test_episode_str_representation(self):
        self.assertEqual(
            str(self.episode), "My Python Podcast: My Awesome Podcast Episode"
        )

'''
In the above code, you use .setUp() to define an example Episode object.

You can now test a few of the Episode attributes to confirm that the model works as expected. 
It’s always a good idea to test the string representation from your models, which you defined in 
Episode.__str__(). The string representation is what you’ll see when debugging your code and 
will make debugging easier if it accurately displays the information you’d expect to see.

Now you can run your tests:

(.venv) $ python manage.py test
'''

# For step 3 onwards visit this link: 
# 