'''operator precedence

1. () : Parentheses (highest precedence) -> Associativity: Left to right
2. x[index], x[index:index] : Subscription, slicing -> Associativity: Left to right
3. await x : Await expression
4. ** : Exponentiation -> Associativity: Right to left
5. +x, -x, ~x : Unary plus, unary minus, bitwise NOT -> Associativity: Right to left
6. *, @, /, //, % : Multiplication, matrix multiplication, division, floor division, remainder -> Associativity: Left to right
7. +, - : Addition and subtraction -> Associativity: Left to right
8. <<, >> : Bitwise shifts -> Associativity: Left to right
9. & : Bitwise AND -> Associativity: Left to right
10. ^ : Bitwise XOR -> Associativity: Left to right
11. | : Bitwise OR -> Associativity: Left to right
12. in, not in, is, is not, <, <=, >, >=, !=, == : Comparisons, membership, identity tests -> Associativity: Left to right
13. not x : Boolean NOT -> Associativity: Right to left
14. and : Boolean AND -> Associativity: Left to right
15. or : Boolean OR -> Associativity: Left to right
16. if-else : Conditional expression -> Associativity: Right to left
17. lambda : Lambda expression
18. := : Assignment expression (Walrus operator) -> Associativity: Right to left
Note: Parentheses () have highest precedence and can override default order. Some operators, like await and lambda, do not have associativity.
 
 '''
# paranthesis
# exponential 
# multiplication or division
# addition or subtraction

x=(10+3)*2**2
print(x)

y=(2+3)*10-3
print(y)