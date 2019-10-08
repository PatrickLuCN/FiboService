# FiboServices Project Make File
# author: Patrick Lu

.PHONY: test

VIRTUALENV := $(shell which virtualenv 2> /dev/null)

clean:
	rm -fr FiboService.egg-info
	rm -fr venv
	rm -fr build
	rm -fr dist

venv:
ifndef VIRTUALENV
	easy_install pip
	python -m pip install -U pip
	pip install virtualenv
endif
	virtualenv venv
install: venv
	. venv/bin/activate; python setup.py install
launch: venv install 
	. venv/bin/activate; python ./calcRestService.py &
test: venv
	. venv/bin/activate; python ./test/FiboService_test.py -v
shutdown:
	ps -ef | grep "calcRestService.py" | grep -v grep | awk '{print $$2}' | xargs kill
