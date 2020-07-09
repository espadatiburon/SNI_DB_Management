
import Tkinter as tk
from PIL import ImageTk, Image
import tkFont

#ADD NOT WORKING
##SETTINGS NOT WORKING (CANNOT PASS THE WINDOW NAME)
### SEARCH ADD DELETE ON CUST INFO NOT DISAPPEARING

#################################################################################################################################################################
#LOGIN WINDOW
class LoginWin(tk.Frame):
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)
        #DB LOGIN

        #LOGIN WINDOW
        master.title("Login")
        tk.img = ImageTk.PhotoImage(Image.open("SNI.jpg").resize((450,400)))
        tk.myPanel = tk.Label(self, image = tk.img, highlightthickness = 0, borderwidth = 0)
        master.geometry("1200x900")

        #FUNCTIONS
        def verifyLogin():
            print("Login")
            master.switch_frame(MenuWin)
        def checkPass():
            print("CheckPass")

        #CONFIG
        self.configure(background = 'white')

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
        tk.myPanel.grid()
        tk.myPanel.grid(column = 1, row = 0,pady = (30,0))
        tk.userLabel.grid(column = 1, row = 1, pady = (20,0))
        tk.userEntry.grid(column = 1, row = 2)
        tk.passLabel.grid(column = 1, row = 3, pady = (5,0))
        tk.passEntry.grid(column = 1, row = 4)
        tk.passCheck.grid(column = 1, row = 5)
        tk.loginButton.grid(column = 1, row = 6, pady = (30,0))

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(2, weight = 1)



#################################################################################################################################################################
#MENU WINDOW
class MenuWin(tk.Frame):
    
    def __init__(self, master):
        #MENU WINDOW
        tk.Frame.__init__(self, master)

        master.title("Main Menu")
        master.geometry("800x575")

        def customerInfo():
            master.switch_frame(CustomerInfoWin)
        def addTransactions():    
            master.switch_frame(NewOrExistingWin)
        def mySettings():
            master.switch_frame(SettingsWin)
        def getReports():
            master.switch_frame(ReportsWin)
            
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
        tk.titleLabel.grid(pady = (25,0))
        tk.CustomerInfoButton.grid(pady = (20,0))
        tk.AddTransactionsButton.grid(pady = (15,0))
        tk.SettingsButton.grid(pady = (15,0))
        tk.ReportsButton.grid(pady = (15,0))

