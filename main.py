#TO-DO LIST

tasks=[]

def show_menue():
    print("\n Your Tasks Menue:")
    print("1.Add task")
    print("2.View Task")
    print("3.Remove task ")
    print("4.Exit")

    #main loop of program
while True:
        show_menue()
        choice=input("Enter a option from 1-4:")

        if choice == "1":
            task=input("Enter a task:")
            tasks.append(task)
            print("Task has been added!")

        elif choice == "2":
            if not tasks:
                print("No tasks are found")
            else:
                print("\n Your tasks:")
                task_number=1
                for task in tasks:
                    print(f"{task_number}.{task}")
                    task_number+=1
        elif choice == "3":
            if not tasks:
                print("No tasks found")
            else:
                print("\n Your tasks:")
                task_number=1
                for task in tasks:
                    print(f"{task_number}.{task}")
                    task_number+=1

                num=input("Enter a task number to remove :")
                if num.isdigit():
                    num=int(num)
                    if 1 <= num <= len(tasks):
                        removed=tasks.pop(num -1)
                        print(f"Removed: {removed}")
                    else:
                        print("Enter a valid task number:")
                elif choice == "4":
                    print("Sucessfully exit!Goodbye")
                    break
                else:
                    print("Enter a valid task number")






                                     
                                 


