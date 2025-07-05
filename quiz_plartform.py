import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk , Image
from tkinter import filedialog as fd 
from tkinter import messagebox as msgbox
from tkinter import ttk
import sqlite3 
import database_access
import json
import time
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from remark import Notipy
from questions_uploader import Generate_question

'''parent window'''
root = ctk.CTk()
'''window title'''
root.title("UTME GUIDE")
my_root_icon =tk.PhotoImage(file= r"C:\Users\owner\Desktop\CBT_PROJECT\employee (2).png")
root.wm_iconphoto(True,my_root_icon)
'''the screen display size'''
root.geometry("1300x700")
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
root.resizable(True,True)
#working with the json file to generate the question
with open(r"C:\Users\owner\Desktop\CBT_PROJECT\my_qustion_bank.json","r") as file:
    file_object = json.load(file)
    questions = file_object["Questions"]
    options = file_object["Options"]
    answers = file_object["Answers"]
    
#function to display question
#fuction  to check answer
# function to check for the student opti on
selected_option =tk.StringVar()
question_no = 0
correct_answer = 0
print(correct_answer)
total_questions = len(questions)
index = total_questions
'''dictionnary for the selected option'''
selection_list = ["null"]
root._set_appearance_mode("system")

############################## loading the question bank ###########################
#with open("r"C:\Users\User\MY_PYTHON_PROJECTS\my_qustion_bank.json","r")

'''variable decleration'''
image_path = tk.StringVar()
################################## selected variable ##################################

'''first frame logo'''
logo_image_path1 = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\bg_image_31.jpg")
logo_image_path1=logo_image_path1.resize((1500,700))
logo_photo1 = ImageTk.PhotoImage(logo_image_path1)
'''option frame path'''
option_frame_path = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\pic11.jpg")
option_frame_path=option_frame_path.resize((1500,700))
option_frame_photo = ImageTk.PhotoImage(option_frame_path)
#admin image
admin_frame_path = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\bg_image_25.jpg")
admin_frame_path=admin_frame_path.resize((1500,700))
admin_frame_photo = ImageTk.PhotoImage(admin_frame_path)

working_frame_path = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\bg_image_31.jpg")
working_frame_path=working_frame_path.resize((1300,700))
working_frame_photo = ImageTk.PhotoImage(working_frame_path)

'''sign up logo '''
logo_image_path2 = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\logo11.png")
logo_image_path2 = logo_image_path2.resize((70,70))
logo_photo2 = ImageTk.PhotoImage(logo_image_path2)
logo_image_path3 = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\logo6.png")
logo_image_path3 = logo_image_path3.resize((90,90))
logo_photo3 = ImageTk.PhotoImage(logo_image_path3)
'''back button icon'''
back_button_icon = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\direction.png")
back_button_icon = back_button_icon.resize((20,25))
back_button_photo = ImageTk.PhotoImage(back_button_icon)
#admin control icons
icon1_path = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\edit1.png")
icon1_path=icon1_path.resize((25,25))
icon1_photo = ImageTk.PhotoImage(icon1_path)

icon2_path = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\coins.png")
icon2_path=icon2_path.resize((25,25))
icon2_photo = ImageTk.PhotoImage(icon2_path)


icon3_path = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\settings.png")
icon3_path=icon3_path.resize((25,25))
icon3_photo = ImageTk.PhotoImage(icon3_path)


icon4_path = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\back-up.png")
icon4_path=icon4_path.resize((25,25))
icon4_photo = ImageTk.PhotoImage(icon4_path)


icon5_path = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\logout.png")
icon5_path=icon5_path.resize((25,25))
icon5_photo = ImageTk.PhotoImage(icon5_path)

# student image path
student_image_path = Image.open(r"C:\Users\owner\Desktop\CBT_PROJECT\profileimage2.png")
student_image_path = student_image_path.resize((90,100))
student_photo = ImageTk.PhotoImage(student_image_path)
gender_var = ctk.StringVar()
option_var = ctk.StringVar()
subject_var = ctk.StringVar()
# passwordvar3.set("")

'''gender variable initialization'''
gender_var.set("Other")
print(gender_var.get())
'''option variable initialization'''
option_var.set("Login mode")
print(option_var.get())
'''subject variable initializatio'''
subject_var.set("None")
selected_subject = "None"
'''option list'''
my_list = ["Male" , "Female"]
option_list = ["Login as administrator","Login as student"]
'''subject list'''
subject_list = ["English","Physics","Mathematics","Chemistry","Biology","Computer"]
image_path1 = r"C:\Users\owner\Desktop\CBT_PROJECT\profileimage2.png "

instruction = """
Attempt all the questions, and each question carried equal mark
you are to answer to complete before the time run out,
in other to avoid missing some question,
and the result will be display immediately after submiting the test,wish you all the best!."""
img = Image.open(image_path1)
img = img.resize((150,200))
photo1 = ImageTk.PhotoImage(img)

###################FUNCTION TO CONTROL THE QUESTION RESPOND ################


'''display question'''
def display_question(ques_no):
    display_question_label.configure(text = f"Q{ques_no + 1}.{questions[question_no]}")

'''check option function'''
    
def check_answer(q_no):
    if selected_option.get() == answers[q_no] and selected_option.get() not in selection_list:
        return True
    else:
        print("wrong option")

'''function to upload the selected option'''
def stored_selected_opt(q_no):
    global selection_list
    global question_no
    
    if selected_option.get() not in selection_list:
        selection_list.append(selected_option.get())
        for selection in selection_list:
             print(selection)
             #selected_option.set(selection_list[q_no])
        #print("you have selected", selection_list[q_no])
    else:
        pass
def set_selected_opt(q_no):
    global question_no
    global selection_list
    try:

        selected_option.set(selection_list[q_no+1])
        print("i am working")
    except IndexError:
        pass

