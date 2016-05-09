# FiboServices Project Make File
# author: Patrick Lu

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

launch: venv
	. venv/bin/activate; python ./calcRestService.py &

test: 
	. venv/bin/activate; python ./test/FiboService_test.py 

shutdown:
	ps -ef | grep "calcRestService.py" | grep -v grep | awk '{print $$2}' | xargs kill  
