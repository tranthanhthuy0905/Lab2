import re

def main():
    pattern = "^[a-z][a-zA-Z0-9_]*$"
    
    inputVar = input("Enter the Java identifiers value: ")
    searching = re.search(pattern, inputVar)
    
    if searching:
        print("It matches well")
        print(searching)
    else:
        print("Oops! We got no match")
    
    x = re.sub(pattern, "V", inputVar)
    print(x)

main()