"""display result function"""
def display_result():
    wrong = total_questions-correct_answer
    score = int((correct_answer/total_questions)*100)
    message = f"CORRECT ANSWERS  : {correct_answer}\nWRONG ANSWERS  : {wrong}\nCOMMULATIVE SCORE: {score}%"
    #msgbox.showinfo("Result",message)
    user_frame.pack_forget()
    result_frame.pack(fill = "both",expand = True)
    result_frame.update()

    result_title = ctk.CTkLabel(result_frame,
                                text = "NOTIFICATION OF A RESULT",
                                font = ("Arial",30,"bold","underline"),
                                text_color = "black")
    result_title.place(x = 100, y = 100) 
    result = ctk.CTkLabel(result_frame,
                          text=message,
                          font = ("Arial",20,"bold"),
                          text_color = "black",)
    result.place(x = 100, y = 150)
    obj1 = Notipy(score,result_frame)
    obj1.comment()
    """displaying the result in piechart"""
    plt.title("piechart presentation of result")
    titles = ["Correct","Wrong"]
    size = [correct_answer,wrong]
    figure,axis = plt.subplots()
    axis.pie(size,labels = titles,autopct = "%1.1f%%")
    my_canvas = FigureCanvasTkAgg(figure,master = result_frame)
    my_canvas.draw()
    my_canvas.get_tk_widget().place(x = 600,y = 50)
    """return to dashboard button"""
    retn = ctk.CTkButton(result_frame,
                         text = "RETURN TO DASHBOARD",
                         hover_color = "green",
                         font = ("Arial",16,"bold"),
                         corner_radius = 20,
                         text_color = "black",
                         cursor = "hand2",
                         command = return_to_dashboard)
    retn.place(x = 500, y = 500 )

"""function to return dashboard"""
def return_to_dashboard():
    global question_no
    return_to_initial()
    #question_no =  question_no
    result_frame.pack_forget()
    user_frame.pack(fill = "both", expand = True)

"""function to return the initial question  and deselected any option"""
def return_to_initial():
    global index
    global selection_list
    global correct_answer
    try:

        while index != 0 :
            previous_function()
            print(selection_list.pop())
            index -= 1
    except IndexError:
        pass
    while correct_answer != 0:
        correct_answer -= 1
    index += total_questions
    print(selection_list)
    print(f"the current index :{index}")
    print(question_no)
    print(f"the final correct answer value : {correct_answer}")

"""function to change the next question"""
def next_question():
    global question_no
    global user_option
    global correct_answer
    try:

        if check_answer(question_no) :
            correct_answer += 1
    except IndexError:
        pass

    if question_no + 1 < total_questions  :
        x = 0
        init_postion = 180
        question_no += 1
        #selected_opt_storage(question_no)
        display_question(question_no)
        previous_button.place(x = 200 ,y = 640 )

        letters = ["A","B","C","D"]
        q_remain_label.configure(text =f"QUESTION:\n {question_no +1}/{total_questions} " )
        for letter, opt in zip(letters,options[question_no]):
            option_list[x].configure(text = f"{letter}. {opt}",value = opt)
            x += 1
            stored_selected_opt(question_no)
        #print(selected_option.get())
        print(selection_list)
        print(f"answer for Q{question_no +1} {answers[question_no]}")
        print(f"you just earned :{correct_answer} marks")
        try:

            selected_option.set(selection_list[question_no +1])
        except IndexError:
            pass
        try:

            print(question_no)
            print(selection_list[question_no])
        except IndexError:
            pass


    else:
        stored_selected_opt(question_no)

        try:
            selected_option.set(selection_list[question_no])
        except IndexError:
            pass
        print(selection_list)
        print(question_no)
        print(f"you just earned :{correct_answer} marks")
        submit_fnt()
'''Previous function'''
def previous_function():
    global question_no
    if question_no >0 :
         
        x = 0
        init_postion = 180
        question_no -= 1
        #print(question_no)
        display_question(question_no)

        letters = ["A","B","C","D"]
        q_remain_label.configure(text =f"QUESTION:\n {question_no +1}/{total_questions} " )
        for letter, opt in zip(letters,options[question_no]):
            option_list[x].configure(text = f"{letter}. {opt}",value = opt)
            x += 1
        set_selected_opt(question_no)
    # if image_path :
    #     placeholder_image_label.pack_forget()
    #     #print(f"Selected image:{image_path}")
    #     img = Image.open(image_path)
    #     img = img.resize((150,180))
    #     photo = ImageTk.PhotoImage(img)
    #     path_label = ctk.CTkLabel(image_frame,
    #                               image = photo,
    #                               text = " ")
    #     path_label.pack(fill = "both" , expand = False)

''' the function for switching to sign up frame'''
def signup_frame():
    user_frame.pack_forget()
    sign_up_frame.pack(fill = "both", expand = True)
    eyeclose_function1()
    eyeclose_function2()

    
    
def eyeclose_function1():
    
    show_button1 = ctk.CTkButton(sign_up_frame ,
                                image = show_photo1,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeopen_function1)
    show_button1.place( x = 314 , y = 432)
    pass_word_entry.configure(show = "*")
    
def eyeopen_function1():
    '''Password entry'''
    hide_button1 = ctk.CTkButton(sign_up_frame ,
                                image = hide_photo1,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeclose_function1)
    hide_button1.place( x = 314 , y = 432)
    pass_word_entry.configure(show = "")
    
def eyeclose_function2():
    '''Password entry'''
    show_button2 = ctk.CTkButton(sign_up_frame ,
                                image = show_photo2,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeopen_function2)
    show_button2.place( x = 314 , y = 492)
    comfirm_entry.configure(show = "*")
     
def eyeopen_function2():
    '''Password entry'''
    hide_button2 = ctk.CTkButton(sign_up_frame ,
                                image = hide_photo2,
                                
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeclose_function2)
    hide_button2.place( x = 314 , y = 492)
    comfirm_entry.configure(show = "")
    

def eyeclose_function3():
    
    '''eyeopen button3'''
    show_button3 = ctk.CTkButton(user_frame ,
                                image = show_photo3,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeopen_function3)
    show_button3.place( x = 615 , y = 392)
    password_entry.configure(show = "*")

def eyeopen_function3():
    '''Password entry'''
    hide_button3 = ctk.CTkButton(user_frame ,
                                image = hide_photo3,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeclose_function3)
    hide_button3.place( x = 615 , y = 392)
    password_entry.configure(show = "")
    
    
