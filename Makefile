MANAGE=django-admin.py
SETTINGS=my42cctest.settings

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) test
	flake8 --exclude '*migrations*,my42cctest/settings/__init__.py' \
		--max-complexity=6 testapps my42cctest

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) syncdb --noinput

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) migrate
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) loaddata testapps/fixtures/users.json
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) loaddata testapps/fixtures/person.json

collectstatic:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) collectstatic --noinput
.PHONY: test syncdb migrate
