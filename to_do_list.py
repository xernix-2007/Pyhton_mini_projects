tasks = [] 
while True:
    print("\n1.add task\n2.view task\n3.delete task\n4.exit")
    choice = input("choose:")
    if choice == "1":
        task = input("enter task:")
        tasks.append(task)
        print("task added.")
    elif choice == "2":   
        for i,t in enumerate(tasks,start = 1):
            print(f"{i}.{t}")
    elif choice == "3":
        num = int(input("task number to delete:"))
        if 0<num<= len(task):
            tasks.pop(num-1)
            print("task deleted.")
        else:
           print("invalid number.")
    elif choice == "4":
        print("good bye")
        break
    else:
        print("invalid option")