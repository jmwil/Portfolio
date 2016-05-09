from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from AddressDB import *


def highlightName(evt):
    global namereal
    w = evt.widget
    index = int(w.curselection()[0])
    namereal = w.get(index)
    return namereal

class AddressBook:
    def __init__(self, master):

        master.title('Address Book')

        self.masterFrame = ttk.Frame(master)
        self.masterFrame.pack()

        self.name = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.address1 = StringVar()
        self.address2 = StringVar()
        self.city = StringVar()
        self.state = StringVar()
        self.zipcode = StringVar()
        self.country = StringVar()

        # Address Listbox
        self.listFrame = ttk.Frame(self.masterFrame)
        self.listFrame.grid(row = 0, column = 0)

        self.yscroll = Scrollbar(self.listFrame)
        self.addresslist = Listbox(self.listFrame, selectmode = SINGLE)
        self.addresslist.pack(side = LEFT, fill = BOTH)
        self.yscroll.pack(side = RIGHT, fill = Y)
        for i in contactList:
            self.addresslist.insert(END, i)
        self.addresslist.bind('<<ListboxSelect>>', highlightName)

        # Content Box with text fields
        self.contentFrame = ttk.Frame(self.masterFrame)
        self.contentFrame.grid(row = 0, column = 1)

        ttk.Label(self.contentFrame, text ='Name:').grid(row = 0, column = 0, sticky = 'e')
        lnameEntry = ttk.Entry(self.contentFrame, textvariable = self.name)
        lnameEntry.grid(row = 0, column = 1)

        ttk.Label(self.contentFrame, text ='Phone:').grid(row = 1, column = 0, sticky = 'e')
        pEntry = ttk.Entry(self.contentFrame, textvariable = self.phone)
        pEntry.grid(row = 1, column = 1)

        ttk.Label(self.contentFrame, text ='Email:').grid(row = 1, column = 2, sticky = 'e')
        eEntry = ttk.Entry(self.contentFrame, textvariable = self.email)
        eEntry.grid(row = 1, column = 3)

        ttk.Label(self.contentFrame, text ='Address 1:').grid(row = 2, column = 0, sticky = 'e')
        a1Entry = ttk.Entry(self.contentFrame, textvariable = self.address1)
        a1Entry.grid(row = 2, column = 1)

        ttk.Label(self.contentFrame, text ='Address 2:').grid(row = 3, column = 0, sticky = 'e')
        a2Entry = ttk.Entry(self.contentFrame, textvariable = self.address2)
        a2Entry.grid(row = 3, column = 1)

        ttk.Label(self.contentFrame, text ='City:').grid(row = 4, column = 0, sticky = 'e')
        cEntry = ttk.Entry(self.contentFrame, textvariable = self.city)
        cEntry.grid(row = 4, column = 1)

        ttk.Label(self.contentFrame, text ='State:').grid(row = 5, column = 0, sticky = 'e')
        sEntry = ttk.Entry(self.contentFrame, textvariable = self.state)
        sEntry.grid(row = 5, column = 1)

        ttk.Label(self.contentFrame, text ='Zip:').grid(row = 5, column = 2, sticky = 'e')
        zEntry = ttk.Entry(self.contentFrame, textvariable = self.zipcode)
        zEntry.grid(row = 5, column = 3)

        ttk.Label(self.contentFrame, text ='Country:').grid(row = 6, column = 0, sticky = 'e')
        coEntry = ttk.Entry(self.contentFrame, textvariable = self.country)
        coEntry.grid(row = 6, column = 1)


        # Button Row
        self.buttonFrame = ttk.Frame(self.masterFrame)
        self.buttonFrame.grid(row = 1, column = 0, columnspan = 2, sticky = '')

        ttk.Button(self.buttonFrame, text = 'Load Contact', command = self.loadContact).pack(side = LEFT)
        ttk.Button(self.buttonFrame, text = 'New', command = self.newContact).pack(side = LEFT)
        ttk.Button(self.buttonFrame, text = 'Save', command = self.saveNewContact).pack(side = LEFT)
        ttk.Button(self.buttonFrame, text = 'Delete', command = self.deleteExistingContact).pack(side = LEFT)

    def loadContact(self):
        self.name.set(namereal)
        self.phone.set(readPhone(namereal))
        self.email.set(readEmail(namereal))
        self.address1.set(readAddressOne(namereal))
        self.address2.set(readAddressTwo(namereal))
        self.city.set(readCity(namereal))
        self.state.set(readState(namereal))
        self.zipcode.set(readZipCode(namereal))
        self.country.set(readCountry(namereal))

    def newContact(self):
        self.name.set('')
        self.phone.set('')
        self.email.set('')
        self.address1.set('')
        self.address2.set('')
        self.city.set('')
        self.state.set('')
        self.zipcode.set('')
        self.country.set('')

    def refreshContactList(self):
        global contactList
        del contactList [:]
        updateContactList()
        self.addresslist.delete(0, END)
        for i in contactList:
            self.addresslist.insert(END, i)

    def saveNewContact(self):
        name = self.name.get()
        phone = self.phone.get()
        email = self.email.get()
        address1 = self.address1.get()
        address2 = self.address2.get()
        city = self.city.get()
        state = self.state.get()
        zipcode = self.zipcode.get()
        country = self.country.get()
        saveContact(name, phone, email, address1, address2, city, state, zipcode, country)
        self.refreshContactList()
        messagebox.showinfo(title = 'Contact Saved', message = 'Your new contact has been saved to your address book!')

    def deleteExistingContact(self):
        global namereal
        confirm = messagebox.askyesno(title = 'Please Confirm', message = 'Are you sure you want to delete {} from your contacts'.format(namereal))
        if confirm == True:
            deleteContact(namereal)
            self.refreshContactList()
            messagebox.showinfo(title = 'Confirmed!', message = 'Your contact {} has successfully been deleted from your address book!'.format(namereal))



def main():
    createTable()
    updateContactList()
    root = Tk()
    abook = AddressBook(root)
    root.mainloop()

if __name__ == "__main__": main()
