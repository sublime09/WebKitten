.PHONY: clean

clean:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-
	rm --force --recursive __pycache__/
	@echo "WebKitten is not clean!"


test:
	# py.test --verbose --color=yes $(TEST_PATH)
	@echo "TODO: NOT IMPLEMENTED YET"

run:
	python main.py


help:
	@echo "    clean"
	@echo "        Remove python and build artifacts."
	@echo "    test"
	@echo "        Run py.test"
	@echo '    run'
	@echo '        Runs WebKitten'
