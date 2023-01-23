install:
	pip install --upgrade pip && \
	pip install --upgrade setuptools && \
	python -m pip install flake8 && \
	pip install -U pyabsa && \
	pip3 install -r requirements.txt
lint:
	flake8 app/*.py
test:
	#test
deploy:
	#deploy
all: install lint test 