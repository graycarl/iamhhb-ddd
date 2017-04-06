default:
	echo 'Nothing here.'

testenv:
	venv/bin/pip install mock pytest watchdog

test:
	venv/bin/py.test -v tests/$t

watch:
	source venv/bin/activate && watchmedo shell-command --command "py.test -v tests/$t" --pattern '*.py' --recursive --drop
