run:
	python3 main.py

test:
	pytest --tb=short

clean:
	rm -f *.pyc
