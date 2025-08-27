# # Playwright examples using Python

Demonstration of:

* [Playwright](https://www.playwright.dev/) browser automation testing
* [Python](https://www.python.org/) programming language
* [Chromium](https://www.chromium.org/) open source web browser

## Install

### Install Python

Install Python from <https://www.python.org/>

Run this to confirm your version:

```sh
python --version
```

Output should be at least:

```stdout
Python 3.13.3
```

### Install Playwright

Install Playwright and whichever browsers you want:

```sh
pip install playwright
playwright install chromium 
playwright install firefox
playwright install webkit
```

Optional for type checking:

```sh
pip install mypy
```

### Update

Run:

```sh
pip install --upgrade pip
pip install --upgrade playwright
pip install --upgrade mypy
```

## Run

Run:

```sh
src/demo.py
```

If you prefer, you can run with python explicitly:

```sh
python src/demo.py
```

If you prefer, you can run with type checking:

```sh
mypy src/demo.py
```

The script will do three things:

1. Launch your local Chrome web browser to view the free open source testing examples web page <https://testingexamples.github.io>.

2. Interact with the web page in various ways, such as finding elements, clicking on elements, filling in form inputs, etc.

3. Print some typical HTML tag output that demonstrates the program is running successfully.

## Additional Python Features

Async Alternative: a commented demo_async() function showing how to use the async API if needed.

Python Type Hints:

* Full type annotations for better IDE support
* Compatible with type checkers like mypy
* Optional but recommended for larger projects

Error Handling:

* Use `traceback` module for detailed error reporting
* Use `sys.stderr` for error output
* Use `sys.exit(1)` for proper exit codes

## Tracking

* Package: playwright-examples-using-python
* Version: 1.4.0
* Created: 2019-11-02T00:00:00Z
* Updated: 2025-04-24T13:58:02Z
* License: GPL-2.0-or-greater or for custom license contact us
* Contact: Joel Parker Henderson <joel.henderson@wales.nhs.uk>
