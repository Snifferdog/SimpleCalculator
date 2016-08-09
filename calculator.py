import tkinter

class Calculator:
  
  def __init__(self):
    window = tkinter.Tk()
    window.geometry("147x190")
    window.resizable(width=False, height=False)
    window.title("Calculator")

    lblText = tkinter.StringVar()
    lbl = tkinter.Label(window, text="placeholder", textvariable=lblText)
    lbl.grid(row=0, column=0, columnspan=3)
    
    self.firstNumArray = []
    self.secondNumArray = []
    self.operation = ""
    self.currentNum = "first"

    def appendNumber(self, number):
      print("Appending Number")
      if self.currentNum == "first":
        self.firstNumArray.append(number)
        print("".join(str(x) for x in self.firstNumArray))
        lblText.set("".join(str(x) for x in self.firstNumArray))
      else:
        self.secondNumArray.append(number)
        lblText.set("".join(str(x) for x in self.secondNumArray))

    for i in range(9):
      btn = tkinter.Button(text=i+1, command=lambda n=i+1: appendNumber(self, n))
      btn.grid(row=i//3+1, column=i%3)
    
    def chooseOperation(self, operation):
      lblText.set("")
      self.currentNum = "second"
      self.operation = operation

    div = tkinter.Button(text="/", command=lambda: chooseOperation(self, "div"))
    mult = tkinter.Button(text="*", command=lambda: chooseOperation(self, "mult"))
    add = tkinter.Button(text="+", command=lambda: chooseOperation(self, "add"))
    sub = tkinter.Button(text="-", command=lambda: chooseOperation(self, "sub"))

    add.grid(row=1, column=3)
    sub.grid(row=2, column=3)
    mult.grid(row=3, column=3)
    div.grid(row=4, column=3)

    button = tkinter.Button(text="0", command=lambda: appendNumber(self, 0))
    button.grid(row=4, column=1)

    def calculate(self):
      firstNum = float("".join(str(x) for x in self.firstNumArray))
      secondNum = float("".join(str(x) for x in self.secondNumArray))
      lblText.set("")
      if self.operation == "add":
        lblText.set("{:10.4f}".format(firstNum + secondNum))
        self.firstNumArray = list(lblText.get())
      elif self.operation == "sub":
        lblText.set("{:10.4f}".format(firstNum - secondNum))
        self.firstNumArray = list(lblText.get())
      elif self.operation == "mult":
        lblText.set("{:10.4f}".format(firstNum * secondNum))
        self.firstNumArray = list(lblText.get())
      elif self.operation == "div":
        lblText.set("{:10.4f}".format(firstNum / secondNum))
        self.firstNumArray = list(lblText.get())
      self.currentNum = "second"
      self.secondNumArray = []

    def clear(self):
      self.firstNumArray = []
      self.secondNumArray = []
      lblText.set("")
      self.currentNum = "first"

    dotBtn = tkinter.Button(text=".", command=lambda: appendNumber(self, ".")).grid(row=4, column=2)
    clearBtn = tkinter.Button(text="C", command=lambda: clear(self)).grid(row=6, column=3)
    calcBtn = tkinter.Button(text="=", command=lambda: calculate(self)).grid(row=5, column=3)

    window.mainloop()



calc = Calculator()

