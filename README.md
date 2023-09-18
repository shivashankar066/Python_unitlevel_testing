# Python_unitlevel_testing

Step 1: Create all functions under class in python file say, main.py



step 2: create another python file in new tab say, test_main.py 



step 3: call all functions in test_main.py file and test each function using assertEqual().


step 4: Run test_main.py as python -m unittest test_main.py -v 


### for Covearge Report

Step 1 : Create all necessray classes and testing those classes.
(Ref: https://www.pythontutorial.net/python-unit-testing/python-run-unittest/)
Step 2 : To run all testes:
  python -m unittest discover -v
Step 3: To test single module:
python -m unittest test.test_circle -v
Step 4: To test single class:
python -m unittest test.test_circle.TestCircle -v


### To generate a coverage report

Ref : https://www.pythontutorial.net/python-unit-testing/python-unittest-coverage/