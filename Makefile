default:
	echo 'Nothing here.'

testenv:
	venv/bin/pip install mock pytest watchdog

test:
	venv/bin/py.test tests
