### Graphene Django Project

This example project demonstrate an integration between Graphene and Django.
You'll build an Event Model to access event objects through GraphQL.

First you'll need to get the source of the project. Do this by cloning the repository:

```bash
# Get the project code
git clone https://github.com/Moesif/moesif-graphene-django-example.git
```

*NOTE: While working with Python, we would recommend to use virtual environment
to keep all the project's dependencies isolated from other projects.*

##### Create your local environment

```bash
conda create -n graphql python=3.6 anaconda # Create the environment
source activate graphql # Activate the environment
```

##### Install dependencies

```python
pip install -r requirements.txt
```

##### Create database table

```bash
python manage.py makemigrations
python manage.py migrate
```

##### Create mock data

```bash
$ python manage.py shell
>>> from events.models import Event
>>> Event.objects.create(name='API Analytics', url='https://www.moesif.com/')
>>> Event.objects.create(name='Trove Marketplace', url='https://www.trove.com/')
```

##### Start the application

```bash
python manage.py runserver
```

##### Query data through GraphQL

Go to [localhost](http://localhost:8000/graphql/) on [Insomnia](https://insomnia.rest/download/#mac)
or your favorite browser to Create/Search/Filter data through GraphQL. More detail on how to write your first
query and mutation could be found [here](https://www.moesif.com/blog/technical/graphql/Getting-Started-with-Python-GraphQL-Part1/).
