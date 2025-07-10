DISTORTION_LIST = ["All or Nothing Thinking","Overgeneralization","Mental Filter","Disqualifying the Positive","Jumping to Conclusions","Magnification and Minimization","Emotional Reasoning","Should Statements","Labelling and Mislabelling","Personalization"]
import customtkinter

app = customtkinter.CTk()
app.geometry("800x500")
app.title("Cognitive Distortion Helper")
app.grid_columnconfigure(1,weight=1)
app.grid_rowconfigure(0,weight=1)
# SIDEBAR
sidebar = customtkinter.CTkFrame(master=app)
sidebar.grid(row=0,column=0,padx=20,pady=20,sticky="nsew")
# SIDEBAR BUTTONS
add_button = customtkinter.CTkButton(sidebar,text="Add Distortion")
add_button.grid(row=0,column=0,pady=20)
view_button = customtkinter.CTkButton(sidebar,text="View Distortions")
view_button.grid(row=1,column=0,pady=20)



# MAIN BODY
main_body = customtkinter.CTkScrollableFrame(app)
main_body.grid(row=0,column=1,padx=20,pady=20,sticky="nsew")
main_body.grid_columnconfigure(0,weight=1)
check_box_frame = customtkinter.CTkFrame(main_body)
check_box_frame.grid(row=2,column=0,padx=20,pady=10)


# ADD DISTORTIONS
automatic_thought_label = customtkinter.CTkLabel(main_body,text="Automatic Thought")
automatic_thought_label.grid(row=0,column=0,padx=20,pady=20,sticky="ew")
automatic_thought = customtkinter.CTkTextbox(main_body)
automatic_thought.grid(row=1,column=0,padx=20,sticky="ew")

# DISTORTION CHECKBOXES
the_checkboxes = []
count = 0 
for da_row in range(0,5):
    for assigned_column in range(0,2):
        distortion_check_box = customtkinter.CTkCheckBox(check_box_frame, text=DISTORTION_LIST[count])

        distortion_check_box.grid(row=da_row,column=assigned_column,sticky="ew",padx=10,pady=5)
        the_checkboxes.append(distortion_check_box)
        count += 1



    


app.mainloop()