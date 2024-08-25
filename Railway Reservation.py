def enter_train():
    train={}
    t_no=int(input("ENTER TRAIN NUMBER"))
    t_name=input("ENTER NAME OF TRAIN")
    t_ac=input("ENTER NO OF AC COMPARTMENT")
    t_sl=int(input("ENTER NO OF SLEEPER COMPARTMENT"))
    f_ac=int(input("ENTER FAIR OF AC COMPARTMENT"))
    f_sl=int(input("ENTER FAIR OF SLEEPER COMPARTMENT "))
    s=input("ENTER SOURCE OF  TRAIN")
    d=input("ENTER DESTINATION OF TRAIN")
    train['T_NO']=t_no
    train['T_NAME']=t_name
    train['T_AC']=t_ac
    train['T_SL']=t_sl
    train['F_AC']=f_ac
    train['F_SL']=f_sl
    train['S']=s
    train['D']=d
    return train
def insert_data():
    import mysql.connector as mysql
    connection= mysql.connect(host="localhost",user="root",password="khushi7625",database="railways_db")
    cursor=connection.cursor()
    train=enter_train()
    retrive="insert into train(T_NO,T_NAME,T_AC,T_SL,F_AC,F_SL,SOURCE,DESTINATION)values('{}','{}','{}','{}','{}','{}','{}','{}')".format(train['T_NO'],train['T_NAME'],train['T_AC'],train['T_SL'],train['F_AC'],train['F_SL'],train['S'],train['D'])
    cursor.execute(retrive)                                                                                                                                                                                                
    connection.commit()
    connection.close()
def update_train():
    import mysql.connector as mysql
    connection= mysql.connect(host="localhost",user="root",password="khushi7625",database="railways_db")
    cursor=connection.cursor()
    rows=show_data()
    sr=int(input("ENTER SR WHOSE RECORD WANT TO UPDATE"))
    print()
    display(rows[sr-1])
    id=rows[sr-1][0]
    print()
    print("WHAT YOU WANT TO UPDATE")
    print()
    print("ENTER 1 : TRAIN_NO ")
    print("ENTER 2 : TRAIN_NAME ")
    print("ENTER 3 : TOTAL AC SEATS")
    print("ENTER 4 : TOTAL SLEEPER SEATS")
    print("ENTER 5 : FARE AC SEATS")
    print("ENTER 6 : FARE SLEEPER SEATS")
    print("ENTER 7 : SOURCE")
    print("ENTER 8 : DESTINATION")
    print()
    ch=int(input("ENTER YOUR CHOICE "))
    print()
    if ch>=1 and ch<=8:
        if ch==1:
            t_no=int(input("enter new train no:")) 
            retrive="update train set t_no='{}' where id='{}'".format(t_no,id)
        elif ch==2:
             t_name=input("enter new train name:")
             retrive="update train set t_name='{}' where id='{}'".format(t_name,id)
        elif ch==3:
             t_ac=int(input("enter new total ac seats"))
             retrive="update train set t_ac='{}' where id='{}'".format(t_ac,id)
        elif ch==4:
             t_sl=int(input("enter new total sleeper seats"))
             retrive="update train set t_sl='{}' where id='{}'".format(t_sl,id)
        elif ch==5:
             f_ac=float(input("enter new fair of ac seats"))
             retrive="update train set f_ac='{}' where id='{}'".format(f_ac,id)
        elif ch==6:
             f_sl=zfloat(input("enter new fair of sleeper seats"))
             retrive="update train set f_sl='{}' where id='{}'".format(f_sl,id)
        elif ch==7:
             source=input("enter new source of train")
             retrive="update train set source='{}' where id='{}'".format(source,id)
        elif ch==8:
             destination=input("enter new destination of train")
             retrive="update train set destination='{}' where id='{}'".format(destination,id)
    cursor.execute(retrive)
    connection.commit()
    connection.close()
    print("DATA IS UPDATED")
def delete_train():
    rows=show_data()
    import mysql.connector as mysql
    connection= mysql.connect(host="localhost",user="root",password="khushi7625",database="railways_db")
    cursor=connection.cursor()
    sr=int(input("ENTER SR WHOSE RECORD WANT TO DELETE"))
    print()
    print("ARE YOU SURE YOU WANT TO DELETE TRAIN OF SERIAL NUMBER",sr)
    print('ENTER 1 TO CONTINUE')
    print('ENTER 0 TO RETRY')
    ch=int(input("ENTER YOUR CHOICE"))
    print()
    id=rows[sr-1][0]
    if ch==1:
        retrive="delete from train where id='{}'".format(id)
        cursor.execute(retrive)
        connection.commit()
        print("RECORD IS DELETED")
    else:
        delete_train()
    connection.close()
