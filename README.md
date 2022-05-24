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


## Run tests in parallel:

    $ pytest -n {number_of_threads}

## Run tests on remote hub
1. Install selenoid - https://aerokube.com/selenoid/latest/
2. Set variables:


    REMOTE_IP={ip_address_of_hub} - in case of local run - "localhost"
    BROWSER=remote
    URL={address_of_test_object} - in case of localhost run - set external ip instead of "localhost"