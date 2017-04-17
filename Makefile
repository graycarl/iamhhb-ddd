default:
	echo 'Nothing here.'

dev:
	venv/bin/pip install mock pytest watchdog

test:
	venv/bin/py.test -v tests/$t

watch:
	source venv/bin/activate && watchmedo shell-command --command "py.test -v tests/$t" --pattern '*.py' --recursive --drop

serve:
	venv/bin/python wsgi.py

init-db:
	sqlite run/db.sqlite < assets/db-schema.sql
