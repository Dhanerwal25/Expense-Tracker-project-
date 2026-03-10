#MINI PROJECT - EXPENSE TRACKER

Expenses = [] # list of expense in form of dict.
print("Welcome🙋🏻 in Expense Tracker : invest your money on right place😊")

    while True :
        print ("«««MENU»»»", )
        print ("1 :Add expense")
        print ("2:view all expenses")
        print ("3:Total expense")
        print ("4:Exit ")
        choice=int(input("enter your choice:"))
#Add expense    
        if choice == 1:
            date = input("Enter date of expense: ")
            category = input("Enter type (food, travel, shopping etc.): ")
            description = input("Enter the details: ")
            amount = float(input("Enter total amount: "))
            
            expense = {
                "Date": date,
                "Category": category,
                "Description": description,
                "Amount": amount
            }  
            Expenses.append(expense)
            print(Expenses)
            print("Bro!  Expense added successfully 😊.")
    
    #View all expenses    
        elif choice == 2:
            if len(Expenses)==0:
                print(" No expenses added.")
            else:
               print(" This is your all expenses —")
               count=1
               for each_expense in Expenses:
                   print(f"Expense number-{count}→")
                   count=count+1
                   print (f"{each_expense['Date']} ,{each_expense['Category']} ,     {each_expense['Description']} ,{each_expense['Amount']}")
        #total expense
        elif choice == 3:
            total = sum(item['Amount'] for item in Expenses)
            print("Total expense:", total)
     
         #Exit 
        elif choice == 4:
            print("Exiting. Goodbye! Thanks for using our system.")
            break 
        else: 
            print (" Invalid choice")
            
        