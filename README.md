# Test performer
A small project that helps to run tests on other projects and detect bugs. 
## How to use
### The tester
The test-performer does not create tests, so it also needs a `tester` for it to work. A `tester` must have:
- `get_test(arg)` - function, returns either list of pairs: test with which to run the script and answer to that test,  or list of tests if there are no answers (only for comparing, no checking)
- `rep()` - generator, generates arg for get_test and loops testing. For example:
```python
rep():
    While(True):
        yield ""
```
However, `rep()` needed only if you want to run it, if you want to add it to your project for using functions from it, `rep()` isn't necessary
will loop testing with test from `get_test("")` until test fails;
- `comparator(s1, s2, t)` - compares s1 and s2 as though they were results of test t
### Runing test performer
When you run `test` you need to give it one or two arguments (path(s) for the programme(s)). `test` will run tests on the programme(s) and compare the results: if there was only one programme given it will compare answer from `get_test()` and this programme result, otherways it will compare results of two programmes. 
## Functions
- **run(path, args):** runs `path` with `args` as input. return tuple with outpput and errors
- **compare(path1, path2, arg="", comp=tester.comparator):** runs `path1` and `path2` with test from `tester.get_test(arg)`  and compares the results with `comp`.  If `comp` returns False, `compare`  returns dictionary with keys: "output1", "output2",  "test" and "arg". If there were errors during testing it will return dictionary with keys: `path1` or `path2`: errore text, "test" and "arg". If all went well it returns None. 
- **check(path, arg="", comp=tester.comparator):** works as compare, but it compares result with answer from `tester.get_test(arg)`. If  `comp` returns False, `check` returns dictionary with keys: "answer", "result", "test" and "arg"
- **main(func, operands):** for test in `tester.rep()` preforms `func(operands)`. If `func` didn't return None, `main` returns string with result of `func`, otherways it returns None
