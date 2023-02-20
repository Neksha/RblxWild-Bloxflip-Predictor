#use server hash for rblxwild and round_id for bloxflip


import tkinter as tk #line:1
import random #line:2
import tkinter .colorchooser #line:3
import tkinter .messagebox #line:4
import tkinter .simpledialog #line:5
import webbrowser #line:6
#import Raient
class MinesPredictor :#line:8
    def __init__ (OO0OOOOO000O0OO0O ,O0O0OOO0OOOOOOOO0 ):#line:9
        OO0OOOOO000O0OO0O .master =O0O0OOO0OOOOOOOO0 #line:10
        OO0OOOOO000O0OO0O .master .title ("Mines Predictor")#line:11
        OO0OOOOO000O0OO0O .background_color ="white"#line:12
        OO0OOOOO000O0OO0O .grid_frame =tk .Frame (OO0OOOOO000O0OO0O .master ,bg =OO0OOOOO000O0OO0O .background_color )#line:14
        OO0OOOOO000O0OO0O .grid_frame .grid (row =0 ,column =0 ,padx =10 ,pady =10 )#line:15
        OO0OOOOO000O0OO0O .generate_button =tk .Button (OO0OOOOO000O0OO0O .master ,text ="Inject",command =OO0OOOOO000O0OO0O .generate_grid_with_input )#line:17
        OO0OOOOO000O0OO0O .generate_button .grid (row =1 ,column =0 ,pady =10 )#line:18
        OO0OOOOO000O0OO0O .customize_button =tk .Button (OO0OOOOO000O0OO0O .master ,text ="Customize",command =OO0OOOOO000O0OO0O .customize )#line:20
        OO0OOOOO000O0OO0O .customize_button .grid (row =2 ,column =0 ,pady =10 )#line:21
        OO0OOOOO000O0OO0O .home_button =tk .Button (OO0OOOOO000O0OO0O .master ,text ="Discord",command =OO0OOOOO000O0OO0O .go_home )#line:23
        OO0OOOOO000O0OO0O .home_button .grid (row =3 ,column =0 ,pady =10 )#line:24
    def generate_grid_with_input (OOOOOO0O0OO000O00 ):#line:26
        OOOO0O00OO0O00000 =tkinter .simpledialog .askstring ("Round ID","Enter round ID:")#line:27
        if OOOO0O00OO0O00000 is not None :#line:28
            if len (OOOO0O00OO0O00000 )<25 :#line:29
                tkinter .messagebox .showerror ("Error","Not a valid round ID. Please enter a round ID from rblxwild or bloxflip")#line:30
            else :#line:31
                OOOOOO0O0OO000O00 .generate_grid ()#line:32
    def generate_grid (OOO0O000OOOO00O0O ):#line:34
        OOO0O000OOOO00O0O .clear_grid ()#line:35
        OOO0O000OOOO00O0O .grid =[]#line:38
        for O00O0OO00000O0OOO in range (4 ):#line:39
            O0OO00OO0O00O0O0O =[]#line:40
            for O0OO0O0O0OO00OOOO in range (5 ):#line:41
                O00OOO000000000O0 =tk .Button (OOO0O000OOOO00O0O .grid_frame ,text ="❌",width =4 ,height =2 ,font =("Arial",16 ),command =lambda row =O00O0OO00000O0OOO ,col =O0OO0O0O0OO00OOOO :OOO0O000OOOO00O0O .check_cell (row ,col ))#line:42
                O00OOO000000000O0 .grid (row =O00O0OO00000O0OOO ,column =O0OO0O0O0OO00OOOO ,padx =2 ,pady =2 )#line:43
                O0OO00OO0O00O0O0O .append (O00OOO000000000O0 )#line:44
            OOO0O000OOOO00O0O .grid .append (O0OO00OO0O00O0O0O )#line:45
        for O00O0OO00000O0OOO in range (4 ):#line:48
            O0OO00OO0O00O0O0O =random .randint (0 ,3 )#line:50
            O00O00O000O00OO00 =random .randint (0 ,4 )#line:51
            OOO0O000OOOO00O0O .grid [O0OO00OO0O00O0O0O ][O00O00O000O00OO00 ].configure (text ="✅")#line:52
    def clear_grid (O0OOOO0OOO000OO0O ):#line:54
        if hasattr (O0OOOO0OOO000OO0O ,"grid"):#line:55
            for OO0OOOO000OO000O0 in O0OOOO0OOO000OO0O .grid :#line:56
                for OOO000O0O00O0OO0O in OO0OOOO000OO000O0 :#line:57
                    OOO000O0O00O0OO0O .destroy ()#line:58
    def customize (OO0O0O00OOOO0O0O0 ):#line:60
        O00O000000OOO00O0 =tk .colorchooser .askcolor ()[1 ]#line:61
        if O00O000000OOO00O0 :#line:62
            OO0O0O00OOOO0O0O0 .background_color =O00O000000OOO00O0 #line:63
            OO0O0O00OOOO0O0O0 .grid_frame .config (bg =OO0O0O00OOOO0O0O0 .background_color )#line:64
    def go_home (O0O000O0OOO00O000 ):#line:66
        webbrowser .open ("https://discord.gg/wsyY76UZgY")#line:67
    def check_cell (OOO0OO0O00O0OO0O0 ,OOO0000000O0000OO ,O0OO00000OO0O0OO0 ):#line:69
        OO0O0000OOOOO000O =OOO0OO0O00O0OO0O0 .grid [OOO0000000O0000OO ][O0OO00000OO0O0OO0 ].cget ("text")#line:70
        if OO0O0000OOOOO000O =="❌":#line:71
            tkinter .messagebox .showwarning ("Mine","This cell is a mine. Please be careful!")#line:72
root =tk .Tk ()#line:74
app =MinesPredictor (root )#line:75
root .mainloop ()#line:76

#$accees rblx/trasnperent.seemines