def show_data():
    import mysql.connector as mysql
    connection= mysql.connect(host="localhost",user="root",password="khushi7625",database="railways_db")
    cursor=connection.cursor()
    retrive="select * from train"
    cursor.execute(retrive)
    rows=cursor.fetchall()
    sr=1
    ch=' '
    print("|---------------------------------------------------------------------------------------------------------------|")
    print("|SR\t|TRAIN_NO\t|TRAIN_NAME\t\t\t|SOURCE\t\t\t\t|DESTINATION                                                    |") 
    print("|---------------------------------------------------------------------------------------------------------------|")
    for row in rows:
        print("|",sr,"\t|",row[1],"\t|",row[2],(25-len(row[2]))*ch,"\t|",row[7],(20-len(row[7]))*ch,"\t|",row[8],(20-len(row[8]))*ch,"|")
        print("|---------------------------------------------------------------------------------------------------------------|")
        sr=sr+1
    return rows
def reservation():
    show_data()
    sr=int(input("ENTER SR WHERE RESERVATION IS TO BE DONE"))
    import mysql.connector as mysql
    connection= mysql.connect(host="localhost",user="root",password="khushi7625",database="railways_db")
    cursor=connection.cursor()
    retrive="select * from train"
    cursor.execute(retrive)
    t_rows=cursor.fetchall()
    t_row=t_rows[sr-1]
    d=date()
    cursor=connection.cursor()
    retrive="select * from book_train where t_id='{}'and date='{}'".format(t_row[0],d)
    cursor.execute(retrive)
    b_row=cursor.fetchone()
    print('ENTER 1 FOR AC RESERVATION')
    print('ENTER 2 FOR SLEEPER RESERVATION')
    ch=int(input('ENTER YOUR CHOICE'))
    seat=int(input('HOW MANY SEATS DO YOU WANT TO BOOK'))
    if b_row==None:
        if ch==1:
            if seat<=t_row[3]:
                bl=fare(seat,t_row[5])
                if bl==True:
                    retrive="insert into book_train(t_id,date,bk_ac,bk_sl) values('{}','{}','{}','{}')".format(t_row[0],d,seat,0)
                    cursor.execute(retrive)
                    connection.commit()
                    print("YOUR SEATS ARE BOOKED")
                    R_ticket()
            else:
                print("AVAILABLE SAETS",t_row[3])
                print("KINDLY ENTER SEATS WITHIN THE RANGE")
                seat=int(input('HOW MANY SEATS DO YOU WANT TO BOOK'))
                if seat<=t_row[3]:
                    bl=fare(seat,t_row[5])
                    if bl==True:
                        retrive="insert into book_train(t_id,date,bk_ac,bk_sl) values('{}','{}','{}','{}')".format(t_row[0],d,seat,0)
                        cursor.execute(retrive)
                        connection.commit()
                        print("YOUR SEATS ARE BOOKED")
                        R_ticket()
                else:
                    print("INCORRECT VALUES")
                    print("TRY AGAIN")
                    rservation()
        elif ch==2:
            if seat<=t_row[4]:
                bl=fare(seat,t_row[6])
                if bl==True:
                    retrive="insert into book_train(t_id,date,bk_ac,bk_sl) values('{}','{}','{}','{}')".format(t_row[0],d,0,seat)
                    cursor.execute(retrive)
                    connection.commit()
                    print("YOUR SEATS ARE BOOKED")
            else:
                print("AVAILABLE SAETS",t_row[4])
                print("KINDLY ENTER SEATS WITHIN THE RANGE")
                seat=int(input('HOW MANY SEATS DO YOU WANT TO BOOK'))
                if seat<=t_row[4]:
                    bl=fare(seat,t-row[6])
                    if bl==True:
                        retrive="insert into book_train(t_id,date,bk_ac,bk_sl) values('{}','{}','{}','{}')".format(t_row[0],d,0,seat)
                        cursor.execute(retrive)
                        connection.commit()
                        print("YOUR SEATS ARE BOOKED")
                        R_ticket()
                else:
                    print("INCORRECT VALUES")
                    print("TRY AGAIN")
                    rservation()
        else:
            print("INCORRECT VALUES")
            print("TRY AGAIN")
            reservation()
    else:   
        if ch==1:
            if b_row[3]<t_row[3]:
                avl=t_row[3]-b_row[3]
                if avl>=seat:
                    bl=fare(seat,t_row[5])
                    if bl==True:
                        retrive="update book_train set bk_ac=bk_ac+{} where t_id='{}' and date='{}'".format(seat,t_row[0],d)
                        cursor.execute(retrive)
                        connection.commit()
                        print("YOUR SEATS ARE BOOKED")
                        R_ticket()
                else:
                    print('SORRY')
                    print('ONLY',avl,'SEATS ARE AVAILABLE FOR BOOKING')
                    seat=int(input('ENTER NO OF SEATS WITHIN THE RANGE'))
                    if avl>=seat:
                        bl=fare(seat,t_row[5])
                        if bl==True:
                            retrive="update book_train set bk_ac=bk_ac+{} where t_id='{}' and date='{}'".format(seat,t_row[0],d)
                            cursor.execute(retrive)
                            connection.commit()
                            print("YOUR SEATS ARE BOOKED")
                            R_ticket()
                    else:
                        print('SORRY')
                        print('TRY AGAIN')
            else:
                 print('SORRY')
                 print('NO TICKETS ARE AVAILABLE FOR BOOKING')
        elif ch==2:
            if b_row[4]<t_row[4]:
                avl=t_row[4]-b_row[4]
                if avl>=seat:
                    bl=fare(seat,t_row[6])
                    if bl==True:
                        retrive="update book_train set bk_sl=bk_sl+{} where t_id='{}' and date='{}'".format(seat,t_row[0],d)
                        cursor.execute(retrive)
                        connection.commit()
                        print("YOUR SEATS ARE BOOKED")
                        R_ticket()
                else:
                    print('SORRY')
                    print('ONLY',avl,'SEATS ARE AVAILABLE FOR BOOKING')
                    seat=int(input('ENTER NO OF SEATS WITHIN THE RANGE'))
                    if avl>=seat:
                        bl=fare(seat,t_row[6])
                        if bl==True:
                            retrive="update book_train set bk_sl=bk_sl+{} where t_id='{}' and date='{}'".format(seat,t_row[0],d)
                            cursor.execute(retrive)
                            connection.commit()
                            print("YOUR SEATS ARE BOOKED")
                            R_ticket()
                    else:
                        print('SORRY')
                        print('TRY AGAIN')
            else:
                 print('SORRY')
                 print('NO TICKETS ARE AVAILABLE FOR BOOKING')
        else:
            print("INCORRECT VALUES")
            print('TRY AGAIN')
            reservation()
     
    connection.close()
