
import Tkinter as tk
from PIL import ImageTk, Image
import tkFont
import psycopg2


#################################################################################################################################################################
#LOGIN WINDOW
class LoginWin(tk.Frame):
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)
        #DB LOGIN

        conn = psycopg2.connect("dbname = LoginInfo user = postgres password = harlan host = localhost")
        cur = conn.cursor()

        #LOGIN WINDOW
        master.title("Login")
        tk.img = ImageTk.PhotoImage(Image.open("SNI.jpg").resize((450,400)))
        tk.myPanel = tk.Label(self, image = tk.img, highlightthickness = 0, borderwidth = 0)
        master.geometry("1200x900")

        #FUNCTIONS
        def verifyLogin():
            cur.execute("SELECT username, password FROM users;")
            for username, password in cur.fetchall():
                if(username == tk.userEntry.get()):
                    if(password == tk.passEntry.get()):
                        master.switch_frame(MenuWin)
                    else:
                        print "Wrong password"

        def checkPass():
            if(tk.myCheck.get() == 0):
                tk.passEntry.config(show="*")
            else:
                tk.passEntry.config(show = "")


        #CONFIG
        self.config(background = 'white')

        #FONT 
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 25)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 25)
        tk.checkFont = tkFont.Font(family = "Verdana", size = 15)

        #LABELS
        tk.userLabel = tk.Label(self, text = "User Name", background = 'white', font = tk.labelFont)
        tk.passLabel = tk.Label(self, text = "Password", background = 'white', font = tk.labelFont)

        #TEXTBOXES
        tk.userEntry = tk.Entry(self, width = 25, font = tk.labelFont, highlightbackground='deep sky blue', highlightthickness = 4)
        tk.passEntry = tk.Entry(self, width = 25, font = tk.labelFont, show="*", highlightbackground = 'deep sky blue', highlightthickness = 4)

        #CHECKBOX
        tk.myCheck = tk.IntVar()
        tk.passCheck = tk.Checkbutton(self, text = "Show Password", background = 'white', font = tk.checkFont, activebackground = 'deep sky blue', highlightthickness = 0, variable = tk.myCheck, command = checkPass)

        #BUTTONS
        tk.loginButton = tk.Button(self, text = "LOGIN", font = tk.buttonFont, command = verifyLogin, background = 'deep sky blue', borderwidth = 0)
        tk.loginButton.config(height = 2, width = 13)

        #PACK
        tk.myPanel.pack(pady = (30,0))
        tk.userLabel.pack(pady = (20,0))
        tk.userEntry.pack()
        tk.passLabel.pack(pady = (5,0))
        tk.passEntry.pack()
        tk.passCheck.pack()
        tk.loginButton.pack(pady = (30,0))


#################################################################################################################################################################
#MENU WINDOW
class MenuWin(tk.Frame):
    
    def __init__(self, master):
        #MENU WINDOW
        tk.Frame.__init__(self, master)

        master.title("Main Menu")
        master.geometry("800x575")

        def customerInfo():
            self.newWindow = self.app
            self.app = SampleApp()
            self.app.mainloop()
            self.app.switch_frame(CustomerInfoWin)
        def addTransactions():    
            self.newWindow = self.app
            self.app = SampleApp()
            self.app.mainloop()
            self.app.switch_frame(NewOrExistingWin)
        def mySettings():
            self.newWindow = self.app
            self.app = SampleApp()
            self.app.mainloop()
            self.app.switch_frame(SettingsWin)
        def getReports():
            self.newWindow = self.app
            self.app = SampleApp()
            self.app.mainloop()
            self.app.switch_frame(ReportsWin)
            
        #CONFIG
        self.config(background = "white")

        #FONT 
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 20)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 30, weight = tkFont.BOLD)

        #LABELS
        tk.titleLabel = tk.Label(self, text = "Main Menu", background = "white", font = tk.labelFont, fg = "blue4")

        #BUTTONS
        tk.CustomerInfoButton = tk.Button(self, text = "Customer Information", font = tk.buttonFont, command = customerInfo, background = 'deep sky blue', borderwidth = 0)
        tk.AddTransactionsButton = tk.Button(self, text = "Add Transaction", font = tk.buttonFont, command = addTransactions, background = 'deep sky blue', borderwidth = 0)
        tk.SettingsButton = tk.Button(self, text = "Settings", font = tk.buttonFont, command = mySettings, background = 'deep sky blue', borderwidth = 0)
        tk.ReportsButton = tk.Button(self, text = "Reports", font = tk.buttonFont, command = getReports, background = 'deep sky blue', borderwidth = 0)
        tk.CustomerInfoButton.config(height = 2, width = 25)
        tk.AddTransactionsButton.config(height = 2, width = 25)
        tk.SettingsButton.config(height = 2, width = 25)
        tk.ReportsButton.config(height = 2, width = 25)

        #PACK
        tk.titleLabel.pack(pady = (25,0))
        tk.CustomerInfoButton.pack(pady = (20,0))
        tk.AddTransactionsButton.pack(pady = (15,0))
        tk.SettingsButton.pack(pady = (15,0))
        tk.ReportsButton.pack(pady = (15,0))



