import mysql.connector as sqltor
import matplotlib as plt
import pandas as pd
#import pyttsx3
#tts=pyttsx3.init()

mycon=sqltor.connect(host="localhost", user="root", passwd="1234", database="outset")

d1=pd.read_sql("select * from emp;",mycon)

uname=str(input("ENTER USERNAME - "))
uid=int(input("ENTER USER ID - "))

if (len(str(uid)))!=6:
    print("ERROR 01: INVALID USER ID")
else:
    logincon=0
    while logincon==0:
        d2=(d1.loc[d1['username'].str.contains(uname)])
        if d2.empty():
            print("ERROR 02: INVALID USERNAME")
            print("RE-ENTER DETAILS - ")
            uname = str(input("ENTER USERNAME - "))
            uid = int(input("ENTER USER ID - "))
        elif (d2.loc[d2['user_id'].str.contains(uid)]).empty():
            print("ERROR 01: INVALID USER ID")
            print("RE-ENTER DETAILS - ")
            uname = str(input("ENTER USERNAME - "))
            uid = int(input("ENTER USER ID - "))
        else:
            man_find = d2['designation'].str.contains('Manager')
            man_occ = man_find.sum()
            igl_find = d2['designation'].str.contains('IGL')
            igl_occ = igl_find.sum()
            gam_find = d2['designation'].str.contains('Gamer')
            gam_occ = gam_find.sum()
            if man_occ==1:
                print("WELCOME MANAGER")
                print()
                print("PRESS 1 TO VIEW/EDIT the DATA")
                print("PRESS 2 TO ACCESS OUTSET MEMBER DATABASE")
                vieweditaccess=int(input("----> "))
                proceed='y'
                while proceed=='y':
                    if vieweditaccess==1:
                        print("YOU CHOSE TO VIEW/EDIT DATA")
                        viewedit = 'y'
                        print("Which game's data would you like to access?")
                        print("PRESS 1 for Valorant")
                        print("PRESS 2 for CS:GO")
                        print("PRESS 3 for BGMI")
                        gvalid='y'
                        while gvalid=='y':
                            g = int(input(">>> "))
                            if g==1:
                                print("ACCESSING VALORANT DATABASE...")
                                gname='valorant'
                                d3=pd.read_csv("C:\\IP_Project_File\\ValorantData.csv")
                                d3=d3.dropna()
                                gvalid='n'
                            elif g==2:
                                print("ACCESSING CS:GO DATABASE...")
                                gname='CS:GO'
                                d3=pd.read_csv("C:\\IP_Project_File\\CSGOData.csv")
                                d3=d3.dropna()
                                gvalid='n'
                            elif g==3:
                                print("ACCESSING BGMI DATABASE...")
                                gname="BGMI"
                                d3 = pd.read_csv("C:\\IP_Project_File\\BGMIData.csv")
                                d3 = d3.dropna()
                                gvalid = 'n'
                            else:
                                print("ERROR 03: INVALID INPUT")
                                gvalid='y'
                        if viewedit == y:
                            print("PRESS 1 for EDITING the DATA")
                            print("PRESS 2 for VIEWING the DATA")
                            vieworedit = int(input("-------->"))
                            if vieworedit == 1:  # edit
                                print("YOU CHOSE TO EDIT THE DATA of ", gname)
                                edit = 'y'
                                pd.set_option('display width', 1000)
                                print(d3)
                                while edit == 'y':
                                    dict_new = {}
                                    date = input("ENTER DATE (in 'DD-MM-YYYY' format) - ")
                                    gw = int(input("ENTER GAMES WON - "))
                                    gl = int(input("ENTER GAMES LOST - "))
                                    rw = int(input("ENTER ROUNDS WON - "))
                                    rl = int(input("ENTER ROUNDS LOST - "))
                                    dict_new['Date'] = date
                                    dict_new['Games Won'] = gw
                                    dict_new['Games Lost'] = gl
                                    dict_new['Rounds Won'] = rw
                                    dict_new['Rounds Lost'] = rl
                                    d3 = d3.append(dict_new, ignore_index=True)
                                    print("RECORD ADDED")
                                    print()
                                    edit = input("DO YOU WANT TO EDIT DATA (Y/N)? ")
                                    edit = edit.lower()
                                    if edit == 'y':
                                        print("YOU CHOSE TO EDIT THE DATA AGAIN...")
                                    elif edit == 'n':
                                        print(" EXITING EDIT MENU ")
                                    else:
                                        print("ERROR : INVALID INPUT ")
                                        edit = 'y'
                                cont = input("do you want to continue?(y/n) ")
                                cont = cont.lower()
                                if cont == 'n':
                                    print("EXITING SYSTEM...")
                                    proceed = 'n'
                            elif vieworedit == 2:  # view
                                print("YOU CHOSE TO VIEW THE DATA of", gname)
                                view(d3)
                                cont = input("do you want to continue?(y/n) ")
                                cont = cont.lower()
                                if cont == 'n':
                                    print("EXITING SYSTEM...")
                                    proceed = 'n'
                            else:
                                print("ERROR : INVALID INPUT")
                        else:
                            print("ERROR : INVALID INPUT ")
                            proceed = 'y'
                    elif vieweditaccess==2:
                        print ("ACCESSING OUTSET MEMBER DATABASE...")
                        access='y'
                        while access=='y':
                            print()
                            print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
                            print()
                            print("PRESS 1 to VIEW THE OUTSET MEMBER DATABASE")
                            print("PRESS 2 to ADD A MEMBER TO THE OUTSET FAMILY")
                            viewacc=int(input("---------> "))
                            if viewacc==1:
                                print(d1)
                                cont = input("do you want to continue?(y/n) ")
                                cont = cont.lower()
                                if cont == 'n':
                                    print("EXITING SYSTEM...")
                                    access = 'n'
                            elif viewacc==2:
                                print()
                                print("ADDING A MEMBER TO THE OUTSET DATABASE")
                                print("ENTER MEMBER DETAILS...")
                                print()
                                nam=str(input("ENTER MEMBER NAME - "))
                                desig=''
                                desigvalid='n'
                                while desigvalid=='n':
                                    desig = str(input("Enter Designation - "))
                                    if ((desig == 'Manager') or (desig == "IGL") or (desig == 'Gamer')):
                                        desigvalid='y'
                                    else:
                                        print("DESIGNATIONS ARE ONLY ALLOWED OF THE FOLLOWING: - ")
                                        print("1. Manager")
                                        print("2. IGL")
                                        print("3. Gamer")
                                        print()
                                        print("NOTE THAT THE DESIGNATION TITLES ARE CASE SENSITIVE AND REQUIRE THE AFOREMENTIONED PATTERN ")
                                        desigvalid='n'
                                dateofbirth=str(input("ENTER Member's Date Of Birth (in the format {YYYY-MM-DD}) - "))
                                newunamevalid = "n"
                                uname_new=''
                                while newunamevalid == 'n':
                                    uname_new = input("ENTER USERNAME of Member - ")
                                    dict2 = (d1.loc[d1['username'].str.contains(uname_new)])
                                    if dict2.empty:
                                        newunamevalid = 'y'
                                    else:
                                        print("USERNAME ALREADY TAKEN")
                                        print("CHOOSE A DIFFERENT USERNAME")
                                        newunamevalid = 'n'
                                newuidvalid='n'
                                uid_new=''
                                while newuidvalid=='n':
                                    uid_new=int(input("ENTER USER ID of Member - "))
                                    dict2=(d1.loc[d1['user_id'].str.contains(uid_new)])
                                    if dict2.empty:
                                        newuidvalid='y'
                                    else:
                                        print("USER ID ALREADY TAKEN")
                                        print("CHOOSE A DIFFERENT USER ID")
                                        newuidvalid='n'
                                gnamevalid='n'
                                gname_new=''
                                while gnamevalid=='n':
                                    gname_new = str(input("Enter Game Name - "))
                                    if ((gname_new == 'Valorant') or (gname_new == "CS:GO") or (gname_new == 'BGMI')):
                                        gnamevalid = 'y'
                                    else:
                                        print("GAME NAMES ARE ONLY ALLOWED OF THE FOLLOWING: - ")
                                        print("1. Valorant")
                                        print("2. CS:GO")
                                        print("3. BGMI")
                                        print()
                                        print("NOTE THAT THE DESIGNATION TITLES ARE CASE SENSITIVE AND REQUIRE THE AFOREMENTIONED PATTERN ")
                                        gnamevalid = 'n'
                                mycursor=mycon.cursor()
                                sql="INSERT INTO emp(name, designation, dob, username, user_id, game_name) values( %s, %s, %s, %s, %s, %s)"
                                val=(nam, desig, dateofbirth, uname_new, uid_new, gname_new)
                                mycursor.execute(sql,val)
                                mycon.commit()
                                d4=pd.read_sql("select * from emp;", mycon)
                                print(d4)
                                cont=str(input("DO YOU WANT TO ACCESS OUTSET DATABASE AGAIN? (y/n) "))
                                cont=cont.lower()
                                if cont=='n':
                                    print("EXITING SYSTEM...")
                                    access='n'
                            else:
                                print("ERROR 03: INVALID INPUT")
                                access = 'y'
                        cont = input("do you want to continue?(y/n) ")
                        cont = cont.lower()
                        if cont == 'n':
                            print("EXITING SYSTEM...")
                            proceed = 'n'
                    else:
                        print("ERROR 03: INVALID INPUT")
                        proceed='y'
            elif igl_occ==1:
                print("WELCOME IGL")
                gname=''
                valo_find = d2['game_name'].str.contains('Valorant')
                valo_occ = valo_find.sum()
                if valo_occ == 1:
                    gname="Valorant"
                    d3=pd.read_csv("C:\\IP_Project_File\\ValorantData.csv")
                    d3=d3.dropna()
                cs_find = d2['game_name'].str.contains('Valorant')
                cs_occ = cs_find.sum()
                if cs_occ == 1:
                    gname="CS:GO"
                    d3=pd.read_csv("C:\\IP_Project_File\\CSGOData.csv")
                    d3=d3.dropna()
                bgmi_find = d2['game_name'].str.contains('Valorant')
                bgmi_occ = bgmi_find.sum()
                if bgmi_occ == 1:
                    gname="BATTLEGROUND MOBILE INDIA"
                    d3=pd.read_csv("C:\\IP_Project_File\\BGMIData.csv")
                    d3=d3.dropna()
                print()
                print('-*'*10)
                print()
                proceed='y'
                while proceed=='y':
                    viewedit=input("Do you want to view or edit data(y/n)? ")
                    viewedit=viewedit.lower()
                    if viewedit==y:
                        print("PRESS 1 for EDITING the DATA")
                        print("PRESS 2 for VIEWING the DATA")
                        vieworedit=int(input("-------->"))
                        if vieworedit==1: #edit
                            print("YOU CHOSE TO EDIT THE DATA of ",gname)
                            edit='y'
                            pd.set_option('display width',1000)
                            print(d3)
                            while edit=='y':
                                dict_new={}
                                date=input("ENTER DATE (in 'DD-MM-YYYY' format) - ")
                                gw = int(input("ENTER GAMES WON - "))
                                gl = int(input("ENTER GAMES LOST - "))
                                rw = int(input("ENTER ROUNDS WON - "))
                                rl = int(input("ENTER ROUNDS LOST - "))
                                dict_new['Date']=date
                                dict_new['Games Won'] = gw
                                dict_new['Games Lost'] = gl
                                dict_new['Rounds Won'] = rw
                                dict_new['Rounds Lost'] = rl
                                d3 = d3.append(dict_new,ignore_index=True)
                                print("RECORD ADDED")
                                print()
                                edit=input("DO YOU WANT TO EDIT DATA (Y/N)? ")
                                edit=edit.lower()
                                if edit=='y':
                                    print("YOU CHOSE TO EDIT THE DATA AGAIN...")
                                elif edit=='n':
                                    print(" EXITING EDIT MENU ")
                                else:
                                    print("ERROR : INVALID INPUT ")
                                    edit='y'
                            cont = input("do you want to continue?(y/n) ")
                            cont = cont.lower()
                            if cont == 'n':
                                print("EXITING SYSTEM...")
                                proceed = 'n'
                        elif vieworedit==2: #view
                            print("YOU CHOSE TO VIEW THE DATA of",gname)
                            view(d3)
                            cont = input("do you want to continue?(y/n) ")
                            cont = cont.lower()
                            if cont == 'n':
                                print("EXITING SYSTEM...")
                                proceed = 'n'
                        else:
                            print("ERROR : INVALID INPUT")
                    elif viewedit=='n':
                        proceed='n'
                        print("THANK YOU FOR VISITING")
                    else:
                        print("ERROR : INVALID INPUT ")
                        proceed='y'
            elif gam_occ==1:
                print("WELCOME GAMER")
                valo_find = d2['game_name'].str.contains('Valorant')
                valo_occ = valo_find.sum()
                if valo_occ == 1:
                    gname = "Valorant"
                    d3 = pd.read_csv("C:\\IP_Project_File\\ValorantData.csv")
                    d3 = d3.dropna()
                cs_find = d2['game_name'].str.contains('Valorant')
                cs_occ = cs_find.sum()
                if cs_occ == 1:
                    gname = "CS:GO"
                    d3 = pd.read_csv("C:\\IP_Project_File\\CSGOData.csv")
                    d3 = d3.dropna()
                bgmi_find = d2['game_name'].str.contains('Valorant')
                bgmi_occ = bgmi_find.sum()
                if bgmi_occ == 1:
                    gname = "BATTLEGROUND MOBILE INDIA"
                    d3 = pd.read_csv("C:\\IP_Project_File\\BGMIData.csv")
                    d3 = d3.dropna()

                view(d3)
            logincon=1 #login while loop break

