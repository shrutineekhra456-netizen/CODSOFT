import tkinter

r=tkinter.Tk()
r.title("TO DO LIST")
r.config(bg="darkgreen")
r.geometry("400x500")

up=False

def update():
    outputvar.set("")

                                   # function to add new item in list
def addlistbar():
    global up
    if inputvar.get()=="":                                      # run this if user not give input
            outputvar.set("Input bar is empty")

    else:   
        if up==True:                                                    # user choose to update
            selected=lb.curselection()                                  # get the index of selected item (after select for update user can delete the selected item so we need to check)
            if selected and inputvar.get() not in lb.get(0,"end"):      # run this if item is selected and user did not delete it and not in list
                lb.delete(selected[0])                                  # delete the selected item from list
                lb.insert(selected[0],inputvar.get())                   # insert new item at that index
                up=False                                                # unchose update
                outputvar.set("Task updated successfully")
            
            else:                                                       # run this if item is not selected and got delete by user after update call
                up=False
                addlistbar()                                            # so add that item as new item in list
            
        
        else:                                                           # run this if no update call (add new item)
            l=lb.get(0,"end")                                           # check that either new item is already exist in list or not
            if inputvar.get() not in l:                                 # run this if new item already existed
                lb.insert("end",inputvar.get())
                outputvar.set("Task added successfully")
            else:                                                       # run this if task already exist
                outputvar.set("Task already exist")
        
    inputvar.set("")                                        # make the input box empty for new input

    lb.selection_clear(0,"end")                                     # deselect all items
    r.after(1500,update)

                                           # function to update selected item from list
def updatelistbar():
    global up
    l=lb.get(0,"end")                                               # get the list(only one item) of selected item is variable s                     
    if not l:                                                       # run this if list is empty
        outputvar.set("list is empty")
        
    else:                                                           # run this if list is not empty
        selected=lb.curselection()                                  # get the index of selected item
        if selected:                                                # run this if item is selected and update it
            
            inputvar.set(lb.get(selected[0]))
            up=True
            
            
        else:
            outputvar.set("No Task selected")
    r.after(1500,update)


                                  # function to delete selected item from list
def deletelistitem():
    s=lb.get(0,"end")                                               # get the list(only one item) of selected item is variable s                      
    if not s:                                                       # run this if list is empty
        outputvar.set("List is Empty")
    else:                                                           # run this if list is not empty
        selected=lb.curselection()                                  # get the index of selected item                           
        if selected:                                                # run this if item is selected and delete it
            lb.delete(selected[0])
            outputvar.set("Deleted successfully")  
        else:
            outputvar.set("No Task selected")                       # run this if item is not selected

    r.after(1500,update)

                           # click function for buttons command
def click(event):
    if event.widget.cget("text")=="CREATE":                                 # run this if CLICK button is press
            addlistbar()
            
    elif event.widget.cget("text")=="UPDATE":                               # run this if UPDATE button is press
        updatelistbar()

    else:
        deletelistitem()                                                    # run this if DELETE button is press


Heading=tkinter.Label(r,text="TO DO LIST",fg="white",bg="darkgreen",font=("Arial",20,"italic","bold"),pady=15)
Heading.pack()

                                             # frame for listbox and scrollbar
f1=tkinter.Frame(r)
f1.pack(fill="x",pady=5)
sb=tkinter.Scrollbar(f1)                                                                    # create a scrollbar
sb.pack(side="right",fill="y")

lb=tkinter.Listbox(f1,height=5,width=50,yscrollcommand=sb.set)                              # create a listbox for items
lb.pack(fill="x")
sb.config(command=lb.yview)                                                                 # connect scrollbar with listbox

                                             #frame for variables and entry widgets
f2=tkinter.Frame(r,bg="green")
f2.pack()

inputvar=tkinter.StringVar()                                                                                 # string variable for input
inputlabel=tkinter.Label(f2,text="Input Task",bg="darkgreen",fg="white",font=("Ariel",13),padx=10)       # Label widget
inputlabel.grid(row=0,column=0)
inputentry=tkinter.Entry(f2,font=("Ariel",15,"bold"),textvariable=inputvar)                                  # Entry widget inputvar connect with it
inputentry.grid(row=0,column=1,pady=5)

outputvar=tkinter.StringVar()                                                                                # string variable for output 
outputentry=tkinter.Entry(f2,state="readonly",width=25,justify="center",bg="black",fg="darkgrey",font=("Ariel",10,"bold"),textvariable=outputvar) # Entry widget ioutputvar connect with it
outputentry.grid(row=1,column=1)

                                         # frame for button
f3=tkinter.Frame(r,bg="darkgreen")
f3.pack(pady=50)

#B
button=tkinter.Button(f3,text="CREATE",width=20,fg="white",bg="grey",padx=10)                               # create button to add new item
button.grid(row=0,column=0,pady=10)
button.bind("<Button-1>",click)
#B
button=tkinter.Button(f3,text="UPDATE",width=20,fg="white",bg="grey",padx=10)                               # update button to update current item
button.grid(row=2,column=0,pady=10)
button.bind("<Button-1>",click)
#B
button=tkinter.Button(f3,text="DELETE",width=20,fg="white",bg="grey",padx=10)                               # delete button to delete item from list
button.grid(row=3,column=0,pady=10)
button.bind("<Button-1>",click)
#B
button=tkinter.Button(f3,text="QUIT",width=20,fg="white",bg="red",padx=10,command=quit)                     # quit button to close the program
button.grid(row=4,column=0,pady=10)


r.mainloop()