def eyeclose_function4():
    
    '''eyeopen button4'''
    show_button4 = ctk.CTkButton(admin_frame ,
                                image = show_photo4,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeopen_function4)
    show_button4.place( x = 331 , y = 183)
    admin_password_entry.configure(show = "*")


def eyeopen_function4():
    '''Password entry'''
    hide_button4 = ctk.CTkButton(admin_frame ,
                                image = hide_photo4,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeclose_function4)
    hide_button4.place( x = 331 , y = 183)
    admin_password_entry.configure(show = "")

# function to check for the user entry
def check_user_details(reg_no, password) :
    #getting the data from databse
    database_access.my_cursor.execute("SELECT * FROM students_record WHERE  Reg_no = ? AND Password = ?",(reg_no,password))
    result = database_access.my_cursor.fetchall()
    if result:
        msgbox.showinfo('login','you have logged in successfully\n wait for a while for program to complete the processing!')
        #print('verification was done')  
        user_frame.pack_forget()
        working_frame.pack(fill = 'both',expand = True)
        
        reg_no_entry.delete(0,tk.END)
        password_entry.delete(0,tk.END)
        
    else:
        msgbox.showerror('Warning','The registration number or password does not exist!')
        #print('the registration number or Password does not Exist!')

    
def login() :
    if reg_no_entry.get() and password_entry.get():
        check_user_details(
            reg_no_entry.get(),
            password_entry.get())
        
            
    else:
        msgbox.showwarning("warning" , "Fill the Entry")
        #database_access.load_data()

'''function for option'''
def proceed():
    if option_var.get() == "Login as student":
        #print("hello")
        user_frame.pack(fill ="both",expand =True)
        main_frame.pack_forget()
        eyeclose_function3()
        #print(option_var.get())   
    elif option_var.get() == "Login as administrator":
        admin_frame.pack(fill = "both",expand =True)
        main_frame.pack_forget()
        eyeclose_function4()
    else:
        msgbox.showwarning("Select","You have not select any option")
        
def submit_function():
    #accessing data from database
    database_access.my_cursor.execute("SELECT * FROM students_record WHERE Username = ? OR Password = ?",(user_name_entry.get(),pass_word_entry.get()))
    result = database_access.my_cursor.fetchall()
    #print(result)
    database_access.connection.commit()
    if result:
        msgbox.showwarning("Username","Username already existed!")
        
    else:
        reg_no = database_access.generate_reg_no()
        database_access.insert_data([f_name_entry.get(),
                                     l_name_entry.get(),
                                     user_name_entry.get(),
                                     mobile_no_entry.get(),
                                     email_entry.get(),
                                     pass_word_entry.get(),
                                     comfirm_entry.get(),
                                     gender_var.get(),
                                     reg_no])
        if pass_word_entry.get() == comfirm_entry.get() and comfirm_entry.get() and pass_word_entry.get():
            msgbox.showinfo("regisration number",F"Dear {f_name_entry.get()} {l_name_entry.get()} your registration number is \n{reg_no}")
            f_name_entry.delete(0,tk.END)
            l_name_entry.delete(0,tk.END)
            user_name_entry.delete(0,tk.END)
            mobile_no_entry.delete(0,tk.END)
            email_entry.delete(0,tk.END)
            pass_word_entry.delete(0,tk.END)
            comfirm_entry.delete(0,tk.END)
            gender_var.set('Other')
    
        
#cheking for admin username and pasword function
def check_admin_info():
    if admin_username_entry.get() and admin_password_entry.get():
        if (
            admin_username_entry.get() =="admin"
            and
            admin_password_entry.get()=="admin"):
            admin_workspace_frame.pack(fill = "both",expand=True)
            admin_frame.pack_forget()
            admin_workspace_frame.update()
            msgbox.showinfo("successfully!",
                            "you have logged successfully.")
            admin_username_entry.delete(0,tk.END)
            admin_password_entry.delete(0,tk.END)
        else:
            msgbox.showwarning("incorrect",
                               "incorrect username or password")
    else:
        msgbox.showwarning("fill","fill in all entry")
    
    
#function to Enlarge admin control frame
def zoom_out(event):
    admin_control_frame.configure(width = 150,height=750) 
    
def zoom_in(event):
    admin_control_frame.configure(width = 50,height = 750)
       
    
    
    

'''back button function1'''
def back_button1():
    sign_up_frame.pack_forget()
    user_frame.pack(fill = "both" , expand = True)
     
'''back button function2'''
def back_button2():
    working_frame.pack_forget()
    user_frame.pack(fill = "both" , expand = True) 
    '''placeholder image label'''
'''back button function3'''
def back_button3():
    user_frame.pack_forget()
    main_frame.pack(fill = "both", expand = True)
    
'''back button function4'''
def back_button4():
    option_var.set("Login mode")
    admin_frame.pack_forget()
    main_frame.pack(fill = "both",expand = True)
'''option frame'''

'''back to main window'''
def home():
    active_btn1.configure(fg_color = "green")
    active_btn2.configure(fg_color = "green")
    active_btn3.configure(fg_color = "green")
    active_btn4.configure(fg_color = "green")
    active_btn5.configure(fg_color = "white")
    
    if msgbox.askyesnocancel("Close","are you sure you want to log out?"):
        
        admin_workspace_frame.pack_forget()
        main_frame.pack(fill = "both",expand = True)
        active_btn3.configure(fg_color = "green")
        option_var.set("Login mode")
    else:
        return None
    
'''function to update student information'''
def update_data():
    active_btn1.configure(fg_color = "white")
    active_btn2.configure(fg_color = "green")
    active_btn3.configure(fg_color = "green")
    active_btn4.configure(fg_color = "green")
    active_btn5.configure(fg_color = "green")
    
'''function to view student information'''
def view_data():
    active_btn1.configure(fg_color = "green")
    active_btn2.configure(fg_color = "white")
    active_btn3.configure(fg_color = "green")
    active_btn4.configure(fg_color = "green") 
    active_btn5.configure(fg_color = "green")


