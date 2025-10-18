from datetime import datetime


def addEmployee(name,depart,postion,sal,hd,status):
    nm=input("Enter Employee Name: ")
    name.append(nm)
    dep=input("Enter Employee Department: ")
    depart.append(dep)
    pose=input("Enter Employee Position: ")
    postion.append(pose)
    while(True):
        salary=float(input("Enter Employee Salary: "))
        if(salary<=0):
            print("please enter valid salary!")
        else:
            sal.append(salary)
            break
    while True:
        hired = input("Enter Hire date (dd/mm/yyyy): ")
        try:
            # Try to parse the input
            date_obj = datetime.strptime(hired, "%d/%m/%Y")
            hd.append(hired) 
            break
        except ValueError:
            print("Invalid format. Please use dd/mm/yyyy.")
    status.append("Active")
    print("Employee has been added successfully!")

def viewAllActiveEmployee(id,name,depart,postion,sal,hd,status):
    i=0
    numOfActive=0
    for val in status:
        if(val == "Active"):
            print(f"""{id[i]}       {name[i]}     {depart[i]}     {postion[i]}      {sal[i]}      {hd[i]}     {status[i]}""")
            numOfActive+=1
        i+=1
    print("Number of Active Employee:",numOfActive)

def searchByID(id,name,depart,postion,sal,hd,status):
    idTosearch=int(input("Enter ID to Search for the Employee: "))
    i=0
    for val in id:
        if(val==idTosearch):
           print(f"""{id[i]}       {name[i]}     {depart[i]}     {postion[i]}      {sal[i]}      {hd[i]}     {status[i]}""")
           break
        i+=1
    print("The user is not found!")

def updateEmployee(id,name,depart,postion,sal,hd,status):
    idToupdate=int(input("Enter ID to Search for the Employee: "))
    i=0
    for val in id:
        if(val==idToupdate):
            print(f"the current employee name: {name[i]}")
            newname=input("Enter the new name or press for the next field:")
            if (newname != ""):
                name[i]=newname
            print(f"the current employee department: {depart[i]}")
            newdep=input("Enter the new department or press for the next field:")
            if (newdep != ""):
                depart[i]=newdep
            print(f"the current employee postion: {postion[i]}")
            newpos=input("Enter the new postion or press for the next field:")
            if (newpos != ""):
                postion[i]=newpos
            print(f"the current employee salary: {sal[i]}")
            newsal=input("Enter the new salary or press for the next field:")
            if (newsal != ""):
                while True:
                    fsalary=float(newsal)
                    if (fsalary<=0):
                        print("please inter valid salary!")
                    else:
                        sal[i]=float(newsal)
                        break
                    newsal=input("Enter the new salary")
            print(f"the current employee hire date: {hd[i]}")
            newhd=input("Enter the new hire date (dd/mm/yyyy) or press to finish:")
            if newhd.strip() != "":
                try:
                    date_obj = datetime.strptime(newhd, "%d/%m/%Y")
                    hd[i] = newhd
                except ValueError:
                    print("Invalid format.")
            break
        i+=1

def changeEmployeeStatuse(id,status):
    idtosearch=int(input("Enter the employee id to change their status: "))
    i=0
    for val in id:
        if(val==idtosearch):
            if(status[i]=="Retired"):
                status[i]="Active"
            else:status[i]="Retired"    
            
            print("the status is changed successfully!")
            break
        i+=1
    print("the employee is not found!")    

def viewAllRetiredEmployees(id,name,depart,postion,sal,hd,status):
    i=0
    numOfRetired=0
    for val in status:
        if(val == "Retired"):
            print(f"""{id[i]}      {name[i]}    {depart[i]}     {postion[i]}      {sal[i]}       {hd[i]}     {status[i]}""")
            numOfRetired+=1
        i+=1
    print("Number of Active Employee:",numOfRetired)

def deleteEmployee(id,name,depart,postion,sal,hd,status):
    idtosearch=int(input("Enter the employee id to delete : "))
    i=0
    for val in id:
        if(val==idtosearch):
            ask=input(f"Are you sure that you want to delete this employee {id[i]}       {name[i]}     {depart[i]}     {postion[i]}      {sal[i]}      {hd[i]}     {status[i]} (Yes/No): ")
            if(ask=="Yes"):
                id[i]=0
                name[i]=None
                depart[i]=None
                postion[i]=None
                sal[i]=0
                hd[i]=None
                status[i]=None
                print("the employee is deleted successfully!")
                break
            else:break

        i+=0
    print("the employee is not found!")   

def main():
    ids=[1000,1001,1002,1003]
    name=["moun","reda","ali","ali"]
    department=["it","oc","pr","hr"]
    postion=["senior","senior","junior","senior"]
    salary=[80000,50000,30000,40000]
    hiredate=["1/10/2020","20/7/2015","31/10/2022","29/2/2025"]
    status=["Active","Retired","Active","Retired"]
    id=1004

    while(True):
        print("""-----------------------------------------
        welcome to hr system:  
-----------------------------------------          
        1-Add Employee
        2-View all active employees
        3-Search for an employee by id
        4-Update an Employee 
        5-Change employee statu
        6-View all retired employees
        7-Delete Employee
        8-Exit""")
        choice=int(input("Enter you choice: "))
        print("---------------------------------------------------------")
        match(choice):
            case 1:
                
                addEmployee(name,department,postion,salary,hiredate,status)
                ids.append(id)
                id+=1
                print("---------------------------------------------------------")
            
            case 2:
                viewAllActiveEmployee(ids,name,department,postion,salary,hiredate,status)
                print("---------------------------------------------------------")
                
            case 3:
                searchByID(ids,name,department,postion,salary,hiredate,status)
                print("---------------------------------------------------------")
                
            case 4:
                updateEmployee(ids,name,department,postion,salary,hiredate,status)
                print("---------------------------------------------------------")
                
            case 5:
                changeEmployeeStatuse(ids,status)
                print("---------------------------------------------------------")
                
            case 6:
                viewAllRetiredEmployees(ids,name,department,postion,salary,hiredate,status)
                print("---------------------------------------------------------")
                
            case 7:
                deleteEmployee(ids,name,department,postion,salary,hiredate,status)
                print("---------------------------------------------------------")
                
            case 8:
                return
            case _:
                print("enter a valid input!")
                

main()



