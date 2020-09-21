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
## How to run tests on Part 1?
This is the part related to unit tests (we assume that the previous steps regarding "Pre-requisites to run locally" were done). 
The test cases for this parte were written in Python using Pytest as test runner. Use the following commands to run different set of test cases.
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
## How to run tests on Part 2?





# TestAutomation
In the repository we have code that cover tests for Solstice (pytest) and Kepler (Behave). The readme files per each project is still in progress. 

## Git commit template.
### How to setup.
Follow these step to setup the commit template in your local environment.

- Open a terminal in your local environment.
- Go to the root path of this repository in your local machine: `cd <root_path_of_this_repo>`
- Run this command: ```git config --global commit.template IT/```
- You are done to start using the template.

### How to use.
Follow these steps to use the commit template in your local environment.
- Start your task/user story, for that create your feature branch as usual and make the changes you need to do.
- Once you need to commit your code, do it this way: `git commit` **(Without the -m flag)** and press enter.
- A new screen will be opened in your terminal, it should look like this: 
> \# <type>:<subject>
> .
> // If applied, this commit will...
> .
>// Explain why this change is being made:
> .
// Binaries affected ( Kepler, api_v1, api_v2, Clientsim, Zapi, etc )
> .
// Provide links to story, task, bug, articles or other resources
> .
> .
> \# SEMANTIC COMMIT MESSAGES
> \# feat:add hat wobble
> \# ^--^  ^------------^
> \# |     |
> \# |     +-> Summary in present tense.
> \# |
> \# +-------> Type: chore, docs, feat, fix, refactor, style, or test.
> \#
> \# MORE EXAMPLES:
> \#
> \# feat:new feature for the user, not a new feature for build script)
> \# fix: (bug fix for the user, not a fix to a build script)
> \# docs: (changes to the documentation)
> \# style: (formatting, missing semi colons, etc; no production code change)
> \# refactor: (refactoring production code, eg. renaming a variable)
> \# test: (adding missing tests, refactoring tests; no production code change)
> \# chore: (updating grunt tasks etc; no production code change)
> \#
> \#
> \# Please enter the commit message for your changes. Lines starting
> \# with '#' will be ignored, and an empty message aborts the commit.
> \#
> \# On branch AT-465
> \# Changes to be committed:
> \#       modified:   IT/.git_commit_msg.text
> \#
> \# Untracked files:
> \#       IT/RemovePod.py
> \#       allure-results/
> \#

- You need to fill the spaces **under the lines** that starts with //, like `If applied, this commit will…` for example, to enable editing, press `i` key in your keyboard.
- Once you fill the spaces, press `esc` botton in your keyboard, and then tipe `:wq` to write changes and quit.
- After that you can push your changes to github.
- That's it.

We can see more information here:
-- https://mersive.atlassian.net/wiki/spaces/PDO/pages/65863711/Commit+Template
-- https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716