def exam_setting():
    active_btn1.configure(fg_color = "green")
    active_btn2.configure(fg_color = "green")
    active_btn3.configure(fg_color = "white")
    active_btn4.configure(fg_color = "green")
    active_btn5.configure(fg_color = "green")


def add_ques():
    active_btn1.configure(fg_color = "green")
    active_btn2.configure(fg_color = "green")
    active_btn3.configure(fg_color = "green")
    active_btn4.configure(fg_color = "white")
    active_btn5.configure(fg_color = "green")
    update_data_frame.pack_forget()
    add_ques_frame.pack(fill = "both",expand = True)
    ques = Generate_question(add_ques_frame,question_task_frame)
    ques.enter_frame()
    
''''function to display test environment frame'''
def start_display_function():
    global selection_list
    if subject_var.get() == "None":
        msgbox.showwarning("Subject","You have not select any subject!")

    else:
        working_frame.pack_forget()
        start_display_frame.pack(fill = "both",expand = True)
        selected_option.set(None)
        selected_subject = f"SUBJECT:\n{subject_var.get()}"
        subject_label.configure(text = selected_subject)
        display_question(question_no)
        print(f"the option list:{selection_list}")
        #timer(3,0)
        working_frame.update()
        
'''submitting exam functon'''
def submit_fnt():
    if msgbox.askyesnocancel("Submit","are you sure you want to submit?"):
        start_display_frame.pack_forget()
        # user_frame.pack(fill = "both",expand = True)
        subject_var.set("None")
        display_result()
        
    else:
        pass
'''function to return main page'''

main_frame = ctk.CTkFrame(root,
                          width = 900,
                          height = 650)
main_frame.pack(fill = "both",expand = True)
''' the user frame'''
user_frame = ctk.CTkFrame(root ,
                          width = 900 , 
                          height = 650 ,
                          bg_color= "transparent",
                          #fg_color = "#035",
                          corner_radius= 10)
#user_frame.pack(fill = "both", expand = True)
admin_frame = ctk.CTkFrame(root,
                           width = 900,
                           height = 650,
                           bg_color = "transparent")

canvas1 = ctk.CTkCanvas(main_frame,
                        width =option_frame_path.width,
                        height = option_frame_path.height)
canvas1.pack(fill = "both",expand = True)

canvas1.create_image(0,0 ,image = option_frame_photo,anchor = "nw")
'''frame title label'''
canvas1.create_text(600,30,
                    text="COMPUTER BASE TEST FOR SECONDARY SCHOOL STUDENTS",
                    font=("Arial black",25,"bold"))

canvas2 = ctk.CTkCanvas(user_frame,
                        width =logo_image_path1.width,
                        height =logo_image_path1.height)
canvas2.pack(fill = "both",expand = True)

canvas2.create_image(0,0 ,
                     image = logo_photo1,
                     anchor ="nw"  )
#title label
canvas2.create_text(600,30,
                    text ="EDUCATION FOR BETTER TOMORROW!",
                    font = ("Arial black",25,"bold"),
                    fill="black")
#admin side
canvas3 = ctk.CTkCanvas(admin_frame,
                        width =admin_frame_path.width,
                        height = admin_frame_path.height)
canvas3.pack(fill = "both",expand = True)

canvas2.create_text(430,320,text = "Registration Number",
                    font = ("Arial",12,"bold"),
                    fill="black")
canvas2.create_text(390,380,text = "Password",
                    font=("Arial",12,"bold"),
                    fill="black")
canvas3.create_image(0,0,
                     image = admin_frame_photo,

                     anchor = "nw" )
#admin username label
canvas3.create_text(200,100,
                    text = "Admin Username",
                    font=("Arial",16,"bold"),
                   fill="light blue" )
'''admin  username entry'''
admin_username_entry = ctk.CTkEntry(admin_frame,
                           width=250,
                           placeholder_text="e.g-admin username here")
admin_username_entry.place(x = 114, y = 112 )
#admin password label
canvas3.create_text(200,170,
                    text="Admin Password" ,
                    font=("Arial",16,"bold"),
                    fill="light blue")
#admin password entry
admin_password_entry = ctk.CTkEntry(admin_frame,
                           width=250,
                           placeholder_text="e.g-admin password here")
admin_password_entry.place(x = 114, y = 180)
#admin login utton
admin_login_button = ctk.CTkButton(admin_frame,
                                   text="Login",
                                   fg_color="green",
                                   font=("Arial",16,"bold"),
                                   bg_color="green",
                                   hover_color="black",
                                   command = check_admin_info)
admin_login_button.place(x = 170,y =220)


'''login option'''
login_option = ctk.CTkComboBox(main_frame,
                           values = option_list,
                           variable = option_var,
                           button_hover_color ="gray",
                           fg_color = "white",
                           corner_radius = 50,
                           dropdown_hover_color = "gray",
                           width = 200)
login_option.place(x =100, y = 100)

proceed_btn = ctk.CTkButton(main_frame,
                            text = "proceed",
                            font = ("Arial",14 ,"bold"),
                            text_color = "white",
                            cursor = "hand2",
                            hover_color = "gray",
                            fg_color = "black",
                            corner_radius = 50,
                            command = proceed)
proceed_btn.place(x = 120, y = 150 )
'''active button'''


reg_no_entry = ctk.CTkEntry(user_frame,
                              width = 300,
                              font=("Arial", 12 , "bold"),
                              #corner_radius = 50,
                              placeholder_text = "e.g - CAN/25/00")
reg_no_entry.place( x = 350 , y = 330 )

password_entry = ctk.CTkEntry(user_frame,
                            width = 300 ,
                            show = "*",
                            #textvariable = passwordvar3,
                            font=("Arial",12 ,"bold"),
                              #corner_radius = 50,
                              placeholder_text = "e.g -1234567abcd"
                              )
password_entry.place( x = 350 , y = 390 )


'''show image'''


hide_image_path3 = r"C:\Users\owner\Desktop\CBT_PROJECT\show.png"
hide_image3= Image.open(hide_image_path3)
hide_photo3 = ImageTk.PhotoImage(hide_image3)
print(f"Your password was hided")

