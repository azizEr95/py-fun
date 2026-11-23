<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
## Assignment C1: Python Expressions & Unit Tests &nbsp
<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->

The assignment demonstrates Python's powerful *"one-liner"* expressions.

### Steps

- [*Step 1:*](#1-create-new-local-branch-c1-expressions) Create new local Branch: `c1-expressions`

- [*Step 2:*](#2-run-code) Run Code

- [*Step 3:*](#3-write-expressions) Write Expressions

- [*Step 4:*](#4-run-tests) Run Tests

- [*Step 5:*](#5-final-test-and-sign-off) Final Test and sign-off

- [*Step 6:*](#6-check-branch-into-your-remote-repository) Check Branch into your remote Repository
<!-- 
Points: [1, 2, 3, 0, 3, 1]
 -->

<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->

&nbsp;
---
### 1. Create new local Branch: `c1-expressions`

Create a new local branch: `c1-expressions` in the project and fill with files
from the remote branch:
[*https://github.com/sgra64/py-fun/tree/c1-expressions*](https://github.com/sgra64/py-fun/tree/c1-expressions).

1. Inspect the remote branch to see what is in it (packages:
    [*src/__init__.py*](src/__init__.py),
    [*src/expressions*](src/expressions) and
    [*tests/expressions*](tests/expressions)).

1. Think about where to branch-off the new local branch `c1-expressions`
    such that it contains project files such as *Makefile*, *setup.py*
    or *pytest.ini*.

1. Fetch the remote branch: `c1-expressions` and merge into the local
    branch `c1-expressions`.


<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->

&nbsp;
---
### 2. Run Code

Run code in your IDE and in the terminal:
```sh
make run
```
```
numbers: [4, 12, 3, 8, 17, 12, 1, 8, 7]
#
a) number of numbers: 9
b) first three numbers: []
c) last three numbers: []
d) last three numbers reverse: []
e) odd numbers: []
f) number of odd numbers: 0
g) sum of odd numbers: 0
h) duplicate numbers removed: []
i) number of duplicate numbers: 0
j) ascending, de-dup (n^2) numbers: []
k) length: NEITHER
```


<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->

&nbsp;
---
### 3. Write Expressions

Complete expressions one after another in
[*src/expressions/expressions.py*](src/expressions/expressions.py).
Use only *"one-liner"* expressions.

Python's [*built-in functions*](https://docs.python.org/3/library/functions.html)
are allowed, but not own functions.

```py
class Expressions:

    def __init__(self, _numbers=default_numbers):
        # a) initialize with number of numbers: 9
        self.a = len(self.numbers)  # one-line expressions

        # b) initialize with the first three numbers: [4, 12, 3]
        self.b = []                 # <-- write new one-line expression here
```

Once you completed an expression, run the code to see results are correct:

```sh
make run
```
```
python -m main

numbers: [4, 12, 3, 8, 17, 12, 1, 8, 7]
#
a) number of numbers: 9
b) first three numbers: [4, 12, 3]
```


<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->

&nbsp;
---
### 4. Run Tests

Once an expression seems to be working, run the correspondig test in the IDE.
Fix your expression in the IDE when the test is failing. When working in the
IDE, run tests selectively in the terminal:

```sh
# run the test for a) test_a_number_of_numbers
pytest -v \
    tests/expressions/test_expressions.py::TestExpressions::test_a_number_of_numbers

# when test a) runs, add test b) test_c_first_three_numbers
pytest -v \
    tests/expressions/test_expressions.py::TestExpressions::test_a_number_of_numbers \
    tests/expressions/test_expressions.py::TestExpressions::test_b_first_three_numbers

# add tests incrementally to the full set
pytest -v \
    tests/expressions/test_expressions.py::TestExpressions::test_a_number_of_numbers \
    tests/expressions/test_expressions.py::TestExpressions::test_b_first_three_numbers \
    tests/expressions/test_expressions.py::TestExpressions::test_c_first_three_numbers \
    tests/expressions/test_expressions.py::TestExpressions::test_d_last_three_in_reverse \
    tests/expressions/test_expressions.py::TestExpressions::test_e_odd_numbers \
    tests/expressions/test_expressions.py::TestExpressions::test_f_number_of_odd_numbers \
    tests/expressions/test_expressions.py::TestExpressions::test_g_sum_of_odd_numbers \
    tests/expressions/test_expressions.py::TestExpressions::test_h_duplicates_removed \
    tests/expressions/test_expressions.py::TestExpressions::test_i_number_of_duplicate_numbers \
    tests/expressions/test_expressions.py::TestExpressions::test_j_ascending_squaredClass_no_duplicates \
    tests/expressions/test_expressions.py::TestExpressions::test_k_classify_as_odd_even_empty

# run all tests at the end
make tests
```


<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->

&nbsp;
---
### 5. Final Test and sign-off

Run all tests:

```sh
# run all tests (using the pytest framework)
make tests

# run tests using the pytest framework
python -m pytest -v
pytest -v

# run tests using the unit-test framework
python -m unittest
```
<!-- 
For sign-off, change into `C_expressions` directory and copy commands into a terminal:

```sh
# Fetch test file from Gitlab and run tests for sign-off.
# The sed-command removes comments from test cases.

test_url=https://gitlab.bht-berlin.de/sgraupner/ds_cs4bd_2324/-/raw/main/C_expressions/test_expressions.py

curl $test_url | \
   sed -e 's/^#.*Test_case_/Test_case_/' | \
   python
```
-->

Result (pytest -v output):

```
collected 11 items

tests/expressions/test_expressions.py::TestExpressions::test_a_number_of_numbers PASSED [  9%]
tests/expressions/test_expressions.py::TestExpressions::test_b_first_three_numbers PASSED [ 18%]
tests/expressions/test_expressions.py::TestExpressions::test_c_first_three_numbers PASSED [ 27%]
tests/expressions/test_expressions.py::TestExpressions::test_d_last_three_in_reverse PASSED [ 36%]
tests/expressions/test_expressions.py::TestExpressions::test_e_odd_numbers PASSED [ 45%]
tests/expressions/test_expressions.py::TestExpressions::test_f_number_of_odd_numbers PASSED [ 54%]
tests/expressions/test_expressions.py::TestExpressions::test_g_sum_of_odd_numbers PASSED [ 63%]
tests/expressions/test_expressions.py::TestExpressions::test_h_duplicates_removed PASSED [ 72%]
tests/expressions/test_expressions.py::TestExpressions::test_i_number_of_duplicate_numbers PASSED [ 81%]
tests/expressions/test_expressions.py::TestExpressions::test_j_ascending_squaredClass_no_duplicates PASSED [ 90%]
tests/expressions/test_expressions.py::TestExpressions::test_k_classify_as_odd_even_empty PASSED [100%]
============================= 11 passed in 0.06s ==============================
```


<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->

&nbsp;
---
### 6. Check Branch into your remote Repository

Check branch `c1-expressions` into your remote repository.
