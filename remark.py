import customtkinter as ctk
"""the class for the remark and grade"""
class Notipy():
    def __init__(self,score,frame):
        self.score = score
        self.frame = frame
        self.message1 = " "
        self.message2 = " "


    """the grade function"""
    def comment(self):
        if self.score >= 70:
            self.message1 = "A"
            self.message2 = "EXCELLENT"

        elif self.score >= 60:
            self.message1 = "B"
            self.message2 = "VERY GOOD"

        elif self.score >= 50:
            self.message1 = "C"
            self.message2 = "PASSED"

        elif self.score >= 40:
            self.message1 = "D"
            self.message2 = "PASSED LITTLE"

        elif self.score >= 30:
            self.message1 = "E"
            self.message2 = "PASSED WEAKLY"

        else:
            self.message1 = "F"
            self.message2 = "FAILED"
        """comment label"""
        comment_label = ctk.CTkLabel(self.frame,
                                     text = "COMMENT",
                                     font = ("Arial",25,"bold","underline"))
        comment_label.place(x = 100, y = 250)

        """the grade label""" 
        grade_label = ctk.CTkLabel(self.frame,
                             text =f"GRADE: {self.message1}",
                             font = ("Arial",20,"bold"))
        grade_label.place(x = 100, y = 300)

        """the remark label"""
        remark_label = ctk.CTkLabel(self.frame,
                              text = f"REMARK: {self.message2}",
                              font = ("Arial",20,"bold"))
        remark_label.place(x = 100,y = 330)

        