#################################################################################################################################################################
#CUSTOMER INFORMATION WINDOW
class CustomerInfoWin(tk.Frame):

    def __init__(self,master):
        
        #DB
        #conn = psycopg2.connect("dbname = LoginInfo user = postgres password = harlan host = localhost")
        #cur = conn.cursor()

        #GET CUSTOMER INFO
        #cur.execute("select * from customers;")
        #result = cur.fetchone()

        #GET ADDRESS INFO
        #cur2 = conn.cursor()
        #cur2.execute("select * from address;")
        #result2 = cur2.fetchone()

        #CUSTOMER WINDOW
        tk.Frame.__init__(self, master)

        master.title("Customer Information")
        master.geometry("1100x700")
        self = tk.Frame(master)
        self.grid(row = 0)
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
        self.config(background = "white")
        tk.InfoFrame.config(background = "white")
        tk.NameFrame.config(background = "white")
        tk.AddFrame.config(background = "white")
        tk.CityFrame.config(background = "white")
        tk.PhoneFrame.config(background = "white")
        tk.ButtonsFrame.config(background = "white")
        tk.ButtonsFrame2.config(background = "white")
        tk.ButtonsFrame3.config(background = "white")

        #FONT
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 15)
        tk.titleFont = tkFont.Font(family = "Verdana", size = 20, weight = tkFont.BOLD)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 15)
        tk.boxFont = tkFont.Font(family = "Verdana", size = 12)

        #BUTTON FUNCTIONS
        def newUser():
            master.switch_frame(AddNewCustWin)

        def editUser():
            tk.clientText.configure(state='normal')
            tk.giftText.configure(state='normal')
            tk.labelCodeText.configure(state='normal')
            tk.copiesText.configure(state='normal')
            tk.startText.configure(state='normal')
            tk.expText.configure(state='normal')

            tk.tNameText.configure(state='normal')
            tk.fNameText.configure(state='normal')
            tk.mNameText.configure(state='normal')
            tk.lNameText.configure(state='normal')

            tk.address1Text.configure(state='normal')
            tk.address2Text.configure(state='normal')

            tk.cityText.configure(state='normal')
            tk.stateText.configure(state='normal')
            tk.zipText.configure(state='normal')
            tk.countryText.configure(state='normal')

            tk.phoneText.configure(state='normal')
            tk.emailText.configure(state='normal')

        def deleteUser():
            master.switch_frame(ConfirmDeleteWin)

        def custLabel():
            print("work in progress for customer label")

        def getSubs():
            print("work in progress for subs")

        def getTransactions():
            print("Work in progress for transactions")

        def getSponsors():
            print("work in progress for checking sponsors and sponsoring")

        def searchUser():
            master.switch_frame(CustomerSearchWin)

        def showHistory():
            print("work in progress for history")

        def showPrev():
            print("work in progress for previous")

        def showNext():
        #    result = cur.fetchone()

            #if not result:
            #    print("no more customers")
            #else:
              #  print("Show next")
                #cur2.execute("select addressid from customers where customerid = %d"%(result[0]))
                #myAddress = cur2.fetchone()
                #cur2.execute("select * from address where addressid = %d;"%(int(myAddress[0])))
                #result2 = cur2.fetchone()
             #   editUser()
            deleteInfo()
                #insertInfo(result, result2)            
            #    makeUneditable()
            print("test")

        def deleteInfo():
            tk.clientText.delete(0,tk.END)
            tk.tNameText.delete(0,tk.END)
            tk.fNameText.delete(0,tk.END)
            tk.mNameText.delete(0,tk.END)
            tk.lNameText.delete(0,tk.END)
            tk.phoneText.delete(0,tk.END)
            tk.emailText.delete(0,tk.END)

            tk.address1Text.delete(0,tk.END)
            tk.address2Text.delete(0,tk.END)
            tk.cityText.delete(0,tk.END)
            tk.stateText.delete(0,tk.END)
            tk.zipText.delete(0,tk.END)
            tk.countryText.delete(0,tk.END)

        #def insertInfo(result, result2):
        #    tk.clientText.insert(0,result[0])
        #    tk.tNameText.insert(0,result[2])
        #    tk.fNameText.insert(0,result[3])
        #    tk.mNameText.insert(0,result[5])
        #    tk.lNameText.insert(0,result[4])
        #    tk.phoneText.insert(0,result[6])
        #    tk.emailText.insert(0,result[7])

        #    tk.address1Text.insert(0,result2[1])
        #    tk.address2Text.insert(0,result2[2])
        #    tk.cityText.insert(0,result2[3])
        #    tk.stateText.insert(0,result2[4])
        #    tk.zipText.insert(0,result2[5])
        #    tk.countryText.insert(0,result2[6])

        def makeUneditable():
            tk.clientText.configure(state='readonly')
            tk.giftText.configure(state='readonly')
            tk.labelCodeText.configure(state='readonly')
            tk.copiesText.configure(state='readonly')
            tk.startText.configure(state='readonly')
            tk.expText.configure(state='readonly')

            tk.tNameText.configure(state='readonly')
            tk.fNameText.configure(state='readonly')
            tk.mNameText.configure(state='readonly')
            tk.lNameText.configure(state='readonly')

            tk.address1Text.configure(state='readonly')
            tk.address2Text.configure(state='readonly')

            tk.cityText.configure(state='readonly')
            tk.stateText.configure(state='readonly')
            tk.zipText.configure(state='readonly')
            tk.countryText.configure(state='readonly')

            tk.phoneText.configure(state='readonly')
            tk.emailText.configure(state='readonly')

        #LABELS
        tk.titleLabel = tk.Label(self,text = "Customer Information", font = tk.titleFont, background = "white", fg = "blue4")

        tk.clientNoLabel = tk.Label(tk.InfoFrame, text = "Client #", font = tk.labelFont, background = "white")
        tk.giftNoLabel = tk.Label(tk.InfoFrame, text = "Gift #", font = tk.labelFont, background = "white")
        tk.labelCodeLabel = tk.Label(tk.InfoFrame, text = "LabelCode", font = tk.labelFont, background = "white")
        tk.copiesLabel = tk.Label(tk.InfoFrame, text = "Copies", font = tk.labelFont, background = "white")
        tk.startLabel = tk.Label(tk.InfoFrame, text = "Start Date", font = tk.labelFont, background = "white")
        tk.expLabel = tk.Label(tk.InfoFrame, text = "Exp Date", font = tk.labelFont, background = "white")

        tk.tNameLabel = tk.Label(tk.NameFrame, text = "Title", font = tk.labelFont, background = "white")
        tk.fNameLabel = tk.Label(tk.NameFrame, text = "FirstName", font = tk.labelFont, background = "white")
        tk.mNameLabel = tk.Label(tk.NameFrame, text = " MiddleName", font = tk.labelFont, background = "white")
        tk.lNameLabel = tk.Label(tk.NameFrame, text = " LastName", font = tk.labelFont, background = "white")

        tk.address1Label = tk.Label(tk.AddFrame, text = "Address 1", font = tk.labelFont, background = "white")
        tk.address2Label = tk.Label(tk.AddFrame, text = " Address 2", font = tk.labelFont, background = "white")

        tk.cityLabel = tk.Label(tk.CityFrame, text = "City", font = tk.labelFont, background = "white")
        tk.stateLabel = tk.Label(tk.CityFrame, text = " State", font = tk.labelFont, background = "white")
        tk.zipCodeLabel = tk.Label(tk.CityFrame, text = " Zip Code", font = tk.labelFont, background = "white")
        tk.countryLabel = tk.Label(tk.CityFrame, text = "Country", font = tk.labelFont, background = "white")

        tk.phoneLabel = tk.Label(tk.PhoneFrame, text = " Phone", font = tk.labelFont, background = "white")
        tk.emailLabel = tk.Label(tk.PhoneFrame, text = "Email", font = tk.labelFont, background = "white")

        #TEXTBOXES
        tk.clientText = tk.Entry(tk.InfoFrame, width = 11, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.giftText = tk.Entry(tk.InfoFrame, width = 11, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.labelCodeText = tk.Entry(tk.InfoFrame, width = 11, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.copiesText = tk.Entry(tk.InfoFrame, width = 11, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.startText = tk.Entry(tk.InfoFrame, width = 15, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.expText = tk.Entry(tk.InfoFrame, width = 15, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        tk.tNameText = tk.Entry(tk.NameFrame, width = 11, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.fNameText = tk.Entry(tk.NameFrame, width = 30, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.mNameText = tk.Entry(tk.NameFrame, width = 13, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.lNameText = tk.Entry(tk.NameFrame, width = 30, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        tk.address1Text = tk.Entry(tk.AddFrame, width = 44, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.address2Text = tk.Entry(tk.AddFrame, width = 44, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        tk.cityText = tk.Entry(tk.CityFrame, width = 25, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.stateText = tk.Entry(tk.CityFrame, width = 12, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.zipText = tk.Entry(tk.CityFrame, width = 16, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.countryText = tk.Entry(tk.CityFrame, width = 30, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        tk.phoneText = tk.Entry(tk.PhoneFrame, width = 31, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.emailText = tk.Entry(tk.PhoneFrame, width = 57, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        #INSERT_INFO
        #insertInfo(result, result2)
        
        #TEXTBOX_CONFIG
        makeUneditable()

        #BUTTONS
        tk.addButton = tk.Button(tk.ButtonsFrame, text = "ADD", font = tk.buttonFont, command = newUser, background = "deep sky blue", borderwidth = 0)
        tk.editButton = tk.Button(tk.ButtonsFrame, text = "EDIT", font = tk.buttonFont, command = editUser, background = "deep sky blue", borderwidth = 0)
        tk.deleteButton = tk.Button(tk.ButtonsFrame, text = "DELETE", font = tk.buttonFont, command = deleteUser, background = "deep sky blue", borderwidth = 0)
        tk.searchButton = tk.Button(tk.ButtonsFrame, text = "SEARCH", font = tk.buttonFont, command = searchUser, background = "deep sky blue", borderwidth = 0)
        tk.printLabelButton = tk.Button(tk.ButtonsFrame2, text = "PRINT LABELS" , font = tk.buttonFont, command  = custLabel, background = "deep sky blue", borderwidth = 0)
        tk.subsButton = tk.Button(tk.ButtonsFrame2, text = "SUBSCRIPTIONS", font = tk.buttonFont, command = getSubs, background = "deep sky blue", borderwidth = 0)
        tk.transButton = tk.Button(tk.ButtonsFrame2, text = "TRANSACTIONS", font = tk.buttonFont, command = getTransactions, background = "deep sky blue", borderwidth = 0)
        tk.sponsorButton = tk.Button(tk.ButtonsFrame2, text = "SPONSORS", font = tk.buttonFont, command = getSponsors, background = "deep sky blue", borderwidth = 0)
        tk.prevButton = tk.Button(tk.ButtonsFrame3, text = "PREVIOUS", font = tk.buttonFont, command = showPrev, background = "deep sky blue", borderwidth = 0)
        tk.historyButton = tk.Button(tk.ButtonsFrame3, text = "HISTORY", font = tk.buttonFont, command = showHistory, background = "deep sky blue", borderwidth = 0)
        tk.nextButton = tk.Button(tk.ButtonsFrame3, text = "NEXT", font = tk.buttonFont, command = showNext, background = "deep sky blue", borderwidth = 0)

        #BUTTON_CONFIG
        tk.addButton.config(height = 1, width = 13)
        tk.editButton.config(height = 1, width = 13)
        tk.deleteButton.config(height = 1, width = 13)
        tk.searchButton.config(height = 1, width = 13)
        tk.printLabelButton.config(height = 1, width = 15)
        tk.subsButton.config(height = 1, width = 15)
        tk.transButton.config(height = 1, width = 15)
        tk.sponsorButton.config(height = 1, width = 15)
        tk.historyButton.config(height = 1, width = 13)
        tk.prevButton.config(height = 1, width = 13)
        tk.nextButton.config(height = 1, width = 13)

        #PACK
        tk.titleLabel.grid(row = 0, column = 0, pady = (30,20))
        tk.clientNoLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.giftNoLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.labelCodeLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        tk.copiesLabel.grid(row = 0, column = 3, sticky = 'w', padx = (0,10))
        tk.startLabel.grid(row = 0, column = 4, sticky = 'w', padx = (0,10))
        tk.expLabel.grid(row = 0, column = 5, sticky = 'w')
        tk.clientText.grid(row = 1, column = 0, padx = (0,10))
        tk.giftText.grid(row = 1, column = 1, padx = (0,10))
        tk.labelCodeText.grid(row = 1, column = 2, padx = (0,70))
        tk.copiesText.grid(row = 1, column = 3, padx = (0,10))
        tk.startText.grid(row = 1, column = 4, padx = (0,10))
        tk.expText.grid(row = 1, column = 5)
        tk.tNameLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.fNameLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.mNameLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        tk.lNameLabel.grid(row = 0, column = 3, sticky = 'w')
        tk.tNameText.grid(row = 1, column = 0, padx = (0,10))
        tk.fNameText.grid(row = 1, column = 1, padx = (0,10))
        tk.mNameText.grid(row = 1, column = 2, padx = (0,10))
        tk.lNameText.grid(row = 1, column = 3)
        tk.address1Label.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.address2Label.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.address1Text.grid(row = 1, column = 0, padx = (0,10))
        tk.address2Text.grid(row = 1, column = 1, padx = (0,10))
        tk.cityLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.stateLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.zipCodeLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        tk.countryLabel.grid(row = 0, column = 3, sticky = 'w', padx = (0,10))
        tk.cityText.grid(row = 1, column = 0, padx = (0,10))
        tk.stateText.grid(row = 1, column = 1, padx = (0,10))
        tk.zipText.grid(row = 1, column = 2, padx = (0,10))
        tk.countryText.grid(row = 1, column = 3, padx = (0,10))
        tk.phoneLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.emailLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.phoneText.grid(row = 1, column = 0, padx = (0,10))
        tk.emailText.grid(row = 1, column = 1, padx = (0,10))
        tk.addButton.grid(row = 0, column = 0, padx = (0,10))
        tk.editButton.grid(row = 0, column = 1, padx = (0,10))
        tk.deleteButton.grid(row = 0, column = 2, padx = (0,10))
        tk.searchButton.grid(row = 0, column = 3)
        tk.printLabelButton.grid(row = 1, column = 0, padx = (0,10))
        tk.subsButton.grid(row = 1, column = 1, padx = (0,10))
        tk.transButton.grid(row = 1, column = 2, padx = (0,10))
        tk.sponsorButton.grid(row = 1, column = 3)
        tk.prevButton.grid(row = 2, column = 0, padx = (0,10))
        tk.historyButton.grid(row = 2, column = 1, padx = (0,10))
        tk.nextButton.grid(row = 2, column = 2)


#################################################################################################################################################################
#NEW OR EXISTING CUSTOMER WINDOW
class NewOrExistingWin(tk.Frame):

    def __init__(self,master):

        #NEW_OR_EXISTING_WINDOW
        tk.Frame.__init__(self, master)
        master.title("New or Existing Customer?")
        master.geometry("600x400")

        #CONFIG
        self.config(background = 'white')

        #FUNCTIONS
        def existingTrans():
            master.switch_frame(OldCustomerSearchWin)
        def newTrans():
            master.switch_frame(AddNewCustWin)

        #FONT 
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 20)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 25)

        #LABELS
        tk.titleLabel = tk.Label(self, text = "New or Existing Customer?", background = 'white', font = tk.labelFont, fg = "blue4")

        #BUTTONS
        tk.newTransButton = tk.Button(self, text = "New" ,font = tk.buttonFont, command = newTrans, background='deep sky blue', borderwidth = 0)
        tk.newTransButton.config(height = 2, width = 20)
        tk.existingTransButton = tk.Button(self, text = "Existing", font = tk.buttonFont, command = existingTrans, background='deep sky blue', borderwidth = 0)
        tk.existingTransButton.config(height = 2, width = 20)

        #PACK
        tk.titleLabel.grid(pady = (30,50))
        tk.newTransButton.grid(pady = (0,10))
        tk.existingTransButton.grid() 




#################################################################################################################################################################
#SETTINGS WINDOW
class SettingsWin(tk.Frame):

    def __init__(self,master):

        #SETTINGS WINDOW
        tk.Frame.__init__(self, master)

        master.title("Settings")
        master.geometry("800x575")

        #FONT
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 20)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 30, weight = tkFont.BOLD)

        
        def changePass():
            master.switch_frame(checkLoginWin('changePass'))

        def changeUser():
            master.switch_frame(checkLoginWin('changeUser'))

        def editItems():
            master.switch_frame(checkLoginWin('editItems'))

        def newUser():
            master.switch_frame(checkLoginWin('newUser'))

        #CONFIG
        self.config(background = "white")

        #LABELS
        tk.titleLabel = tk.Label(self, text = "My Settings", background = "white", font = tk.labelFont, fg = "blue4")

        #BUTTONS
        tk.changePassButton = tk.Button(self, text = "Change Password", font = tk.buttonFont, command = changePass, background = "deep sky blue", borderwidth = 0)
        tk.changeUserButton = tk.Button(self, text = "Change Username", font = tk.buttonFont, command = changeUser, background = "deep sky blue", borderwidth = 0)
        tk.editItemsButton = tk.Button(self, text = "Edit Items", font = tk.buttonFont, command = editItems, background = "deep sky blue", borderwidth = 0)
        tk.newUserButton = tk.Button(self, text = "Add New User", font = tk.buttonFont, command = newUser, background = "deep sky blue", borderwidth = 0)
        tk.changePassButton.config(height = 2, width = 25)
        tk.changeUserButton.config(height = 2, width = 25)
        tk.editItemsButton.config(height = 2, width = 25)
        tk.newUserButton.config(height = 2, width = 25)

        #PACK
        tk.titleLabel.grid(pady = (30,20))
        tk.editItemsButton.grid()
        tk.newUserButton.grid(pady = (15,0))
        tk.changeUserButton.grid(pady = (15,0))
        tk.changePassButton.grid(pady = (15,0))




#################################################################################################################################################################
#REPORTS WINDOW
class ReportsWin(tk.Frame):

    def __init__(self,master):
        #master
        tk.Frame.__init__(self, master)

        master.title("Reports")
        master.geometry("800x575")

        #CONFIG
        self.config(background = "white")

        #FONT
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 20)
        tk.labelFont = tkFont.Font(family = "verdana", size = 30, weight = tkFont.BOLD)

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
        tk.titleLabel = tk.Label(self, text = "Reports", background = "white", font = tk.labelFont, fg = "blue4")

        #BUTTONS
        tk.noticesButton = tk.Button(self, text = "Notices of Expiration", font = tk.buttonFont, command = getNotices, background = "deep sky blue", borderwidth = 0)
        tk.areaButton = tk.Button(self, text = "By Area", font = tk.buttonFont, command = getByArea, background = "deep sky blue", borderwidth = 0)
        tk.transactionButton = tk.Button(self, text = "Transaction History", font = tk.buttonFont, command = getTransactions, background = "deep sky blue", borderwidth = 0)
        tk.expiredButton = tk.Button(self, text = "Expired Subscriptions", font = tk.buttonFont, command = getExpired, background = "deep sky blue", borderwidth = 0)

        #BUTTON CONFIG
        tk.noticesButton.config(height = 2, width = 25)
        tk.areaButton.config(height = 2, width = 25)
        tk.transactionButton.config(height = 2, width = 25)
        tk.expiredButton.config(height = 2, width = 25)

        #PACK
        tk.titleLabel.grid(pady = (25,20))
        tk.noticesButton.grid()
        tk.areaButton.grid(pady = (15,0))
        tk.transactionButton.grid(pady = (15,0))
        tk.expiredButton.grid(pady = (15,0))

#################################################################################################################################################################
#CHECK LOGIN WINDOW
class CheckLoginWin(tk.Frame):

    def __init__(self, master,nextWindow):
        

        #DB LOGIN
        #conn = psycopg2.connect("dbname = LoginInfo user = postgres password = harlan host = localhost")
        #cur = conn.cursor()

        #LOGIN WINDOW
        tk.Frame.__init__(self, master)
        master.title("Login")
        master.geometry("700x500")

        #FUNCTIONS
        def verifyLogin():
            #myVerify = False
            #cur.execute("SELECT username, password FROM users;")
            #for username, password in cur.fetchall():
            #    if(username == self.userEntry.get()):
            #        if(password == self.passEntry.get()):
            #            myVerify = True
            #        else:
            #            print "Wrong Password"
            #    else:
            #        print "Wrong Username"

            #if(myVerify):   
           #    if(nextWindow == 'changePass'):
            #        self.newWindow = tk.Toplevel(self.master)
            #        self.app = ChangePassWin(self.newWindow)
            #        conn.close()
            #    elif(nextWindow == 'changeUser'):
            #        self.newWindow = tk.Toplevel(self.master)
            #        self.app = ChangeUserWin(self.newWindow)
            #        conn.close()
            #    elif(nextWindow == 'editItems'):
            #        self.newWindow = tk.Toplevel(self.master)
            #        self.app = EditItemsWin(self.newWindow)
            #        conn.close()
            #    elif(nextWindow == 'newUser'):
            #        self.newWindow = tk.Toplevel(self.master)
            #        self.app = AddNewUserWin(self.newWindow)
            #        conn.close()
           # else:
            #    self.master.destroy()
            print("testing")
        def checkPass():
            if(myCheck.get() == 0):
                tk.passEntry.config(show="*")
            else:
                tk.passEntry.config(show = "")

        #CONFIG
        self.configure(background = 'white')

        #FONT 
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 25)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 25)
        tk.checkFont = tkFont.Font(family = "Verdana", size = 15)
        tk.titleFont = tkFont.Font(family = "Verdana", size = 25, weight = tkFont.BOLD)

        #LABELS
        tk.titleLabel = tk.Label(self, text = "Please Login", background = "white", font = tk.titleFont, fg = "blue4")
        tk.userLabel = tk.Label(self, text = "User Name", background = 'white', font = tk.labelFont)
        tk.passLabel = tk.Label(self, text = "Password", background = 'white', font = tk.labelFont)

        #TEXTBOXES
        tk.userEntry = tk.Entry(self, width = 25, font = tk.labelFont, highlightbackground='deep sky blue', highlightthickness = 4)
        tk.passEntry = tk.Entry(self, width = 25, font = tk.labelFont, show="*", highlightbackground = 'deep sky blue', highlightthickness = 4)

        #CHECKBOX
        myCheck = tk.IntVar()
        tk.passCheck = tk.Checkbutton(self, text = "Show Password", background = 'white', font = tk.checkFont, activebackground = 'deep sky blue', highlightthickness = 0, variable = myCheck, command = checkPass)

        #BUTTONS
        tk.loginButton = tk.Button(self, text = "LOGIN", font = tk.buttonFont, command = verifyLogin, background = 'deep sky blue', borderwidth = 0)
        tk.loginButton.config(height = 2, width = 13)

        #PACK
        tk.titleLabel.grid(pady = (30,0))
        tk.userLabel.grid(pady = (20,0))
        tk.userEntry.grid()
        tk.passLabel.grid(pady = (5,0))
        tk.passEntry.grid()
        tk.passCheck.grid()
        tk.loginButton.grid(pady = (30,0))


#################################################################################################################################################################
#EDIT ITEMS WINDOW
class EditItemsWin(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        print("WIP: Edit Items")

#################################################################################################################################################################
#ADD NEW USER WINDOW
class AddNewUserWin(tk.Frame):

    def __init__(self, master):
        
        #DB LOGIN
        #conn = psycopg2.connect("dbname = LoginInfo user = postgres password = harlan host = localhost")
        #cur = conn.cursor()

        #ADD_NEW_USER_WINDOW
        tk.Frame.__init__(self, master)
        master.title("Create New User")
        master.geometry("900x700")

        #FUNCTIONS
        def CreateUser():
            #cur.execute("SELECT usersid FROM users where username = '%s';" % self.userEntry.get())
            #alreadyUsed = cur.fetchall()
            #if not alreadyUsed:
            #    mySql = "insert into users values (DEFAULT, 1, '%s', '%s')" % (self.userEntry.get(), self.passEntry.get())
            #    cur.execute(mySql)
            #    conn.commit()
            #    conn.close()
                print("Success!")
           # else:
                print("This username has already been used!")

        def checkPass():
            if(myCheck.get() == 0):
                tk.passEntry.config(show = "*")
            else:
                tk.passEntry.config(show = "")

        #FONT 
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 20)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 20)
        tk.checkFont = tkFont.Font(family = "Verdana", size = 15)
        tk.radioFont = tkFont.Font(family = "Verdana", size = 13)

        #CONFIG
        self.config(background = "white")

        #LABELS
        tk.titleLabel = tk.Label(self, text = "New User", background = "white", font = ("Verdana", 30, tkFont.BOLD), fg = "blue4")
        tk.userLabel = tk.Label(self, text = "User Name", background = "white", font = tk.labelFont)
        tk.passLabel = tk.Label(self, text = "Password", background = "white", font = tk.labelFont)
        tk.privLabel = tk.Label(self, text = "Permissions", background = "white", font = tk.labelFont)

        #TEXTBOXES
        tk.userEntry = tk.Entry(self, width = 22, font = ("Verdana", 30), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.passEntry = tk.Entry(self, width = 22, font = ("Verdana", 30), show = "*", highlightbackground='deep sky blue', highlightthickness = 4)

        #CHECKBOX
        myCheck = tk.IntVar()
        tk.passCheck = tk.Checkbutton(self, text = "Show Password", background = 'white', font = tk.checkFont, activebackground = 'deep sky blue', highlightthickness = 0, variable = myCheck, command = checkPass)

        #RADIO_BUTTONS
        tk.adminRadio = tk.Radiobutton(self, text = "Admin", value = 1, background = "white", font = tk.radioFont, tristatevalue = 0, highlightthickness = 0, activebackground = 'deep sky blue')
        tk.editRadio = tk.Radiobutton(self, text = "Edit Only", value = 2, background = "white", font = tk.radioFont, tristatevalue = 0, highlightthickness = 0, activebackground = 'deep sky blue')
        tk.readRadio = tk.Radiobutton(self, text = "Read Only", value = 3, background = "white", font = tk.radioFont, tristatevalue = 0, highlightthickness = 0, activebackground = 'deep sky blue')

        #BUTTONS
        tk.CreateButton = tk.Button(self, text = "CREATE USER" ,font = tk.buttonFont, command = CreateUser, background = "deep sky blue", borderwidth = 0)
        tk.CreateButton.config(height = 2, width = 13)


        #PACK
        tk.titleLabel.grid(pady=(30,20))
        tk.userLabel.grid()
        tk.userEntry.grid()
        tk.passLabel.grid(pady = (20,0))
        tk.passEntry.grid()
        tk.passCheck.grid()
        tk.privLabel.grid(pady = (25,0))
        tk.adminRadio.grid()
        tk.editRadio.grid()
        tk.readRadio.grid()
        tk.CreateButton.grid(pady = (20,0))


#################################################################################################################################################################
#CHANGE USER WINDOW
class ChangeUserWin(tk.Frame):

    def __init__(self, master):

        #CHANGE_USER_WINDOW
        tk.Frame.__init__(self, master)
        master.title("Change Username")
        master.geometry("600x400")

        #FUNCTIONS
        def verifyChange():
            print("WIP:Change User")

        #CONFIG
        self.configure(background = 'white')

        #FONT 
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 25)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 25)
        tk.titleFont = tkFont.Font(family = "Verdana", size = 25, weight = tkFont.BOLD)

        #LABELS
        tk.titleLabel = tk.Label(self, text = "Enter New Username", background = "white", font = tk.titleFont, fg = "blue4")
        tk.userLabel = tk.Label(self, text = "User Name", background = 'white', font = tk.labelFont)

        #TEXTBOXES
        tk.userEntry = tk.Entry(self, width = 25, font = tk.labelFont, highlightbackground='deep sky blue', highlightthickness = 4)

        #BUTTONS
        tk.confirmButton = tk.Button(self, text = "Confirm", font = tk.buttonFont, command = verifyChange, background = 'deep sky blue', borderwidth = 0)
        tk.confirmButton.config(height = 2, width = 13)

        #PACK
        tk.titleLabel.grid(pady = (30,0))
        tk.userLabel.grid(pady = (20,0))
        tk.userEntry.grid()
        tk.confirmButton.grid(pady = (30,0))


#################################################################################################################################################################
#CHANGE PASS WINDOW
class ChangePassWin(tk.Frame):

    def __init__(self, master):
        
        #LOGIN WINDOW
        tk.Frame.__init__(self, master)
        master.title("Change Password")
        master.geometry("600x500")

        #FUNCTIONS
        def verifyChange():
            print("WIP:Change Password")
        def checkPass():
            if(tk.myCheck.get() == 0):
                tk.passEntry.config(show="*")
                tk.passEntry2.config(show="*")
            else:
                tk.passEntry.config(show = "")
                tk.passEntry2.config(show = "")

        #CONFIG
        self.configure(background = 'white')

        #FONT 
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 25)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 25)
        tk.checkFont = tkFont.Font(family = "Verdana", size = 15)
        tk.titleFont = tkFont.Font(family = "Verdana", size = 25, weight = tkFont.BOLD)

        #LABELS
        tk.titleLabel = tk.Label(self, text = "Enter New Password", background = "white", font = tk.titleFont, fg = "blue4")
        tk.passLabel = tk.Label(self, text = "Password", background = 'white', font = tk.labelFont)
        tk.passLabel2 = tk.Label(self, text = "Confirm Password", background = 'white', font = tk.labelFont)

        #TEXTBOXES
        tk.passEntry = tk.Entry(self, width = 25, font = tk.labelFont, show="*", highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.passEntry2 = tk.Entry(self, width = 25, font = tk.labelFont, show="*", highlightbackground = 'deep sky blue', highlightthickness = 4)

        #CHECKBOX
        tk.myCheck = tk.IntVar()
        tk.passCheck = tk.Checkbutton(self, text = "Show Password", background = 'white', font = tk.checkFont, activebackground = 'deep sky blue', highlightthickness = 0, variable = tk.myCheck, command = checkPass)

        #BUTTONS
        tk.confirmButton = tk.Button(self, text = "Confirm", font = tk.buttonFont, command = verifyChange, background = 'deep sky blue', borderwidth = 0)
        tk.confirmButton.config(height = 2, width = 13)

        #PACK
        tk.titleLabel.grid(pady = (30,0))
        tk.passLabel.grid(pady = (20,0))
        tk.passEntry.grid()
        tk.passLabel2.grid(pady = (10,0))
        tk.passEntry2.grid()
        tk.passCheck.grid()
        tk.confirmButton.grid(pady = (30,0))


#################################################################################################################################################################
#CUSTOMER SEARCH WINDOW
class CustomerSearchWin(tk.Frame):
    
    def __init__(self,master):

        #CUSTOMER_SEARCH_WINDOW
        tk.Frame.__init__(self, master)
        master.title("Search for User")
        master.geometry("925x400")
        self.grid(row = 0, pady= (20,30))
        tk.nameFrame = tk.Frame(master)
        tk.nameFrame.grid(row = 1, padx = (30,0))
        tk.addFrame = tk.Frame(master)
        tk.addFrame.grid(row = 2, padx = (35,0))
        tk.cityFrame = tk.Frame(master)
        tk.cityFrame.grid(row = 3, padx = (35,0))
        tk.buttonFrame = tk.Frame(master)
        tk.buttonFrame.grid(row = 4, pady = (30,0))

        #FONT
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 20)
        tk.titleFont = tkFont.Font(family = "Verdana", size = 20, weight = tkFont.BOLD)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 15)

        #BUTTON FUNCTIONS
        def searchFunc():
            print("WIP: Search")

        #CONFIG
        self.config(background = "white")
        tk.nameFrame.config(background = "white")
        tk.addFrame.config(background = "white")
        tk.cityFrame.config(background = "white")
        tk.buttonFrame.config(background = "white")

        #LABELS
        tk.instLabel = tk.Label(self, text = "Enter one of the following to search", font = tk.titleFont, background = "white", fg = "blue4")

        tk.clientNoLabel = tk.Label(tk.nameFrame, text = "Client #", font = tk.labelFont, background = "white")

        tk.fNameLabel = tk.Label(tk.nameFrame, text = "First Name", font = tk.labelFont, background = "white")
        tk.mNameLabel = tk.Label(tk.nameFrame, text = " Middle Name", font = tk.labelFont, background = "white")
        tk.lNameLabel = tk.Label(tk.nameFrame, text = " Last Name", font = tk.labelFont, background = "white")

        tk.add1Label = tk.Label(tk.addFrame, text = "Address 1", font = tk.labelFont, background = "white")
        tk.add2Label = tk.Label(tk.addFrame, text = "Address 2", font = tk.labelFont, background = "white")

        tk.cityLabel = tk.Label(tk.cityFrame, text = "City", font = tk.labelFont, background = "white")
        tk.stateLabel = tk.Label(tk.cityFrame, text = "State", font = tk.labelFont, background = "white")
        tk.zipLabel = tk.Label(tk.cityFrame, text = "Zipcode", font = tk.labelFont, background = "white")
        tk.countryLabel = tk.Label(tk.cityFrame, text = "Country", font = tk.labelFont, background = "white")

        #TEXTBOXES
        tk.clientText = tk.Entry(tk.nameFrame, width = 10, font = ("Verdana",12), highlightbackground='deep sky blue', highlightthickness = 4)

        tk.fNameText = tk.Entry(tk.nameFrame, width = 25, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.mNameText = tk.Entry(tk.nameFrame,width = 15, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.lNameText = tk.Entry(tk.nameFrame,width = 20, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        tk.add1Text = tk.Entry(tk.addFrame, width = 37, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.add2Text = tk.Entry(tk.addFrame, width = 37, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        tk.cityText = tk.Entry(tk.cityFrame, width = 25, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.stateText = tk.Entry(tk.cityFrame, width = 10, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.zipText = tk.Entry(tk.cityFrame, width = 15, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.countryText = tk.Entry(tk.cityFrame, width = 20, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        #BUTTONS
        tk.searchButton = tk.Button(tk.buttonFrame, text = "SEARCH", font = tk.buttonFont, command = searchFunc, background = "deep sky blue", borderwidth = 0)
        tk.searchButton.config(height = 1, width = 15)

        #PACK
        tk.instLabel.grid(row = 0, column = 0)
        tk.clientNoLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.fNameLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.mNameLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        tk.lNameLabel.grid(row = 0, column = 3, sticky = 'w') 
        tk.clientText.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        tk.fNameText.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        tk.mNameText.grid(row = 1, column = 2, sticky = 'w', padx = (0,10))
        tk.lNameText.grid(row = 1, column = 3, sticky = 'w')
        tk.add1Label.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.add2Label.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.add1Text.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        tk.add2Text.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        tk.cityLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.stateLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.zipLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        tk.countryLabel.grid(row = 0, column = 3, sticky = 'w', padx = (0,10))
        tk.cityText.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        tk.stateText.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        tk.zipText.grid(row = 1, column = 2, sticky = 'w', padx = (0,10))
        tk.countryText.grid(row = 1, column = 3, sticky = 'w', padx = (0,10))
        tk.searchButton.grid(row = 0, column = 0)


#################################################################################################################################################################
#OLD CUSTOMER SEARCH WINDOW
class OldCustomerSearchWin(tk.Frame):
    
    def __init__(self,master):
        #CUSTOMER_SEARCH_WINDOW
        tk.Frame.__init__(self, master)
        master.title("Search for User")
        master.geometry("925x400")
        self.grid(row = 0, pady= (20,30))
        tk.nameFrame = tk.Frame(master)
        tk.nameFrame.grid(row = 1, padx = (30,0))
        tk.addFrame = tk.Frame(master)
        tk.addFrame.grid(row = 2, padx = (35,0))
        tk.cityFrame = tk.Frame(master)
        tk.cityFrame.grid(row = 3, padx = (35,0))
        tk.buttonFrame = tk.Frame(master)
        tk.buttonFrame.grid(row = 4, pady = (30,0))

        #FONT
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 20)
        tk.titleFont = tkFont.Font(family = "Verdana", size = 20, weight = tkFont.BOLD)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 15)

        #BUTTON FUNCTIONS
        def searchFunc():
            print("WIP: Search")

        #CONFIG
        self.config(background = "white")
        tk.nameFrame.config(background = "white")
        tk.addFrame.config(background = "white")
        tk.cityFrame.config(background = "white")
        tk.buttonFrame.config(background = "white")

        #LABELS
        tk.instLabel = tk.Label(self, text = "Enter one of the following to search", font = tk.titleFont, background = "white", fg = "blue4")

        tk.clientNoLabel = tk.Label(tk.nameFrame, text = "Client #", font = tk.labelFont, background = "white")

        tk.fNameLabel = tk.Label(tk.nameFrame, text = "First Name", font = tk.labelFont, background = "white")
        tk.mNameLabel = tk.Label(tk.nameFrame, text = " Middle Name", font = tk.labelFont, background = "white")
        tk.lNameLabel = tk.Label(tk.nameFrame, text = " Last Name", font = tk.labelFont, background = "white")

        tk.add1Label = tk.Label(tk.addFrame, text = "Address 1", font = tk.labelFont, background = "white")
        tk.add2Label = tk.Label(tk.addFrame, text = "Address 2", font = tk.labelFont, background = "white")

        tk.cityLabel = tk.Label(tk.cityFrame, text = "City", font = tk.labelFont, background = "white")
        tk.stateLabel = tk.Label(tk.cityFrame, text = "State", font = tk.labelFont, background = "white")
        tk.zipLabel = tk.Label(tk.cityFrame, text = "Zipcode", font = tk.labelFont, background = "white")
        tk.countryLabel = tk.Label(tk.cityFrame, text = "Country", font = tk.labelFont, background = "white")

        #TEXTBOXES
        tk.clientText = tk.Entry(tk.nameFrame, width = 10, font = ("Verdana",12), highlightbackground='deep sky blue', highlightthickness = 4)

        tk.fNameText = tk.Entry(tk.nameFrame, width = 25, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.mNameText = tk.Entry(tk.nameFrame,width = 15, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.lNameText = tk.Entry(tk.nameFrame,width = 20, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        tk.add1Text = tk.Entry(tk.addFrame, width = 37, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.add2Text = tk.Entry(tk.addFrame, width = 37, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        tk.cityText = tk.Entry(tk.cityFrame, width = 25, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.stateText = tk.Entry(tk.cityFrame, width = 10, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.zipText = tk.Entry(tk.cityFrame, width = 15, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)
        tk.countryText = tk.Entry(tk.cityFrame, width = 20, font = ("Verdana", 12), highlightbackground='deep sky blue', highlightthickness = 4)

        #BUTTONS
        tk.searchButton = tk.Button(tk.buttonFrame, text = "SEARCH", font = tk.buttonFont, command = searchFunc, background = "deep sky blue", borderwidth = 0)
        tk.searchButton.config(height = 1, width = 15)

        #PACK
        tk.instLabel.grid(row = 0, column = 0)
        tk.clientNoLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.fNameLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.mNameLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        tk.lNameLabel.grid(row = 0, column = 3, sticky = 'w') 
        tk.clientText.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        tk.fNameText.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        tk.mNameText.grid(row = 1, column = 2, sticky = 'w', padx = (0,10))
        tk.lNameText.grid(row = 1, column = 3, sticky = 'w')
        tk.add1Label.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.add2Label.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.add1Text.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        tk.add2Text.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        tk.cityLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.stateLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.zipLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        tk.countryLabel.grid(row = 0, column = 3, sticky = 'w', padx = (0,10))
        tk.cityText.grid(row = 1, column = 0, sticky = 'w', padx = (0,10))
        tk.stateText.grid(row = 1, column = 1, sticky = 'w', padx = (0,10))
        tk.zipText.grid(row = 1, column = 2, sticky = 'w', padx = (0,10))
        tk.countryText.grid(row = 1, column = 3, sticky = 'w', padx = (0,10))
        tk.searchButton.grid(row = 0, column = 0)


#################################################################################################################################################################
#CONFIRM DELETE WINDOW
class ConfirmDeleteWin(tk.Frame):

    def __init__(self,master):
        #CONFIRM_DELETION_WINDOW
        tk.Frame.__init__(self, master)
        master.title("Are you sure you want to delete?")
        master.geometry("500x400")

        #CONFIG
        self.config(background = 'white')

        #FUNCTIONS
        def deleteCust():
            print("WIP: Delete Customer")
        def dontDeleteCust():
            self.master.destroy()

        #FONT 
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 20)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 25, weight = tkFont.BOLD)

        #LABELS
        tk.titleLabel = tk.Label(self, text = "Are you sure?", background = 'white', font = tk.labelFont, fg = "blue4")

        #BUTTONS
        tk.deleteButton = tk.Button(self, text = "Delete" ,font = tk.buttonFont, command = deleteCust, background='deep sky blue', borderwidth = 0)
        tk.deleteButton.config(height = 2, width = 20)
        tk.noButton = tk.Button(self, text = "Cancel", font = tk.buttonFont, command = dontDeleteCust, background='deep sky blue', borderwidth = 0)
        tk.noButton.config(height = 2, width = 20)

        #PACK
        tk.titleLabel.grid(pady = (30,50))
        tk.deleteButton.grid(pady = (0,10))
        tk.noButton.grid() 



#################################################################################################################################################################
#SETTINGS WINDOW
class AddNewCustWin(tk.Frame):

    def __init__(self,master):
        
        #DB LOGIN
        #conn = psycopg2.connect("dbname = LoginInfo user = postgres password = harlan host = localhost")
        #cur = conn.cursor()

        #NEW_master
        tk.Frame.__init__(self, master)
        master.title("Customer Information")
        master.geometry("1000x600")
        self.grid(row = 0)
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
        self.config(background = "white")
        tk.InfoFrame.config(background = "white")
        tk.NameFrame.config(background = "white")
        tk.AddFrame.config(background = "white")
        tk.CityFrame.config(background = "white")
        tk.PhoneFrame.config(background = "white")
        tk.ButtonsFrame.config(background = "white")
        tk.ButtonsFrame2.config(background = "white")
        tk.ButtonsFrame3.config(background = "white")

        #FONT
        tk.buttonFont = tkFont.Font(family = "Verdana", size = 15)
        tk.titleFont = tkFont.Font(family = "Verdana", size = 20, weight = tkFont.BOLD)
        tk.labelFont = tkFont.Font(family = "Verdana", size = 15)
        tk.boxFont = tkFont.Font(family = "Verdana", size = 12)

        #BUTTON FUNCTIONS
        def addUser():
            #cur.execute("INSERT INTO address VALUES (DEFAULT, '%s', '%s', '%s', '%s', '%s', '%s')" % (tk.address1Text.get(), tk.address2Text.get(), tk.cityText.get(), tk.stateText.get(), tk.zipText.get(), tk.countryText.get()))
            #conn.commit()
            #cur.execute("SELECT AddressID FROM address where Address1 = '%s' and Address2 = '%s' and City = '%s' and State = '%s' and ZipCode = '%s' and Country = '%s';" % (tk.address1Text.get(), tk.address2Text.get(), tk.cityText.get(), tk.stateText.get(), tk.zipText.get(), tk.countryText.get()))
            #conn.commit()
            #rows = cur.fetchone()
            #cur.execute("INSERT INTO customers VALUES (%d, %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (int(tk.clientText.get()), int(rows[0]), tk.tNameText.get(), tk.fNameText.get(), tk.lNameText.get(), tk.mNameText.get(), tk.phoneText.get(), tk.emailText.get(), ' '))
            #conn.commit()
            #conn.close()
            print("USER ADDED!")

        #LABELS
        tk.titleLabel = tk.Label(self,text = "Add New Customer", font = tk.titleFont, background = "white", fg = "blue4")

        tk.clientNoLabel = tk.Label(tk.InfoFrame, text = "Client #", font = tk.labelFont, background = "white")
        tk.labelCodeLabel = tk.Label(tk.InfoFrame, text = "LabelCode", font = tk.labelFont, background = "white")

        tk.tNameLabel = tk.Label(tk.NameFrame, text = "Title", font = tk.labelFont, background = "white")
        tk.fNameLabel = tk.Label(tk.NameFrame, text = "FirstName", font = tk.labelFont, background = "white")
        tk.mNameLabel = tk.Label(tk.NameFrame, text = " MiddleName", font = tk.labelFont, background = "white")
        tk.lNameLabel = tk.Label(tk.NameFrame, text = " LastName", font = tk.labelFont, background = "white")

        tk.address1Label = tk.Label(tk.AddFrame, text = "Address 1", font = tk.labelFont, background = "white")
        tk.address2Label = tk.Label(tk.AddFrame, text = " Address 2", font = tk.labelFont, background = "white")

        tk.cityLabel = tk.Label(tk.CityFrame, text = "City", font = tk.labelFont, background = "white")
        tk.stateLabel = tk.Label(tk.CityFrame, text = " State", font = tk.labelFont, background = "white")
        tk.zipCodeLabel = tk.Label(tk.CityFrame, text = " Zip Code", font = tk.labelFont, background = "white")
        tk.countryLabel = tk.Label(tk.CityFrame, text = "Country", font = tk.labelFont, background = "white")

        tk.phoneLabel = tk.Label(tk.PhoneFrame, text = " Phone", font = tk.labelFont, background = "white")
        tk.emailLabel = tk.Label(tk.PhoneFrame, text = "Email", font = tk.labelFont, background = "white")

        #TEXTBOXES
        tk.clientText = tk.Entry(tk.InfoFrame, width = 11, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.labelCodeText = tk.Entry(tk.InfoFrame, width = 11, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        tk.tNameText = tk.Entry(tk.NameFrame, width = 11, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.fNameText = tk.Entry(tk.NameFrame, width = 30, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.mNameText = tk.Entry(tk.NameFrame, width = 13, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.lNameText = tk.Entry(tk.NameFrame, width = 30, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        tk.address1Text = tk.Entry(tk.AddFrame, width = 44, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.address2Text = tk.Entry(tk.AddFrame, width = 44, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        tk.cityText = tk.Entry(tk.CityFrame, width = 25, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.stateText = tk.Entry(tk.CityFrame, width = 12, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.zipText = tk.Entry(tk.CityFrame, width = 16, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.countryText = tk.Entry(tk.CityFrame, width = 30, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        tk.phoneText = tk.Entry(tk.PhoneFrame, width = 31, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)
        tk.emailText = tk.Entry(tk.PhoneFrame, width = 57, font = tk.boxFont, highlightbackground = 'deep sky blue', highlightthickness = 4)

        #BUTTONS
        tk.addButton = tk.Button(tk.ButtonsFrame, text = "ADD", font = tk.buttonFont, command = addUser, background = "deep sky blue", borderwidth = 0)

        #BUTTON_CONFIG
        tk.addButton.config(height = 2, width = 15)

        #PACK
        tk.titleLabel.grid(row = 0, column = 0, pady = (30,20))
        tk.clientNoLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.labelCodeLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.clientText.grid(row = 1, column = 0, padx = (0,10))
        tk.labelCodeText.grid(row = 1, column = 1, padx = (0,70))
        tk.tNameLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.fNameLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.mNameLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        tk.lNameLabel.grid(row = 0, column = 3, sticky = 'w')
        tk.tNameText.grid(row = 1, column = 0, padx = (0,10))
        tk.fNameText.grid(row = 1, column = 1, padx = (0,10))
        tk.mNameText.grid(row = 1, column = 2, padx = (0,10))
        tk.lNameText.grid(row = 1, column = 3)
        tk.address1Label.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.address2Label.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.address1Text.grid(row = 1, column = 0, padx = (0,10))
        tk.address2Text.grid(row = 1, column = 1, padx = (0,10))
        tk.cityLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.stateLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.zipCodeLabel.grid(row = 0, column = 2, sticky = 'w', padx = (0,10))
        tk.countryLabel.grid(row = 0, column = 3, sticky = 'w', padx = (0,10))
        tk.cityText.grid(row = 1, column = 0, padx = (0,10))
        tk.stateText.grid(row = 1, column = 1, padx = (0,10))
        tk.zipText.grid(row = 1, column = 2, padx = (0,10))
        tk.countryText.grid(row = 1, column = 3, padx = (0,10))
        tk.phoneLabel.grid(row = 0, column = 0, sticky = 'w', padx = (0,10))
        tk.emailLabel.grid(row = 0, column = 1, sticky = 'w', padx = (0,10))
        tk.phoneText.grid(row = 1, column = 0, padx = (0,10))
        tk.emailText.grid(row = 1, column = 1, padx = (0,10))
        tk.addButton.grid(row = 0, column = 0, padx = (0,10))

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
        self._frame.grid()


#Main
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()