import subprocess as sub
import sys
import tester

## tester must have:
# - get_test(arg) - function, returns either list of pairs: test with which to run the script and answer to that test, 
#                   or list of tests, if there are no answers (only for comparing, no checking)
# - rep() - generator, generates arg for get_test and loops testing. needed only if you want to run it, 
# if you want to add it to your project for using functions from it, `rep()` isn't necessary
# - comparator(s1, s2, t) - compares s1 and s2 as though they were results of test t
##


def run(path, args):
    try:
        proc = sub.Popen(path, stdout=sub.PIPE, stdin=sub.PIPE, stderr=sub.PIPE, text=True)
    except OSError as err:
        return ("","OS error: {0}".format(err))
    outs, err = proc.communicate(input=args)
    proc.kill()
    return (outs, err)


def compare(path1, path2, arg="", comp=tester.comparator):
    tests = tester.get_test(arg)
    for test in tests:
        if isinstance(test, tuple):
            test, _ = test
        s1, err1 = run(path1, test)
        s2, err2 = run(path2, test)
        if err1 != '':
            return {path1 : err1, "test": test, "arg": arg}
        if err2 != '':
            return {path2: err2, "test": test, "arg": arg}
        if comp(s1, s2, test) is False:
            return {"output1": s1, "output2": s2, "test": test, "arg": arg}
    return None


def check(path, arg="", comp=tester.comparator):
    tests = tester.get_test(arg)
    for test, ans in tests:
        result, err = run(path, test)
        if err != '':
            return {path : err, "test": test, "arg": arg}
        if comp(result, ans, test) is False:
            return {"answer": ans, "result": result, "test": test, "arg": arg}
    return None


def main(func, operands):
    for test in tester.rep():
        data = func(*operands, arg=test)
        if data is not None:
            l = ''''''
            for i, j in data.items():
                l += (str(i) + " : " + str(j)+'\n')
                
            return l
    return None


if __name__ == "__main__":
    #import pdb; pdb.set_trace()
    operand = sys.argv[1:]
    if len(operand) == 2:
        ans = main(compare, operand)
        if ans is not None:
            print(ans)
        else:
            print("All tests went well\n")
    elif len(operand) == 1:
        ans = main(check, operand)
        if ans is not None:
            print(ans)
        else:
            print("All tests went well\n")
    else:
        print("too many arg")
