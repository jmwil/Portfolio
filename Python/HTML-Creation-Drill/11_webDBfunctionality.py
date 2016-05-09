import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from DBqueries import *

#
#   Create Database that:
#       Fetches all titles
#       Displays all titles in scroll bar
#       Clicking on titles displays title and web text
#       Update GUI to add scrollbar with database data


doctype = ''' <!DOCTYPE html>
<html>
<head>
<title> '''
title = "Summer Blowout"
head = '''</title>
<meta charset="UTF-8">
</title>
<body> '''
contents = "Stay tuned for our amazing summer sale!"
closing = '''</body>
</html> '''

content = ''
ptitle = ''
def createPage(text, filename): #this function creates the html document
    output = open(filename, "w")
    output.write(text)
    output.close()

def viewPage(webpageText, filename='temp.html'): #this functions calls the createpage function to write the document and opens it in the browser
    import webbrowser, os.path
    createPage(webpageText, filename)
    webbrowser.open('file:///' + os.path.abspath(filename))

def highlightTemplate(evt):
    global content
    w = evt.widget
    index = int(w.curselection()[0])
    title = w.get(index)
    c = loadTemplates(title)
    content = str(c).replace('(\'','').replace('\',)','').replace('\",)','').replace('(\"','')
    return content

def highlightTitle(evt):
    global ptitle
    w = evt.widget
    index = int(w.curselection()[0])
    ptitle = w.get(index)
    return ptitle



class WebpageNew:
    def __init__(self, master):
        global temparray

        master.title('Create a New Webpage')
        master.resizable(False, False)

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # Top Label and app description
        ttk.Label(self.frame_header, text = 'Create a simple webpage').grid(row = 0, column = 0, columnspan = 3)
        ttk.Label(self.frame_header, wraplength = 400, text = ("Compose the text for your simple webpage below, or select one of the available templates! Click \'Submit\' to create and view your webpage, \'Save Template\' to save current settings for later use, and \'Clear\' to clear the title and content fields.")).grid(row = 1, column = 0, columnspan = 3)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        #Labels for each box
        ttk.Label(self.frame_content, text = 'Page Templates:').grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
        ttk.Label(self.frame_content, text = 'Webpage Title (50 character limit):').grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'w')
        ttk.Label(self.frame_content, text = 'Webpage Text:').grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

        #Template chooser listbox and scrollbar
        self.scroll_frame = ttk.Frame(self.frame_content)
        self.scroll_frame.grid(row = 3, column = 0, rowspan = 3)
        self.yscroll = Scrollbar(self.scroll_frame).pack(side = LEFT, fill = Y)
        self.templist = Listbox(self.scroll_frame, selectmod = SINGLE, yscrollcommand = self.yscroll)
        self.templist.pack(side = LEFT, fill = BOTH)
        for i in temparray:
            self.templist.insert(END, i)
        ttk.Button(self.scroll_frame, text = 'Load', command = self.loadButton).pack(side = BOTTOM)
        ttk.Button(self.scroll_frame, text = 'Refresh', command = self.refreshTemplates).pack(side = BOTTOM)
        self.templist.bind('<<ListboxSelect>>', highlightTemplate, add ='+')
        self.templist.bind('<<ListboxSelect>>', highlightTitle, add = '+')


        # Title entry box
        self.page_title = Text(self.frame_content, width = 50, height = 1, font = ('Arial',10))
        self.page_title.grid(row =3, column = 1, columnspan = 2)

        # Contents entry box
        self.page_contents = Text(self.frame_content, width = 50, height = 10, font = ('Arial',10))
        self.page_contents.grid(row = 5, column = 1, columnspan = 2)

        ttk.Button(self.frame_content, text = 'Submit & View', command = self.submit).grid(row = 6, column = 0, padx = 5, pady = 5)
        ttk.Button(self.frame_content, text = 'Save Template', command = self.saveTemplate).grid(row = 6, column = 1, padx = 5, pady = 5)
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 6, column = 2, padx = 5, pady = 5)

    def submit(self):       #captures user input as Page Content and creates webpage
        global contents
        global title
        title = self.page_title.get(1.0, 'end').replace('\n','').replace('\t','').replace('"','')
        contents = self.page_contents.get(1.0, 'end')
        self.clear()
        viewPage((doctype + title + head + contents + closing))
        messagebox.showinfo(title = 'Complete!', message = 'Your new webpage has been created! You will be re-directed to your browser to view your beautiful creation.')

    def saveTemplate(self):
        title = str(self.page_title.get(1.0, 'end')).replace('\n','').replace('\t','').replace('"','')
        contents = self.page_contents.get(1.0, 'end')
        insert(title, contents)

    def clear(self):
        self.page_contents.delete(1.0, 'end')
        self.page_title.delete(1.0, 'end')

    def refreshTemplates(self):
        global temparray
        del temparray[:]
        read()
        self.templist.delete(0,END)
        for i in temparray:
            self.templist.insert(END, i)

    def clear(self):
        self.page_contents.delete(1.0, 'end')
        self.page_title.delete(1.0, 'end')

    def loadButton(self):
        global content
        global ptitle
        self.clear()
        self.page_contents.insert(1.0, content)
        self.page_title.insert(1.0, ptitle)

def main():
    createTable()
    read()
    root = Tk()
    newPage = WebpageNew(root)
    root.mainloop()

if __name__ == "__main__": main()
