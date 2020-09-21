# Introduction
This is a repository where you can find the tests and scenarios to be covered as part of SecureWorks test. It have created the following layers in this repository:
- Part 1.
    - Python unit tests using Pytest.
- Part 2 (I did twice using 2 different frameworks).
    - Cypress (Javascript).
    - Behave (Python)

As you can see, all of these is in the same repository for the test purposes.

# Pre-requisites to run locally.
- Tools
    - Python 3.7 (or higher).
    - Pip
    - npm
- Move to a desired folder and create a new virtual environment (highly recommended to install dependencies in an isoleted environment), you can install ir using pip.
    - `virtualenv -p python3.7 venv_test_secureworks`   
- Move to the folder `venv_test_secureworks` and clone the repository inside the virtual environment (Code is in master branch, so you do not need to checkout to other branch)..
```bash
cd venv_test_secureworks
git clone https://github.com/ovalerio280788/test_secureworks.git
``` 
- Activate the virtual environment and install dependencies for python tests.
```bash
source bin/activate                 // activate virtual environment
cd test_secureworks                 // move to the repository folder
pip install -r requirements.txt     // install dependencies from file
pip freeze                          // to verify the installed libraries
```
- For Cypress run `npm install` to generate the `node_modules`.
## How to run tests on Part 1?
This is the part related to unit tests (we assume that the previous steps regarding "Pre-requisites to run locally" were done). 
The test cases for this part were written in Python using Pytest as test runner. Use the following commands to run different set of test cases.
```bash
export PYTHONPATH=$(pwd)    // set the python path/(working directory) as the root path of the repository
pytest -v                   // to run all test cases
pytest -v -m positive       // to run all positive test cases
pytest -v -m negative       // to run all positive test cases
```
One example of an output is the following:
```bash
(venv_test_secureworks2) oscar.valerio@Oscar-Valerio-MacBook-Pro test_secureworks % pytest -v
====================================================== test session starts ======================================================
platform darwin -- Python 3.7.0, pytest-5.0.1, py-1.8.0, pluggy-0.11.0 -- /usr/local/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/ovalerio/workspace/venv_test_secureworks2/test_secureworks, inifile: pytest.ini
collected 8 items

python/test_part1/tests/test_largest_words.py::test_read_valid_existing_file_one_word_per_line PASSED                                                                                                [ 12%]
python/test_part1/tests/test_largest_words.py::test_read_valid_existing_file_multiple_words_one_line PASSED                                                                                          [ 25%]
python/test_part1/tests/test_largest_words.py::test_read_valid_existing_file_multiple_words_multiple_lines PASSED                                                                                    [ 37%]
python/test_part1/tests/test_largest_words.py::test_read_valid_existing_file_multiple_numbers_multiple_lines PASSED                                                                                  [ 50%]
python/test_part1/tests/test_largest_words.py::test_read_non_existing_file PASSED                                                                                                                    [ 62%]
python/test_part1/tests/test_largest_words.py::test_read_invalid_file_format PASSED                                                                                                                  [ 75%]
python/test_part1/tests/test_largest_words.py::test_read_corrupted_file PASSED                                                                                                                       [ 87%]
python/test_part1/tests/test_largest_words.py::test_read_empty_file PASSED
```
## How to run tests on Part 2 (Behave)?
This is the part related to UI with API test (we assume that the previous steps regarding "Pre-requisites to run locally" were done).
For this part you need to configure the Chrome and Firefox (Geckodriver) to be accesible anywhere. On Mac you can follow these steps:
- Create a new folder to put the browser drivers.
- Add the path of the folder created at the end of this file: `/etc/paths`.
- If you have the terminal opened then close it and open it again.
- Download Chromedriver based on your chrome version (https://chromedriver.chromium.org/downloads) into the just created folder.
- Download Geckodriver (https://github.com/mozilla/geckodriver/releases) into the just created folder.

The test cases for this part were written in Python using Behave (BDD framework) as test runner. Use the following commands to run the test case.
```bash
export username=shopmanager
export password="<the_password_that_is_not_here_for_security>"  // Use "" to wrap the password if it has spaces on it. i.e password="hello world 123"
behave python/test_part2/features/                              // to run the test case on Chrome by default
behave python/test_part2/features/ -D browser=firefox           // to run the test case on Firefox
```
## How to run tests on Part 2 (Cypress)?
This is the part related to UI with API test (we assume that the previous steps regarding "Pre-requisites to run locally" were done).

The test cases for this part were written in Javascript using Cypress as test runner. Use the following commands to run the test case.
```bash
export CYPRESS_USERNAME=shopmanager
export CYPRESS_PASSWORD="<the_password_that_is_not_here_for_security>"  // Use "" to wrap the password if it has spaces on it. i.e password="hello world 123"

// Under package.json I added 2 custom script nodes to run tests against Firefox and Chrome
npm run test-firefox                // to run the test on firefox
npm run test-chrome                 // to run the test on firefox
```