show_image_path3 = r"C:\Users\owner\Desktop\CBT_PROJECT\hide.png"
show_image3= Image.open(show_image_path3)
show_photo3 = ImageTk.PhotoImage(show_image3)
print(f"Your password was hided")

'''get password 1'''
hide_image_path1 = r"C:\Users\owner\Desktop\CBT_PROJECT\show.png"
hide_image1 = Image.open(hide_image_path1)
hide_photo1 = ImageTk.PhotoImage(hide_image1  )
#print(f"Your visibled password was : {pass_word_entry.get()}")

show_image_path1 = r"C:\Users\owner\Desktop\CBT_PROJECT\hide.png"
show_image1 = Image.open(show_image_path1)
show_photo1 = ImageTk.PhotoImage(show_image1)
print(f"Your password was hided")

'''get comfirm password'''
hide_image_path2 = r"C:\Users\owner\Desktop\CBT_PROJECT\show.png"
hide_image2 = Image.open(hide_image_path2)
hide_photo2 = ImageTk.PhotoImage(hide_image2)
print(f"Your password was hided")

show_image_path2 = r"C:\Users\owner\Desktop\CBT_PROJECT\hide.png"
show_image2 = Image.open(show_image_path2)
show_photo2 = ImageTk.PhotoImage(show_image2)
#print(f"Your visibled password was : {comfirm_entry.get()}")

'''get comfirm password'''
hide_image_path4 = r"C:\Users\owner\Desktop\CBT_PROJECT\show.png"
hide_image4 = Image.open(hide_image_path4)
hide_photo4 = ImageTk.PhotoImage(hide_image4)
print(f"Your password was hided")

show_image_path4 = r"C:\Users\owner\Desktop\CBT_PROJECT\hide.png"
show_image4 = Image.open(show_image_path4)
show_photo4 = ImageTk.PhotoImage(show_image4)


show_button3 = ctk.CTkButton(user_frame ,
                                image = show_photo3,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeopen_function3)
show_button3.place( x = 615 , y = 392)
print(password_entry.get())
    


login_button = ctk.CTkButton(user_frame ,
                             text = "Login ",
                             font = ("Arial" , 16 , "bold"),
                             hover_color = "#025",
                             cursor = "hand2",
                             #corner_radius = 50,
                             fg_color = "green",
                             border_width=0,
                             bg_color="green",
                             command = login)
login_button.place(x = 420 , y = 430)


sign_up_button = ctk.CTkButton(user_frame ,
                               text = "Sign Up Here ?" ,
                               bg_color = "black",
                               fg_color = "black",
                               hover_color = "#1475dd", 
                               cursor = "hand2",
                               font = ("arial",12,"bold"),
                               command = signup_frame)
sign_up_button.place(x = 420 , y = 490)

sign_up_frame = ctk.CTkFrame(root , 
                             bg_color= "green",
                             fg_color = "white")
sign_up_frame.pack_forget()

print("hello")
#working frame
working_frame = ctk.CTkFrame(root,
                             fg_color = 'white',
                             bg_color = 'white',
                             border_width = 5,
                             border_color ="black")
#test environment frame
start_display_frame = ctk.CTkFrame(root,
                                  border_width = 10,
                                  border_color = "dark blue",
                                  corner_radius = 0,
                                  fg_color="white")
display_question_label = ctk.CTkLabel(start_display_frame,
                                          text =f"Q{question_no + 1}. {questions[question_no]}",
                                          font=("Arial",25,"bold"))
display_question_label.place(x =30,y = 80)
"""result frame"""
result_frame = ctk.CTkFrame(root,
                            fg_color= "white",
                            border_width = 20,
                            border_color = "green",
                            corner_radius = 20)

init_postion = 180
selected_option.set(" ")
option_list = []
alphabets = ["A","B","C","D"]
for alphabet, option in zip(alphabets,options[question_no]) :

    radio_bttn = tk.Radiobutton(start_display_frame,
                                     text = f"{alphabet}. {option}" ,
                                     variable = selected_option,
                                     value = option,
                                     font=("Arial",12,"normal"),
                                     background = "white",
                                     cursor = "hand2")
    radio_bttn.place(x = 30,y = init_postion)
    option_list.append(radio_bttn)
    init_postion += 40
    #print(option_list)        
    




#time and other frame
time_frame = ctk.CTkFrame(start_display_frame,
                          border_width =5,
                          border_color = "dark blue",
                          fg_color = "light green",
                          corner_radius = 0,
                          width=1200,height=50)
time_frame.place(x = 0,y = 0)
#subject label
subject_label = ctk.CTkLabel(time_frame,
                             text = selected_subject,
                             font =("Arial",16,"bold"))
subject_label.place(x = 8,y = 7)

duration_label = ctk.CTkLabel(time_frame,
                             text ="DURATION:\n40:00mins",
                             font =("Arial",16,"bold"))
duration_label.place(x = 200,y = 7)


q_remain_label = ctk.CTkLabel(time_frame,
                             text =F"QUESTION:\n {question_no + 1}/{total_questions} ",
                             font =("Arial",16,"bold"))
q_remain_label.place(x = 450,y = 7)

time_remain_label = ctk.CTkLabel(time_frame,
                              text = " ",
                              font =("Arial",16,"bold"))
time_remain_label.place(x = 600,y = 7)

#the next button
next_button = ctk.CTkButton(start_display_frame,
                            text= "NEXT",
                            font=("Arials",16,"bold"),
                            fg_color= "light green",
                            hover_color="green",
                            cursor = "hand2",
                            width = 20,
                            text_color="black",
                            command =next_question)
next_button.place(x = 400 ,y = 640 )

'''previous button'''
previous_button = ctk.CTkButton(start_display_frame,
                            text= "PREVIOUS",
                            font=("Arials",16,"bold"),
                            fg_color= "orange",
                            hover_color="green",
                            cursor = "hand2",
                            width = 50,
                            text_color="black",
                            command =previous_function)

