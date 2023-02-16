import mysql.connector 
import os

def create():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Boogieman@1",
    database="world",  
    )
    print("1.Create New Account")
    print("2.Witdraw Cash")
    print("3.Deposit Cash")
    print("4.Balance Enquiry")
    print("5.Fast Cash")
    user=int(input("Enter the Number:"))
    if user==1:
        add()
       
    mycursor = mydb.cursor()
    
    #mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), pin int, accountnumber int)")
    #print("table created")
    def add():
        sql="insert into customers (name,pin,accountnumber)values(%s,%s,%s)"
        db_name=input("Enter the Name:")
        db_pin=int(input("Set Your Pin:"))
        db_balance=int(input("Enter the Account Number:"))
        val=(db_name,db_pin,db_balance)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Account Created Successfully")
    add
create

def main():
    pin1=1111  
    bal1=10000
    

    user=int(input("Enter the Pin:"))
    if user==pin1:

    
        
        def user1():
            print("1.Withdraw Cash")
            print("2.Deposit Cash")
            print("3.Balance Enquiry")
            print("4.Fast Cash")
            select=int(input("Enter the Transcation You Want:"))
            if select==1:
                print("1.Savings Account")
                print("2.Current Account")
                acc_type=int(input("Enter the Account Type"))
                if acc_type==1:
                    widraw=int(input("Enter the Amount:"))
                    balance=bal1-widraw
                if widraw<=bal1:
                    print(f"Collect Your Cash Rs:{widraw}")
                    print(f"Your Account Balance is:{balance}")
            elif select==2:
                depoist_amt=int(input("Enter the Amount To Be Deposited: "))
                total_balance=bal1+depoist_amt
                print(f"Your Deposited Amount is{depoist_amt}")
                print(f"Your Account Balance is {total_balance}")
            elif select==3:
                print(f"Your Account Balance is:{bal1}")
            elif select==4:
                print("1: Witdraw Rs.7000")
                print("2. Witdraw Rs.3000")
                print("3. witdraw Rs.10000")
                choose=int(input("Enter the amount:"))
                if choose<=1:
                    print("Collet Your Cash:7000")
                elif choose<=2:
                    print("Collect Your Cash:3000")
                elif choose<=3:
                    print("Collect Your Cash:10000")
                    
    user1    
        
main()

            
           
    

        