def date():
    d=input("ENTER DATE")
    m=input("ENTER MONTH")
    y=input("ENTER YEAR")
    date=y+"-"+m+"-"+d
    return date
def fare(seat,fr):
    amt=seat*fr
    print("FARE FOR YOUR TICKETS IS",amt)
    print("KINDLY PAY THE AMOUNT FIRST FOR RESERVATION")
    am=float(input("ENTER YOUR AMOUNT"))
    if am==amt:
        return True
    else:
        print("YOUR MONEY IS REFUNDED")
        print("YOU HAVE PAID INCORRECT AMOUNT")
        print("PLEASE AGAIN PAY THE AMOUNT")
        am=float(input("ENTER YOUR AMOUNT"))
        if am==amt:
            return True
        else:
            print("ERROR")
            print("TRY AGAIN")
            fare(seat,fr)
def cancellation():
    show_data()
    sr=int(input("ENTER SR WHERE CANCELLATION IS TO BE DONE"))
    import mysql.connector as mysql
    connection= mysql.connect(host="localhost",user="root",password="diya1503",database="railways_db")
    cursor=connection.cursor()
    retrive="select * from train"
    cursor.execute(retrive)
    t_rows=cursor.fetchall()
    t_row=t_rows[sr-1]
    d=date()
    cursor=connection.cursor()
    retrive="select * from book_train where t_id='{}'and date='{}'".format(t_row[0],d)
    cursor.execute(retrive)
    b_row=cursor.fetchone()
    print('ENTER 1 FOR AC CANCELLATION')
    print('ENTER 2 FOR SLEEPER CANCELLATION')
    ch=int(input('ENTER YOUR CHOICE'))
    seat=int(input('HOW MANY SEATS DO YOU WANT TO CANCELLATION'))
    if b_row==None:
        print('NO DATA FOUND')
        print('YOU MIGHT HAVE ENTERED INCORRECT VALUES')
        print('TRY AGAIN')
        cancellation()
    else:
        if ch==1:
            if b_row[3]>=seat:
               retrive="update book_train set bk_ac=bk_ac-{} where t_id='{}' and date='{}' ".format(seat,t_row[0],d)
               cursor.execute(retrive)
               connection.commit()
               print("YOUR SEATS ARE CANCELLED")
               C_ticket()
            else:
                print('INCORRECT VALUES')
                print('TRY AGAIN')
                cancellation()
        elif ch==2:
            if b_row[4]>=seat:
               retrive="update book_train set bk_sl=bk_sl-{} where t_id='{}' and date='{}'".format(seat,t_row[0],d)
               cursor.execute(retrive)
               connection.commit()
               print("YOUR SEATS ARE CANCELLED")
               C_ticket()
            else:
                print('INCORRECT VALUES')
                print('TRY AGAIN')
                cancellation()
    connection.close()
