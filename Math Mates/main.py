from tkinter import *
from ask_ai import Ask_Ai
from PIL import ImageTk, Image
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import scrolledtext
from ttkthemes import ThemedTk
import customtkinter


    
# simple window name + resizing

root = ThemedTk(theme='Adapta')
root.title('Math Mates')

root.geometry('400x300')
root.resizable(False,False)

root.columnconfigure(0)
root.columnconfigure(1)
root.rowconfigure(0)

root.configure(background='lightgreen')

logo_text_menu_frame = Frame(root)


#logo
root.iconbitmap(r'Assets\logo.ico')

# Custom fonts

bigFont = Font(family = 'Calibri', size = 42, weight = 'bold')
regFont = Font(family = 'Calibri', size = 12, weight = 'bold')
smolFont = Font(family = 'Calibri', size = 9)



def destroy_everything():
    for widget in root.winfo_children():
        widget.destroy()





def write_page_answers():


    def enter_hit():

        
        try:
            ai_frame.destroy
        except:
            pass

        

        ai_loading_popout = ThemedTk('adapta')


        ai_loading_popout.resizable(False,False)

        ai_loading_popout.geometry('750x750')

        ai_loading_popout.configure(background = 'lightgreen')

        ai_loading_popout.title('Math Mates - Step by step Walkthrough')

        ai_loading_popout.iconbitmap(r'Assets\logo.ico')

        ai_frame = Frame(ai_loading_popout)
        loading_frame = Frame(ai_loading_popout)



        loading = Label(text='Loading...', master = loading_frame, font=bigFont, background='lightgreen').grid(row=9, column=0)
        loading_frame.grid(row=9, column=0)
        root.update()


        user_i = user_entry.get()
        ai_response = Label(text=Ask_Ai.step_by_step(user_i), master=ai_frame, wraplength=750, font=smolFont, background='lightgreen').grid(row=8,column=0)
        ai_frame.grid(row=8,column=0)
        loading_frame.destroy()
        ai_frame.update_idletasks()


    root.geometry('400x300')


    #menu
    menu_button = ttk.Menubutton(master = root, text = 'Menu')
    menu_button.grid(row = 1, column = 0, pady = 10)

    button_sub_menu = tk.Menu(master=menu_button, tearoff=False)

    button_sub_menu.add_command(label = 'Step by Step Walkthrough', command=switch_to_step_by_Step_answers)
    button_sub_menu.add_command(label = 'Practice Problems', command=switch_to_practice_problems)



    menu_button.configure(menu=button_sub_menu)



    logo_text_menu_frame = Frame(root)




    #never changing logo + brand name

    title_label = ttk.Label(logo_text_menu_frame, text = 'Math Mates   ', foreground='green', font = bigFont)

    #image - math mates logo

    image = Image.open(r'Assets\logo.png')


    resize_image = image.resize((50, 50))

    img = ImageTk.PhotoImage(resize_image)


    Label_for_image = Label(master = logo_text_menu_frame, image=img)
    Label_for_image.image = img





    title_label.grid(row = 0, column = 1, padx = 10)
    Label_for_image.grid(row = 0, column = 0, padx = 10)


    logo_text_menu_frame.grid(row=0, column = 0)

    title_label.grid(row = 0, column = 1, padx = 10)
    Label_for_image.grid(row = 0, column = 0, padx = 10)



    logo_text_menu_frame.grid(row=0, column = 0)

    wya_label = Label(text = 'You are in: Step-by-Step Walkthrough', font=regFont, foreground='green', background='lightgreen')
    wya_label.grid(row = 3, column=0, pady = 10, padx=5)


    instructions_for_user_entry = Label(text = 'Put ya problem in the field below, mate', font=regFont,background='lightgreen')
    instructions_for_user_entry.grid(row = 4, column=0, pady = 10, padx=5)

    user_entry = Entry(width=30, font=regFont)
    user_entry.grid(row = 6, column=0, pady=5)

    enter_button = Button(text='Enter', font=regFont, command=enter_hit)
    enter_button.grid(row=7,column=0)


def write_page_questions():


    def enter_hit():


        user_in = expanded_entry.get("1.0",END)

        try:
            ai_frame_1.destroy
        except:
            pass

        

        ai_loading_popout_1 = ThemedTk('adapta')

        ai_loading_popout_1.resizable(False,False)

        ai_loading_popout_1.geometry('750x750')

        ai_loading_popout_1.configure(background = 'lightgreen')

        ai_loading_popout_1.title('Math Mates - Practice Questions')

        ai_loading_popout_1.iconbitmap(r'Assets\logo.ico')

        ai_frame_1 = Frame(ai_loading_popout_1)
        loading_frame_1 = Frame(ai_loading_popout_1)

        loading_1 = Label(text='Loading...', master = loading_frame_1, font=bigFont, background='lightgreen').grid(row=9, column=0)
        loading_frame_1.grid(row=9, column=0)
        root.update()



        ai_response = Label(text=Ask_Ai.practice_problems(user_in), master=ai_frame_1, wraplength=750, font=smolFont, background='lightgreen').grid(row=8,column=0)
        ai_frame_1.grid(row=0,column=0)
        loading_frame_1.destroy()
        ai_frame_1.update_idletasks()


    root.geometry('400x375')

    #menu
    menu_button = ttk.Menubutton(master = root, text = 'Menu')
    menu_button.grid(row = 1, column = 0, pady = 10)

    button_sub_menu = tk.Menu(master=menu_button, tearoff=False)

    button_sub_menu.add_command(label = 'Step-by-Step Walkthrough', command=switch_to_step_by_Step_answers)
    button_sub_menu.add_command(label = 'Practice Problems', command=switch_to_practice_problems)




    menu_button.configure(menu=button_sub_menu)



    logo_text_menu_frame = Frame(root)

    #i put spaces here so the white line goes from left to right
    title_label = ttk.Label(logo_text_menu_frame, text = 'Math Mates  ', foreground='green', font = bigFont)

    #image - math mates logo

    image = Image.open(r'Assets\logo.png')


    resize_image = image.resize((50, 50))

    img = ImageTk.PhotoImage(resize_image)


    Label_for_image = Label(master = logo_text_menu_frame, image=img)
    Label_for_image.image = img

    title_label.grid(row = 0, column = 1, padx = 10)
    Label_for_image.grid(row = 0, column = 0, padx = 10)


    logo_text_menu_frame.grid(row=0, column = 0)

    title_label.grid(row = 0, column = 1, padx = 10)
    Label_for_image.grid(row = 0, column = 0, padx = 10)



    logo_text_menu_frame.grid(row=0, column = 0)


    expanded_entry = tk.Text(root, width=35, height=3)
  
    expanded_entry.grid(row = 5, column=0, padx=10) 


    enter_button = Button(text='Enter', font=regFont, command=enter_hit)
    enter_button.grid(row=7,column=0, pady=5)

    instructions_for_user_entry = Label(text = 'Chuck your maths questions here to snag 10 practice problems just like it! For the answers, pop it in our step-by-step solver, mate', font=regFont, wraplength=400,background='lightgreen')
    instructions_for_user_entry.grid(row = 4, column=0, pady = 10, padx=5)


    wya_label = Label(text = 'You are in: Practice Problems', font=regFont, foreground='green',background='lightgreen')
    wya_label.grid(row = 3, column=0, pady = 10, padx=5)


def switch_to_practice_problems():
    destroy_everything()
    write_page_questions()


def switch_to_step_by_Step_answers():
    destroy_everything()
    write_page_answers()


write_page_answers()


root.mainloop()