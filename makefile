install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	yapf -ir -vv --style pep8 .
lint:
	for i in $(find . -type f -regex '.*\.py' -print); do pylint --disable=R,C -sy $i; done
testing:
	pytest -vv --cov=. . --cov-report xml:reports/coverage/coverage.xml
coverage_badge:
	genbadge coverage
cleaning:
	rm -rf reports
git:
	git config --local user.email "aurel.pere@gmail.com"
	git config --local user.name "aurelpere"
	git add coverage-badge.svg
	git commit --allow-empty -m "Updating the test coverage badge"
all: install format lint testing coverage_badge cleaning