#-*-coding:utf-8-*-
#@Time:20:41
#@Author:Alvin Hu

import Login
atm_menu_show = [
    "1.Check account"
    "2. Add Money",
    "3. Delete",
    "4.Transfer",
    "5.Withdraw",
    "6.Frozen/Unfrozen Account",
    "7.Payment",
    "8.Print Statement"
]
















@Login.login
def main_ATM():
    print("Welcome to your ATM")
    for i in atm_menu_show:
        print("\t"+i)




