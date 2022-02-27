import re


def javaIdCheck(inputVar):
    pattern = "^[a-z][a-zA-Z0-9_]*$"
    searching = re.search(pattern, inputVar)

    # if searching:
    #     print("It matches well")
    #     print(searching)
    # else:
    #     print("Oops! We got no match")

    x = re.sub(pattern, "X", inputVar)
    return(x)


javaIdCheck("testing")              # X
javaIdCheck("testing123")           # X
javaIdCheck("testing_")             # X
javaIdCheck("@testing")             # @testing
javaIdCheck("testing something")    # testing something
