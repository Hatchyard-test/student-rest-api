# Student REST API

Student Details retrieve REST API using FAST

Install
-------

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install Dependencies::

    $ pip install -r requirements.txt
    
Run
---
On Windows cmd::

    > python -u server/main.py
    
API Swagger doc URL:

Open http://localhost:8000/docs in a browser.

Run Test Cases
---

On Windows cmd::

    > python -m pytest tests/ 
    
Generate Bandit Report
---

On Windows cmd::

    > bandit -r . -f html -o bandit_report -x .\tests

Run from Docker
-------

To build a container and run::

    $ docker-compose up -d --build

    
API Swagger doc URL:
Open http://localhost:8000/docs in a browser.

To run test cases::

    $ docker-compose exec web pytest .


Features
---
  * Student details retrieve API endpoints
     * **GET**:: All student details/ filter by ID
     * **POST**:: Create new student
     * **PUT**:: Update existing student details
     * **DELETE**:: Delete student entry
  * Swagger window

TODO
---
  * Implement the authentication bash endpoint call(using Refresh token)
