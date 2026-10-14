USER_DATA = {
    "username": "admin",
    "acc.no"  : 123456,
    "pin"     : 1234,
    "balance" :10000
} 

def user_info():

    if USER_DATA and USER_DATA["username"]:
        return f"\nHi user {}"