#To-Do list

tasks=[]

def show_menu():
    print("Your Tasks:")
    print("1.Add task:")
    print("2.View task:")
    print("3.Remove task:")
    print("4.Exit")

#Main program loop
while True:
    show_menu()
    choice=input("Enter a task number 1-4:")

    if choice == "1":
        task=input("Enter a task:")
        tasks.append(task)
        print("Task has been added!")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            print("\n Your tasks")
            task_number=1
            for task in tasks:
                print(f"{task_number}.{task}")
                task_number+=1
    elif choice == "3":
        if not tasks:
            print("No tasks found")
        else:
            print("\n Your tasks")
            task_number=1
            for task in tasks:
                print(f"{task_number}.{task}")
                task_number+=1
            num=input("Enter a task number to remove:")
            if not num.isdigit():
                print("Please enter a valid task number:")
                continue
            num = int(num)
            if 1 <= num <= len(tasks):
                removed=tasks.pop(num -1)
                print(f"Removed:{removed}")
            else:
                print("Add a valid task number:")
    elif choice == "4":
        print("Sucessfully exited!goodbye")
        break
    else:
        print("Enter a valid number ")




                                     
                                 


