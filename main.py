DISTORTION_LIST = ["All or Nothing Thinking","Overgeneralization","Mental Filter","Disqualifying the Positive","Jumping to Conclusions","Magnification and Minimization","Emotional Reasoning","Should Statements","Labelling and Mislabelling","Personalization"]
import customtkinter

app = customtkinter.CTk()
app.geometry("800x500")
app.title("Cognitive Distortion Helper")
app.grid_columnconfigure(1,weight=1)
app.grid_rowconfigure(0,weight=1)

# Grid placement functions
def show_main_body():
    view_frame.grid_forget()
    main_body.grid(row=0,column=1,padx=20,pady=20,sticky="nsew")
    main_body.grid_columnconfigure(0,weight=1)
    automatic_thought_label.grid(row=0,column=0,padx=20,pady=20,sticky="ew")
    automatic_thought.grid(row=1,column=0,padx=20,sticky="ew")
    checkbox_label.grid(row=2,column=0,padx=20,pady=20)
    check_box_frame.grid(row=3,column=0,padx=20,pady=10)
    create_checkboxes()
    rational_response_label.grid(row=4,column=0,padx=20,pady=20,sticky="ew")
    rational_response.grid(row=5,column=0,padx=20,pady=20,sticky="ew")
    save_button.grid(row=6,column=0,padx=20,pady=20)

def show_view_body():
    main_body.grid_forget()
    view_frame.grid(row=0,column=1,padx=20,pady=20,sticky="nsew")
    view_frame.grid_columnconfigure((0,1,2,3),weight=1)
    id_header.grid(row=0,column=0,padx=10,pady=10)
    automatic_thought_header.grid(row=0,column=1,padx=10,pady=10)
    thought_distortions.grid(row=0,column=2,padx=10,pady=10)
    rational_response_header.grid(row=0,column=3,padx=10,pady=10)
    da_thought.grid(row=1,column=1,padx=10,pady=10)
    da_distortions.grid(row=1,column=2,padx=10,pady=10)
    da_response.grid(row=1,column=3,padx=10,pady=10)
    
    
# SIDEBAR
sidebar = customtkinter.CTkFrame(master=app)
sidebar.grid(row=0,column=0,padx=20,pady=20,sticky="nsew")
# SIDEBAR BUTTONS
add_button = customtkinter.CTkButton(sidebar,text="Add Distortion",command=show_main_body)
add_button.grid(row=0,column=0,pady=20)
view_button = customtkinter.CTkButton(sidebar,text="View Distortions",command=show_view_body)
view_button.grid(row=1,column=0,pady=10)





# MAIN BODY FRAME
main_body = customtkinter.CTkScrollableFrame(app)
check_box_frame = customtkinter.CTkFrame(main_body)



# ADD DISTORTIONS
# AUTOMATIC THOUGHT TEXTBOX
automatic_thought_label = customtkinter.CTkLabel(main_body,text="Automatic Thought")
automatic_thought = customtkinter.CTkTextbox(main_body)


# DISTORTION CHECKBOXES
checkbox_label = customtkinter.CTkLabel(main_body,text="Category of Mental Distortion")
def create_checkboxes():
    the_checkboxes = []
    count = 0 
    for da_row in range(0,5):
        for assigned_column in range(0,2):
            distortion_check_box = customtkinter.CTkCheckBox(check_box_frame, text=DISTORTION_LIST[count])

            distortion_check_box.grid(row=da_row,column=assigned_column,sticky="ew",padx=10,pady=5)
            the_checkboxes.append(distortion_check_box)
            count += 1

# RATIONAL RESPONSE TEXTBOX
rational_response_label = customtkinter.CTkLabel(main_body,text="Rational Response")
rational_response = customtkinter.CTkTextbox(main_body)

# SAVE BUTTON
save_button = customtkinter.CTkButton(main_body,text="Save")

# VIEW FRAME
view_frame = customtkinter.CTkScrollableFrame(app)

id_header = customtkinter.CTkLabel(view_frame,text="ID")
automatic_thought_header = customtkinter.CTkLabel(view_frame,text="AUTOMATIC THOUGHT")
thought_distortions = customtkinter.CTkLabel(view_frame,text="THOUGHT DISTORTIONS")
rational_response_header = customtkinter.CTkLabel(view_frame,text="RATIONAL RESPONSE")
expand_header = customtkinter.CTkLabel(view_frame,text="EXPAND")

da_thought = customtkinter.CTkTextbox(view_frame)
da_thought.insert("0.0","I'm the only one who makes mistakes.")
da_thought.configure(state="disabled")
da_distortions = customtkinter.CTkTextbox(view_frame)
da_distortions.insert("0.0",'All or Nothing Thinking","Overgeneralization","Mental Filter","Disqualifying the Positive","Jumping to Conclusions","Magnification and Minimization","Emotional Reasoning","Should Statements","Labelling and Mislabelling","Personalization"')
da_distortions.configure(state="disabled")
da_response = customtkinter.CTkTextbox(view_frame)
da_response.insert("0.0",'No you are not the only person that makes mistakes. It literally makes no sense. Even among your peer group you are not the only one that fucked up.')
da_response.configure(state="disabled")




show_main_body()
app.mainloop()