#################################################################################################################################################################
#CUSTOMER INFORMATION WINDOW
class CustomerInfoWin:

    def __init__(self,master):
        
        #DB
        conn = psycopg2.connect("dbname = LoginInfo user = postgres password = harlan host = localhost")
        cur = conn.cursor()

        #GET CUSTOMER INFO
        cur.execute("select * from customers;")
        result = cur.fetchone()

        #GET ADDRESS INFO
        cur2 = conn.cursor()
        cur2.execute("select * from address;")
        result2 = cur2.fetchone()

        #CUSTOMER WINDOW
        tk.Frame.__init__(self, master)

        master.title("Customer Information")
        master.geometry("1100x700")
        tk.TitleFrame = tk.Frame(master)
        tk.TitleFrame.grid(row = 0)
        tk.InfoFrame = tk.Frame(master)
        tk.InfoFrame.grid(row = 1, padx = (35,0))
        tk.NameFrame = tk.Frame(master)
        tk.NameFrame.grid(row = 2, padx = (35,0))
        tk.AddFrame = tk.Frame(master)
        tk.AddFrame.grid(row = 3, padx = (45,0))
        tk.CityFrame = tk.Frame(master)
        tk.CityFrame.grid(row = 4, padx = (35,0))
        tk.PhoneFrame = tk.Frame(master)
        tk.PhoneFrame.grid(row = 5, padx = (40,0))
        tk.ButtonsFrame = tk.Frame(master)
        tk.ButtonsFrame.grid(row = 6, pady = (50,0))
        tk.ButtonsFrame2 = tk.Frame(master)
        tk.ButtonsFrame2.grid(row = 7, pady = (10,0))
        tk.ButtonsFrame3 = tk.Frame(master)
        tk.ButtonsFrame3.grid(row = 8, pady = (10,0))

        #CONFIG 
        self.configure(background = "white")
        tk.TitleFrame.config(background = "white")
        tk.InfoFrame.config(background = "white")
        tk.NameFrame.config(background = "white")
        tk.AddFrame.config(background = "white")
        tk.CityFrame.config(background = "white")
        tk.PhoneFrame.config(background = "white")
        tk.ButtonsFrame.config(background = "white")
        tk.ButtonsFrame2.config(background = "white")
        tk.ButtonsFrame3.config(background = "white")

        #FONT
        buttonFont = tkFont.Font(family = "Verdana", size = 15)
        titleFont = tkFont.Font(family = "Verdana", size = 20, weight = tkFont.BOLD)
        labelFont = tkFont.Font(family = "Verdana", size = 15)
        boxFont = tkFont.Font(family = "Verdana", size = 12)

        #BUTTON FUNCTIONS
        def newUser():
            self.newWindow = tk.Toplevel(self.master)
            self.app = AddNewCustWin(self.newWindow)

        def editUser():
            self.clientText.configure(state='normal')
            self.giftText.configure(state='normal')
            self.labelCodeText.configure(state='normal')
            self.copiesText.configure(state='normal')
            self.startText.configure(state='normal')
            self.expText.configure(state='normal')

            self.tNameText.configure(state='normal')
            self.fNameText.configure(state='normal')
            self.mNameText.configure(state='normal')
            self.lNameText.configure(state='normal')

            self.address1Text.configure(state='normal')
            self.address2Text.configure(state='normal')

            self.cityText.configure(state='normal')
            self.stateText.configure(state='normal')
            self.zipText.configure(state='normal')
            self.countryText.configure(state='normal')

            self.phoneText.configure(state='normal')
            self.emailText.configure(state='normal')

        def deleteUser():
            self.newWindow = tk.Toplevel(self.master)
            self.app = ConfirmDeleteWin(self.newWindow)

        def custLabel():
            print("work in progress for customer label")

        def getSubs():
            print("work in progress for subs")

        def getTransactions():
            print("Work in progress for transactions")

        def getSponsors():
            print("work in progress for checking sponsors and sponsoring")

        def searchUser():
            self.newWindow = tk.Toplevel(self.master)
            self.app = CustomerSearchWin(self.newWindow)

        def showHistory():
            print("work in progress for history")

        def showPrev():
            print("work in progress for previous")

        def showNext():
            result = cur.fetchone()

            if not result:
                print("no more customers")
            else:
                print("Show next")
                cur2.execute("select addressid from customers where customerid = %d"%(result[0]))
                myAddress = cur2.fetchone()
                cur2.execute("select * from address where addressid = %d;"%(int(myAddress[0])))
                result2 = cur2.fetchone()
                editUser()
                deleteInfo()
                insertInfo(result, result2)            
                makeUneditable()

        def deleteInfo():
            self.clientText.delete(0,tk.END)
            self.tNameText.delete(0,tk.END)
            self.fNameText.delete(0,tk.END)
            self.mNameText.delete(0,tk.END)
            self.lNameText.delete(0,tk.END)
            self.phoneText.delete(0,tk.END)
            self.emailText.delete(0,tk.END)

            self.address1Text.delete(0,tk.END)
            self.address2Text.delete(0,tk.END)
            self.cityText.delete(0,tk.END)
            self.stateText.delete(0,tk.END)
            self.zipText.delete(0,tk.END)
            self.countryText.delete(0,tk.END)

        def insertInfo(result, result2):
            self.clientText.insert(0,result[0])
            self.tNameText.insert(0,result[2])
            self.fNameText.insert(0,result[3])
            self.mNameText.insert(0,result[5])
            self.lNameText.insert(0,result[4])
            self.phoneText.insert(0,result[6])
            self.emailText.insert(0,result[7])

            self.address1Text.insert(0,result2[1])
            self.address2Text.insert(0,result2[2])
            self.cityText.insert(0,result2[3])
            self.stateText.insert(0,result2[4])
            self.zipText.insert(0,result2[5])
            self.countryText.insert(0,result2[6])

        def makeUneditable():
            self.clientText.configure(state='readonly')
            self.giftText.configure(state='readonly')
            self.labelCodeText.configure(state='readonly')
            self.copiesText.configure(state='readonly')
            self.startText.configure(state='readonly')
            self.expText.configure(state='readonly')

            self.tNameText.configure(state='readonly')
            self.fNameText.configure(state='readonly')
            self.mNameText.configure(state='readonly')
            self.lNameText.configure(state='readonly')

            self.address1Text.configure(state='readonly')
            self.address2Text.configure(state='readonly')

            self.cityText.configure(state='readonly')
            self.stateText.configure(state='readonly')
            self.zipText.configure(state='readonly')
            self.countryText.configure(state='readonly')

            self.phoneText.configure(state='readonly')
            self.emailText.configure(state='readonly')

        #LABELS
        self.titleLabel = tk.Label(self.TitleFrame,text = "Customer Information", font = titleFont, background = "white", fg = "blue4")

        self.clientNoLabel = tk.Label(self.InfoFrame, text = "Client #", font = labelFont, background = "white")
        self.giftNoLabel = tk.Label(self.InfoFrame, text = "Gift #", font = labelFont, background = "white")
        self.labelCodeLabel = tk.Label(self.InfoFrame, text = "LabelCode", font = labelFont, background = "white")
        self.copiesLabel = tk.Label(self.InfoFrame, text = "Copies", font = labelFont, background = "white")
        self.startLabel = tk.Label(self.InfoFrame, text = "Start Date", font = labelFont, background = "white")
        self.expLabel = tk.Label(self.InfoFrame, text = "Exp Date", font = labelFont, background = "white")

        self.tNameLabel = tk.Label(self.NameFrame, text = "Title", font = labelFont, background = "white")
        self.fNameLabel = tk.Label(self.NameFrame, text = "FirstName", font = labelFont, background = "white")
        self.mNameLabel = tk.Label(self.NameFrame, text = " MiddleName", font = labelFont, background = "white")
        self.lNameLabel = tk.Label(self.NameFrame, text = " LastName", font = labelFont, background = "white")

        self.address1Label = tk.Label(self.AddFrame, text = "Address 1", font = labelFont, background = "white")
        self.address2Label = tk.Label(self.AddFrame, text = " Address 2", font = labelFont, background = "white")

        self.cityLabel = tk.Label(self.CityFrame, text = "City", font = labelFont, background = "white")
        self.stateLabel = tk.Label(self.CityFrame, text = " State", font = labelFont, background = "white")
        self.zipCodeLabel = tk.Label(self.CityFrame, text = " Zip Code", font = labelFont, background = "white")
        self.countryLabel = tk.Label(self.CityFrame, text = "Country", font = labelFont, background = "white")

        self.phoneLabel = tk.Label(self.PhoneFrame, text = " Phone", font = labelFont, background = "white")
        self.emailLabel = tk.Label(self.PhoneFrame, text = "Email", font = labelFont, background = "white")

        #TEXTBOXES
        self.clientText = tk.Entry(self.InfoFrame, width = 11, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.giftText = tk.Entry(self.InfoFrame, width = 11, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.labelCodeText = tk.Entry(self.InfoFrame, width = 11, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.copiesText = tk.Entry(self.InfoFrame, width = 11, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.startText = tk.Entry(self.InfoFrame, width = 15, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.expText = tk.Entry(self.InfoFrame, width = 15, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        self.tNameText = tk.Entry(self.NameFrame, width = 11, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.fNameText = tk.Entry(self.NameFrame, width = 30, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.mNameText = tk.Entry(self.NameFrame, width = 13, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.lNameText = tk.Entry(self.NameFrame, width = 30, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        self.address1Text = tk.Entry(self.AddFrame, width = 44, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.address2Text = tk.Entry(self.AddFrame, width = 44, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        self.cityText = tk.Entry(self.CityFrame, width = 25, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.stateText = tk.Entry(self.CityFrame, width = 12, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.zipText = tk.Entry(self.CityFrame, width = 16, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.countryText = tk.Entry(self.CityFrame, width = 30, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        self.phoneText = tk.Entry(self.PhoneFrame, width = 31, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.emailText = tk.Entry(self.PhoneFrame, width = 57, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        #INSERT_INFO
        insertInfo(result, result2)
        
        #TEXTBOX_CONFIG
        makeUneditable()

        #BUTTONS
        self.addButton = tk.Button(self.ButtonsFrame, text = "ADD", font = buttonFont, command = newUser, background = "deep sky blue", borderwidth = 0)
        self.editButton = tk.Button(self.ButtonsFrame, text = "EDIT", font = buttonFont, command = editUser, background = "deep sky blue", borderwidth = 0)
        self.deleteButton = tk.Button(self.ButtonsFrame, text = "DELETE", font = buttonFont, command = deleteUser, background = "deep sky blue", borderwidth = 0)
        self.searchButton = tk.Button(self.ButtonsFrame, text = "SEARCH", font = buttonFont, command = searchUser, background = "deep sky blue", borderwidth = 0)
        self.printLabelButton = tk.Button(self.ButtonsFrame2, text = "PRINT LABELS" , font = buttonFont, command  = custLabel, background = "deep sky blue", borderwidth = 0)
        self.subsButton = tk.Button(self.ButtonsFrame2, text = "SUBSCRIPTIONS", font = buttonFont, command = getSubs, background = "deep sky blue", borderwidth = 0)
        self.transButton = tk.Button(self.ButtonsFrame2, text = "TRANSACTIONS", font = buttonFont, command = getTransactions, background = "deep sky blue", borderwidth = 0)
        self.sponsorButton = tk.Button(self.ButtonsFrame2, text = "SPONSORS", font = buttonFont, command = getSponsors, background = "deep sky blue", borderwidth = 0)
        self.prevButton = tk.Button(self.ButtonsFrame3, text = "PREVIOUS", font = buttonFont, command = showPrev, background = "deep sky blue", borderwidth = 0)
        self.historyButton = tk.Button(self.ButtonsFrame3, text = "HISTORY", font = buttonFont, command = showHistory, background = "deep sky blue", borderwidth = 0)
        self.nextButton = tk.Button(self.ButtonsFrame3, text = "NEXT", font = buttonFont, command = showNext, background = "deep sky blue", borderwidth = 0)

        #BUTTON_CONFIG
        self.addButton.config(height = 1, width = 13)
        self.editButton.config(height = 1, width = 13)
        self.deleteButton.config(height = 1, width = 13)
        self.searchButton.config(height = 1, width = 13)
        self.printLabelButton.config(height = 1, width = 15)
        self.subsButton.config(height = 1, width = 15)
        self.transButton.config(height = 1, width = 15)
        self.sponsorButton.config(height = 1, width = 15)
        self.historyButton.config(height = 1, width = 13)
        self.prevButton.config(height = 1, width = 13)
        self.nextButton.config(height = 1, width = 13)

        #PACK
        self.titleLabel.grid(row = 0, column = 0, pady = (30,20))
        self.clientNoLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.giftNoLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.labelCodeLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        self.copiesLabel.grid(row = 0, column = 3, sticky = 'w', padx = (0,10))
        self.startLabel.grid(row = 0, column = 4, sticky = 'w', padx = (0,10))
        self.expLabel.grid(row = 0, column = 5, sticky = 'w')
        self.clientText.grid(row = 1, column = 0, padx = (0,10))
        self.giftText.grid(row = 1, column = 1, padx = (0,10))
        self.labelCodeText.grid(row = 1, column = 2, padx = (0,70))
        self.copiesText.grid(row = 1, column = 3, padx = (0,10))
        self.startText.grid(row = 1, column = 4, padx = (0,10))
        self.expText.grid(row = 1, column = 5)
        self.tNameLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.fNameLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.mNameLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        self.lNameLabel.grid(row = 0, column = 3, sticky = 'w')
        self.tNameText.grid(row = 1, column = 0, padx = (0,10))
        self.fNameText.grid(row = 1, column = 1, padx = (0,10))
        self.mNameText.grid(row = 1, column = 2, padx = (0,10))
        self.lNameText.grid(row = 1, column = 3)
        self.address1Label.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.address2Label.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.address1Text.grid(row = 1, column = 0, padx = (0,10))
        self.address2Text.grid(row = 1, column = 1, padx = (0,10))
        self.cityLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.stateLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.zipCodeLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        self.countryLabel.grid(row = 0, column = 3, sticky = 'w', padx = (0,10))
        self.cityText.grid(row = 1, column = 0, padx = (0,10))
        self.stateText.grid(row = 1, column = 1, padx = (0,10))
        self.zipText.grid(row = 1, column = 2, padx = (0,10))
        self.countryText.grid(row = 1, column = 3, padx = (0,10))
        self.phoneLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.emailLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.phoneText.grid(row = 1, column = 0, padx = (0,10))
        self.emailText.grid(row = 1, column = 1, padx = (0,10))
        self.addButton.grid(row = 0, column = 0, padx = (0,10))
        self.editButton.grid(row = 0, column = 1, padx = (0,10))
        self.deleteButton.grid(row = 0, column = 2, padx = (0,10))
        self.searchButton.grid(row = 0, column = 3)
        self.printLabelButton.grid(row = 1, column = 0, padx = (0,10))
        self.subsButton.grid(row = 1, column = 1, padx = (0,10))
        self.transButton.grid(row = 1, column = 2, padx = (0,10))
        self.sponsorButton.grid(row = 1, column = 3)
        self.prevButton.grid(row = 2, column = 0, padx = (0,10))
        self.historyButton.grid(row = 2, column = 1, padx = (0,10))
        self.nextButton.grid(row = 2, column = 2)





#################################################################################################################################################################
#NEW OR EXISTING CUSTOMER WINDOW
class NewOrExistingWin:

    def __init__(self,master):
        #NEW_OR_EXISTING_WINDOW
        self.master = master
        master.title("New or Existing Customer?")
        master.geometry("600x400")
        self.frame = tk.Frame(master)

        #CONFIG
        self.master.config(background = 'white')
        self.frame.config(background = 'white')

        #FUNCTIONS
        def existingTrans():
            self.newWindow = tk.Toplevel(self.master)
            self.app = OldCustomerSearchWin(self.newWindow)
        def newTrans():
            self.newWindow = tk.Toplevel(self.master)
            self.app = AddNewCustWin(self.newWindow)

        #FONT 
        buttonFont = tkFont.Font(family = "Verdana", size = 20)
        labelFont = tkFont.Font(family = "Verdana", size = 25)

        #LABELS
        self.titleLabel = tk.Label(self.frame, text = "New or Existing Customer?", background = 'white', font = labelFont, fg = "blue4")

        #BUTTONS
        self.newTransButton = tk.Button(self.frame, text = "New" ,font = buttonFont, command = newTrans, background='deep sky blue', borderwidth = 0)
        self.newTransButton.config(height = 2, width = 20)
        self.existingTransButton = tk.Button(self.frame, text = "Existing", font = buttonFont, command = existingTrans, background='deep sky blue', borderwidth = 0)
        self.existingTransButton.config(height = 2, width = 20)

        #PACK
        self.frame.pack()
        self.titleLabel.pack(pady = (30,50))
        self.newTransButton.pack(pady = (0,10))
        self.existingTransButton.pack() 




#################################################################################################################################################################
#SETTINGS WINDOW
class SettingsWin:

    def __init__(self,master):

        #SETTINGS WINDOW
        self.master = master
        self.frame = tk.Frame(master)
        master.title("Settings")
        master.geometry("800x575")

        #FONT
        buttonFont = tkFont.Font(family = "Verdana", size = 20)
        labelFont = tkFont.Font(family = "Verdana", size = 30, weight = tkFont.BOLD)

        #BUTTON FUNCTIONS
        def changePass():
            self.newWindow = tk.Toplevel(self.master)
            self.app = CheckLoginWin(self.newWindow, 'changePass')

        def changeUser():
            self.newWindow = tk.Toplevel(self.master)
            self.app = CheckLoginWin(self.newWindow, 'changeUser')

        def editItems():
            self.newWindow = tk.Toplevel(self.master)
            self.app = CheckLoginWin(self.newWindow, 'editItems')

        def newUser():
            self.newWindow = tk.Toplevel(self.master)
            self.app = CheckLoginWin(self.newWindow, 'newUser')

        #CONFIG
        self.frame.config(background = "white")
        self.master.config(background = "white")

        #LABELS
        self.titleLabel = tk.Label(self.frame, text = "My Settings", background = "white", font = labelFont, fg = "blue4")

        #BUTTONS
        self.changePassButton = tk.Button(self.frame, text = "Change Password", font = buttonFont, command = changePass, background = "deep sky blue", borderwidth = 0)
        self.changeUserButton = tk.Button(self.frame, text = "Change Username", font = buttonFont, command = changeUser, background = "deep sky blue", borderwidth = 0)
        self.editItemsButton = tk.Button(self.frame, text = "Edit Items", font = buttonFont, command = editItems, background = "deep sky blue", borderwidth = 0)
        self.newUserButton = tk.Button(self.frame, text = "Add New User", font = buttonFont, command = newUser, background = "deep sky blue", borderwidth = 0)
        self.changePassButton.config(height = 2, width = 25)
        self.changeUserButton.config(height = 2, width = 25)
        self.editItemsButton.config(height = 2, width = 25)
        self.newUserButton.config(height = 2, width = 25)

        #PACK
        self.frame.pack()
        self.titleLabel.pack(pady = (30,20))
        self.editItemsButton.pack()
        self.newUserButton.pack(pady = (15,0))
        self.changeUserButton.pack(pady = (15,0))
        self.changePassButton.pack(pady = (15,0))




#################################################################################################################################################################
#REPORTS WINDOW
class ReportsWin:

    def __init__(self,master):
        #master
        self.master = master
        self.frame = tk.Frame(master)
        master.title("Reports")
        master.geometry("800x575")

        #CONFIG
        self.master.config(background = "white")
        self.frame.config(background = "white")

        #FONT
        buttonFont = tkFont.Font(family = "Verdana", size = 20)
        labelFont = tkFont.Font(family = "verdana", size = 30, weight = tkFont.BOLD)

        #BUTTON FUNCTIONS
        def getNotices():
            print("WIP: get notices")

        def getByArea():
            print("WIP: get by area")

        def getTransactions():
            print("WIP: get transactions")

        def getExpired():
            print("WIP: get expired")

        #LABELS
        self.titleLabel = tk.Label(self.frame, text = "Reports", background = "white", font = labelFont, fg = "blue4")

        #BUTTONS
        self.noticesButton = tk.Button(self.frame, text = "Notices of Expiration", font = buttonFont, command = getNotices, background = "deep sky blue", borderwidth = 0)
        self.areaButton = tk.Button(self.frame, text = "By Area", font = buttonFont, command = getByArea, background = "deep sky blue", borderwidth = 0)
        self.transactionButton = tk.Button(self.frame, text = "Transaction History", font = buttonFont, command = getTransactions, background = "deep sky blue", borderwidth = 0)
        self.expiredButton = tk.Button(self.frame, text = "Expired Subscriptions", font = buttonFont, command = getExpired, background = "deep sky blue", borderwidth = 0)

        #BUTTON CONFIG
        self.noticesButton.config(height = 2, width = 25)
        self.areaButton.config(height = 2, width = 25)
        self.transactionButton.config(height = 2, width = 25)
        self.expiredButton.config(height = 2, width = 25)

        #PACK
        self.frame.pack()
        self.titleLabel.pack(pady = (25,20))
        self.noticesButton.pack()
        self.areaButton.pack(pady = (15,0))
        self.transactionButton.pack(pady = (15,0))
        self.expiredButton.pack(pady = (15,0))


#################################################################################################################################################################
#CHECK LOGIN WINDOW
class CheckLoginWin:

    def __init__(self, master, nextWindow):
        
        #DB LOGIN
        conn = psycopg2.connect("dbname = LoginInfo user = postgres password = harlan host = localhost")
        cur = conn.cursor()

        #LOGIN WINDOW
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title("Login")
        master.geometry("700x500")

        #FUNCTIONS
        def verifyLogin():
            myVerify = False
            cur.execute("SELECT username, password FROM users;")
            for username, password in cur.fetchall():
                if(username == self.userEntry.get()):
                    if(password == self.passEntry.get()):
                        myVerify = True
                    else:
                        print "Wrong Password"
                else:
                    print "Wrong Username"

            if(myVerify):   
                if(nextWindow == 'changePass'):
                    self.newWindow = tk.Toplevel(self.master)
                    self.app = ChangePassWin(self.newWindow)
                    conn.close()
                elif(nextWindow == 'changeUser'):
                    self.newWindow = tk.Toplevel(self.master)
                    self.app = ChangeUserWin(self.newWindow)
                    conn.close()
                elif(nextWindow == 'editItems'):
                    self.newWindow = tk.Toplevel(self.master)
                    self.app = EditItemsWin(self.newWindow)
                    conn.close()
                elif(nextWindow == 'newUser'):
                    self.newWindow = tk.Toplevel(self.master)
                    self.app = AddNewUserWin(self.newWindow)
                    conn.close()
            else:
                self.master.destroy()
        def checkPass():
            if(myCheck.get() == 0):
                self.passEntry.config(show="*")
            else:
                self.passEntry.config(show = "")

        #CONFIG
        self.master.configure(background = 'white')
        self.frame.configure(background = 'white')

        #FONT 
        buttonFont = tkFont.Font(family = "Verdana", size = 25)
        labelFont = tkFont.Font(family = "Verdana", size = 25)
        checkFont = tkFont.Font(family = "Verdana", size = 15)
        titleFont = tkFont.Font(family = "Verdana", size = 25, weight = tkFont.BOLD)

        #LABELS
        self.titleLabel = tk.Label(self.frame, text = "Please Login", background = "white", font = titleFont, fg = "blue4")
        self.userLabel = tk.Label(self.frame, text = "User Name", background = 'white', font = labelFont)
        self.passLabel = tk.Label(self.frame, text = "Password", background = 'white', font = labelFont)

        #TEXTBOXES
        self.userEntry = tk.Entry(self.frame, width = 25, font = labelFont, highlightbackground='deep sky blue', highlightthickness = 4)
        self.passEntry = tk.Entry(self.frame, width = 25, font = labelFont, show="*", highlightbackground = 'deep sky blue', highlightthickness = 4)

        #CHECKBOX
        myCheck = tk.IntVar()
        self.passCheck = tk.Checkbutton(self.frame, text = "Show Password", background = 'white', font = checkFont, activebackground = 'deep sky blue', highlightthickness = 0, variable = myCheck, command = checkPass)

        #BUTTONS
        self.loginButton = tk.Button(self.frame, text = "LOGIN", font = buttonFont, command = verifyLogin, background = 'deep sky blue', borderwidth = 0)
        self.loginButton.config(height = 2, width = 13)

        #PACK
        self.frame.pack()
        self.titleLabel.pack(pady = (30,0))
        self.userLabel.pack(pady = (20,0))
        self.userEntry.pack()
        self.passLabel.pack(pady = (5,0))
        self.passEntry.pack()
        self.passCheck.pack()
        self.loginButton.pack(pady = (30,0))


#################################################################################################################################################################
#EDIT ITEMS WINDOW
class EditItemsWin:

    def __init__(self, master):
        print("WIP: Edit Items")

#################################################################################################################################################################
#ADD NEW USER WINDOW
class AddNewUserWin:

    def __init__(self, master):
        
        #DB LOGIN
        conn = psycopg2.connect("dbname = LoginInfo user = postgres password = harlan host = localhost")
        cur = conn.cursor()

        #ADD_NEW_USER_WINDOW
        self.master = master
        self.frame = tk.Frame(master)
        master.title("Create New User")
        master.geometry("900x700")

        #FUNCTIONS
        def CreateUser():
            cur.execute("SELECT usersid FROM users where username = '%s';" % self.userEntry.get())
            alreadyUsed = cur.fetchall()
            if not alreadyUsed:
                mySql = "insert into users values (DEFAULT, 1, '%s', '%s')" % (self.userEntry.get(), self.passEntry.get())
                cur.execute(mySql)
                conn.commit()
                conn.close()
                print("Success!")
            else:
                print("This username has already been used!")

        def checkPass():
            if(myCheck.get() == 0):
                self.passEntry.config(show = "*")
            else:
                self.passEntry.config(show = "")

        #FONT 
        buttonFont = tkFont.Font(family = "Verdana", size = 20)
        labelFont = tkFont.Font(family = "Verdana", size = 20)
        checkFont = tkFont.Font(family = "Verdana", size = 15)
        radioFont = tkFont.Font(family = "Verdana", size = 13)

        #CONFIG
        self.frame.config(background = "white")
        self.master.config(background = "white")

        #LABELS
        self.titleLabel = tk.Label(self.frame, text = "New User", background = "white", font = ("Verdana", 30, tkFont.BOLD), fg = "blue4")
        self.userLabel = tk.Label(self.frame, text = "User Name", background = "white", font = labelFont)
        self.passLabel = tk.Label(self.frame, text = "Password", background = "white", font = labelFont)
        self.privLabel = tk.Label(self.frame, text = "Permissions", background = "white", font = labelFont)

        #TEXTBOXES
        self.userEntry = tk.Entry(self.frame, width = 22, font = ("Verdana", 30), highlightbackground='deep sky blue', highlightthickness = 4)
        self.passEntry = tk.Entry(self.frame, width = 22, font = ("Verdana", 30), show = "*", highlightbackground='deep sky blue', highlightthickness = 4)

        #CHECKBOX
        myCheck = tk.IntVar()
        self.passCheck = tk.Checkbutton(self.frame, text = "Show Password", background = 'white', font = checkFont, activebackground = 'deep sky blue', highlightthickness = 0, variable = myCheck, command = checkPass)

        #RADIO_BUTTONS
        self.adminRadio = tk.Radiobutton(self.frame, text = "Admin", value = 1, background = "white", font = radioFont, tristatevalue = 0, highlightthickness = 0, activebackground = 'deep sky blue')
        self.editRadio = tk.Radiobutton(self.frame, text = "Edit Only", value = 2, background = "white", font = radioFont, tristatevalue = 0, highlightthickness = 0, activebackground = 'deep sky blue')
        self.readRadio = tk.Radiobutton(self.frame, text = "Read Only", value = 3, background = "white", font = radioFont, tristatevalue = 0, highlightthickness = 0, activebackground = 'deep sky blue')

        #BUTTONS
        self.CreateButton = tk.Button(self.frame, text = "CREATE USER" ,font = buttonFont, command = CreateUser, background = "deep sky blue", borderwidth = 0)
        self.CreateButton.config(height = 2, width = 13)


        #PACK
        self.frame.pack()
        self.titleLabel.pack(pady=(30,20))
        self.userLabel.pack()
        self.userEntry.pack()
        self.passLabel.pack(pady = (20,0))
        self.passEntry.pack()
        self.passCheck.pack()
        self.privLabel.pack(pady = (25,0))
        self.adminRadio.pack()
        self.editRadio.pack()
        self.readRadio.pack()
        self.CreateButton.pack(pady = (20,0))

    def close_windows(self):
        self.master.destroy()

#################################################################################################################################################################
#CHANGE USER WINDOW
class ChangeUserWin:

    def __init__(self, master):

        #CHANGE_USER_WINDOW
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title("Change Username")
        master.geometry("600x400")

        #FUNCTIONS
        def verifyChange():
            print("WIP:Change User")

        #CONFIG
        self.master.configure(background = 'white')
        self.frame.configure(background = 'white')

        #FONT 
        buttonFont = tkFont.Font(family = "Verdana", size = 25)
        labelFont = tkFont.Font(family = "Verdana", size = 25)
        titleFont = tkFont.Font(family = "Verdana", size = 25, weight = tkFont.BOLD)

        #LABELS
        self.titleLabel = tk.Label(self.frame, text = "Enter New Username", background = "white", font = titleFont, fg = "blue4")
        self.userLabel = tk.Label(self.frame, text = "User Name", background = 'white', font = labelFont)

        #TEXTBOXES
        self.userEntry = tk.Entry(self.frame, width = 25, font = labelFont, highlightbackground='deep sky blue', highlightthickness = 4)

        #BUTTONS
        self.confirmButton = tk.Button(self.frame, text = "Confirm", font = buttonFont, command = verifyChange, background = 'deep sky blue', borderwidth = 0)
        self.confirmButton.config(height = 2, width = 13)

        #PACK
        self.frame.pack()
        self.titleLabel.pack(pady = (30,0))
        self.userLabel.pack(pady = (20,0))
        self.userEntry.pack()
        self.confirmButton.pack(pady = (30,0))


#################################################################################################################################################################
#CHANGE PASS WINDOW
class ChangePassWin:

    def __init__(self, master):
        
        #LOGIN WINDOW
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title("Change Password")
        master.geometry("600x500")

        #FUNCTIONS
        def verifyChange():
            print("WIP:Change Password")
        def checkPass():
            if(myCheck.get() == 0):
                self.passEntry.config(show="*")
                self.passEntry2.config(show="*")
            else:
                self.passEntry.config(show = "")
                self.passEntry2.config(show = "")

        #CONFIG
        self.master.configure(background = 'white')
        self.frame.configure(background = 'white')

        #FONT 
        buttonFont = tkFont.Font(family = "Verdana", size = 25)
        labelFont = tkFont.Font(family = "Verdana", size = 25)
        checkFont = tkFont.Font(family = "Verdana", size = 15)
        titleFont = tkFont.Font(family = "Verdana", size = 25, weight = tkFont.BOLD)

        #LABELS
        self.titleLabel = tk.Label(self.frame, text = "Enter New Password", background = "white", font = titleFont, fg = "blue4")
        self.passLabel = tk.Label(self.frame, text = "Password", background = 'white', font = labelFont)
        self.passLabel2 = tk.Label(self.frame, text = "Confirm Password", background = 'white', font = labelFont)

        #TEXTBOXES
        self.passEntry = tk.Entry(self.frame, width = 25, font = labelFont, show="*", highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.passEntry2 = tk.Entry(self.frame, width = 25, font = labelFont, show="*", highlightbackground = 'deep sky blue', highlightthickness = 4)

        #CHECKBOX
        myCheck = tk.IntVar()
        self.passCheck = tk.Checkbutton(self.frame, text = "Show Password", background = 'white', font = checkFont, activebackground = 'deep sky blue', highlightthickness = 0, variable = myCheck, command = checkPass)

        #BUTTONS
        self.confirmButton = tk.Button(self.frame, text = "Confirm", font = buttonFont, command = verifyChange, background = 'deep sky blue', borderwidth = 0)
        self.confirmButton.config(height = 2, width = 13)

        #PACK
        self.frame.pack()
        self.titleLabel.pack(pady = (30,0))
        self.passLabel.pack(pady = (20,0))
        self.passEntry.pack()
        self.passLabel2.pack(pady = (10,0))
        self.passEntry2.pack()
        self.passCheck.pack()
        self.confirmButton.pack(pady = (30,0))


#################################################################################################################################################################
#CUSTOMER SEARCH WINDOW
class CustomerSearchWin:
    
    def __init__(self,master):

        #CUSTOMER_SEARCH_WINDOW
        self.master = master
        master.title("Search for User")
        master.geometry("925x400")
        self.titleFrame = tk.Frame(master)
        self.titleFrame.grid(row = 0, pady= (20,30))
        self.nameFrame = tk.Frame(master)
        self.nameFrame.grid(row = 1, padx = (30,0))
        self.addFrame = tk.Frame(master)
        self.addFrame.grid(row = 2, padx = (35,0))
        self.cityFrame = tk.Frame(master)
        self.cityFrame.grid(row = 3, padx = (35,0))
        self.buttonFrame = tk.Frame(master)
        self.buttonFrame.grid(row = 4, pady = (30,0))

        #FONT
        buttonFont = tkFont.Font(family = "Verdana", size = 20)
        titleFont = tkFont.Font(family = "Verdana", size = 20, weight = tkFont.BOLD)
        labelFont = tkFont.Font(family = "Verdana", size = 15)

        #BUTTON FUNCTIONS
        def searchFunc():
            print("WIP: Search")

        #CONFIG
        self.master.config(background = "white")
        self.titleFrame.config(background = "white")
        self.nameFrame.config(background = "white")
        self.addFrame.config(background = "white")
        self.cityFrame.config(background = "white")
        self.buttonFrame.config(background = "white")

        #LABELS
        self.instLabel = tk.Label(self.titleFrame, text = "Enter one of the following to search", font = titleFont, background = "white", fg = "blue4")

        self.clientNoLabel = tk.Label(self.nameFrame, text = "Client #", font = labelFont, background = "white")

        self.fNameLabel = tk.Label(self.nameFrame, text = "First Name", font = labelFont, background = "white")
        self.mNameLabel = tk.Label(self.nameFrame, text = " Middle Name", font = labelFont, background = "white")
        self.lNameLabel = tk.Label(self.nameFrame, text = " Last Name", font = labelFont, background = "white")

        self.add1Label = tk.Label(self.addFrame, text = "Address 1", font = labelFont, background = "white")
        self.add2Label = tk.Label(self.addFrame, text = "Address 2", font = labelFont, background = "white")

        self.cityLabel = tk.Label(self.cityFrame, text = "City", font = labelFont, background = "white")
        self.stateLabel = tk.Label(self.cityFrame, text = "State", font = labelFont, background = "white")
        self.zipLabel = tk.Label(self.cityFrame, text = "Zipcode", font = labelFont, background = "white")
        self.countryLabel = tk.Label(self.cityFrame, text = "Country", font = labelFont, background = "white")

        #TEXTBOXES
        self.clientText = tk.Entry(self.nameFrame, width = 10, font = ("Verdana",12), highlightbackground='deep sky blue', highlightthickness = 4)

        self.fNameText = tk.Entry(self.nameFrame, width = 25, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.mNameText = tk.Entry(self.nameFrame,width = 15, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.lNameText = tk.Entry(self.nameFrame,width = 20, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        self.add1Text = tk.Entry(self.addFrame, width = 37, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.add2Text = tk.Entry(self.addFrame, width = 37, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        self.cityText = tk.Entry(self.cityFrame, width = 25, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.stateText = tk.Entry(self.cityFrame, width = 10, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.zipText = tk.Entry(self.cityFrame, width = 15, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.countryText = tk.Entry(self.cityFrame, width = 20, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        #BUTTONS
        self.searchButton = tk.Button(self.buttonFrame, text = "SEARCH", font = buttonFont, command = searchFunc, background = "deep sky blue", borderwidth = 0)
        self.searchButton.config(height = 1, width = 15)

        #PACK
        self.instLabel.grid(row = 0, column = 0)
        self.clientNoLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.fNameLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.mNameLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        self.lNameLabel.grid(row = 0, column = 3, sticky = 'w') 
        self.clientText.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        self.fNameText.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        self.mNameText.grid(row = 1, column = 2, sticky = 'w', padx = (0,10))
        self.lNameText.grid(row = 1, column = 3, sticky = 'w')
        self.add1Label.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.add2Label.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.add1Text.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        self.add2Text.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        self.cityLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.stateLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.zipLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        self.countryLabel.grid(row = 0, column = 3, sticky = 'w', padx = (0,10))
        self.cityText.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        self.stateText.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        self.zipText.grid(row = 1, column = 2, sticky = 'w', padx = (0,10))
        self.countryText.grid(row = 1, column = 3, sticky = 'w', padx = (0,10))
        self.searchButton.grid(row = 0, column = 0)


#################################################################################################################################################################
#OLD CUSTOMER SEARCH WINDOW
class OldCustomerSearchWin:
    
    def __init__(self,master):
        #CUSTOMER_SEARCH_WINDOW
        self.master = master
        master.title("Search for User")
        master.geometry("925x400")
        self.titleFrame = tk.Frame(master)
        self.titleFrame.grid(row = 0, pady= (20,30))
        self.nameFrame = tk.Frame(master)
        self.nameFrame.grid(row = 1, padx = (30,0))
        self.addFrame = tk.Frame(master)
        self.addFrame.grid(row = 2, padx = (35,0))
        self.cityFrame = tk.Frame(master)
        self.cityFrame.grid(row = 3, padx = (35,0))
        self.buttonFrame = tk.Frame(master)
        self.buttonFrame.grid(row = 4, pady = (30,0))

        #FONT
        buttonFont = tkFont.Font(family = "Verdana", size = 20)
        titleFont = tkFont.Font(family = "Verdana", size = 20, weight = tkFont.BOLD)
        labelFont = tkFont.Font(family = "Verdana", size = 15)

        #BUTTON FUNCTIONS
        def searchFunc():
            print("WIP: Search")

        #CONFIG
        self.master.config(background = "white")
        self.titleFrame.config(background = "white")
        self.nameFrame.config(background = "white")
        self.addFrame.config(background = "white")
        self.cityFrame.config(background = "white")
        self.buttonFrame.config(background = "white")

        #LABELS
        self.instLabel = tk.Label(self.titleFrame, text = "Enter one of the following to search", font = titleFont, background = "white", fg = "blue4")

        self.clientNoLabel = tk.Label(self.nameFrame, text = "Client #", font = labelFont, background = "white")

        self.fNameLabel = tk.Label(self.nameFrame, text = "First Name", font = labelFont, background = "white")
        self.mNameLabel = tk.Label(self.nameFrame, text = " Middle Name", font = labelFont, background = "white")
        self.lNameLabel = tk.Label(self.nameFrame, text = " Last Name", font = labelFont, background = "white")

        self.add1Label = tk.Label(self.addFrame, text = "Address 1", font = labelFont, background = "white")
        self.add2Label = tk.Label(self.addFrame, text = "Address 2", font = labelFont, background = "white")

        self.cityLabel = tk.Label(self.cityFrame, text = "City", font = labelFont, background = "white")
        self.stateLabel = tk.Label(self.cityFrame, text = "State", font = labelFont, background = "white")
        self.zipLabel = tk.Label(self.cityFrame, text = "Zipcode", font = labelFont, background = "white")
        self.countryLabel = tk.Label(self.cityFrame, text = "Country", font = labelFont, background = "white")

        #TEXTBOXES
        self.clientText = tk.Entry(self.nameFrame, width = 10, font = ("Verdana",12), highlightbackground='deep sky blue', highlightthickness = 4)

        self.fNameText = tk.Entry(self.nameFrame, width = 25, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.mNameText = tk.Entry(self.nameFrame,width = 15, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.lNameText = tk.Entry(self.nameFrame,width = 20, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        self.add1Text = tk.Entry(self.addFrame, width = 37, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.add2Text = tk.Entry(self.addFrame, width = 37, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        self.cityText = tk.Entry(self.cityFrame, width = 25, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.stateText = tk.Entry(self.cityFrame, width = 10, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.zipText = tk.Entry(self.cityFrame, width = 15, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        self.countryText = tk.Entry(self.cityFrame, width = 20, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        #BUTTONS
        self.searchButton = tk.Button(self.buttonFrame, text = "SEARCH", font = buttonFont, command = searchFunc, background = "deep sky blue", borderwidth = 0)
        self.searchButton.config(height = 1, width = 15)

        #PACK
        self.instLabel.grid(row = 0, column = 0)
        self.clientNoLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.fNameLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.mNameLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        self.lNameLabel.grid(row = 0, column = 3, sticky = 'w') 
        self.clientText.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        self.fNameText.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        self.mNameText.grid(row = 1, column = 2, sticky = 'w', padx = (0,10))
        self.lNameText.grid(row = 1, column = 3, sticky = 'w')
        self.add1Label.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.add2Label.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.add1Text.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        self.add2Text.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        self.cityLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.stateLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.zipLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        self.countryLabel.grid(row = 0, column = 3, sticky = 'w', padx = (0,10))
        self.cityText.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        self.stateText.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        self.zipText.grid(row = 1, column = 2, sticky = 'w', padx = (0,10))
        self.countryText.grid(row = 1, column = 3, sticky = 'w', padx = (0,10))
        self.searchButton.grid(row = 0, column = 0)


#################################################################################################################################################################
#CONFIRM DELETE WINDOW
class ConfirmDeleteWin:

    def __init__(self,master):
        #CONFIRM_DELETION_WINDOW
        self.master = master
        master.title("Are you sure you want to delete?")
        master.geometry("500x400")
        self.frame = tk.Frame(master)

        #CONFIG
        self.master.config(background = 'white')
        self.frame.config(background = 'white')

        #FUNCTIONS
        def deleteCust():
            print("WIP: Delete Customer")
        def dontDeleteCust():
            self.master.destroy()

        #FONT 
        buttonFont = tkFont.Font(family = "Verdana", size = 20)
        labelFont = tkFont.Font(family = "Verdana", size = 25, weight = tkFont.BOLD)

        #LABELS
        self.titleLabel = tk.Label(self.frame, text = "Are you sure?", background = 'white', font = labelFont, fg = "blue4")

        #BUTTONS
        self.deleteButton = tk.Button(self.frame, text = "Delete" ,font = buttonFont, command = deleteCust, background='deep sky blue', borderwidth = 0)
        self.deleteButton.config(height = 2, width = 20)
        self.noButton = tk.Button(self.frame, text = "Cancel", font = buttonFont, command = dontDeleteCust, background='deep sky blue', borderwidth = 0)
        self.noButton.config(height = 2, width = 20)

        #PACK
        self.frame.pack()
        self.titleLabel.pack(pady = (30,50))
        self.deleteButton.pack(pady = (0,10))
        self.noButton.pack() 



#################################################################################################################################################################
#SETTINGS WINDOW
class AddNewCustWin:

    def __init__(self,master):
        
        #DB LOGIN
        conn = psycopg2.connect("dbname = LoginInfo user = postgres password = harlan host = localhost")
        cur = conn.cursor()

        #NEW_master
        self.master = master
        master.title("Customer Information")
        master.geometry("1000x600")
        self.TitleFrame = tk.Frame(master)
        self.TitleFrame.grid(row = 0)
        self.InfoFrame = tk.Frame(master)
        self.InfoFrame.grid(row = 1, padx = (35,0))
        self.NameFrame = tk.Frame(master)
        self.NameFrame.grid(row = 2, padx = (35,0))
        self.AddFrame = tk.Frame(master)
        self.AddFrame.grid(row = 3, padx = (45,0))
        self.CityFrame = tk.Frame(master)
        self.CityFrame.grid(row = 4, padx = (35,0))
        self.PhoneFrame = tk.Frame(master)
        self.PhoneFrame.grid(row = 5, padx = (40,0))
        self.ButtonsFrame = tk.Frame(master)
        self.ButtonsFrame.grid(row = 6, pady = (50,0))
        self.ButtonsFrame2 = tk.Frame(master)
        self.ButtonsFrame2.grid(row = 7, pady = (10,0))
        self.ButtonsFrame3 = tk.Frame(master)
        self.ButtonsFrame3.grid(row = 8, pady = (10,0))

        #CONFIG 
        self.master.config(background = "white")
        self.TitleFrame.config(background = "white")
        self.InfoFrame.config(background = "white")
        self.NameFrame.config(background = "white")
        self.AddFrame.config(background = "white")
        self.CityFrame.config(background = "white")
        self.PhoneFrame.config(background = "white")
        self.ButtonsFrame.config(background = "white")
        self.ButtonsFrame2.config(background = "white")
        self.ButtonsFrame3.config(background = "white")

        #FONT
        buttonFont = tkFont.Font(family = "Verdana", size = 15)
        titleFont = tkFont.Font(family = "Verdana", size = 20, weight = tkFont.BOLD)
        labelFont = tkFont.Font(family = "Verdana", size = 15)
        boxFont = tkFont.Font(family = "Verdana", size = 12)

        #BUTTON FUNCTIONS
        def addUser():
            cur.execute("INSERT INTO address VALUES (DEFAULT, '%s', '%s', '%s', '%s', '%s', '%s')" % (self.address1Text.get(), self.address2Text.get(), self.cityText.get(), self.stateText.get(), self.zipText.get(), self.countryText.get()))
            conn.commit()
            cur.execute("SELECT AddressID FROM address where Address1 = '%s' and Address2 = '%s' and City = '%s' and State = '%s' and ZipCode = '%s' and Country = '%s';" % (self.address1Text.get(), self.address2Text.get(), self.cityText.get(), self.stateText.get(), self.zipText.get(), self.countryText.get()))
            conn.commit()
            rows = cur.fetchone()
            cur.execute("INSERT INTO customers VALUES (%d, %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (int(self.clientText.get()), int(rows[0]), self.tNameText.get(), self.fNameText.get(), self.lNameText.get(), self.mNameText.get(), self.phoneText.get(), self.emailText.get(), ' '))
            conn.commit()
            conn.close()
            print("USER ADDED!")

        #LABELS
        self.titleLabel = tk.Label(self.TitleFrame,text = "Add New Customer", font = titleFont, background = "white", fg = "blue4")

        self.clientNoLabel = tk.Label(self.InfoFrame, text = "Client #", font = labelFont, background = "white")
        self.labelCodeLabel = tk.Label(self.InfoFrame, text = "LabelCode", font = labelFont, background = "white")

        self.tNameLabel = tk.Label(self.NameFrame, text = "Title", font = labelFont, background = "white")
        self.fNameLabel = tk.Label(self.NameFrame, text = "FirstName", font = labelFont, background = "white")
        self.mNameLabel = tk.Label(self.NameFrame, text = " MiddleName", font = labelFont, background = "white")
        self.lNameLabel = tk.Label(self.NameFrame, text = " LastName", font = labelFont, background = "white")

        self.address1Label = tk.Label(self.AddFrame, text = "Address 1", font = labelFont, background = "white")
        self.address2Label = tk.Label(self.AddFrame, text = " Address 2", font = labelFont, background = "white")

        self.cityLabel = tk.Label(self.CityFrame, text = "City", font = labelFont, background = "white")
        self.stateLabel = tk.Label(self.CityFrame, text = " State", font = labelFont, background = "white")
        self.zipCodeLabel = tk.Label(self.CityFrame, text = " Zip Code", font = labelFont, background = "white")
        self.countryLabel = tk.Label(self.CityFrame, text = "Country", font = labelFont, background = "white")

        self.phoneLabel = tk.Label(self.PhoneFrame, text = " Phone", font = labelFont, background = "white")
        self.emailLabel = tk.Label(self.PhoneFrame, text = "Email", font = labelFont, background = "white")

        #TEXTBOXES
        self.clientText = tk.Entry(self.InfoFrame, width = 11, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.labelCodeText = tk.Entry(self.InfoFrame, width = 11, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        self.tNameText = tk.Entry(self.NameFrame, width = 11, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.fNameText = tk.Entry(self.NameFrame, width = 30, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.mNameText = tk.Entry(self.NameFrame, width = 13, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.lNameText = tk.Entry(self.NameFrame, width = 30, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        self.address1Text = tk.Entry(self.AddFrame, width = 44, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.address2Text = tk.Entry(self.AddFrame, width = 44, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        self.cityText = tk.Entry(self.CityFrame, width = 25, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.stateText = tk.Entry(self.CityFrame, width = 12, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.zipText = tk.Entry(self.CityFrame, width = 16, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.countryText = tk.Entry(self.CityFrame, width = 30, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        self.phoneText = tk.Entry(self.PhoneFrame, width = 31, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        self.emailText = tk.Entry(self.PhoneFrame, width = 57, font = boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        #BUTTONS
        self.addButton = tk.Button(self.ButtonsFrame, text = "ADD", font = buttonFont, command = addUser, background = "deep sky blue", borderwidth = 0)

        #BUTTON_CONFIG
        self.addButton.config(height = 2, width = 15)

        #PACK
        self.titleLabel.grid(row = 0, column = 0, pady = (30,20))
        self.clientNoLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.labelCodeLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.clientText.grid(row = 1, column = 0, padx = (0,10))
        self.labelCodeText.grid(row = 1, column = 1, padx = (0,70))
        self.tNameLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.fNameLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.mNameLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        self.lNameLabel.grid(row = 0, column = 3, sticky = 'w')
        self.tNameText.grid(row = 1, column = 0, padx = (0,10))
        self.fNameText.grid(row = 1, column = 1, padx = (0,10))
        self.mNameText.grid(row = 1, column = 2, padx = (0,10))
        self.lNameText.grid(row = 1, column = 3)
        self.address1Label.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.address2Label.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.address1Text.grid(row = 1, column = 0, padx = (0,10))
        self.address2Text.grid(row = 1, column = 1, padx = (0,10))
        self.cityLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.stateLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.zipCodeLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        self.countryLabel.grid(row = 0, column = 3, sticky = 'w', padx = (0,10))
        self.cityText.grid(row = 1, column = 0, padx = (0,10))
        self.stateText.grid(row = 1, column = 1, padx = (0,10))
        self.zipText.grid(row = 1, column = 2, padx = (0,10))
        self.countryText.grid(row = 1, column = 3, padx = (0,10))
        self.phoneLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        self.emailLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        self.phoneText.grid(row = 1, column = 0, padx = (0,10))
        self.emailText.grid(row = 1, column = 1, padx = (0,10))
        self.addButton.grid(row = 0, column = 0, padx = (0,10))


#################################################################################################################################################################
#################################################################################################################################################################
#Sample App
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginWin)
        self.configure(background = 'white')

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

################################################################################################################################################################
#Main
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()