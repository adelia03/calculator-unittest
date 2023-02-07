def calculator(expression):
    allowed = '+-*/'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'The expression must contain at least 1 character ({allowed})!')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left, right)
            except(ValueError, TypeError):
                raise ValueError("The expression must contain 2 integer nums and 1 character!")


if __name__ == '__main__':
    print(calculator('10/5'))