def display(train):
    print("|////////////////////////////////////|")
    print("|TRAIN_NO               |",train[1],"|")
    print("|------------------------------------|")
    print("|TRAIN_NAME             |",train[2],"|")
    print("|------------------------------------|")
    print("|TOTAL AC SEATS         |",train[3],"|")
    print("|------------------------------------|")
    print("|TOTAL SLEEPER SEATS    |",train[4],"|")
    print("|------------------------------------|")
    print("|FARE OF AC SEATS       |",train[5],"|")
    print("|------------------------------------|")
    print("|FARE OF SLEEPER SEATS  |",train[6],"|")
    print("|------------------------------------|")
    print("|SOURCE                 |",train[7],"|")
    print("|------------------------------------|")
    print("|DESTINATION            |",train[8],"|")
    print("|////////////////////////////////////|")
def R_ticket():
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(" -------------------YOUR RESERVATION IS SUCCESSFULLY!!!--------------------")
    print(" -------------------------HAVE A SAFE JOURNEY-----------------------------")
    print(" ------------------------!!HAVE A GREAT DAY!!-----------------------------")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
def C_ticket():
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(" -----------------YOUR TICKET IS CANCEL SUCCESSFULLY!!!--------------------")
    print(" ------------------------!!HAVE A GREAT DAY!!-----------------------------")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
def intro_fun():
    print("********************************************************************")
    print("|----------------------------WELCOME TO----------------------------|")
    print("********************************************************************")
    print("********************************************************************")
    print("|------------------------INDIAN RAILWAY SYSTEM---------------------|")
    print("********************************************************************")
def menu_adm():
    while True:
        print("---------------MENU----------------")
        print("|1|:INSERT DETAIL OF NEW TRAIN    |")
        print("-----------------------------------")
        print("|2|:UPDATE DETAIL OF TRAIN        |")
        print("-----------------------------------")
        print("|3|:DELETE DETAIL OF TRAIN        |")
        print("-----------------------------------")
        print("|4|:SHOW DETAILS OF TRAINS        |")
        print("-----------------------------------")
        print("|5|:EXIT                          |")
        print("-----------------------------------")
        ch=int(input("ENTER YOUR CHOICE"))
        if ch==1:
            insert_data()
        elif ch==2:
            update_train()
        elif ch==3:
            delete_train()
        elif ch==4:
            show_data()
        elif ch==5:
            break
def menu_user():
    while True:
        print("---------------MENU----------------")
        print("|1|:SHOW THE TRAIN DETAILS        |")
        print("-----------------------------------")
        print("|2|:RESERVATION OF TRAIN          |")
        print("-----------------------------------")
        print("|3|:CANCELLATION OF TRAIN         |")
        print("-----------------------------------")
        print("|4|:EXIT                          |")
        print("-----------------------------------")
        ch=int(input("enter ur choice"))
        if ch==1:
            show_data()
        elif ch==2:
            reservation()
        elif ch==3:
            cancellation()
        elif ch==4:
            break
        else:
            print("INVALID ENTRY")
            print("TRY AGAIN")
            menu_user()
        
def admin():
    print("++++++++++++++++++++++++++++")
    print("+ PRESS 1 FOR ADMIN        +")
    print("++++++++++++++++++++++++++++")
    print("+ PRESS 2 FOR USER         +")
    print("++++++++++++++++++++++++++++")
    print("+ PRESS 0 FOR EXIT         +")
    print("++++++++++++++++++++++++++++")
    ch=int(input("ENTER YOUR CHOICE"))
    if ch==1:
       p=input("ENTER UR PASSWARD")
       if p=="IR1234":
          menu_adm()
       else:
           print("INVALID PASSWORD")
           admin()
    elif ch==2:
         menu_user()
    elif ch==0:
        print("THANK YOU")
    else:
        print("INVALID ENTRY")
        print("TRY AGAIN")
        admin()
intro_fun()
admin()


