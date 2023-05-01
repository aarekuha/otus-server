SHELL=/bin/bash

start:
	@nohup python httpd.py -w 10 &

stop:
	@kill -TERM $$(ps ax | grep -v grep | grep "python httpd.py" | awk '{print $$1}') && echo "Stopped"

status:
	@echo Workers started: $$(ps ax | grep -v grep | grep "python httpd.py" | awk '{print $$1}' | wc -l)

restart: stop start
