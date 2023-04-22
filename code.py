import tkinter
from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image 


win = Tk()
win.geometry('500x500')
win.title("My friends Gallery")
#main window with title 



def exit_que():
    answer = messagebox.askquestion("confirm", "Are you sure you want to exit?")
    if answer == "yes":
        win.destroy()
    else: 
        ExitButton = Button(win,text= "Exit", command = exit_que)
        ExitButton.grid(row = 0 , column = 5 , pady = 2 ,)

# function for the exit button so a message would appear  


exit = Button(win, text = 'Exit ', bd = '3' , command = exit_que)
exit.grid(row = 0 , column = 5 , pady = 2)

# button display and characteristics 

def show_friends():
    Adam_picture = "code folder /coursework_images/adam.png"
    image = Image.open(Adam_picture) #opens adamns picture 
    size_image = image.resize((100,100)) # size of the image displayed on the window 
    photo = ImageTk.PhotoImage(size_image) # save all the features of the picture in one variable 'photo'
    
    photo_label = Label(win,image = photo)
    photo_label.grid(row = 1 , column = 1)
    photo_label.grid = photo

    adam_button = Button(win, text = "Adam", font = 'Helvetica 13 bold' , command = "")
    adam_button.grid(row=2,column=1)



show_friends = Button(win, text = 'Show Friends', bd = '3' , command = show_friends )
show_friends.grid(row = 0 , column = 1 , pady = 2)




                     
# button to display friends

clear_all = Button(win, text = 'Clear all', bd = '3' , command = "")

#button to clear all 

delete_friend = Button(win, text = 'Delete a Friend', bd = '3' , command = "")

# button to delete a friend 

add_friend = Button(win, text = 'Add a Friend ', bd = '3' , command = "" )

# button to add a friend 




#x = Button(win , text = 'x' , bd = '1', command = "")


clear_all.grid(row = 0 , column = 2 , pady = 2)
delete_friend.grid(row = 0, column = 3 , pady = 2)
add_friend.grid(row = 0 , column = 4 , pady = 2)


#x.grid(row = 0, column = 6 , pady = 2 )

# displays the buttons on the window and position






win.mainloop()
# keeps the window up until closed 