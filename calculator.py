
def add(xx, yy):
    return xx + yy

def sub(xx, yy):
    return xx - yy

def mul(xx, yy):
    return xx * yy

def div(xx, yy):
    return xx / yy

def main():
    op = input("Enter an operation (+, -, *, /):")
    n1 = int(input("Enter the first number..."))
    n2 = int(input("Enter the second number..."))
    res = None
    if op == "+":
        res = add(n1, n2)
    elif op == "-":
        res = sub(n1, n2)
    elif op == "*":
        res = mul(n1, n2)
    elif op == "/":
        res = div(n1, n2)

    if res:
        print("-->", res)
    else:
        print("Invalid operation:", op)

if __name__ == "__main__":
    main()
