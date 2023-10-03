# CodeClauseInternship_Project
Code Clause Internship
def calculate(a, b, op):
    if op == '+':
        return a+b

    elif op == '-':
        return a-b

    elif op == '*':
        return a*b

    elif op == '/':
        return a/b

    elif op == '%':
        return a % b

    else:
        pass


def mainProg():
    try:
        a = int(input("enter the 1st number"))
        b = int(input("enter the 2nd number"))
        op = input("enter the operator")

        print(calculate(a, b, op))

        user = input('Enter E to exit:')

        if str(user).lower() == 'exit' or str(user).lower() == 'e':
            print('Calculation Over')
        else:
            mainProg()
    except Exception as e:
        print(e)
        mainProg()
