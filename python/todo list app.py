tasks = []
while True:
    print("1.Add task")
    print("2.View task")
    print("3.End")
    choice = int(input("Enter choice: "))
    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == 2:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == 3:
        break 
    else:
        print("Invalid Choice")