.PHONY: init lint test clean

init:
	pip install -r requirements.txt

lint:
	pylint auscultor tests

test:
	pytest

clean:
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	rm -rf auscultor/__pycache__/
	rm -rf tests/__pycache__/
	rm -rf build/
