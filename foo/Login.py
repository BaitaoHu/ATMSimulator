#-*-coding:utf-8-*-
#@Time:21:16
#@Author:Alvin Hu

import json,sys,os,datetime
DIR_NAME= os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_NAME)



def saveUser():
    with open(DIR_NAME+'\\doc\\'+"Account.json","w") as outfile:
        json.dump(userInfo,outfile)

def loadUser():
    with open(DIR_NAME+'\\doc\\'+"Account.json","r") as infile:
        return json.load(infile)

def existingLogin():
    global user_status
    userName = input("Your Username:")
    passWord = input("Your Password:")
    for item in userInfo:
        if item[0]==userName and item[1]==passWord:
            print("Login Success")
            user_status=True
    if user_status ==False:
            print("Login Failed")

def newUser():
    global userInfo
    print("Create a new account>>")
    newName = input("\tAccount name:")
    newPassword = input("\tPassWord:")
    newBalance =  input("\tPlease enter your balance:")
    newCredit = input("\tPlease enter your credit:")
    #createTime = datetime.date.today()
    #expireTime = createTime+datetime.timedelta(days=1095)
    ifFrozen = False
    newAccount = [newName,newPassword,newBalance,newCredit,ifFrozen]
    userInfo.append(newAccount)
    saveUser()
    user_status = True
    print("Welcome!"+""+newName)


userInfo = loadUser()
user_status=False

def login(func):

    def inner():
        global user_status

        if user_status==False:
            print("Please Sign up or Sign in")
            print("\t1.Sign up")
            print("\t2.Sign in")
            choice = input("Choice>>:").strip()
            if choice == "1":
                newUser()
                func()
            elif choice == "2":
                existingLogin()
                func()
        else:
            func()

    return inner






