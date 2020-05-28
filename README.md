# Backend Test

Minimal python API

## Getting Started

1 - Create a virtualenv :

```bash
virtualenv -p python3 venv
```

2 - Activate it :

```bash
source venv/bin/activate
```

3 - Install requirements :

```bash
pip install -r requirements.txt
```

4 - Run migrations and django server :

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Running tests and quality

Check if source code is pep8 compliant :

```bash
flake8 --ignore E501
```
(too long lines are ignored)

Run units tests :

```bash
python manage.py test
```

Check coverage on api app :

```bash
coverage run --source=api manage.py test
coverage report

Name                             Stmts   Miss  Cover
----------------------------------------------------
api/__init__.py                      0      0   100%
api/apps.py                          3      0   100%
api/migrations/0001_initial.py       8      0   100%
api/migrations/__init__.py           0      0   100%
api/models.py                       14      0   100%
api/serializers.py                  15      0   100%
api/tests/__init__.py                8      0   100%
api/tests/test_models.py            24      0   100%
api/tests/test_views.py             27      0   100%
api/urls.py                         12      0   100%
api/views.py                        32      0   100%
----------------------------------------------------
TOTAL                              143      0   100%
```

Check if source code is bandit compliant (no vulnerabilities) :

```bash
bandit -r api/ -s B101

Run started:2020-05-27 23:38:29.466576

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 158
	Total lines skipped (#nosec): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0.0
		Low: 0.0
		Medium: 0.0
		High: 0.0
	Total issues (by confidence):
		Undefined: 0.0
		Low: 0.0
		Medium: 0.0
		High: 0.0
Files skipped (0):
```
(-s B101 is to skip assert vulnerabilities in unit tests)
