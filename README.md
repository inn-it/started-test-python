# We are starting with python for automated testing in browser

This project is an example of a minimum setup in Python.
We run the simplest test to find **selene** by _google_.

Let's start!

## Acknowledgments

[Яков Крамаренко](https://github.com/yashaka)

## Test Google

Run [the test for Google](google_search_selene.py)

## What is tested

We'll test an auth form on [site](http://the-internet.herokuapp.com/login).
Steps:

1. Explore the form with Developer Tools (press F12). Make the proof of concept.
2. Create a new project and a file of tests.

   **Notice**: The project's name has the short description of the project, e.g. heroku-app-tests.

   **Notice**: The file's name is beginning at **test** and has the description of the test object,
   e.g. _test_auth_form_. This file will have some tests of the form (see chapter below).

3. Create the positive and negative tests.

   The test cases are

   - login and password are correct;
   - login is correct and password is incorrect;
   - both login and password are incorrect.

4. Run the tests.

## References

- [Selene in Pypi](https://pypi.org/project/selene/2.0.0b4/).
