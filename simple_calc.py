while True:
    print("choose operator: + - * / or type exit")
    op = input("choose operature: ")
    if op == "exit":
        break
    a = float(input("enter integer: "))
    b = float(input("enter integer: "))
    if op == "+" : print("result:",a+b)
    elif op == "-" : print("result:",a-b)
    elif op == "*" : print("result:",a*b)
    elif op == "/" :print("result:",a/b if b!=0 else "error! divided by zero")
    else: print("invalid operator")
