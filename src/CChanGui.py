# @package CchanGui
# GUI for calc-chan
from CChanMathlib import CChanMathlib
import tkinter as tk 
import tkinter.messagebox as tkmsg

import random

##
# @brief Function that pops up new window (showinfo from messagebox) which show some help how to use calc-chan
def Napoveda():
    tkmsg.showinfo("Calc-chan nápověda","""Calc-chan dovoluje zápis matematický výrazů přímo do pole k tomu určenému.\n
Další možností jsou tlačítka která přidávají text za kurzor.\n
Speciální funkce:
    DEL - smaže celý výraz
    CE - smaže znak před kurzorem
    ln( ) - přirozený logaritmus
    ! - faktoriál
    ^ - mocina
    √ - odmocnina
    Syntax error - špatně zapsaný výraz
    Value error - např. ln(0)
    ZeroDivison - dělení nulou""")

##
# @brief Function to add string to end of expression
# @param text_to_add text that will be added to end of expression on display
def add_to_str(text_to_add):
        display.insert(tk.INSERT,text_to_add)

    
##
# @brief Function to evaluate expression in display and set that expression back
def calc_chan_do_the_calc():
    expr=display.get(1.0,tk.END).strip()
    try:
        vysledek=str(CChanMathlib.eval(expr))
    except SyntaxError:
        vysledek="Syntax error"
    except ValueError:
        vysledek="Value error"
    except ZeroDivisionError:
        vysledek="Zero division"
    display.delete(1.0,tk.END)
    display.insert(1.0,vysledek)


##
# @brief Function to add random number in range <0,1> to end of expression on display
def str_random():
    #momentalne zbytecna fce protoze pro tlacitko random nezbylo misto
    display.insert(tk.INSERT,str(random.random()))


##
# @brief Function that deletes last character of expression on display
def str_ce():
    line,char=display.index(tk.INSERT).split(".",1)
    if line==1 and char==0:
        return#cursor je na zacatku
    if char !=0:
        char=str(int(char)-1)
    display.delete(line+"."+char)

    
##
# @brief Function that deletes whole expression on display
def str_del():
    display.delete(1.0,tk.END)
    


hlavni=tk.Tk()
hmenu=tk.Menu(hlavni)
hlavni.minsize(250,400)
hlavni.title("Calc-chan")
hlavni.resizable(width=False, height=False)

displayed_text=""
which_button=tk.StringVar()

t0=tk.Button(hlavni,text="0",width=6,heigh=3,command=lambda text_to_add="0" : add_to_str(text_to_add))
tcarka=tk.Button(hlavni,text=",",width=6,heigh=3,command=lambda text_to_add="." : add_to_str(text_to_add))
#pro tlacitko random zatim neni misto
#trandom=Button(hlavni,text="rand",width=6,heigh=3,command=str_random)
t1=tk.Button(hlavni,text="1",width=6,heigh=3,command=lambda text_to_add="1" : add_to_str(text_to_add))
t2=tk.Button(hlavni,text="2",width=6,heigh=3,command=lambda text_to_add="2" : add_to_str(text_to_add))
t3=tk.Button(hlavni,text="3",width=6,heigh=3,command=lambda text_to_add="3" : add_to_str(text_to_add))
t4=tk.Button(hlavni,text="4",width=6,heigh=3,command=lambda text_to_add="4" : add_to_str(text_to_add))
t5=tk.Button(hlavni,text="5",width=6,heigh=3,command=lambda text_to_add="5" : add_to_str(text_to_add))
t6=tk.Button(hlavni,text="6",width=6,heigh=3,command=lambda text_to_add="6" : add_to_str(text_to_add))
t7=tk.Button(hlavni,text="7",width=6,heigh=3,command=lambda text_to_add="7" : add_to_str(text_to_add))
t8=tk.Button(hlavni,text="8",width=6,heigh=3,command=lambda text_to_add="8" : add_to_str(text_to_add))
t9=tk.Button(hlavni,text="9",width=6,heigh=3,command=lambda text_to_add="9" : add_to_str(text_to_add))
teq=tk.Button(hlavni,text="=",width=6,heigh=3,command=calc_chan_do_the_calc)
tplus=tk.Button(hlavni,text="+",width=6,heigh=3,command=lambda text_to_add="+" : add_to_str(text_to_add))
tminus=tk.Button(hlavni,text="-",width=6,heigh=3,command=lambda text_to_add="-" : add_to_str(text_to_add))
tmult=tk.Button(hlavni,text="*",width=6,heigh=3,command=lambda text_to_add="*" : add_to_str(text_to_add))
tdiv=tk.Button(hlavni,text="/",width=6,heigh=3,command=lambda text_to_add="/" : add_to_str(text_to_add))
tce=tk.Button(hlavni,text="CE",width=6,heigh=3,command=str_ce)
tdel=tk.Button(hlavni,text="DEL",width=6,heigh=3,command=str_del)
tlb=tk.Button(hlavni,text="(",width=6,heigh=3,command=lambda text_to_add="(" : add_to_str(text_to_add))
trb=tk.Button(hlavni,text=")",width=6,heigh=3,command=lambda text_to_add=")" : add_to_str(text_to_add))
tsquare=tk.Button(hlavni,text="^",width=6,heigh=3,command=lambda text_to_add="^" : add_to_str(text_to_add))
troot=tk.Button(hlavni,text="√",width=6,heigh=3,command=lambda text_to_add="2√" : add_to_str(text_to_add))
tln=tk.Button(hlavni,text="ln",width=6,heigh=3,command=lambda text_to_add="ln(" : add_to_str(text_to_add))
tfact=tk.Button(hlavni,text="!",width=6,heigh=3,command=lambda text_to_add="!" : add_to_str(text_to_add))
display=tk.Text(hlavni,font="arial 17",heigh=4,width=20,bg="white")

hmenu.add_command(label=u"Nápověda",command=Napoveda)
hlavni.config(menu=hmenu)

t0.grid(row=6,column=0,pady=3)
tcarka.grid(row=6,column=1,pady=3)
tfact.grid(row=6,column=2,pady=3)
t1.grid(row=5,column=0,pady=3)
t2.grid(row=5,column=1,pady=3)
t3.grid(row=5,column=2,pady=3)

t4.grid(row=4,column=0,pady=3)
t5.grid(row=4,column=1,pady=3)
t6.grid(row=4,column=2,pady=3)

t7.grid(row=3,column=0,pady=3)
t8.grid(row=3,column=1,pady=3)
t9.grid(row=3,column=2,pady=3)

teq.grid(row=6,column=3,pady=3)
tplus.grid(row=5,column=3,pady=3)
tminus.grid(row=4,column=3,pady=3)
tmult.grid(row=3,column=3,pady=3)

tdiv.grid(row=2,column=3,pady=3)
tdel.grid(row=2,column=2,pady=3)
tce.grid(row=2,column=1,pady=3)

trb.grid(row=2,column=0,pady=3)
tlb.grid(row=1,column=0,pady=3)
tln.grid(row=1,column=1,pady=3)
troot.grid(row=1,column=2,pady=3)
tsquare.grid(row=1,column=3,pady=3)

display.grid(row=0,column=0,columnspan=4,pady=3)
tk.mainloop()