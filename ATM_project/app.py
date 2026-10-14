# import withdraw_calc , deposit_calc
import calc as ca

USER_DATA = {
    "username": "admin",
    "acc.no"  : 123456,
    "pin"     : 1234,
    "balance" :10000
} 

def user_info():

    if USER_DATA and USER_DATA["username"]:
        return f"\nHi user {USER_DATA['username']} your acc no is {USER_DATA['acc.no']}"
    else:
        print("user not found")

def deposit(deposit_amount):
    if deposit_amount:
        amount = ca.deposit_calc(USER_DATA["balance"],deposit_amount)
        USER_DATA["balance"] = amount
        return amount
    else:
        print("Amount not found")

def withdraw(withdraw_amount):

    if withdraw_amount:
        amount = ca.withdraw_calc(USER_DATA["balance"],withdraw_amount)
        USER_DATA["balance"] = amount
        return amount
    else:
        print("Amount Not Found")

def check_balance():
    return USER_DATA["balance"]

def main():
    print("Welcome to TP ATM...")
    pin_no = int(input("Enter the Pin No. :"))

    if USER_DATA and USER_DATA["pin"] ==pin_no:

        print(user_info())
        while True:

            choice = int(input("""
            1. Deposit
            2. Withdraw
            3. Check Balance
            4. Exit
            Enter your choice :"""))

            match choice:

                case 1:
                    amount = int(input("Enter the amount :"))
                    print(f"Deposite succesfully,ypur total balnce is:{deposit(amount)}")

                case 2:
                    amount = int(input("Enter the Amount: "))
                    print(f"Wthidraw succesfully, ypur tatal balance is : {withdraw(amount)}")
                case 3:
                    print(f"your total balance is :{check_balance()}")
                case 4:
                    print("Thanks for using TP ATM ")
                    break
                case _:
                    print("Invalid choice please select 1 to 4")

    else:
        print("Invalid pin No.")
if __name__ == "__main__":
    main()