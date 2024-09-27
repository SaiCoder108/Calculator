"""
Build an application to perform
arithmetic operations such as addition, subtraction, multiplication, division,
mean, maximum number, minimum number, square root, Power off,
greatest common multiple, exponent, etc. (you can add more Math
operations for your calculator). The application must allow the user to enter
the arithmetic operation and enter any numbers they want.
"""

#Imports
import tkinter as tk #Import Tkinter Modeule
import math as m #Import Math Module

#Calculation Line
calculation = "" #Create the Calculation line
ans = "" #Create Previous Ans holder
history=[] #Histry List
#Functions
def add_to_calc(symbol): #Adding to Calculation Function
    global calculation #Makes Calculation var Global
    calculation += str(symbol) #Adds any user inputs to calculation string
    text_result.delete(1.0, "end")  #Clears Old String from Screen
    text_result.insert(1.0, calculation) #Displays Update String

def eval_calc(): #Evaluates Calcuation line
    global calculation #Makes Calculation var Global
    global ans #Makes ans var global
    try: #Try Block #Try Block
        hisline = calculation #Has the calculation before eval
        calculation = str(eval(calculation)) #Uses eval() to evalute calculation line and covnverts it to string
        text_result.delete(1.0, "end")  #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Displays Update String
        ans = float(calculation) #Takes Previous Answer
        history.append(f"{hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except: #Except Block: #except: #Except Block Block catches errors (Zero division)
        clear_screen() #Calls Clear Screen Function
        text_result.insert(1.0, "Error") #Displays Error

def clear_screen():
    global calculation #Makes Calculation var Global
    calculation = "" #Clear Calculation Line
    text_result.delete(1.0, "end")  #Clears Old String from Screen

#Average intakes a string of number seperated by commas
def avg(lst): #Average Function
    try: #Try Block
        lst = lst.split(",") #Takes a string seprates by commas
        for x in range(len(lst)): #Loops in the list
            lst[x] = float(lst[x]) #Coverts all numerical elements into floats
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(sum(lst) / len(lst)) #Calculate the average
        text_result.delete(1.0, "end")  #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Display Average
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Avg: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except: #Except Block: #except: #Except Block Block
        clear_screen() #Calls Clear scren function
        text_result.insert(1.0, "Error") #Displays Error

#Maximum Number takes in a list seperated by commas
def max_num(lst): #Maximum Number Function
    try:  # Try Block #Try block
        lst = lst.split(",")  # Takes a string separates by commas
        for x in range(len(lst)):  # Loops in the list
            lst[x] = float(lst[x])  # Coverts all numerical elements into floats
        global calculation  # Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(max(lst))  # Calculate the max value
        text_result.delete(1.0, "end")  #Clears Old String from Screen
        text_result.insert(1.0, calculation)  # Display Max value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Max: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except:  # Except Block: #except: #Except Block Block
        clear_screen()  # Calls Clear screen function
        text_result.insert(1.0, "Error")  # Displays Error

#Minimum Number takes in a list seperated by commas
def min_num(lst): #Minimum Number Function
    try:  # Try Block #Try block
        lst = lst.split(",")  # Takes a string separates by commas
        for x in range(len(lst)):  # Loops in the list
            lst[x] = float(lst[x])  # Coverts all numerical elements into floats
        global calculation  # Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(min(lst))  # Calculate the Min value
        text_result.delete(1.0, "end")  #Clears Old String from Screen
        text_result.insert(1.0, calculation)  # Display Min Value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Min: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except:  # Except Block: #except: #Except Block Block
        clear_screen()  # Calls Clear screen function
        text_result.insert(1.0, "Error")  # Displays Error

#Square Root takes a single numerical input
def num_root(num): #Square Root Function
    try: #Try Block
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(m.sqrt(float(num))) #Sqaureroots the Number and converts the result to a string
        text_result.delete(1.0, "end")  #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Displays Sqaure Root Value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Square Root: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error

#Least Common Multiple takes two numerical inputs
def LCM(lst): #LCM Function
    try: #Try Block
        lst = lst.split(",") #Takes a string separates by commas
        for x in range(len(lst)): #Loops in the List
            lst[x] = int(lst[x]) #Coverts each element into a int
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(m.lcm(*lst)) #LCM is set to Calculation
        text_result.delete(1.0, "end") #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Displays LCM
        ans = float(calculation)  # Takes Previous Answer
        history.append(f"LCM: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history()  # Call History Function
    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error

#Great Common Factor
def GCF(lst): #GCF Functions
    try:  # Try Block
        lst = lst.split(",")  # Takes a string separates by commas
        for x in range(len(lst)):  # Loops in the List
            lst[x] = int(lst[x])  # Coverts each element into a float
        global calculation  # Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(m.gcd(*lst))  # GCD is set to Calculation
        text_result.delete(1.0, "end")  # Clears Old String from Screen
        text_result.insert(1.0, calculation)  # Displays GCD
        ans = float(calculation)  # Takes Previous Answer
        history.append(f"GCF: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history()  # Call History Function
    except:  # Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error

#Logrithms
def logrith(lst):
    try: #Try Block
        lst = lst.split(",") #Takes a string separates by commas
        for x in range(len(lst)): #Loops in string
            lst[x] = float(lst[x]) #Converts each element into a float
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        if len(lst) == 1: #Check if only number was inputted
            num = lst[0] #Set num to the first elelemt in the list
            base = 10
            calculation = str(m.log(int(num), base)) #Sets calculation to logrithmic value in a string
            text_result.delete(1.0, "end") #Clears Old String from Screen
            text_result.insert(1.0, calculation) #Outputs Log Value
            ans = float(calculation)  # Takes Previous Answer
            history.append(f"Log: {hisline} = {ans}")  # Add the current calculation and result to history
            update_history()  # Call History Function

        elif len(lst) == 2: #Checks for num and base
            num = lst[0] #Sets num to first element in the list
            base = lst[1] #Sets base to second element in the list
            calculation = str(m.log(int(num), int(base)))
            text_result.delete(1.0, "end") #Clears Old String from Screen
            text_result.insert(1.0, calculation) #Displays Log Value
            ans = float(calculation)  # Takes Previous Answer
            history.append(f"Logbase {hisline} = {ans}")  # Add the current calculation and result to history
            update_history()  # Call History Function

    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error
#Sine
def sine(num):
    try: #Try Block
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(m.sin(float(num))) #Calculation is Set to Sin value as a string
        text_result.delete(1.0, "end") #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Displays the Sin value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Sin: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error

#Cos
def cosine(num):
    try: #Try Block
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(m.cos(float(num))) #Calculation is set to Cos value as a string
        text_result.delete(1.0, "end") #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Oisplays the Cos value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Cos: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error
#Tan
def tangent(num):
    try: #Try Block
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(m.tan(float(num))) #Calculation set to tan value as a string
        text_result.delete(1.0, "end") #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Displays Tan value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Tan:{hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function

    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error

#Inverse Function
def inverse(num): #Create Inverse Function
    try: #Try Block
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(1/float(num)) #Calculation set to Inverse value as a string
        text_result.delete(1.0, "end") #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Displays Inverse value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Inverse: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error

#Radians Function
def radians(num): #Create Radians Function
    try: #Try Block
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(m.radians(float(num))) #Calculation set to Radians value as a string
        text_result.delete(1.0, "end") #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Displays Radians value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Radians: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error

#Degrees Function
def degrees(num): #Create Degrees Function
    try: #Try Block
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(m.degrees(float(num))) #Calculation set to Degrees value as a string
        text_result.delete(1.0, "end") #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Displays Degrees value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Degrees: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error

#Natural Log Function
def natlog(num): #Create Degrees Function
    try: #Try Block
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        calculation = str(m.log(float(num))) #Calculation set to Natural Log value as a string
        text_result.delete(1.0, "end") #Clears Old String from Screen
        text_result.insert(1.0, calculation) #Displays Degrees value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Natural Log: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error

#Facotrial Function
def factorial(num): #Create Factorail Function
    try: #Try Block
        global calculation #Makes Calculation var Global
        hisline = calculation  # Has the calculation before eval
        if num == 1 or num == 0:
            calculation = str(1) #Calculation set to Natural Log value as a string
            text_result.delete(1.0, "end") #Clears Old String from Screen
            text_result.insert(1.0, calculation) #Displays Factorial value
        else:
            calculation = str(m.factorial(int(num))) #Calculation set to Natural Log value as a string
            text_result.delete(1.0, "end") #Clears Old String from Screen
            text_result.insert(1.0, calculation) #Displays Factorial value
        ans = float(calculation) #Takes Previous Answer
        history.append(f"Factorial: {hisline} = {ans}")  # Add the current calculation and result to history
        update_history() #Call History Function
    except: #Except Block:
        clear_screen()  # Calls Clear Screen Function
        text_result.insert(1.0, "Error")  # Displays Error

#Color Swap Function
colors = ["#D3D3D3","black","blue", "#8CCA72","#5B00C0","pink","#FFD580","grey","#DC143C"] #Color list
swap = 1 #Swap Counter
def colorswap(): #Color Swap Function
    global swap #Makes Swap Var Global
    global colors #Makes Colors list Global
    global label1 #Makes Label1 global
    global label2 #Makes Label2 global
    root.configure(bg=colors[swap]) #Changes Color

    if swap == 8: #Checks for index range
        swap = 0 #Resets swap count
    else: #else
        swap+=1 #Adds one to swap

#Memory Function
def memory(): #Creats Memory Function
    global calculation #Makes calculation var global
    global ans #Makes ans var global
    calculation += str(ans) #Adds previous ans to calculation
    text_result.delete(1.0, "end") #Clear screen
    text_result.insert(1.0, calculation) #Displays new calculation

#Delete Function
def delete(): #Creats Memory Function
    global calculation #Makes calculation var global
    calculation = calculation[:len(calculation)-1]
    text_result.delete(1.0, "end") #Clear screen
    text_result.insert(1.0, calculation) #Displays new calculation

#History Size
def hiswind():
    root.geometry("800x380")  # Window size

#Advanced function size
def func():
    root.geometry("430x550")  # Window size

#Normal function size
def norm():
    root.geometry("430x380")  # Window size

#Window
root = tk.Tk() #Windown Create
root.title("Harish's Python Calculator")
root.geometry("430x380") #Window size
root.configure(bg="#D3D3D3") #Sets Color to Red


#Text Box
text_result = tk.Text(root, height=3, width=20, font=("Arial", 24)) #Create Text Box
text_result.grid(row=0, column=2, columnspan=5, rowspan=2) #Text box grid space

#History Function
def update_history(): #Create History Function
    if len(history) >= 8:
        history.pop(0)
    text_history.delete(1.0, "end")  # Clear the history widget
    for item in history: #Loop in History List
        text_history.insert("end", item + "\n") #Outputs

# History Label
history_label = tk.Label(root, text="History", font=("Arial", 20)) #Create Text Box
history_label.grid(row=0, column=12, columnspan=3) #Grid Specs
#History Text Box
text_history = tk.Text(root, height=9, width=20, font=("Arial", 24)) #Create Text Box
text_history.grid(row=1, column=12, columnspan=3, rowspan=9) #Grid Specs

#--------------------------------------------Buttons (Numbers)------------------------------------------
#Num 1
btn_1 = tk.Button(root, text=1, command=lambda: add_to_calc(1), width=6, font=("Arial", 16), bg="cyan")
btn_1.grid(row=2, column=1)
#Num 2
btn_2 = tk.Button(root, text=2, command=lambda: add_to_calc(2), width=6, font=("Arial", 16), bg="cyan")
btn_2.grid(row=2, column=2)
#Num 3
btn_3 = tk.Button(root, text=3, command=lambda: add_to_calc(3), width=6, font=("Arial", 16), bg="cyan")
btn_3.grid(row=2, column=3)
#Num 4
btn_4 = tk.Button(root, text=4, command=lambda: add_to_calc(4), width=6, font=("Arial", 16), bg="cyan")
btn_4.grid(row=3, column=1)
#Num 5
btn_5 = tk.Button(root, text=5, command=lambda: add_to_calc(5), width=6, font=("Arial", 16), bg="cyan")
btn_5.grid(row=3, column=2)
#Num 6
btn_6 = tk.Button(root, text=6, command=lambda: add_to_calc(6), width=6, font=("Arial", 16), bg="cyan")
btn_6.grid(row=3, column=3)
#Num 7
btn_7 = tk.Button(root, text=7, command=lambda: add_to_calc(7), width=6, font=("Arial", 16), bg="cyan")
btn_7.grid(row=4, column=1)
#Num 8
btn_8 = tk.Button(root, text=8, command=lambda: add_to_calc(8), width=6, font=("Arial", 16), bg="cyan")
btn_8.grid(row=4, column=2)
#Num 9
btn_9 = tk.Button(root, text=9, command=lambda: add_to_calc(9), width=6, font=("Arial", 16), bg="cyan")
btn_9.grid(row=4, column=3)
#Num 0
btn_0 = tk.Button(root, text=0, command=lambda: add_to_calc(0), width=6, font=("Arial", 16), bg="cyan")
btn_0.grid(row=5, column=2)
#--------------------------------------------Buttons (Simple Operations)------------------------------------------
#Addition
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calc("+"), width=6, font=("Arial", 16), bg="yellow")
btn_plus.grid(row=2, column=4)
#Subtraction
btn_sub = tk.Button(root, text="-", command=lambda: add_to_calc("-"), width=6, font=("Arial", 16), bg="yellow")
btn_sub.grid(row=3, column=4)
#Multiplication
btn_mul = tk.Button(root, text="x", command=lambda: add_to_calc("*"), width=6, font=("Arial", 16), bg="yellow")
btn_mul.grid(row=4, column=4)
#Division
btn_div = tk.Button(root, text="÷", command=lambda: add_to_calc("/"), width=6, font=("Arial", 16), bg="yellow")
btn_div.grid(row=5, column=4)
#Open Bracket
btn_open = tk.Button(root, text="(", command=lambda: add_to_calc("("), width=6, font=("Arial", 16), bg="cyan")
btn_open.grid(row=5, column=1)
#Close Bracket
btn_close = tk.Button(root, text=")", command=lambda: add_to_calc(")"), width=6, font=("Arial", 16), bg="cyan")
btn_close.grid(row=5, column=3)
#Exponent
btn_close = tk.Button(root, text="x^y", command=lambda: add_to_calc("**"), width=6, font=("Arial", 16), bg="yellow")
btn_close.grid(row=4, column=5)
#Comma
btn_comma = tk.Button(root, text=",", command=lambda: add_to_calc(","), width=6, font=("Arial", 16), bg="yellow")
btn_comma.grid(row=2, column=5)
#Dot
btn_dot = tk.Button(root, text=".", command=lambda: add_to_calc("."), width=6, font=("Arial", 16), bg="yellow")
btn_dot.grid(row=3, column=5)
#Inverse
btn_inv = tk.Button(root, text="1/x", command= lambda: inverse(calculation), width=6, font=("Arial", 16), bg="yellow")
btn_inv.grid(row=5, column=5)
#--------------------------------------------Buttons (Extra Operations)------------------------------------------
#Average
btn_avg = tk.Button(root, text="AVG", command= lambda: avg(calculation), width=6, font=("Arial", 16), bg="orange")
btn_avg.grid(row=10, column=1, columnspan=2)
#Max
btn_max = tk.Button(root, text="MAX", command= lambda: max_num(calculation), width=6, font=("Arial", 16), bg="orange")
btn_max.grid(row=10, column=2, columnspan=2)
#Min
btn_min = tk.Button(root, text="MIN", command= lambda: min_num(calculation), width=6, font=("Arial", 16), bg="orange")
btn_min.grid(row=10, column=3, columnspan=2)
#Square Roo
btn_sqrt = tk.Button(root, text="SQRT", command= lambda: num_root(calculation), width=6, font=("Arial", 16), bg="orange")
btn_sqrt.grid(row=10, column=4, columnspan=2)
#LCM
btn_lcm = tk.Button(root, text="LCM", command= lambda: LCM(calculation), width=6, font=("Arial", 16), bg="orange")
btn_lcm.grid(row=11, column=1, columnspan=2)
#GCF
btn_gcf = tk.Button(root, text="GCF", command= lambda: GCF(calculation), width=6, font=("Arial", 16), bg="orange")
btn_gcf.grid(row=11, column=2, columnspan=2)
#LOG
btn_log = tk.Button(root, text="LOG", command= lambda: logrith(calculation), width=6, font=("Arial", 16), bg="orange")
btn_log.grid(row=11, column=3, columnspan=2)
#Sine
btn_sin = tk.Button(root, text="SIN", command= lambda: sine(calculation), width=6, font=("Arial", 16), bg="orange")
btn_sin.grid(row=11, column=4, columnspan=2)
#Cosine
btn_cos = tk.Button(root, text="COS", command= lambda: cosine(calculation), width=6, font=("Arial", 16), bg="orange")
btn_cos.grid(row=12, column=1, columnspan=2)
#Tangent
btn_tan = tk.Button(root, text="TAN", command= lambda: tangent(calculation), width=6, font=("Arial", 16), bg="orange")
btn_tan.grid(row=12, column=2, columnspan=2)
#Pi Number
btn_pi = tk.Button(root, text="π", command= lambda: add_to_calc(m.pi), width=6, font=("Arial", 16), bg="orange")
btn_pi.grid(row=12, column=3, columnspan=2)
#Modulas Operator
btn_mod = tk.Button(root, text="%", command=lambda: add_to_calc("%"), width=6, font=("Arial", 16), bg="orange")
btn_mod.grid(row=12, column=4, columnspan=2)
#Degrees Operator
btn_deg = tk.Button(root, text="DEG", command=lambda: degrees(calculation), width=6, font=("Arial", 16), bg="orange")
btn_deg.grid(row=13, column=1, columnspan=2)
#Radians Operator
btn_rad = tk.Button(root, text="RAD", command=lambda: radians(calculation), width=6, font=("Arial", 16), bg="orange")
btn_rad.grid(row=13, column=2, columnspan=2)
#Radians Operator
btn_ln = tk.Button(root, text="LN", command=lambda: natlog(calculation), width=6, font=("Arial", 16), bg="orange")
btn_ln.grid(row=13, column=3, columnspan=2)
#Factorial Operator
btn_fac = tk.Button(root, text="n!", command=lambda: factorial(calculation), width=6, font=("Arial", 16), bg="orange")
btn_fac.grid(row=13, column=4, columnspan=2)
# Blank row as a spacer
blank_row_label = tk.Label(root, text="", bg="black", highlightthickness=0, borderwidth=0, anchor="w")
blank_row_label.grid(row=6, column=0, columnspan=10, sticky="w")

#--------------------------------------------Buttons (Core Functions)------------------------------------------
#Equals
btn_equal = tk.Button(root, text="=", command=eval_calc, width=13, font=("Arial", 16), bg="#87CEEB")
btn_equal.grid(row=7, column=1, columnspan=2)
#Clear
btn_clear = tk.Button(root, text="C", command=clear_screen, width=6, font=("Arial", 16), bg="#E75480")
btn_clear.grid(row=7, column=3)
#PWR_off
btn_off = tk.Button(root, text="OFF", command= lambda: exit(), width=6, font=("Arial", 16), bg="#E75480")
btn_off.grid(row=0, column=1)
#Color_Swap
btn_clr = tk.Button(root, text="Color", command= lambda: colorswap(), width=6, font=("Arial", 16), bg="#E75480")
btn_clr.grid(row=1, column=1)
#Memory
btn_ans = tk.Button(root, text="ANS", command=memory, width=6, font=("Arial", 16), bg="#E75480")
btn_ans.grid(row=7, column=4)
#Delete
btn_del = tk.Button(root, text="DEL", command=delete, width=6, font=("Arial", 16), bg="#E75480")
btn_del.grid(row=7, column=5)
#History
btn_his = tk.Button(root, text="History", command=lambda: hiswind(), width=13, font=("Arial", 16), bg="#90EE90")
btn_his.grid(row=8, column=1, columnspan=2)
#Functions
btn_func = tk.Button(root, text="FUNC", command=lambda: func(), width=13, font=("Arial", 16), bg="#90EE90")
btn_func.grid(row=8, column=3, columnspan=2)
#Normal
btn_norm = tk.Button(root, text="NORM", command=lambda: norm(), width=6, font=("Arial", 16), bg="#90EE90")
btn_norm.grid(row=8, column=5, columnspan=1)

#Keyboard
def keyboard(event): #Keyboard Input Function
    key = event.char #Key is set to the character evet
    if key.isdigit() or key in "+-*/.(),": #Checks the validity of the input
        add_to_calc(key) #Add keyboard input to calculation
    elif key == "=" or key == "\r":  # Check for both "=" and Enter key ("\r")
        eval_calc() #Evalutes Calculation
    elif key.lower() == "c":  # Allow both uppercase and lowercase "c" for clearing the screen
        clear_screen()
    elif key == '\x08': # Check for Backspace key ('\x08' is the ASCII code for Backspace)
        delete()
# Bind the keyboard function to the root window to capture key events
root.bind("<Key>", keyboard)

# Main Loop
root.mainloop()