'''timer function'''
def timer(minute,second):
        
    total_time =minute*60 + second
    while total_time >=0 :
            if submit_fnt():
                break
            else:
                mins = total_time//60
                secs = total_time % 60
                print(f"{mins:02d}:{secs:02d}",end = "\r")
                time_remain_label.configure(text =f"TIME REMAINED:\n {mins:02d}:{secs:02d}")
                time.sleep(1)
                total_time -= 1
                time_remain_label.update()
        
    start_display_frame.pack_forget()
    result_frame.pack(fill = "both",expand = True)
    display_result()
    #user_frame.pack(fill = "both",expand = True)
    subject_var.set("None")
        
#student details frame

student_details_frame = ctk.CTkFrame(start_display_frame,
                          border_width =5,
                          border_color = "dark blue",
                          fg_color = "light green",
                          corner_radius = 0,
                          width=260,
                          height=700)
student_details_frame.place(x = 1100,y = 0)

#profile image label
profile_image = ctk.CTkLabel(student_details_frame,
                             text = "",
                             image = student_photo)
profile_image.place(x = 53 ,y =80)
#submit button
submit_button1 = ctk.CTkButton(student_details_frame,
                               text = "SUBMIT",
                               font = ("Arial",16,"bold"),
                               corner_radius = 50,
                               cursor = "hand2",
                               command = submit_fnt)
submit_button1.place(x=35,y = 200)
#student name label
full_name_label = ctk.CTkLabel(student_details_frame,
                            text= "NAME:",
                            font=("Arial",16,"bold","underline"))
full_name_label.place(x = 65, y = 250)

# reg number
reg_no_label = ctk.CTkLabel(student_details_frame,
                            text= "REG NO:",
                            font=("Arial",16,"bold","underline"))
reg_no_label.place(x = 60, y = 350)

select_cs_lbl = ctk.CTkLabel(working_frame,
                             text = "select subject",
                             font = ("Arial",14,"bold"),
                             text_color="black",
                             fg_color="white")
select_cs_lbl.place(x = 400,y = 175)

subject_option = ctk.CTkComboBox(working_frame,
                                  variable = subject_var,
                                  values = subject_list,
                                  dropdown_text_color ="black",
                                  dropdown_hover_color = "green",
                                  dropdown_fg_color = "light gray")
subject_option.place(x = 400,y = 200)
# start button
start_button = ctk.CTkButton(working_frame,
                             text = "START",
                             text_color = "black",
                             font = ("Arial",20,"bold"),
                             cursor = "hand2",
                             hover_color = "light green",
                             command = start_display_function)
start_button.place(x = 500,y = 500 )
#option frame
instruction_frame =ctk.CTkFrame(working_frame ,
                           width=350,
                           height = 750,
                           fg_color = "light green",
                           border_width = 5,
                           border_color ="black")
instruction_frame.pack(side = "left")
#introction label
instruction_label = ctk.CTkLabel(instruction_frame,
                                 text = "INSTRUCTION",
                                 font = ("Arial",20,"bold","underline"),
                                 bg_color="light green",
                                 fg_color = "light green",
                                 text_color = "black")
instruction_label.place(x = 80,y = 10)
#instruction text
instructio_text = ctk.CTkLabel(instruction_frame,
                               text =instruction,
                               wraplength = 200,
                               font = ("Arial",16,"bold"))
instructio_text.place(x = 50,y = 50)
#admin workspace
admin_workspace_frame =ctk.CTkFrame(root)
admin_control_frame = ctk.CTkFrame(admin_workspace_frame,
                                   width=50,
                                   height=750,
                                   corner_radius = 0,
                                   #cursor = "hand2",
                                   fg_color="green")
admin_control_frame.pack(side ="left")
admin_control_frame.bind("<Enter>", zoom_out)
admin_control_frame.bind("<Leave>",zoom_in) 

'''frame for updating data'''
update_data_frame = ctk.CTkFrame(admin_workspace_frame,
                                  width =1400,
                                  height = 700,
                                  fg_color ="white",
                                  border_width =10,
                                  corner_radius = 0,
                                  border_color = "green")
update_data_frame.pack(side = "right")

"""welcome message"""
welcome_label = ctk.CTkLabel(update_data_frame,
                             text = "WELCOME TO ADMIN SECTION",
                             text_color = "black",
                             font = ("Arial",40,"bold","underline"))
welcome_label.place(x = 400, y = 100)

"""question frame"""
add_ques_frame = ctk.CTkFrame(admin_workspace_frame,
                                  width =1400,
                                  height = 700,
                                  fg_color ="white",
                                  border_width =10,
                                  corner_radius = 0,
                                  border_color = "green")

"""add question task frame"""
question_task_frame = ctk.CTkFrame(admin_workspace_frame,                            
                                    width = 1400,
                                    height = 700,
                                    fg_color = "white",
                                    border_width = 10,
                                    corner_radius = 0,
                                    border_color = "green"  )
                              
'''active button'''
active_btn1 = ctk.CTkLabel(admin_control_frame,
                           fg_color="green",
                           width=14,
                           height=14,
                           text="")
active_btn1.place(x=2,y=18)

active_btn2 = ctk.CTkLabel(admin_control_frame,
                           fg_color="green",
                           width=14,
                           height=14,
                           text="")
active_btn2.place(x=2,y=68)

active_btn3 = ctk.CTkLabel(admin_control_frame,
                           fg_color="green",
                           width=14,
                           height=14,
                           text="")
active_btn3.place(x=2,y=120)

active_btn4 = ctk.CTkLabel(admin_control_frame,
                           fg_color="green",
                           width=14,
                           height=14,
                           text="")
active_btn4.place(x=2,y=168)


active_btn5 = ctk.CTkLabel(admin_control_frame,
                           fg_color="green",
                           width=14,
                           height=14,
                           text="")
active_btn5.place(x=2,y=650)


#icon1 photo label
icon1_image_button = ctk.CTkButton(admin_control_frame,
                           image=icon1_photo,
                           text = "",
                           cursor = "hand2",
                           width = 25,
                           height = 25,
                           fg_color="green",
                           border_width=0,
                           command = update_data)
