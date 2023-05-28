# How to develop on ExceptNotifier

ExceptNotifier welcomes contributions from the community.

**You need PYTHON3**

## ExceptNotifier
We have decided to designate version `0.2.11` of ExceptNotifier as the PyPI release version, while continuing to develop the GitHub version. In the alpha version 0.3, our focus will be on adding new features, refactoring code, and fixing bugs. For version 0.4, we plan to conduct beta testing by incorporating quality assurance and preparing new documentation. Once version 0.5 becomes a stable product, we will update the PyPI release version.

## Key Contribution Rules

Core maintainer: @[dsdanielpark](https://github.com/dsdanielpark)

1. To make a contribution, you must ensure that one or more applications have implemented (or extended) complete functionality or have been refactored and are functioning correctly.
   - Before refactoring, refer to this refactoring sample. https://github.com/dsdanielpark/CatchException
2. Please submit a Pull Request after completing documentation, QA, refactoring, and feature implementation for one or more applications.
3. If you have suggestions for a better structure, create a Discussion or submit a Draft Pull Request for code review.
4. Pull Requests will be accepted if the contributor has made sufficient contributions.
   - Minor fixes such as typos, black formatting, or very small documentation changes may not be accepted as Pull Requests, but we will review and make the necessary modifications.
5. Exceptionally, contributions related to fixing non-functional code or bugs will be considered.
6. Contribution rules may be added by the community.

Furthermore, if you consistently contribute to the project, you will be recognized as a Core maintainer or maintainer.

While the ExceptNotifier project aims for community growth, it will not indefinitely expand the list of project contributors to include those who do not have a sufficient commitment to ExceptNotifier.

## Setting up your own fork of this repo.

- On github interface click on `Fork` button.
- Clone your fork of this repo. `git clone https://github.com/dsdanielpark/ExceptNotifier.git`
- Enter the directory `cd ExceptNotifier`
- Add upstream repo `git remote add upstream https://github.com/dsdanielpark/ExceptNotifier.git`

## Setting up your own virtual environment

Run `make virtualenv` to create a virtual environment.
then activate it with `source .venv/bin/activate`.

## Install the project in develop mode

Run `make install` to install the project in develop mode.

## Run the tests to ensure everything is working

Run `make test` to run the tests.

## Create a new branch to work on your contribution

Run `git checkout -b my_contribution`

## Make your changes

Edit the files using your preferred editor. (we recommend VIM or VSCode)

## Format the code

Run `make fmt` to format the code.

## Run the linter

Run `make lint` to run the linter.

## Test your changes

Run `make test` to run the tests.

Ensure code coverage report shows `100%` coverage, add tests to your PR.

## Build the docs locally
`cd docs` to make docs

Run `make docs` to build the docs.

Ensure your new changes are documented.

## Commit your changes

This project uses [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0/).

Example: `fix: update setup.py arguments` (emojis are fine too)

## Push your changes to your fork

Run `git push origin my_contribution`

## Submit a pull request

On github interface, click on `Pull Request` button.

Wait CI to run and one of the developers will review your PR.