def view(d3):
    viewing=1
    while viewing==1:
        print()
        print('-*' * 15)
        print()
        print("Would you like to view your data in GRAPH or TABLE format")
        print("PRESS 1 for TABLE format")
        print("PRESS 2 for GRAPH format")
        print()
        viewinput = int(input("-----> "))
        print()
        print('-*' * 15)
        print()
        if viewinput==1:
            print()
            print("YOU CHOSE TABLE FORMAT")
            print('-*' * 10)
            print(d3)
            print()
            print('-*' * 10)
            print()
            cont=input("do you want to continue?(y/n) ")
            cont=cont.lower()
            if cont=='n':
                print("EXITING SYSTEM...")
                viewing=0
        elif viewinput==2:
            print("YOU CHOSE GRAPH FORMAT")
            print('-*' * 10)
            rw = d3['Rounds Won']
            rl = d3['Rounds Lost']
            x = d3['Date']
            plt.plot(x, rw, 'co', markersize=5, ls='solid', markeredgecolor='r', label='Rounds Won')
            plt.plot(x, rl, 'ko', markersize=5, ls='solid', markeredgecolor='r', label='Rounds Lost')
            plt.xlabel('Date')
            plt.ylabel('No. of Rounds')
            plt.yticks(range(0, 35))

            plt.grid(True)

            plt.title('Rounds Won & Lost')
            plt.legend(loc='upper right')
            plt.show()
            cont = input("do you want to continue?(y/n) ")
            cont = cont.lower()
            if cont == 'n':
                print("EXITING SYSTEM...")
                viewing = 0
        else:
            print("ERROR 03: INVALID INPUT")
