#-*-coding:utf-8-*-
#@Time:20:14
#@Author:Alvin Hu

import os
import sys

DIR_NAME= os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_NAME)

import ATM
import Shopping

while True:
    print("Welcome to Shopping Cart demo")
    print("\t1.Go Shopping")
    print("\t2.Manage my ATM")
    choice = input("Choice(q to quit)>>:").strip()
    if choice=="1":
        Shopping.main_Shopping()
    elif choice=="2":
        ATM.main_ATM()
    elif choice=="q":
        print("GoodBye")
        exit(0)





