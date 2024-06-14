setup:
	pip install -r requirements.txt --no-deps

run:
	@cd src/; \
	python main.py

lint:
	@flake8

tests:
	@cd src/; \
	python -m unittest
