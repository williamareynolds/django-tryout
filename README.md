# MedAPI

Med API is a simple REST API example demonstrating the most common endpoints
used in REST APIs. 

## Trachoma PGP3 Antigen Test Application

This application delivers sample data from a study of different tests used to
detect the presence of the Trachoma PGP3 Antigen in blood and serum samples. The
sqlite database committed with the project already includes the full dataset, 
but the CDC website provides several valuable resources for understanding and
interacting with this data:

[Study Home](https://data.cdc.gov/Global-Health/Tests-for-antibodies-to-trachoma-PGP3-antigen/pwgb-7r9t)

### Requirements

- Uses Django 1.11 with Python 2.7
- Uses SQLite database
- Implements JSON REST API
- Uses django-rest-framework
- Unit tests written for the API
- Uses migrations to manage database schema

### Design Choices

- Wherever sufficient, Django's implementations are preferred over
    django-rest-framework implementations.
- Function-based views over Generic View Classes. This makes the code a bit
    easier to reason about and makes the intent more clear (in my opinion).
- No authentication or authorization. This application delivers a public
    dataset without any concept for a production environment.
- A full set of CRUD operations is provided. 
- Decimal numbers use the Decimal implementations available over floating point.

### Desired Enhancements

- Using PostgreSQL would provide a neat option of creating custom datatypes
    which could conveniently represent qualitative types, or even wrap entire
    antigen test platforms.
- The django-rest-framework ViewSet seems like it offers a couple benefits which
    aren't available for the Django generic view classes. The opportunity to 
    generate URL confs is appealing, especially since there's nothing special
    about the confs used here.

## Install and Run

It is recommended to create a virtual environment first.

This application has been tested on python 2.7

1. pip install -r requirements.txt

2. python medapi/manage.py runserver localhost:8000

The application has django-rest-framework's browsable api enabled, so you can
visit http://localhost:8000/api/v1/trachoma_pgp3_antigen/samples/1/ to see the
first sample. You can also check with curl:

`curl http://localhost:8000/api/v1/trachoma_pgp3_antigen/samples/1/`

### API Routes

#### Sample

| action   | method | uri | success code  |
|:--------:|-------:|:----|:--------------|
| index | GET | api/v1/trachoma_pgp3_antigen/samples/ | 200 |
| create | POST | api/v1/trachoma_pgp3_antigen/samples/ | 201 |
| retrieve | GET | api/v1/trachoma_pgp3_antigen/samples/{id}/ | 200 |
| update | PUT | api/v1/trachoma_pgp3_antigen/samples/{id}/ | 204 |
| delete | DELETE | api/v1/trachoma_pgp3_antigen/samples/{id}/ | 204 |


## Other Notes

- The browsable api is very slow when loading the index route. This isn't an
    issue when calling the api from curl, so browsing there would probably be
    more convenient using curl and [jq](https://stedolan.github.io/jq/).
- Tests can be run by calling `python manage.py test 
    trachoma_pgp3_antigen/tests/`.
