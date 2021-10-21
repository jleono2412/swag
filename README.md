# Sauce demo test
_Project for test saucedemo.com portal_

## To execute the project 🔧 

* clone repository

* Follow this page to create a virtual environment
https://docs.python.org/es/3/tutorial/venv.html

* In cmd execute pip install -r requirements.txt command

* Download the webdriver depending on the operating system and place it in the Drivers folder

## Executing Tests ⚙️

To run any feature you need execute 

[behave -f allure_behave.formatter:AllureFormatter -o results folder site_tests/behave/features/feature name.feature]

## Executing exercise

In a cmd locate the folder where the algorithm_problem.py file is located then

run python algorithm_problem.py "string to check"


### To see Report

If you want to see report, you need execute [allure serve results folder]

### Tools
* [Python]

* [Bejave]

* [Allure]
