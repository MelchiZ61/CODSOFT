# A To-Do List application is a useful project that helps users manage and organize their tasks efficiently.
# This project aims to create a command-line or GUI-based application using Python
# , allowing users to create, update, and track their to-do lists

def main_menu():
    print("-----------------------------------------------")
    print("type 1 to add tasks")
    print("type 2 to view tasks")
    print("type 3 to mark tasks as done")
    print("type 4 to EXIT")
    print("-----------------------------------------------")
#------------------------------------------
#------------------------------------------
def add_tasks(tasks):
    new_task=input("enter your task: ")
    new_task=new_task.upper()
    for i in tasks:
        if i==new_task:
            print("task already present")
    tasks.append(new_task)
#------------------------------------------
#------------------------------------------
def view_tasks(tasks):
    print("\nToDoList:")
    if len(tasks)==0:
        print("ToDoList is EMPTY!!!!!!")
    else:
        for i,task in enumerate(tasks,start=1):
            print(f"{i}.{task}")
    print()
#------------------------------------------
#------------------------------------------
def mark_as_done(tasks):
    if not tasks:
        print("Can't perform operation as ToDoList is EMPTY!!!!!!")
    else:
        view_tasks(tasks)
        try:
            index=int(input("enter the number of task to mark as done: "))-1
        except ValueError as e:
            print(e)
            print("please enter the correct index value")
        else:
            if 0<=index<len(tasks):
                removed_task=tasks.pop(index)
                print(f"'{index}:{removed_task}' marked as done and removed")
                print()
            else:
                print("invalid index value, please try again")
                print()
#------------------------------------------
#------------------------------------------

ToDoList=[]

while True:
    main_menu()
    print()
    try:
        choice=int(input("Enter your choice:"))
    except ValueError as e:
        print(e)
        print("please enter the correct option")
    else:
        if choice==1:
            add_tasks(ToDoList)
            while True:
                try:
                    another_task = int(input("Do you want to add another task? (1/0): "))
                    if another_task==1:
                        add_tasks(ToDoList)
                    elif another_task==0:
                        print()
                        break
                except ValueError:
                    print("please choose from the choices!!!")
        elif choice==2:
            view_tasks(ToDoList)
        elif choice==3:
            mark_as_done(ToDoList)
        elif choice==4:
            print("EXITING..........")
            break
        else:
            print("Invalid choice")

print("DONE :)")