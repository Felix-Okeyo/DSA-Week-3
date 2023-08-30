# Question 1: Implement a function is_balanced(expression) that takes a string 
# containing parentheses, curly braces, and square brackets,and determines whether 
# the expression is balanced. 

# An expression is considered balanced if each opening bracket has a corresponding closing 
# bracket in the correct order.

# sample input = 

# expression1 = "([]{})"
# expression2 = "([)]"
# print(is_balanced(expression1))  # Output: True
# print(is_balanced(expression2))  # Output: False 


def is_balanced(input_expression):
    bracket_stack = []
    for individual_bracket in input_expression:
        if individual_bracket in ["(", "{", "["]:
            bracket_stack.append(individual_bracket)
        else:
            if not bracket_stack:
                return False
            current_stack_bracket = bracket_stack.pop()
            if current_stack_bracket == '(':
                if individual_bracket != ")":
                    return False
            if current_stack_bracket == '{':
                if individual_bracket != "}":
                    return False
            if current_stack_bracket == '[':
                if individual_bracket != "]":
                    return False
    if bracket_stack:
        return False
    return True

test_expression1 = "([]{})"
test_expression2 = "([)]"
print(is_balanced(test_expression1))  # Output: True
print(is_balanced(test_expression2))  # Output: False

