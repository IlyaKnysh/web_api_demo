# web-api-demo

This is a demo project for web/api tests.

Stack:

- PyTest
- Selene
- Allure

## Install requirements:

    $ pip install -e .

## Run tests and generate report:

### 1. install allure globally

    $ npm install -g allure-commandline --save-dev

### 2. Run tests

    $ pytest --alluredir=allure-results

### 3. Generate report

    $ allure generate allure-results --clean -o allure-report && allure open

