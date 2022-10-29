# NOTE : 

><p>"__new__.__defaults__ to create Task objects without having to specify all the fields."

- The test_defaults() test is there to demonstrate and validate how the defaults work.

- The test_member_access() test is to demonstrate how to access members by name and not by

- index, which is one of the main reasons to use namedtuples."


---

> "The part of pytest execution where pytest goes off and finds which tests to run is called test"

##### pytest naming conventions. 
    
- Here’s a brief overview of the naming conventions to keep your test code discoverable by pytest:
    - Test files should be named `test_<something>.py or <something>_test.py`
    - Test methods and functions should be named `test_<something>`
    - Test classes should be named `Test<Something>`

----

##### Here are the possible outcomes of a test function:
    
```markdown 
    PASSED (.): The test ran successfully.
    FAILED (F): The test did not run successfully (or XPASS + strict).
    SKIPPED (s): The test was skipped. You can tell pytest to skip a test by using either the
    @pytest.mark.skip() or pytest.mark.skipif() decorators, discussed in ​Skipping Tests​.
    xfail (x): The test was not supposed to pass, ran, and failed. You can tell pytest that a test
    is expected to fail by using the @pytest.mark.xfail() decorator, discussed in ​Marking Tests
    as Expecting to Fail​.
    XPASS (X): The test was not supposed to pass, ran, and passed.
    ERROR (E): An exception happened outside of the test function, in either a fixture
```
---
> Running only one test in a pytest form a python file 
    
    
> example: `pytest​​ ​​-v​​ ​​tasks/test_four.py::test_asdict`
syntax : `pytest <test_file_name>::test_name`

---

##### Using Options

> pytest [options] [file_or_dir] [file_or_dir] [...]

- We’ve used the verbose option, -v or --verbose, a couple of times already, but there are many
    more options worth knowing about.
    
    You can see all of them with `pytest --help.`
    
    - The following are a handful of options that are quite useful when starting out with pytest. 
    ​  ​$ ​​`pytest​​ ​​--help`​
    ​  ​
    **OPTIONS**: 
    ```markdown
    ​ 
    -k EXPRESSION only run tests/classes which match the given
    ​  substring expression.
    ​  Example: -k 'test_method or test_other' matches
    ​  all test functions and classes whose name
    ​  contains 'test_method' or 'test_other'.
    
    ​-m MARKEXPR only run tests matching given mark expression.
    ​  example: -m 'mark1 and not mark2'.
    
    ​-x, --exitfirst exit instantly on first error or failed test.
    
    ​--maxfail=num exit after first num failures or errors.
    
    ​--capture=method per-test capturing method: one of fd|sys|no.
    
    -s shortcut for --capture=no.
    
    ​--lf, --last-failed rerun only the tests that failed last time
    ​  (or all if none failed)
    
    ​--ff, --failed-first run all tests but run the last failures first.
    
    ​-v, --verbose increase verbosity.
    
    ​-q, --quiet decrease verbosity.
    
    ​-l, --showlocals show locals in tracebacks (disabled by default).
    
    ​--tb=style traceback print mode (auto/long/short/line/native/no).
    
    ​--durations=N show N slowest setup/test durations (N=0 for all).
    
    ​--collect-only only collect tests, don't execute them.
    
    ​--version display pytest lib version and import information.
    
    ​-h, --help show help message and configuration info

    ```
