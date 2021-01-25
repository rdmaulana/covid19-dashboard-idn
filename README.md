# Indonesia Covid-19 Dashboard

[![Python Version](https://img.shields.io/badge/python-3.8.5-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.1.4-brightgreen.svg)](https://djangoproject.com)

![Dashboard Screenshot](https://i.paste.pics/0fa4a085d24979c395696a98bd3a3d4a.png)

Demo version [Indonesia Covid-19 Dashboard](https://dash-cov19.herokuapp.com).

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/rdmaulana/covid19-dashboard-idn.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create account on rapidapi.com to use this API.

```bash
https://rapidapi.com/api-sports/api/covid-193
```

In settings.py , edit "API_KEY" with your API KEY.

```bash
API_KEY = "YOUR_API_KEY"
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/rdmaulana/covid19-dashboard-idn/blob/main/LICENSE).

