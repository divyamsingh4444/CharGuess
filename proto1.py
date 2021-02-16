# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:06 2021

@author: divya
"""

import tkinter as tk
from tkinter import messagebox
import random
import csv

chrs=[' ! ', ' ~ ', ' @ ', ' # ',
      ' $ ', ' % ', ' ^ ', ' & ',
      ' * ', ' — ', ' + ', ' = ',
      ' π ', ' ∞ ', ' √ ', ' Ø ',
      ' ¤ ', ' ʃ ', ' α ', ' ϴ ']
usernames=[]
highscore_dict={}

def register():
    global register_window, register_username_entry, register_password_entry
    
    register_window=tk.Tk()
    register_window.title("Register")
    register_window.iconbitmap("CharGuess icon 2.ico")
    
    register_title=tk.Label(register_window, text="Register Window", font=('Arial', 40))
    register_title.pack(fill="x", pady=5)

    instructions=tk.Label(register_window, text="Please enter details below to register")
    instructions.pack()

    register_username_label=tk.Label(register_window, font=('Arial'), text="Username * ")
    register_username_label.pack(pady=5)
    
    register_username_entry=tk.Entry(register_window, font=('Arial'))
    register_username_entry.pack(pady=5, padx=5)
    
    register_password_label=tk.Label(register_window, font=('Arial'), text="Password * ")
    register_password_label.pack(pady=5)

    register_password_entry=tk.Entry(register_window, font=('Arial'), show='*')
    register_password_entry.pack(pady=5, padx=5)
    
    register_ok_button=tk.Button(register_window, font=('Arial'), text="Register", width=10, command=lambda: register_user())
    register_ok_button.pack(pady=5)
    
    register_window.mainloop()

def login():
    global login_window, login_username_entry, login_password_entry
    
    login_window=tk.Tk()
    login_window.title("Login")
    login_window.iconbitmap("CharGuess icon 2.ico")

    login_title=tk.Label(login_window, text="Login Window", font=('Arial', 40))
    login_title.pack(fill="x", pady=5)

    instructions=tk.Label(login_window, text="Please enter details below to login")
    instructions.pack()

    login_username_label=tk.Label(login_window, font=('Arial'), text="Username * ")
    login_username_label.pack(pady=5)
    
    login_username_entry=tk.Entry(login_window, font=('Arial'))
    login_username_entry.pack(pady=5, padx=5)
    
    login_password_label=tk.Label(login_window, font=('Arial'), text="Password * ")
    login_password_label.pack(pady=5)

    login_password_entry=tk.Entry(login_window, font=('Arial'), show= '*')
    login_password_entry.pack(pady=5, padx=5)
    
    login_ok_button=tk.Button(login_window, font=('Arial'), text="Login", width=10,
                              command=lambda: login_verify( login_username_entry.get(), login_password_entry.get() ))
    login_ok_button.pack(pady=5)
    
    login_window.mainloop()

def register_user():
    global register_window, register_username_entry, register_password_entry, highscore_dict
    username_info = register_username_entry.get()
    password_info = register_password_entry.get()

    with open('username_password.csv', 'a', newline='') as csvfile:
        accountwriter=csv.writer(csvfile, delimiter=',')
        accountwriter.writerow([username_info, password_info])
        
    with open('highscores.csv', 'a', newline='') as hsfile:
        hswriter=csv.writer(hsfile, delimiter=",")
        hswriter.writerow([username_info, 0.0])
        
    register_username_entry.delete(0, tk.END)
    register_password_entry.delete(0, tk.END)
 
    success_message=tk.Label(register_window, text="Registration Success", fg="green", font=("calibri", 11))
    success_message.pack()

def login_verify(username, password):
    global usernames, current_username
    passwords=[]
    
    current_username=username
    
    with open('username_password.csv') as csvfile:
        user_reader=csv.reader(csvfile, delimiter=',')
        for row in user_reader:
            usernames.append(row[0])
    with open('username_password.csv') as csvfile:
        password_reader=csv.reader(csvfile, delimiter=',')
        for row in password_reader:
            passwords.append(row[1])
    
    if username in usernames:
        if password in passwords:
            login_success()
        else:
            invalid_password()
    else:
        user_not_found()

def login_success():
    global login_success_window, current_username
    login_success_window=tk.Toplevel(login_window)
    login_success_window.title("Success")
    login_success_window.geometry("150x100")
    success_message=tk.Label(login_success_window, text="Login Success \nWelcome"+current_username)
    success_message.pack()
    login_success_ok_button=tk.Button(login_success_window, text="OK", command=delete_login_success)
    login_success_ok_button.pack()

def invalid_password():
    global invalid_password_window, login_username_entry, login_password_entry
    invalid_password_window=tk.Toplevel(login_window)
    invalid_password_window.title("Success")
    invalid_password_window.geometry("150x100")
    invalid_message=tk.Label(invalid_password_window, text="Invalid Password")
    invalid_message.pack()
    
    invalid_password_ok_button=tk.Button(invalid_password_window, text="OK", command=delete_invalid_password_window)
    invalid_password_ok_button.pack()
    
    login_username_entry.delete(0, tk.END)
    login_password_entry.delete(0, tk.END)

def user_not_found():
    global user_not_found_screen
    user_not_found_screen=tk.Toplevel(login_window)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    user_not_found_message=tk.Label(user_not_found_screen, text="User Not Found")
    user_not_found_message.pack()
    user_not_found_ok_button=tk.Button(user_not_found_screen, text="OK", command=lambda: delete_user_not_found_screen)
    user_not_found_ok_button.pack()

def delete_login_success():
    global account_window, gamemode, highscore_dict
    login_window.destroy()
    account_window.destroy()
    
    with open('highscores.csv', 'r', newline="") as hsfile:
        hsreader=csv.reader(hsfile, delimiter=',')
        for row in hsreader:
            if row[0]!="username":
                highscore_dict[row[0]]=row[1]
    
    if gamemode=="single_player":
        single_player_settings()
    else:
        game_intro_screen()
    
def delete_invalid_password_window():
    global invalid_password_window
    invalid_password_window.destroy()
  
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def account_screen():
    global account_window
    
    account_window=tk.Tk()
    account_window.state("zoomed")
    account_window.title("CharGuess!")
    account_window.geometry("600x350")
    account_window.configure(bg="SeaGreen2")
    account_window.iconbitmap("CharGuess icon 2.ico")
    
    Choice_Label=tk.Label(account_window, text="Select Your Choice", bg="turquoise2", width="300", font=("Calibri", 75, 'bold'))
    Choice_Label.pack(pady=5)
    
    Login_Button=tk.Button(account_window, text="Login", height="2", width="30", font=("Arial", 30, 'bold'), bg="orchid2", command = login)
    Login_Button.pack(pady=10)
    
    Register_Button=tk.Button(account_window, text="Register", height="2", width="30", font=("Arial", 30, 'bold'), bg="orchid2", command=register)
    Register_Button.pack(pady=10)
    
    back_to_intro_screen=tk.Button(account_window, text="Back To Main Menu", font=("Arial", 30, 'bold'), bg="gold", command=lambda: back_to_main_menu())
    back_to_intro_screen.pack(pady=5)
    
    account_window.mainloop()

def back_to_main_menu():
    account_window.destroy()
    game_intro_screen()

#####################################################################################################################################################

def gotologin_and_chardestroy():
    global gamemode
    gamemode="single_player"
    charguess.destroy()
    account_screen()
    
def single_player_settings():
    global chrs, attempts_entry, chr_choice_entry, single_player_window, attempts_label, chr_choice_label, ok_button, warning_label, attempts_choice, chr_choice
    
    single_player_window=tk.Tk()
    single_player_window.title('Single Player Mode')
    single_player_window.state('zoomed')
    single_player_window.configure(bg="VioletRed3")
    single_player_window.iconbitmap("CharGuess icon 2.ico")
    
    header=tk.Label(single_player_window, text="Single Player Mode", font=('Impact', 80), bg="chocolate1")
    header.pack(fill="x", pady=10)
    
    attempts_label=tk.Label(single_player_window, text="How many attempts do you want? (4-15) :", font=('Arial', 25), bg="VioletRed3")
    attempts_label.pack(anchor='center', pady=5)
    attempts_entry=tk.Entry(single_player_window, fg="VioletRed3", font=('Arial', 22))
    attempts_entry.pack(anchor='center', pady=5)
    
    chr_choice_label=tk.Label(single_player_window, text="How many characters do you want? (4-10) :", font=('Arial', 25), bg="VioletRed3")
    chr_choice_label.pack(anchor='center', pady=5)
    chr_choice_entry=tk.Entry(single_player_window, fg="VioletRed3", font=('Arial', 22))
    chr_choice_entry.pack(anchor='center', pady=5)
    
    note_label=tk.Label(single_player_window, text="Note: Number of attempts must be greater than number of characters.", fg="gray54", font=('Arial', 15))
    note_label.pack(pady=10)
    
    ok_button=tk.Button(single_player_window, text="OK", font=('Arial', 25),
                        command=lambda: ok_button_single_player_choice(), bg="medium spring green")
    ok_button.pack(anchor='center', pady=15)
    
    go_back=tk.Button(single_player_window, text="Go Back To Main Menu", font=("Arial", 25, "bold"),
                      command=lambda: goback_main_menu_from_sps(), bg="gold")
    go_back.pack(anchor='center', pady=5)
    
    single_player_window.mainloop()
    
def goback_main_menu_from_sps():
    global single_player_window
    single_player_window.destroy()
    game_intro_screen()
    
def ok_button_single_player_choice():
    
    global attempts_entry, chr_choice_entry, single_player_window, ok_button, warning_label, attempts_choice, chr_choice
    
    attempts_choice=(attempts_entry.get())
    chr_choice=(chr_choice_entry.get())
    L1=[x for x in range(4,16)]
    L2=[y for y in range(4,11)]
    
    if attempts_choice.isdigit() and chr_choice.isdigit() and (int(attempts_choice) in L1) and (int(chr_choice) in L2) and (int(attempts_choice)>=int(chr_choice)):
        single_player_window.destroy()
        single_player_game()
        
    else:
        messagebox.showinfo("Title", "Input invalid.")
        attempts_entry.delete(0, tk.END)
        chr_choice_entry.delete(0, tk.END)        
    
def single_player_game():
    
    global sp_gamewindow, attempts_choice, chr_choice
    global single_player_window, chrs, random_chrs, discovered_chrs
    global reveal_frame, rp_frame, reveal_dict, chr_button_dict
    global attempts_tillnow, success, failure
    global status1, status2, status3, gamemode
        
    sp_gamewindow=tk.Tk()
    sp_gamewindow.state("zoomed")
    sp_gamewindow.title("CharGuess")
    sp_gamewindow.configure(bg="DeepSkyBlue2")
    sp_gamewindow.iconbitmap("CharGuess icon 2.ico")
    
    header=tk.Label(sp_gamewindow, text="CharGuess", font=("Impact", 80, "bold"), bg="PaleVioletRed1")
    header.pack(fill="x")
    
    rp_frame=tk.Frame(sp_gamewindow, bg="DeepSkyBlue2")
    rp_frame.pack(anchor="center")
    
    reveal_frame=tk.Frame(rp_frame, bg="DeepSkyBlue2")
    reveal_frame.pack(anchor="center", ipady=25)
    
    attempts_choice=int(attempts_choice)
    chr_choice=int(chr_choice)
    attempts_tillnow=0
    success=0
    failure=0
    
    random_chrs=random.sample(chrs, chr_choice)
    discovered_chrs=[" ? " for x in range(chr_choice)]
    
    reveal_dict={'reveal_label%s'%x : tk.Label(reveal_frame, text=" ? ", font=('Arial Black', 40, 'bold'), relief="raised") for x in range(chr_choice)}
    
    for x in reveal_dict:
        reveal_dict[x].pack(side="left", padx=10, pady=10)
    
    chr_frame=tk.Frame(sp_gamewindow, bg="DeepSkyBlue2")
    chr_frame.pack(anchor="center", pady=20)
    chr_button_dict={}
    
    for x in range(len(chrs)):
        chr_button_dict[chrs[x]]=tk.Button(chr_frame, text=chrs[x], font=('Arial', 19, 'bold'), fg="DarkOrchid3", command=lambda j=chrs[x]: character_clicked(j))
        
    for x in chr_button_dict:
        chr_button_dict[x].pack(side="left", padx=4, pady=5)
    
    play_again=tk.Button(sp_gamewindow, text="Play Again", font=("Arial", 27, "bold"),
                         command=lambda: play_single_player_again(), bg="medium spring green")
    play_again.pack(anchor='center', pady=15)

    back_to_sp_settings=tk.Button(sp_gamewindow, text="Back To Settings", font=("Arial", 27, "bold"),
                                  command=lambda: backto_sps_and_spgame_destroy(), bg="gold")
    back_to_sp_settings.pack(anchor='center', pady=10)
    
    status_bar=tk.Frame(sp_gamewindow, borderwidth=4, relief="raised", bg="PaleVioletRed2")
    status_bar.pack(side="bottom", fill="x", expand=1, anchor="s")
    
    status1=tk.Label(status_bar, text="Total attempts: "+str(attempts_choice),
                     borderwidth=2, font=("Arial", 24), bg="PaleVioletRed2")
    status1.pack(side="left", fill="x", padx=5, expand=1)
    
    status2=tk.Label(status_bar, text="Attempts Remaining: "+str(attempts_choice-attempts_tillnow)+"/"+str(attempts_choice),
                     borderwidth=2, font=("Arial", 24), bg="PaleVioletRed2")
    status2.pack(side="left", fill="x", padx=5, expand=1)
    
    status3=tk.Label(status_bar, text="Successful attempts: "+str(success)+"/"+str(attempts_choice),
                     borderwidth=2, font=("Arial", 24), bg="PaleVioletRed2")
    status3.pack(side="left", fill="x", padx=5, expand=1)
    
    
    sp_gamewindow.mainloop()

def play_single_player_again():
    global sp_gamewindow, score, success, failure, attempts_tillnow
    success=0
    failure=0
    attempts_tillnow=0
    score=0
    sp_gamewindow.destroy()
    single_player_game()

def backto_sps_and_spgame_destroy():
    sp_gamewindow.destroy()
    go_back_sp_settings()
    
def go_back_sp_settings():
    global sp_gamewindow
    single_player_settings()

##########################################################################################################################################################

def character_clicked(st):
    global random_chrs, reveal_frame, discovered_chrs, rp_frame
    global reveal_dict, chr_button_dict, attempts_tillnow
    global attempts_choice, failure, success
    global status1, status2, status3, score
    global highscore_dict, current_username, gamemode
        
    attempts_tillnow+=1
    
    color="firebrick1"
    
    if " ? " in discovered_chrs:
        if st in random_chrs:
            color="chartreuse"
            success+=1

            discovered_chrs.remove(" ? ")
            discovered_chrs.insert(random.randint(0, len(discovered_chrs)), st)

            for k in range(len(discovered_chrs)):
                reveal_dict['reveal_label%s'%k].configure(text=discovered_chrs[k])
                if discovered_chrs[k]!=" ? ":
                    reveal_dict['reveal_label%s'%k].configure(bg="cyan2")

        chr_button_dict[st].configure(state='disabled')
        chr_button_dict[st].configure(bg=color)
    
    failure=attempts_tillnow-success
    
    if success==len(random_chrs):
        messagebox.showinfo("GAME OVER", "Result: \nSuccess = "+str(success)+"\nFailure = "+str(failure)+"\nScore = "+str((success/attempts_tillnow)*100))
        score=(success/attempts_tillnow)*100
        
        if score>=float(highscore_dict[current_username]):
            highscore_dict[current_username]=(score)
    
        with open("highscores.csv", "w", newline="") as hsfile:
            hsdwriter=csv.writer(hsfile, delimiter=",")
            for m in highscore_dict:
                hsdwriter.writerow([m, highscore_dict[m]])
        
        for h in chr_button_dict:
            chr_button_dict[h].configure(state='disabled')
        
    elif attempts_tillnow==attempts_choice:
        messagebox.showinfo("GAME OVER", "Result: \nSuccess = "+str(success)+"\nFailure = "+str(failure)+"\nScore = "+str((success/attempts_tillnow)*100))
        
        score=(success/attempts_tillnow)*100
        
        if gamemode=="single_player":
            if score>=float(highscore_dict[current_username]):
                highscore_dict[current_username]=(score)
        
            with open("highscores.csv", "w", newline="") as hsfile:
                hsdwriter=csv.writer(hsfile, delimiter=",")
                for m in highscore_dict:
                    hsdwriter.writerow([m, highscore_dict[m]])
        
        for h in chr_button_dict:
            chr_button_dict[h].configure(state='disabled')
    
    score=(success/attempts_tillnow)*100
    
    # if score>=float(highscore_dict[current_username]):
    #     highscore_dict[current_username]=(score)
    
    # with open("highscores.csv", "w", newline="") as hsfile:
    #     hsdwriter=csv.writer(hsfile, delimiter=",")
    #     for m in highscore_dict:
    #         hsdwriter.writerow([m, highscore_dict[m]])
            
    # with open('highscores.csv', 'w', newline='') as hsfile:
    #     hsdwriter=csv.DictWriter(hsfile, delimiter=',', fieldnames=['username','highscore'])
    #     sorted_d = dict( sorted(highscore_dict.items(), key=operator.itemgetter(1),reverse=True))
    #     hsdwriter.writerows(sorted_d)
            
    # print(st)
    # print(random_chrs)
    # print(discovered_chrs)
    # print("\n")
    # print("attempts_tillnow =", attempts_tillnow)
    # print("attempts_choice = ", attempts_choice)
    
    status1.configure(text="Total attempts: "+str(attempts_choice))
    status2.configure(text="Attempts Remaining: "+str(attempts_choice-attempts_tillnow)+"/"+str(attempts_choice))
    status3.configure(text="Successful attempts: "+str(success)+"/"+str(attempts_choice))
    
######################################################################################################################################################

def dps_and_chardestroy():
    charguess.destroy()
    double_player_settings()
    
def double_player_settings():
    global chrs, attempts_entry, chr_choice_entry, double_player_window, attempts_label, chr_choice_label, ok_button, warning_label, attempts_choice, chr_choice, player1_name_entry, player2_name_entry
    
    double_player_window=tk.Tk()
    double_player_window.title('Double Player Mode')
    double_player_window.state('zoomed')
    double_player_window.configure(bg="VioletRed3")
    double_player_window.iconbitmap("CharGuess icon 2.ico")
    
    header=tk.Label(double_player_window, text="Double Player Mode", bg="chocolate1", font=('Impact', 70))
    header.pack(fill="x", pady=5)
    
    player1_name_label=tk.Label(double_player_window, text="Name of Player 1: ", font=('Arial', 25), bg="VioletRed3")
    player1_name_label.pack(anchor='center', pady=3)
    player1_name_entry=tk.Entry(double_player_window, font=('Arial', 20), fg="VioletRed3")
    player1_name_entry.pack(anchor='center', pady=3)

    player2_name_label=tk.Label(double_player_window, text="Name of Player 2: ", font=('Arial', 25), bg="VioletRed3")
    player2_name_label.pack(anchor='center', pady=3)    
    player2_name_entry=tk.Entry(double_player_window, font=('Arial', 20), fg="VioletRed3")
    player2_name_entry.pack(anchor='center', pady=3)
    
    attempts_label=tk.Label(double_player_window, text="How many attempts do you want? (4-15): ", font=('Arial', 25), bg="VioletRed3")
    attempts_label.pack(anchor='center', pady=3)
    attempts_entry=tk.Entry(double_player_window, font=('Arial', 20), fg="VioletRed3")
    attempts_entry.pack(anchor='center', pady=3)
    
    chr_choice_label=tk.Label(double_player_window, text="How many characters do you want? (4-10): ", font=('Arial', 25), bg="VioletRed3")
    chr_choice_label.pack(anchor='center', pady=3)
    chr_choice_entry=tk.Entry(double_player_window, font=('Arial', 20), fg="VioletRed3")
    chr_choice_entry.pack(anchor='center', pady=3)
    
    note_label=tk.Label(double_player_window, text="Note: Number of attempts must be greater than number of characters.", fg="gray54", font=('Arial', 13))
    note_label.pack(pady=3)
    
    ok_button=tk.Button(double_player_window, text="OK", font=('Arial', 20), bg="medium spring green", command=lambda: ok_button_double_player_choice())
    ok_button.pack(anchor='center', pady=3)
    
    go_back=tk.Button(double_player_window, text="Go Back To Main Menu", font=("Arial", 18, "bold"), bg="gold", command=lambda: goback_main_menu_from_dps())
    go_back.pack(anchor='center', pady=6)
    
    double_player_window.mainloop()

def goback_main_menu_from_dps():
    global double_player_window
    double_player_window.destroy()
    game_intro_screen()

def ok_button_double_player_choice():
    global ok_button, warning_label, attempts_choice, chr_choice, gameplayer1, gameplayer2, gameplayerlist
    
    attempts_choice=(attempts_entry.get())
    chr_choice=(chr_choice_entry.get())
    L1=[x for x in range(4,16)]
    L2=[y for y in range(4,11)]
    
    playerlist=[player1_name_entry.get(), player2_name_entry.get()]
    
    gameplayer1=random.choice(playerlist)
    gameplayer2=random.choice([ele for ele in playerlist if ele!=gameplayer1])
    gameplayerlist=[gameplayer1, gameplayer2]
    
    if attempts_choice.isdigit() and chr_choice.isdigit() and (int(attempts_choice) in L1) and (int(chr_choice) in L2) and (int(attempts_choice)>=int(chr_choice)):
        messagebox.showinfo("Player Order", "Gameplayer 1: " + gameplayer1 + "\nGameplayer 2: " + gameplayer2)
        double_player_window.destroy()
        double_player_game()
        
    else:
        messagebox.showinfo("Title", "Input invalid.")
        attempts_entry.delete(0, tk.END)
        chr_choice_entry.delete(0, tk.END)       

def double_player_game():
    global dp_gamewindow, attempts_choice, chr_choice
    global game1, gameplayer1, reveal_frame1, random_chrs1, reveal_dict1, chr_frame1, chr_button_dict1, discovered_chrs1, attempts_tillnow1, success1, failure1
    global game2, gameplayer2, reveal_frame2, random_chrs2, reveal_dict2, chr_frame2, chr_button_dict2, discovered_chrs2, attempts_tillnow2, success2, failure2
    global status1_2, status1_4, status1_5, status2_2, status2_4, status2_5
    
    attempts_choice=int(attempts_choice)
    chr_choice=int(chr_choice)
    attempts_tillnow1=0
    success1=0
    failure1=0
    score1=0
    
    attempts_tillnow2=0
    success2=0
    failure2=0
    score2=0
    
    dp_gamewindow=tk.Tk()
    dp_gamewindow.state("zoomed")
    dp_gamewindow.config(bg="DeepSkyBlue2")
    dp_gamewindow.iconbitmap("CharGuess icon 2.ico")
    
    header=tk.Label(dp_gamewindow, text="CharGuess", font=("Impact", 75, "bold"), bg="PaleVioletRed1")
    header.pack(fill="x")
    
    game1=tk.Frame(dp_gamewindow)
    
    rp_frame1=tk.Frame(dp_gamewindow, bg="DeepSkyBlue2")
    rp_frame1.pack(anchor="center")
    
    game_player_label1=tk.Label(rp_frame1, text="Player 1: " + gameplayer1, font=("Arial", 20), bg="DeepSkyBlue2")
    game_player_label1.pack()
    
    reveal_frame1=tk.Frame(rp_frame1, bg="DeepSkyBlue2")
    reveal_frame1.pack(anchor="center", pady=3)
    
    random_chrs1=random.sample(chrs, chr_choice)
    discovered_chrs1=[" ? " for x in range(chr_choice)]
    reveal_dict1={'reveal_label%s'%x : tk.Label(reveal_frame1, text=" ? ", font=('Arial Black', 40, 'bold'), relief="raised") for x in range(chr_choice)}
    
    for x in reveal_dict1:
        reveal_dict1[x].pack(side="left", padx=10, pady=0)
    
    chr_frame1=tk.Frame(dp_gamewindow, bg="DeepSkyBlue2")
    chr_frame1.pack(anchor="center")
    chr_button_dict1={}
    
    for x in range(len(chrs)):
        chr_button_dict1[chrs[x]]=tk.Button(chr_frame1, text=chrs[x], font=('Arial', 18, 'bold'), fg="DarkOrchid3", command=lambda j=chrs[x]: dp_cc1(j))
        
    for x in chr_button_dict1:
        chr_button_dict1[x].pack(side="left", padx=4, pady=5)
        
    game1.pack(anchor="center", pady=0)
    
    
    
    game2=tk.Frame(dp_gamewindow)
    
    rp_frame2=tk.Frame(dp_gamewindow, bg="DeepSkyBlue2")
    rp_frame2.pack(anchor="center")
    
    game_player_label2=tk.Label(rp_frame2, text="Player 2: " + gameplayer2, font=("Arial", 20), bg="DeepSkyBlue2")
    game_player_label2.pack()
    
    reveal_frame2=tk.Frame(rp_frame2, bg="DeepSkyBlue2")
    reveal_frame2.pack(anchor="center", pady=3)
    
    random_chrs2=random.sample(chrs, chr_choice)
    discovered_chrs2=[" ? " for x in range(chr_choice)]
    reveal_dict2={'reveal_label%s'%x : tk.Label(reveal_frame2, text=" ? ", font=('Arial Black', 40, 'bold'), relief="raised") for x in range(chr_choice)}
    
    for x in reveal_dict2:
        reveal_dict2[x].pack(side="left", padx=10, pady=0)
    
    chr_frame2=tk.Frame(dp_gamewindow, bg="DeepSkyBlue2")
    chr_frame2.pack(anchor="center")
    chr_button_dict2={}
    
    for x in range(len(chrs)):
        chr_button_dict2[chrs[x]]=tk.Button(chr_frame2, text=chrs[x], font=('Arial', 18, 'bold'), fg="DarkOrchid3", command=lambda j=chrs[x]: dp_cc2(j))
        
    for x in chr_button_dict2:
        chr_button_dict2[x].pack(side="left", padx=4, pady=5)
    
    status_bar1=tk.Frame(dp_gamewindow, borderwidth=4, relief="raised", bg="PaleVioletRed1")
    status_bar1.pack(side="left", fill="x", expand=1, padx=5)
    
    status1_1=tk.Label(status_bar1, text="Player 1: " + gameplayer1, borderwidth=2, font=('Arial', 25), bg="PaleVioletRed1")
    status1_1.pack(fill="x", padx=5)
    
    status1_2=tk.Label(status_bar1, text="Score: " + str(score1), borderwidth=2, font=17, bg="PaleVioletRed1")
    status1_2.pack(fill="x", padx=5)
    
    status1_3=tk.Label(status_bar1, text="Total attempts: " + str(attempts_choice), borderwidth=2, font=17, bg="PaleVioletRed1")
    status1_3.pack(fill="x", padx=5)
    
    status1_4=tk.Label(status_bar1, text="Attempts Remaining: " + str(attempts_choice - attempts_tillnow1) + " / " + str(attempts_choice),
                       bg="PaleVioletRed1", borderwidth=2, font=17)
    status1_4.pack(fill="x", padx=5)
    
    status1_5=tk.Label(status_bar1, text="Successful Attempts: " + str(success1) + " / " + str(attempts_choice),
                       bg="PaleVioletRed1", borderwidth=2, font=17)
    status1_5.pack(fill="x", padx=5)
    
    
    Buttons_Frame=tk.Frame(dp_gamewindow, bg="DeepSkyBlue2")
    Buttons_Frame.pack(side="left", fill="x", expand=1)
    
    play_again=tk.Button(Buttons_Frame, text="Play Again", font=("Arial", 20, "bold"), command=lambda: play_double_player_again(), bg="medium spring green")
    play_again.pack(anchor='center', pady=6)
    
    back_to_dp_settings=tk.Button(Buttons_Frame, text="Back To Settings", font=("Arial", 20, "bold"), command=lambda: backto_dps_and_dpgame_destroy(), bg="gold")
    back_to_dp_settings.pack(anchor='center', pady=6)
    
    
    status_bar2=tk.Frame(dp_gamewindow, borderwidth=4, relief="raised", bg="PaleVioletRed1")
    status_bar2.pack(side="left", fill="x", expand=1, padx=5)
    
    status2_1=tk.Label(status_bar2, text="Player 2: " + gameplayer2, borderwidth=2, font=('Arial', 25), bg="PaleVioletRed1")
    status2_1.pack(fill="x", padx=5)
    
    status2_2=tk.Label(status_bar2, text="Score: " + str(score2), borderwidth=2, font=17, bg="PaleVioletRed1")
    status2_2.pack(fill="x", padx=5)
    
    status2_3=tk.Label(status_bar2, text="Total attempts: " + str(attempts_choice), borderwidth=2, font=17, bg="PaleVioletRed1")
    status2_3.pack(fill="x", padx=5)
    
    status2_4=tk.Label(status_bar2, text="Attempts Remaining: " + str(attempts_choice - attempts_tillnow2) + " / " + str(attempts_choice),
                       bg="PaleVioletRed1", borderwidth=2, font=17)
    status2_4.pack(fill="x", padx=5)

    status2_5=tk.Label(status_bar2, text="Successful Attempts: " + str(success2) + " / " + str(attempts_choice),
                       borderwidth=2, font=17, bg="PaleVioletRed1")
    status2_5.pack(fill="x", padx=5)

    dp_gamewindow.mainloop()

def dp_cc1(st):
    global game1, reveal_frame1, random_chrs1, reveal_dict1, chr_frame1, chr_button_dict1, discovered_chrs1, attempts_tillnow1, success1, failure1, score1, gameplayer1
    global attempts_choice, chr_choice
    global game2
    global status1_2, status1_4, status1_5, status2_2, status2_4, status2_5
    global game1over, game2over
    
    attempts_tillnow1+=1
    color="firebrick1"
    
    if " ? " in discovered_chrs1:
        if st in random_chrs1:
            color="chartreuse"
            success1+=1
            discovered_chrs1.remove(" ? ")
            discovered_chrs1.insert(random.randint(0, len(discovered_chrs1)), st)

            for k in range(len(discovered_chrs1)):
                reveal_dict1['reveal_label%s'%k].configure(text=discovered_chrs1[k])
                if discovered_chrs1[k]!=" ? ":
                    reveal_dict1['reveal_label%s'%k].configure(bg="cyan2")
        chr_button_dict1[st].configure(state='disabled')
        chr_button_dict1[st].configure(bg=color)
    failure1=attempts_tillnow1-success1
    
    if success1==len(random_chrs1):
        score1=(success1/attempts_tillnow1)*100
        messagebox.showinfo("GAME OVER", "Result: \nSuccess = " + str(success1) + "\nFailure = " + str(failure1) + "\nScore = " + str(score1))
        game1over=True
        
        for h in chr_button_dict1:
            chr_button_dict1[h].configure(state='disabled')
        game2.pack(anchor="center", pady=20)
        
        if game1over==True and game2over==True:
            if score1 > score2:
                messagebox.showinfo("GAME OVER", "Result: \n"+gameplayer1+" wins!")
            elif score1 < score2:
                messagebox.showinfo("GAME OVER", "Result: \n"+gameplayer2+" wins!")
            elif score1==score2:
                messagebox.showinfo("GAME OVER", "Result: \nMatch Tied!")
        
    elif attempts_tillnow1==attempts_choice:
        score1=(success1/attempts_tillnow1)*100
        messagebox.showinfo("GAME OVER", "Result: \nSuccess = " + str(success1) + "\nFailure = " + str(failure1) + "\nScore = " + str(score1))
        game1over=True
        
        for h in chr_button_dict1:
            chr_button_dict1[h].configure(state='disabled')
        game2.pack(anchor="center", pady=20)
        
        if game1over==True and game2over==True:
            if score1 > score2:
                messagebox.showinfo("GAME OVER", "Result: \n"+gameplayer1+" wins!")
            elif score1 < score2:
                messagebox.showinfo("GAME OVER", "Result: \n"+gameplayer2+" wins!")
            elif score1==score2:
                messagebox.showinfo("GAME OVER", "Result: \nMatch Tied!")
        
    score1=(success1/attempts_tillnow1)*100
            
    # print(st)
    # print(random_chrs1)
    # print(discovered_chrs1)
    # print("\n")
    # print("attempts_tillnow for " + gameplayer1 + ": ", attempts_tillnow1)
    # print("attempts_choice for both players: ", attempts_choice)
    
    status1_2.configure(text="Score: " + str(score1))
    status1_4.configure(text="Attempts Remaining: " + str(attempts_choice - attempts_tillnow1) + " / " + str(attempts_choice))
    status1_5.configure(text="Successful Attempts: " + str(success1) + " / " + str(attempts_choice))

def dp_cc2(st):
    global game2, reveal_frame2, random_chrs2, reveal_dict2, chr_frame2, chr_button_dict2, discovered_chrs2, attempts_tillnow2, success2, failure2, score2, gameplayer2
    global attempts_choice, chr_choice
    global status1_2, status1_4, status1_5, status2_2, status2_4, status2_5
    global game1over, game2over
    
    attempts_tillnow2+=1
    color="firebrick1"
    
    if " ? " in discovered_chrs2:
        if st in random_chrs2:
            color="chartreuse"
            success2+=1
            discovered_chrs2.remove(" ? ")
            discovered_chrs2.insert(random.randint(0, len(discovered_chrs2)), st)

            for k in range(len(discovered_chrs2)):
                reveal_dict2['reveal_label%s'%k].configure(text=discovered_chrs2[k])
                if discovered_chrs2[k]!=" ? ":
                    reveal_dict2['reveal_label%s'%k].configure(bg="cyan2")
        chr_button_dict2[st].configure(state='disabled')
        chr_button_dict2[st].configure(bg=color)
    failure2=attempts_tillnow2-success2
    
    if success2==len(random_chrs2):
        score2=(success2/attempts_tillnow2)*100
        messagebox.showinfo("GAME OVER", "Result: \nSuccess = " + str(success2) + "\nFailure = " + str(failure2) + "\nScore = " + str(score2))
        game2over=True
        
        for h in chr_button_dict2:
            chr_button_dict2[h].configure(state='disabled')
            
        if game1over==True and game2over==True:
            if score1 > score2:
                messagebox.showinfo("GAME OVER", "Result: \n"+gameplayer1+" wins!")
            elif score1 < score2:
                messagebox.showinfo("GAME OVER", "Result: \n"+gameplayer2+" wins!")
            elif score1==score2:
                messagebox.showinfo("GAME OVER", "Result: \nMatch Tied!")
        
    elif attempts_tillnow2==attempts_choice:
        score2=(success1/attempts_tillnow2)*100
        messagebox.showinfo("GAME OVER", "Result: \nSuccess = " + str(success2) + "\nFailure = " + str(failure2) + "\nScore = " + str(score2))
        game2over=True
        
        for h in chr_button_dict2:
            chr_button_dict2[h].configure(state='disabled')
            
        if game1over==True and game2over==True:
            if score1 > score2:
                messagebox.showinfo("GAME OVER", "Result: \n"+gameplayer1+" wins!")
            elif score1 < score2:
                messagebox.showinfo("GAME OVER", "Result: \n"+gameplayer2+" wins!")
            elif score1==score2:
                messagebox.showinfo("GAME OVER", "Result: \nMatch Tied!")
            
    score2=(success2/attempts_tillnow2)*100
            
    # print(st)
    # print(random_chrs2)
    # print(discovered_chrs2)
    # print("\n")
    # print("attempts_tillnow for " + gameplayer2 + ":", attempts_tillnow1)
    # print("attempts_choice for both players: ", attempts_choice)
    
    status2_2.configure(text="Score: " + str(score2))
    status2_4.configure(text="Attempts Remaining: " + str(attempts_choice - attempts_tillnow2) + " / " + str(attempts_choice))
    status2_5.configure(text="Successful Attempts: " + str(success2) + " / " + str(attempts_choice))

def play_double_player_again():
    global dp_gamewindow, game1over, game2over, score1, score2, success1, success2, failure1, failure2, attempts_tillnow1, attempts_tillnow2
    success1, success2= 0,0
    failure1, failure2= 0,0
    attempts_tillnow1, attempts_tillnow2= 0,0
    game1over=False
    game2over=False
    score1=0
    score2=0
    dp_gamewindow.destroy()
    double_player_game()
    
def backto_dps_and_dpgame_destroy():
    dp_gamewindow.destroy()
    go_back_dp_settings()

def go_back_dp_settings():
    global dp_gamewindow
    double_player_settings()

######################################################################################################################################################

def ips_and_chardestroy():
    global gamemode
    charguess.destroy()
    gamemode="instant_player"
    instant_player_settings()
    
def instant_player_settings():
    global chrs, attempts_entry, chr_choice_entry, instant_player_window, attempts_label, chr_choice_label, ok_button, warning_label, attempts_choice, chr_choice
    
    instant_player_window=tk.Tk()
    instant_player_window.title('Instant Player Mode')
    instant_player_window.state('zoomed')
    instant_player_window.configure(bg="VioletRed3")
    instant_player_window.iconbitmap("CharGuess icon 2.ico")
    
    header=tk.Label(instant_player_window, text="Instant Player Mode", font=('Impact', 80), bg="chocolate1")
    header.pack(fill="x", pady=5)
    
    attempts_label=tk.Label(instant_player_window, text="How many attempts do you want? (4-15): ", font=('Arial', 25), bg="VioletRed3")
    attempts_label.pack(anchor='center', pady=5)
    attempts_entry=tk.Entry(instant_player_window, font=('Arial', 20), fg="VioletRed3")
    attempts_entry.pack(anchor='center', pady=5)
    
    chr_choice_label=tk.Label(instant_player_window, text="How many characters do you want? (4-10): ", font=('Arial', 25), bg="VioletRed3")
    chr_choice_label.pack(anchor='center', pady=5)
    chr_choice_entry=tk.Entry(instant_player_window, font=('Arial', 20), fg="VioletRed3")
    chr_choice_entry.pack(anchor='center', pady=5)
    
    note_label=tk.Label(instant_player_window, text="Note: Number of attempts must be greater than number of characters.", fg="gray54", font=('Arial', 15))
    note_label.pack(pady=10)
    
    ok_button=tk.Button(instant_player_window, text="Ok", font=('Arial', 26), command=lambda: ok_button_instant_player_choice(), bg="medium spring green")
    ok_button.pack(anchor='center', pady=5)
    
    go_back=tk.Button(instant_player_window, text="Go Back To Main Menu", font=("Arial", 25, "bold"), command=lambda: goback_main_menu_from_ips(), bg='gold')
    go_back.pack(anchor='center', pady=6)
    
    instant_player_window.mainloop()
    
def goback_main_menu_from_ips():
    global instant_player_window
    instant_player_window.destroy()
    game_intro_screen()
    
def ok_button_instant_player_choice():
    global attempts_entry, chr_choice_entry
    global instant_player_window, ok_button, warning_label
    global attempts_choice, chr_choice
    
    attempts_choice=(attempts_entry.get())
    chr_choice=(chr_choice_entry.get())
    L1=[x for x in range(4,16)]
    L2=[y for y in range(4,11)]
    
    if attempts_choice.isdigit() and chr_choice.isdigit() and\
        (int(attempts_choice) in L1) and (int(chr_choice) in L2) and\
            (int(attempts_choice)>=int(chr_choice)):
        instant_player_window.destroy()
        instant_player_game()
        
    else:
        messagebox.showinfo("Title", "Input invalid.")
        attempts_entry.delete(0, tk.END)
        chr_choice_entry.delete(0, tk.END)    
    
def instant_player_game():
    global ip_gamewindow, attempts_choice, chr_choice, single_player_window, chrs, random_chrs, discovered_chrs, reveal_frame, rp_frame, reveal_dict, chr_button_dict, attempts_tillnow, success, failure, status1, status2, status3
        
    ip_gamewindow=tk.Tk()
    ip_gamewindow.state("zoomed")
    ip_gamewindow.title("CharGuess!")
    ip_gamewindow.configure(bg="DeepSkyBlue2")
    ip_gamewindow.iconbitmap("CharGuess icon 2.ico")
    
    header=tk.Label(ip_gamewindow, text="CharGuess", font=("Impact", 80, "bold"), bg="Pale Violet Red2")
    header.pack(fill="x", pady=5)
    
    rp_frame=tk.Frame(ip_gamewindow, bg="DeepSkyBlue2")
    rp_frame.pack(anchor="center", pady=20)
    
    reveal_frame=tk.Frame(rp_frame, bg="DeepSkyBlue2")
    reveal_frame.pack(anchor="center")
    
    attempts_choice=int(attempts_choice)
    chr_choice=int(chr_choice)
    attempts_tillnow=0
    success=0
    failure=0
    
    random_chrs=random.sample(chrs, chr_choice)
    discovered_chrs=[" ? " for x in range(chr_choice)]
    
    reveal_dict={'reveal_label%s'%x : tk.Label(reveal_frame, text=" ? ", font=('Arial Black', 40, 'bold'), relief="raised") for x in range(chr_choice)}
    
    for x in reveal_dict:
        reveal_dict[x].pack(side="left", padx=10, pady=10)
    
    chr_frame=tk.Frame(ip_gamewindow, bg="DeepSkyBlue2")
    chr_frame.pack(anchor="center", pady=20)
    chr_button_dict={}
    
    for x in range(len(chrs)):
        chr_button_dict[chrs[x]]=tk.Button(chr_frame, text=chrs[x], font=('Arial', 18, 'bold'), fg="DarkOrchid3", command=lambda j=chrs[x]: character_clicked(j))
        
    for x in chr_button_dict:
        chr_button_dict[x].pack(side="left", padx=4, pady=5)
    
    play_again=tk.Button(ip_gamewindow, text="Play Again", font=("Arial", 22, "bold"),
                         command=lambda: play_instant_player_again(), bg="medium spring green")
    play_again.pack(anchor='center', pady=10)
    
    back_to_ip_settings=tk.Button(ip_gamewindow, text="Back To Settings", font=("Arial", 22, "bold"),
                                  command=lambda: backto_ips_and_ipgame_destroy(), bg="gold")
    back_to_ip_settings.pack(anchor='center', pady=10)
    
    status_bar=tk.Frame(ip_gamewindow, borderwidth=4, relief="raised", bg="Pale Violet Red2")
    status_bar.pack(side="bottom", fill="x", expand=1, anchor="s")
    
    status1=tk.Label(status_bar, text="Total attempts: "+str(attempts_choice), borderwidth=2, font=('Arial', 25), bg="Pale Violet Red2")
    status1.pack(side="left", fill="both", padx=5, expand=1)
    
    status2=tk.Label(status_bar, text="Attempts Remaining: "+str(attempts_choice-attempts_tillnow)+"/"+str(attempts_choice),
                     borderwidth=2, font=('Arial', 25), bg="Pale Violet Red2")
    status2.pack(side="left", fill="both", padx=5, expand=1)
    
    status3=tk.Label(status_bar, text="Successful attempts: "+str(success)+"/"+str(attempts_choice),
                     borderwidth=2, font=('Arial', 25), bg="Pale Violet Red2")
    status3.pack(side="left", fill="both", padx=5, expand=1)
    
    ip_gamewindow.mainloop()

def play_instant_player_again():
    global ip_gamewindow, score, success, failure, attempts_tillnow
    success=0
    failure=0
    attempts_tillnow=0
    score=0
    ip_gamewindow.destroy()
    instant_player_game()
    
def backto_ips_and_ipgame_destroy():
    ip_gamewindow.destroy()
    go_back_ip_settings()

def go_back_ip_settings():
    global ip_gamewindow
    instant_player_settings()

######################################################################################################################################################

def game_intro_screen():
    global charguess
    charguess=tk.Tk()
    
    charguess.title("CharGuess")
    charguess.config(bg="firebrick1")
    charguess.state("zoomed")    
    
    charguess.iconbitmap("CharGuess icon 2.ico")
    
    intro_label=tk.Label(charguess, text="Welcome To CharGuess!!", font=('Impact', 85), bg="RoyalBlue1")
    intro_label.pack( fill="x", pady=5)    
    
    Buttons_Frame=tk.Frame(charguess, bg="firebrick4")
    Buttons_Frame.pack(pady=0, ipadx=10)
    
    Player_Choice=tk.Label(Buttons_Frame, text="Playing Modes", font=("Arial", 40, 'bold'), bg="firebrick1")
    Player_Choice.pack(fill="x")
    
    Single_Player_Button=tk.Button(Buttons_Frame, text="Single Player", height=2, font=("Arial", 25, 'bold'), bg="dark turquoise",
                                   command=lambda: gotologin_and_chardestroy())
    Single_Player_Button.pack(padx=10, pady=4, fill="x")
    
    Double_Player_Button=tk.Button(Buttons_Frame, text="Double Player", height=2, font=("Arial", 25, 'bold'), bg="dark turquoise",
                                   command=lambda: dps_and_chardestroy())
    Double_Player_Button.pack(padx=10, pady=4, fill="x")
    
    Instant_Player_Button=tk.Button(Buttons_Frame, text="Instant Play", height=2, font=("Arial", 25, 'bold'), bg="dark turquoise",
                                    command=lambda: ips_and_chardestroy())
    Instant_Player_Button.pack(padx=10, pady=4, fill="x")
    
    Final_Exit=tk.Button(charguess, text="Exit", command=charguess.destroy, 
                         font=("Arial", 30, 'bold'), width=20, bg="gold")
    Final_Exit.pack(pady=5)

    charguess.mainloop()

game_intro_screen()