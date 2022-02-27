import JavaIdentifiers
import Numbers


def statementParsing(expression):
    result = ""

    expressionsList = expression.split(" ")
    for elm in expressionsList:
        if Numbers.numberCheck(elm) == "F" or Numbers.numberCheck(elm) == "I":
            result += Numbers.numberCheck(elm)
        elif JavaIdentifiers.javaIdCheck(elm) == "X":
            result += "X"
        else:
            result += elm
        if expressionsList.index(elm) != len(expressionsList) - 1:
            result += " "
    print('Parsed result: ', result)

statementParsing("num1 + 4.2")          # X + F
statementParsing("num1 + w * -2")       # X + X * I
statementParsing(" num1 * num2 – num3") # X * X - X