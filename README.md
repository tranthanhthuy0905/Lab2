# Regular Expression

### 1) Legal and customary Java Identifiers.

Draw the FSA for the Regular Expression that describes legitimate and customary java variable identifiers. Btw, "customary" means follow not just the language enforced rules but also the strong traditions (variable, function identifiers start with lower case; class names start with capital letters)

Once you have the FSA, convert it to a set of Regular Grammar Rules in Bakus-Naur form[1].

Using metacharacters from regular expressions, write a python program, using regular expressions that certifies whether a string is a valid identifier name or not.

Once you can find/match the identifiers, adapt the code to replace each identifier with an X[2].

### 2) Numbers

Adapt the unsigned digit FSA (seen in class) to accept all integers and another to accept all floats.

Write the python re code to replace all numbers (ints or floats) with an I or F respectively. You can start with an unsigned integer, then adapt for a signed integer, then adapt that for a float.

### 3) Arithmetic expressions

Write a simple parse tree for arithmetic expressions. At this point don't distinguish between Add/Sub and Mult/Divide or parentheses.

Write a set of regular expressions that parse an arithmetic statement in stages, starting with replacing the identifiers and numbers as in Steps 1 and 2. This means that once you replaced each identifier with an X and number with an I or F, your regular expression to parses arithmetic expressions can use generic X,I and F. Replace the arithmetic expression with an E.

a) Start with binary statements

ans = num1 + 4.2;

b) build up to longer expressions:

x = num1 + w \* -2;

x = num1 \* num2 – num3;

Note: if you have used Steps 1 and 2 correctly all identifiers will be replaced with X, all numbers with F and I for step 3 parsing.

To Pass In: pictures or FSA, parse trees, the code that runs the arithmetic expression parser, examples of strings that pass/failed, and a reflection on what didn't work or worked but is a mystery (or note "it all worked" if it did)

[1] BNF rules for unsigned integer Digit::=[0-9], Integer::=Digit| Digit Integer

[2] At some point, it might be useful to replace each identifier with $X or some longer label.