icon1_image_button.place(x=6, y=10)
icon1_image_button.bind("<Enter>",zoom_out)
icon1_image_button.bind("<Leave>",zoom_in)
icon1_text_label = ctk.CTkLabel(admin_control_frame,
                           text = "Update data",
                           font =("arial",13,"bold"),
                           fg_color = "green",
                           text_color = "white",
                           bg_color="green",
                           cursor = "hand2")
icon1_text_label.place(x=50,y=10 )

icon2_image_button = ctk.CTkButton(admin_control_frame,
                           image=icon2_photo,
                           text = "",
                           cursor = "hand2",
                           width=25,
                           height=25,
                           fg_color="green",
                           border_width=0,
                           command = view_data)
icon2_image_button.place(x=6, y=60)
icon2_image_button.bind("<Enter>",zoom_out)
icon2_image_button.bind("<Leave>",zoom_in)

icon2_text_label = ctk.CTkLabel(admin_control_frame,
                           text = "View data",
                           font =("arial",13,"bold"),
                           fg_color = "green",
                           text_color = "white",
                           bg_color="green",
                           cursor = "hand2")
icon2_text_label.place(x=50,y=60 )

icon3_image_button = ctk.CTkButton(admin_control_frame,
                           image=icon3_photo,
                           text = "",
                           cursor = "hand2",
                           width=25,
                           height=25,
                           fg_color="green",
                           border_width=0,
                           command = exam_setting)
icon3_image_button.place(x=6, y=110)
icon3_image_button.bind("<Enter>",zoom_out)
icon3_image_button.bind("<Leave>",zoom_in)

icon3_text_label = ctk.CTkLabel(admin_control_frame,
                           text = "Exam setup",
                           font =("arial",13,"bold"),
                           fg_color = "green",
                           text_color = "white",
                           bg_color="green",
                           cursor = "hand2")
icon3_text_label.place(x=50,y=110 )

icon4_image_button = ctk.CTkButton(admin_control_frame,
                           image=icon4_photo,
                           text = "",
                           cursor = "hand2",
                           width=25,
                           height=25,
                           fg_color="green",
                           border_width=0,
                           command = add_ques)
icon4_image_button.place(x=6, y=160)
icon4_image_button.bind("<Enter>",zoom_out)
icon4_image_button.bind("<Leave>",zoom_in)

icon4_text_label = ctk.CTkLabel(admin_control_frame,
                           text = "Set Questions",
                           font =("arial",13,"bold"),
                           fg_color = "green",
                           text_color = "white",
                           bg_color="green",
                           cursor = "hand2")
icon4_text_label.place(x=50,y=160 )




icon5_image_button = ctk.CTkButton(admin_control_frame,
                           image=icon5_photo,
                           text = "",
                           cursor = "hand2",
                           width=25,
                           height=25,
                           fg_color="green",
                           border_width=0,
                           command =home )
icon5_image_button.place(x=6, y=640)
icon5_image_button.bind("<Enter>",zoom_out)
icon5_image_button.bind("<Leave>",zoom_in)

icon5_text_label = ctk.CTkLabel(admin_control_frame,
                           text = "Logout",
                           font =("arial",13,"bold"),
                           fg_color = "green",
                           text_color = "white",
                           bg_color="green",
                           cursor = "hand2")
icon5_text_label.place(x=50,y=640 )


show_button1 = ctk.CTkButton(sign_up_frame ,
                                image = show_photo1,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeopen_function1)
show_button1.place( x = 314 , y = 432)

'''eyeopen button2'''
show_button2 = ctk.CTkButton(sign_up_frame,
                                image = show_photo2,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeopen_function2)
show_button2.place( x = 314 , y = 492)

'''eyeopen button2'''
show_button4 = ctk.CTkButton(admin_frame,
                                image = show_photo4,
                                text =" ",
                                width = 0.0001,
                                height = 0.00001,
                                border_spacing = 0,
                                fg_color = "white",
                                bg_color = "white",
                                hover_color = "white",
                                corner_radius = 50,
                                cursor = "hand2",
                                command = eyeopen_function4)
show_button4.place( x = 331 , y = 183)


'''left sign up  frame logo label'''
logo_label2 = ctk.CTkLabel(sign_up_frame,
                           image = logo_photo2 ,
                           text = " ")
logo_label2.place(x = 70 , y = 5)
'''right sign up  frame logo label'''
logo_label3 = ctk.CTkLabel(sign_up_frame, 
                           image = logo_photo3,
                           text = " ")
logo_label3.place(x = 1100 , y = 5)
#delele button
# delete_button = ctk.CTkButton(sign_up_frame)
# delete_button.pack()
'''back button'''
back_button1 = ctk.CTkButton(sign_up_frame ,
                            image = back_button_photo ,
                            text= " " ,
                            fg_color = "white" ,
                            hover_color = "white" ,
                            cursor = "hand2" ,
                            width = 0.001 ,
                            command = back_button1)
back_button1.place( x = 5 , y = 20)

back_button2 = ctk.CTkButton(working_frame ,
                            image = back_button_photo ,
                            text= " ",
                            fg_color = 'white',
                            bg_color = 'white',
                            hover_color = 'white',
                            cursor = "hand2" ,
                            width = 0.001 ,
                            command = back_button2)
back_button2.place( x = 350 , y = 5)
#back to the home main window 
back_button3 = ctk.CTkButton(user_frame ,
                            image = back_button_photo ,
                            text= " ",
                            fg_color = 'white',
                            bg_color = 'white',
                            hover_color = 'white',
                            cursor = "hand2" ,
                            width = 0.001 ,
                            border_width = 0,
                            command = back_button3)
back_button3.place( x = 5 , y = 5)

back_button4 = ctk.CTkButton(admin_frame ,
                            image = back_button_photo ,
                            text= " ",
                            fg_color = 'white',
                            bg_color = 'white',
                            hover_color = 'white',
                            cursor = "hand2" ,
                            width = 0.001 ,
                            border_width = 0,
                            command = back_button4)
back_button4.place( x = 5 , y = 5)



