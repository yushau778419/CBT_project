import customtkinter as ctk
import json
from tkinter import messagebox as msgbox

class Generate_question():
    def __init__ (self,target_frame,another_frame):
        self.target_frame = target_frame
        self.another_frame = another_frame
        self.index = 1
            
    """switching to adding question frame"""
    def enter_frame(self):

        self.question_storage = {}
        self.questions = []
        self.main_options = []
        self.answers = []
            
        """main label"""
        main_label = ctk.CTkLabel(self.target_frame,
                                  text = "QUESTION UPLOADER",
                                  font = ("arial",40,"bold","underline"),
                                  text_color = "black")
        main_label.place(x = 400, y = 50)
        """the question input label"""


        question_input_label = ctk.CTkLabel(self.target_frame,
                                            text = "No of Questions",
                                            font = ("arial",20,"bold"),
                                            text_color = "black")
        question_input_label.place(x = 100, y = 200)

        question_no_entry = ctk.CTkEntry(self.target_frame,
                                         width = 200)
        question_no_entry.place(x = 100 , y =  225)

        """the sublect input label"""
        subject_input_label = ctk.CTkLabel(self.target_frame,
                                            text = "Subject Name",
                                            font = ("arial",20,"bold"),
                                            text_color = "black")
        subject_input_label.place(x = 100, y = 300)

        subject_name_entry = ctk.CTkEntry(self.target_frame,
                                         width = 300)
        subject_name_entry.place(x = 100 , y =  325)

        def get_value():
            if (question_no_entry.get() == "" or subject_name_entry.get() == ""):
                msgbox.showwarning("Warning","please fill in all field!")
            else:
                if (type(question_no_entry.get()) == int or type(subject_name_entry.get()) == str):
                    print(type(subject_name_entry.get()))

                    self.target_frame.pack_forget()
                    self.another_frame.pack(fill = "both", expand = True)
                    print(f"the number of question:{question_no_entry.get()}")
                    print(f"subject name :{subject_name_entry.get()}")
                    index_label.configure(text =  f"QUESTION {self.index}/{question_no_entry.get()} ")
                    # question_no_entry.delete(0,ctk.END)
                    # subject_name_entry.delete(0,ctk.END)
                else:
                    msgbox.showwarning("Warning","the question number must be interger type,\n and the subject name must be a word without space!")
                    question_no_entry.delete(0,ctk.END)
                    subject_name_entry.delete(0,ctk.END)
        """the function to save and move to next """
        def save_entry():
            self.options = []
            if (
                question_entry.get("0.0","end") == "" 
                or
                option_entry1.get() == ""
                or
                option_entry2.get() == ""
                or
                option_entry3.get() == ""
                or
                option_entry4.get() == ""
                or
                answer_entry.get() == ""
            ):
                msgbox.showwarning("Field","fill in all the field!")
            else:


                if self.index  < int (question_no_entry.get()) + 1:
                    self.index += 1
                    index_label.configure(text =  f"QUESTION {self.index}/{question_no_entry.get()} ")
                    
                    self.questions.append(question_entry.get("0.0","end"))
                    self.options.append(option_entry1.get())
                    self.options.append(option_entry2.get())
                    self.options.append(option_entry3.get())
                    self.options.append(option_entry4.get())
                    self.main_options.append(self.options)
                    self.answers.append(answer_entry.get())

                    self.question_storage["Questions"] = self.questions
                    self.question_storage["Options"] = self.main_options
                    self.question_storage["Answers"] = self.answers

                    print(self.question_storage)
                    save_file(self.question_storage)



                    print(self.index)
                    print(question_entry.get("0.0" , "end"))


                    """clearing the entry"""
                    question_entry.delete("0.0", "end")
                    option_entry1.delete(0,ctk.END)
                    option_entry2.delete(0,ctk.END)
                    option_entry3.delete(0,ctk.END)
                    option_entry4.delete(0,ctk.END)
                    answer_entry.delete(0,ctk.END)

                if self.index == int(question_no_entry.get()) + 1:
                    index_label.configure(text = "Data Uploaded Successfully!.")
                    save_button.place_forget()
                    finish_button.place(x = 650 , y = 560)
                    
                else:
                    pass


        def save_file(question_list):
            """creating the question bank"""
            filename = f"{subject_name_entry.get()}.json"
            with open(filename,"w") as file:
                json.dump(question_list,file , indent = 3)

        def return_to_base():
            question_no_entry.delete(0,ctk.END)
            subject_name_entry.delete(0,ctk.END)
            self.another_frame.pack_forget()
            self.target_frame.pack(fill = "both", expand = True)
            finish_button.place_forget()
            save_button.place(x = 550, y = 560)
            while self.index !=1 :
                self.index -= 1

            


            """main label"""
        main_label = ctk.CTkLabel(self.another_frame,
                                  text = "QUESTION UPLOADER",
                                  font = ("arial",40,"bold","underline"),
                                  text_color = "black")
        main_label.place(x = 400, y = 50)

        """the label for the question iput"""
        ques_label = ctk.CTkLabel(self.another_frame,
                                  text = "WRITE YOUR QUESTION BELOW",
                                  font = ("arial",16,"bold"),
                                  text_color = "black")
        ques_label.place(x = 60, y = 120)

        """the text entry for the qustion"""
        question_entry = ctk.CTkTextbox(self.another_frame,
                                        width = 350,
                                        height = 500,
                                        border_color = "black",
                                        border_width = 4,
                                        font = ("Arial",14,"bold"))
        question_entry.place(x = 20, y = 150)
        
        """main option label"""
        option_label = ctk.CTkLabel(self.another_frame,
                                     text = "OPTIONS",
                                     font = ("Arial",25,"bold","underline"),
                                     text_color = "black")
        option_label.place(x = 590 , y = 140)

        """the option labels and entry"""
        option_label1 = ctk.CTkLabel(self.another_frame,
                                     text = "Option1",
                                     font = ("Arial",16,"bold"),
                                     text_color = "black")
        option_label1.place(x = 400 , y = 175)

        option_entry1 = ctk.CTkEntry(self.another_frame,
                                     width = 500,
                                     placeholder_text = "Option 1")
        option_entry1.place(x = 400,y = 200)


        option_label2 = ctk.CTkLabel(self.another_frame,
                                     text = "Option2",
                                     font = ("Arial",16,"bold"),
                                     text_color = "black")
        option_label2.place(x = 400 , y = 235)

        option_entry2 = ctk.CTkEntry(self.another_frame,
                                     width = 500,
                                     placeholder_text = "Option 2")
        option_entry2.place(x = 400,y = 260)


        option_label3 = ctk.CTkLabel(self.another_frame,
                                     text = "Option3",
                                     font = ("Arial",16,"bold"),
                                     text_color = "black")
        option_label3.place(x = 400 , y = 295)

        option_entry3 = ctk.CTkEntry(self.another_frame,
                                     width = 500,
                                     placeholder_text = "Option 3")
        option_entry3.place(x = 400,y = 320)

        option_label4 = ctk.CTkLabel(self.another_frame,
                                     text = "Option4",
                                     font = ("Arial",16,"bold"),
                                     text_color = "black")
        option_label4.place(x = 400 , y = 355)

        option_entry4 = ctk.CTkEntry(self.another_frame,
                                     width = 500,
                                     placeholder_text = "Option 4")
        option_entry4.place(x = 400,y = 380)
        """the answer main label"""
        answer_label = ctk.CTkLabel(self.another_frame,
                                     text = "ANSWER",
                                     font = ("Arial",25,"bold","underline"),
                                     text_color = "black")
        answer_label.place(x = 590 , y = 430)

        answer_lb = ctk.CTkLabel(self.another_frame,
                                 text = "Answer",
                                 font = ("Arial",16,"bold"),
                                 text_color = "black")
        answer_lb.place(x = 400, y = 480)

        answer_entry = ctk.CTkEntry(self.another_frame,
                                     width = 450,
                                     placeholder_text = "Your answer here")
        answer_entry.place(x = 400,y = 505)

        """index label"""
        index_label = ctk.CTkLabel(self.another_frame,
                                   text = " ",
                                   font = ("Arial",20,"bold"),
                                   text_color = "black")
        index_label.place(x = 950, y = 180)
        
        save_button = ctk.CTkButton(self.another_frame,
                                    text = "SAVE",
                                    font = ("Arial",25,"bold"),
                                    fg_color = "green",
                                    hover_color = "black",
                                    cursor = "hand2",
                                    corner_radius = 50,
                                    command = save_entry)
        save_button.place(x = 550, y = 560)

        finish_button = ctk.CTkButton(self.another_frame,
                                    text = "FINISH",
                                    font = ("Arial",25,"bold"),
                                    fg_color = "black",
                                    hover_color = "green",
                                    cursor = "hand2",
                                    corner_radius = 50,
                                    command = return_to_base)


        """the button to proceed"""
        proceed_bttn = ctk.CTkButton(self.target_frame,
                                          text = "PROCEED",
                                          text_color = "black",
                                          font = ("arial",20,"bold"),
                                          hover_color = "green",
                                          fg_color = "light blue",
                                          corner_radius = 50,
                                          cursor = "hand2",
                                          command = get_value)
        proceed_bttn.place(x = 400 , y = 500)


