# FiboServices Project Make File
# author: Patrick Lu

.PHONY: test

VIRTUALENV = $(shell which virtualenv)

clean: 
	rm -fr FiboService.egg-info
	rm -fr venv
	rm -fr build
	rm -fr dist

venv:
	$(VIRTUALENV) venv
install: venv
	. venv/bin/activate; python setup.py install
launch: venv install 
	. venv/bin/activate; python ./calcRestService.py &
test: venv
	. venv/bin/activate; python ./test/FiboService_test.py -v
shutdown:
	ps -ef | grep "calcRestService.py" | grep -v grep | awk '{print $$2}' | xargs kill
