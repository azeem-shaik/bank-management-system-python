import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exist ")
    except Exception as error:
        print(f"An Exception occured as {error}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __generate_account_number(cls):
        alphabet = random.choices(string.ascii_letters, k = 3)
        number = random.choices(string.digits, k = 3)
        special = random.choices("!@#$%^&*()-+", k = 1)
        id = alphabet + number + special
        random.shuffle(id)
        return ''.join(id)

    
    def Createaccount(self):
        info = {
            "name": input("Tell your name :- "),
            "age" : int(input("Tell your age :- ")),
            "email": input("Tell Your Email :- "),
            "pin"  : int(input("Tell your 4 number pin :- ")),
            "accountNo.": Bank.__generate_account_number(),
            "balance" : 0

        }
        if info['age'] <18 or len(str(info["pin"])) != 4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i}: {info[i]}")
            print("Please note down your account number")

        Bank.data.append(info)

        Bank.__update()

    def Deposit(self):
        accnumber = input("Tell your account number:- ")
        pin = int(input("Tell your 4 number pin:- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == []:
            print("Sorry No such account exist or pin is incorrect Please check your account number and pin")
        else:
            amount = int(input("Tell the amount you want to deposit:- "))
            if amount <= 0 or amount > 10000:
                print("Sorry you cannot deposit this amount. The amount should be greater than 0 and less than 10000")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print(f"Amount has been deposited successfully. Your current balance is {userdata[0]['balance']}")

    def Withdraw(self):
        accnumber = input("Tell your account number:- ")
        pin = int(input("Tell your 4 number pin:- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == []:
            print("Sorry No such account exist or pin is incorrect Please check your account number and pin")
        else:
            amount = int(input("Tell the amount you want to withdraw:- "))
            if amount <= 0 or amount > 10000:
                print("Sorry you cannot withdraw this amount. The amount should be greater than 0 and less than 10000")
            elif userdata[0]['balance'] < amount:
                print(f"Sorry you dont have enough balance. Your current balance is {userdata[0]['balance']}")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print(f"Amount has been withdrawn successfully. Your current balance is {userdata[0]['balance']}")

    def Details(self):
        accnumber = input("Tell your account number:- ")
        pin = int(input("Tell your 4 number pin:- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == []:
            print("Sorry No such account exist or pin is incorrect Please check your account number and pin")
        else:
            print("Your account details are as follows:-")
            for i in userdata[0]:
                print(f"{i}: {userdata[0][i]}")

    def Update(self):
        accnumber = input("Tell your account number:- ")
        pin = int(input("Tell your 4 number pin:- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata ==[]:
            print("Sorry No such account exist or pin is incorrect Please check your account number and pin")
        else:
            print("You can update your name, email, and pin. You cannot update your age, pin, account number and balance") 
            print("Fill the details you want to update. If you dont want to update any field then leave it blank")

            newdata = {
                "name": input("Enter your new name or press Enter to skip: "),
                "email": input("Enter your new email or press Enter to skip: "),
                "pin": input("Enter your new pin or press Enter to skip: ")
            }
            if newdata['name']== "":
                newdata['name'] = userdata[0]['name']
            if newdata['email']== "":
                newdata['email'] = userdata[0]['email']
            if newdata['pin']== "":
                newdata['pin'] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                  continue
                else:
                  userdata[0][i] = newdata[i]

        Bank.__update()    
        print("Your details have been updated successfully.")

    def Delete(self):
        accnumber = input("Tell your account number:- ")
        pin = int(input("Tell your 4 number pin:- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata ==[]:
            print("Sorry No such account exist or pin is incorrect Please check your account number and pin")
        else:
            check = input("Press Y to delete your account or N to cancel:- ")
            if check == "N" or check == "n":
                print("Your account deletion has been cancelled.")
                
            else:
                if check == "Y" or check == "y":
                   Bank.data.remove(userdata[0])
                   Bank.__update()
                   print("Your account has been deleted successfully.")
        

user = Bank()
print("Press 1 for creating an account:")
print("Press 2 for Depositing the money in your account:")
print("Press 3 for Withdrawing the money: ")
print("Press 4 for Details:")
print("Press 5 for Updating the details:")
print("Press 6 for deleting your account:")

check = int(input("Tell your response:-"))

if check==1:
    user.Createaccount()

if check==2:
    user.Deposit()

if check==3:
    user.Withdraw()

if check==4:
    user.Details()

if check==5:
    user.Update()

if check==6:
    user.Delete()