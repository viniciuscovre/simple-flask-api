db:
	make db/init && make db/migrate && make db/upgrade

db/init:
	pipenv run python migrate.py db init

db/migrate:
	pipenv run python migrate.py db migrate

db/upgrade:
	pipenv run python migrate.py db upgrade

serve:
	pipenv run python run.py

lint:
	pipenv run flake8 .

install:
	pipenv install --dev
