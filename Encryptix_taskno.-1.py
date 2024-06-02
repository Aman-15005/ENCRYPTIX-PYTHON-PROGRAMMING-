task=[]
#these print commands give the introduction to the application
print("-------WELCOME TO YOUR TO DO LIST--------- ")
print("These are the options for commands")
print("\t 1.ADD - To add a item to the to do list")
print("\t 2.VIEW - To view the to do list")
print("\t 3.UPDATE- To update an item to the to do list")
print("\t 4.DELETE - To delete an item from the to do list")
print("\t 5.QUIT - To quit the to do list")
#defining the functions
def add(x):
    task.append(x)
def update(a,b):
    task[a-1]=b
def delete(a):
    task.remove(task[a-1])
#defining the main function
def main():
    while True:
        print("Enter the choice from below")
        print("\t 1.ADD ")
        print("\t 2.VIEW ")
        print("\t 3.UPDATE")
        print("\t 4.DELETE")
        print("\t 5.QUIT ")
        choice=int(input("enter your choice"))
        if choice==1:
            a=input("Enter the item to add")
            add(a)
        elif choice==2:
            for index,tasks in enumerate(task,start=1):
                print(f"{[index]}--{tasks}")
        elif choice==3:
            a=int(input("enter the number of task that you want to update"))
            b=input("Enter the task to be updated")
            update(a,b)
            print("Task updated successfully")
        elif choice==4:
            a=int(input("enter the number of task that you want to delete"))
            delete(a)
            print("Task deleted successfully")
        elif choice==5:
            print("THANK YOU FOR USING THE APPLICATION")
            break
        else:
            print("Invalid choice entered")
if __name__=="__main__":
    main()
