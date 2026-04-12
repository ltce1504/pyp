task_list = [
    ("Buy Groceries",1),
    ("Complete Assignment",2),
    ("Call the doctor",3),
    ("Pay bills",1),
    ("Read a book",2),
]

def addTask():
    t = input("Enter Task: ")
    try:
        p = int(input("Enter the Task Priority (1 - High , 2 - Medium , 3 - Low)"))
        if p not in [1,2,3]:
            print("Please enter a valid priority : 1,2, or 3.")
        else:
            task_list.append((t,p))
            print("Tasks added successfully !!")
        
    except ValueError:
        print("Priority must be an integer.")

def removeTask():
    try:
        ind = int(input("Please enter the index to be removed: "))
        if 1 <= ind <= len(task_list):
            task_list.pop(ind - 1)
            print("Task removed successfully !")
        else:
            print("Invalid index.Please enter a valid index.")
    except:
        if len(task_list) == 0:
            print("No tasks to remove.")
            return

  
def displaytask():
    print(task_list)
    
def updateTask():
    t = input("Enter Task: ")
    try:
        ind = int(input("Please enter the index to be updated: "))
        if 1 <= ind <= len(task_list):
            print("Invalid index.Please enter a valid index.")
            try:
                p = int(input("Enter the Task Priority (1 - High , 2 - Medium , 3 - Low)"))
                if p not in [1,2,3]:
                    print("Please enter a valid property : 1,2, or 3.")
                else:
                    task_list[ind - 1] = (t,p)
                    return task_list
                print("Tasks added successfully !!")
            except ValueError:
                print("Priority must be an integer.")
    except:
        if len(task_list) == 0:
            print("No tasks to update .")
            return
while True:
    print("-------Welcome to the task list--------")
    print("1.ADD Task")
    print("2.Delete Task")
    print("3.Display Task")
    print("4.Update Task")
    print("5.Exit")
    choice = int(input("Please enter your choice of service (1-5):"))
    if choice == 1:
        addTask()
    elif choice == 2:
        removeTask()
    elif choice == 3:
        displaytask()
    elif choice == 4:
        updateTask()
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Please enter a valid choice of service")
