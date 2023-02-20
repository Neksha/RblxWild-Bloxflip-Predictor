import tkinter as tk #line:1
import random #line:2
import tkinter .colorchooser #line:3
import tkinter .messagebox #line:4
import tkinter .simpledialog #line:5
import webbrowser #line:6
class MinesPredictor :#line:8
    def __init__ (OOOOOO0O0O0OOO00O ,OO000000O00OO0OO0 ):#line:9
        OOOOOO0O0O0OOO00O .master =OO000000O00OO0OO0 #line:10
        OOOOOO0O0O0OOO00O .master .title ("Mines Predictor")#line:11
        OOOOOO0O0O0OOO00O .background_color ="white"#line:12
        OOOOOO0O0O0OOO00O .grid_frame =tk .Frame (OOOOOO0O0O0OOO00O .master ,bg =OOOOOO0O0O0OOO00O .background_color )#line:14
        OOOOOO0O0O0OOO00O .grid_frame .grid (row =0 ,column =0 ,padx =10 ,pady =10 )#line:15
        OOOOOO0O0O0OOO00O .generate_button =tk .Button (OOOOOO0O0O0OOO00O .master ,text ="Inject",command =OOOOOO0O0O0OOO00O .generate_grid_with_input )#line:17
        OOOOOO0O0O0OOO00O .generate_button .grid (row =1 ,column =0 ,pady =10 )#line:18
        OOOOOO0O0O0OOO00O .customize_button =tk .Button (OOOOOO0O0O0OOO00O .master ,text ="Customize",command =OOOOOO0O0O0OOO00O .customize )#line:20
        OOOOOO0O0O0OOO00O .customize_button .grid (row =2 ,column =0 ,pady =10 )#line:21
        OOOOOO0O0O0OOO00O .home_button =tk .Button (OOOOOO0O0O0OOO00O .master ,text ="Discord",command =OOOOOO0O0O0OOO00O .go_home )#line:23
        OOOOOO0O0O0OOO00O .home_button .grid (row =3 ,column =0 ,pady =10 )#line:24
    def generate_grid_with_input (OO0OO00OOO0OO0O00 ):#line:26
        OOO000O0O0OO00O00 =tkinter .simpledialog .askstring ("Round ID","Enter round ID:")#line:27
        if OOO000O0O0OO00O00 is not None :#line:28
            if len (OOO000O0O0OO00O00 )<20 :#line:29
                tkinter .messagebox .showerror ("Error","Not a valid round ID. Please enter a round ID from rblxwild or bloxflip")#line:30
            else :#line:31
                OO0OO00OOO0OO0O00 .generate_grid ()#line:32
    def generate_grid (OO0O000OOOOOO0O00 ):#line:34
        OO0O000OOOOOO0O00 .clear_grid ()#line:35
        OO0O000OOOOOO0O00 .grid =[]#line:38
        for O0O000O00O00OOOO0 in range (5 ):#line:39
            OO000O00OOOOOO000 =[]#line:40
            for O0OOO0OOO0OO00O00 in range (5 ):#line:41
                OOOOOO0OO00OO0OO0 =tk .Button (OO0O000OOOOOO0O00 .grid_frame ,text ="❌",width =4 ,height =2 ,font =("Arial",16 ),command =lambda row =O0O000O00O00OOOO0 ,col =O0OOO0OOO0OO00O00 :OO0O000OOOOOO0O00 .check_cell (row ,col ))#line:42
                OOOOOO0OO00OO0OO0 .grid (row =O0O000O00O00OOOO0 ,column =O0OOO0OOO0OO00O00 ,padx =2 ,pady =2 )#line:43
                OO000O00OOOOOO000 .append (OOOOOO0OO00OO0OO0 )#line:44
            OO0O000OOOOOO0O00 .grid .append (OO000O00OOOOOO000 )#line:45
        for O0O000O00O00OOOO0 in range (4 ):#line:48
            OO000O00OOOOOO000 =random .randint (0 ,4 )#line:50
            O000000O00O00O000 =random .randint (0 ,4 )#line:51
            OO0O000OOOOOO0O00 .grid [OO000O00OOOOOO000 ][O000000O00O00O000 ].configure (text ="✅")#line:52
    def clear_grid (O00O00OOOOOOOO0O0 ):#line:54
        if hasattr (O00O00OOOOOOOO0O0 ,"grid"):#line:55
            for OO0O000OO0O0OO0OO in O00O00OOOOOOOO0O0 .grid :#line:56
                for OO0O00OOO0OO00OO0 in OO0O000OO0O0OO0OO :#line:57
                    OO0O00OOO0OO00OO0 .destroy ()#line:58
    def customize (OOOOO00O00O000OO0 ):#line:60
        O00OOOO00O0000OOO =tk .colorchooser .askcolor ()[1 ]#line:61
        if O00OOOO00O0000OOO :#line:62
            OOOOO00O00O000OO0 .background_color =O00OOOO00O0000OOO #line:63
            OOOOO00O00O000OO0 .grid_frame .config (bg =OOOOO00O00O000OO0 .background_color )#line:64
    def go_home (OOO0OOOOO0OOOOO0O ):#line:66
        webbrowser .open ("https://discord.com")#line:67
    def check_cell (O00O00OO00O00O0OO ,OOOO0000OO00OO00O ,OO0O000000O00O0OO ):#line:69
        OOO0OOOOO00O000O0 =O00O00OO00O00O0OO .grid [OOOO0000OO00OO00O ][OO0O000000O00O0OO ].cget ("text")#line:70
        if OOO0OOOOO00O000O0 =="❌":#line:71
            tkinter .messagebox .showwarning ("Mine","This cell is a mine. Please be careful!")#line:72
root =tk .Tk ()#line:74
app =MinesPredictor (root )#line:75
root .mainloop ()#line:76
