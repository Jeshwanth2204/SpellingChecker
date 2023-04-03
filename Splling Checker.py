from tkinter import *
from textblob import TextBlob

root = Tk()

root.title('spelling checker')
root.geometry('700x400')
root.config(background = '#202020')
root.resizable(False,False)

# Working with funtions

def check_spelling():
  global enter_text
  word = enter_text.get()
  a = TextBlob(word)
  corrected = str(a.correct())
  spell.config(text = corrected)

  result_label = Label(root,text =('Correct text is : '),bg = '#202020',fg = '#44EDFF',font=('poppins',20))
  result_label.place(x = 100,y = 260)

def ac():
    enter_text.delete(0,END)

def backspace():
  enter_text.delete(len(enter_text.get())-1, END)

#GUI 
  
heading = Label(root,text = 'Spelling Checker',font=('Alkatra',30,'bold'),bg='#202020',fg = '#ff007f')
heading.pack(pady =(50,0))

enter_text = Entry(root,justify = 'center',font = ('arial',25),width = 30,bg = 'white',border = 2)
enter_text.pack(pady =(15,0))
enter_text.focus()

button = Button(root,text= 'Check',font=('arial',10,'bold'),height = 3,width = 15,bg ='#00ff00',fg='black',command = check_spelling)
button.pack(pady = (8,0))

spell = Label(root,font = ('poppins',20),bg = '#202020',fg = '#ffff00')
spell.place(x = 320,y = 260)


acc = Button(root,text = 'del',height = 3,width = 7,bg= 'red',fg = 'black',command = ac)
acc.place(x = 450 , y= 173)
acc.config(font = ('arial',10,'bold'))

back = Button(root,text = '<',height = 3,width = 7,bg ='#ff8000' ,fg ='black' ,font = ('arial',10,'bold'),command = backspace)
back.place(x =158,y = 173)


root.mainloop()