sign_up_label = ctk.CTkLabel(sign_up_frame, text = " NEW STUDENT REGISTRATION FORM ",
                             font = ("Arial",35 ,"bold"),
                             bg_color= "white",
                             fg_color = "white",
                             text_color ="green" ,
                             corner_radius = 100
                             )
sign_up_label.pack(side = "top" ,expand = True, pady = (0,600),padx = (20,0)) 
'''first name label'''
f_name_label = ctk.CTkLabel(sign_up_frame ,
                            text = "First Name" ,
                            font = ("Arial", 16 ,"bold"),
                            text_color = "black")
f_name_label.place(x = 50 , y = 107)
'''first name entry'''
f_name_entry = ctk.CTkEntry(sign_up_frame ,
                            width = 300,
                            placeholder_text = "e.g - Yusha'u",
                            )
f_name_entry.place(x = 50, y = 130 )

'''last name label'''
l_name_label = ctk.CTkLabel(sign_up_frame ,
                            text = "Last Name" ,
                            font = ("Arial", 16 ,"bold"),
                            text_color = "black")
l_name_label.place(x = 50 , y = 167)
'''first name entry'''
l_name_entry = ctk.CTkEntry(sign_up_frame ,
                            width = 300,
                            #corner_radius = 50,
                            placeholder_text = " e.g - Abdullahi")
l_name_entry.place(x = 50, y = 190 )

'''User name label'''
user_name_label = ctk.CTkLabel(sign_up_frame ,
                            text = "UserName" ,
                            font = ("Arial", 16 ,"bold"),
                            text_color = "black")
user_name_label.place(x = 50 , y = 227)
'''Username entry'''
user_name_entry = ctk.CTkEntry(sign_up_frame ,
                               width = 300,
                               #corner_radius = 50,
                               placeholder_text = "e.g - Engineer1234")
user_name_entry.place(x = 50, y = 250 )

'''Mobile number label'''
mobile_no_label = ctk.CTkLabel(sign_up_frame ,
                            text = "Mobile No" ,
                            font = ("Arial", 16 ,"bold"),
                            text_color = "black")
mobile_no_label.place(x = 50 , y = 287)
'''Mobile number entry'''
mobile_no_entry = ctk.CTkEntry(sign_up_frame ,
                               width = 300,
                               #corner_radius = 50,
                               placeholder_text = " e.g - 08012345678")
mobile_no_entry.place(x = 50, y = 310 )


'''Email label'''
email_label = ctk.CTkLabel(sign_up_frame ,
                            text = "Email Address" ,
                            font = ("Arial", 16 ,"bold"),
                            text_color = "black")
email_label.place(x = 50 , y = 347)
'''Email  entry'''
email_entry = ctk.CTkEntry(sign_up_frame ,
                           width = 300,
                           #corner_radius = 50,
                           placeholder_text = "e.g - myapp1234@gmail.com")
email_entry.place(x = 50, y = 370 )

'''Password label'''
pass_word_label = ctk.CTkLabel(sign_up_frame ,
                            text = "Password" ,
                            font = ("Arial", 16 ,"bold"),
                            text_color = "black")
pass_word_label.place(x = 50 , y = 407)
'''Password entry'''
pass_word_entry = ctk.CTkEntry(sign_up_frame ,
                               width = 300,
                               show = "*",
                               #corner_radius = 50,
                               placeholder_text = " e.g -  123456789 ")
pass_word_entry.place(x = 50, y = 430 )

'''Comfirm label label'''
comfirm_label = ctk.CTkLabel(sign_up_frame ,
                            text = "Comfirm" ,
                            font = ("Arial", 16 ,"bold"),
                            text_color = "black")
comfirm_label.place(x = 50 , y = 467)
'''Comfirm entry'''
comfirm_entry = ctk.CTkEntry(sign_up_frame ,
                             width = 300,
                             show = "*",
                             #corner_radius = 50,
                             placeholder_text = " e.g - 123456789"
                             )
comfirm_entry.place(x = 50, y = 490 )

'''gender label'''
gender_label = ctk.CTkLabel(sign_up_frame ,
                            text = "Gender" ,
                            font = ("Arial", 16 ,"bold"),
                            text_color = "black")
gender_label.place(x = 50 , y = 527)
'''the combox'''
gender_option = ctk.CTkComboBox(sign_up_frame ,
                                variable = gender_var,
                                values = my_list,
                                #corner_radius = 50,
                                width =300)
gender_option.place( x = 50 ,y = 550)

'''getting student image'''
std_image_button = ctk.CTkButton(sign_up_frame ,
                                 text = "Profile Picture?" ,
                                 text_color = "white",
                                 bg_color = "white",
                                 fg_color = "blue",
                                 hover_color = "gray",
                                 corner_radius = 50,
                                 font = ("arial",16,"bold"),
                                 command = None)
std_image_button.place(x = 600 , y= 350)

'''Submit button'''
submit_button = ctk.CTkButton(sign_up_frame , text = "Submit" ,
                              font = ("Arial" , 20 , "bold"),
                              corner_radius = 50,
                              cursor = "hand2",
                              hover_color = "gray",
                              fg_color = "black",
                              text_color = "white",
                              command = submit_function )
submit_button.place(x = 130, y = 600  )

#image_path_label =ctk.CTkLabel(sign_up_frame ,
                               #text = "Image Path:",
                               #font = ("Arial" ,16, "bold") )
#image_path_label.place(x = 460 , y = 350 )  

image_frame = ctk.CTkFrame(sign_up_frame ,
                           width = 180 ,
                           height = 230
                           )
image_frame.place( x = 600 , y = 100 )
#path_frame = ctk.CTkFrame(sign_up_frame, width = 335 , height= 20)
#path_frame.place( x = 555 , y = 353)

'''placeholder image label'''
placeholder_image_label = ctk.CTkLabel(image_frame,
                              image = photo1,
                              text = " "
                                )
placeholder_image_label.pack(fill = "both",
                             expand = False)
#eyeclose_function3()
#eyeclose_function4()
root.mainloop()
database_access.connection.close()