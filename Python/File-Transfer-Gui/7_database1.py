import pytz, shutil, os, time
from datetime import datetime, timedelta
import wx
import sqlite3

conn = sqlite3.connect('FileTransferDB.db', timeout=10)
c = conn.cursor()

now = datetime.now()
yesterday = now - timedelta(hours = 24)
unix = time.time()

ft = '%H:%M:%S'
fmt = '%d %H:%M:%S'
fmtm = '%B %d %H:%M:%S'

working="C:\Users\Jimmy Wilcox\Desktop\working\\" # working files located here
edited="C:\Users\Jimmy Wilcox\Desktop\edited\\"   # edited files ready for transfer

files = []
moved_files = []

recentDate = ''

# SQL Functions
def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS fileTransferTimes (id INTEGER PRIMARY KEY AUTOINCREMENT, time CHAR(50))")

def dateEntry():
    c.execute("INSERT INTO fileTransferTimes VALUES (NULL,?)", ['{}'.format(now.strftime(fmtm))])
    conn.commit()

def readDate():
    global recentDate
    c.execute("SELECT time FROM fileTransferTimes ORDER BY id DESC LIMIT 1")
    d = c.fetchall()
    recentDate = str(d).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',','')
    return recentDate

readDate()

# only prints/appends modification time if it's happened within last 24 hours.
def modTime(f):
    global working
    global files
    nf = working + f
    t = os.path.getmtime(nf)
    mt = datetime.fromtimestamp(t)
    if mt > yesterday:
        files.append('%s modified %s' %(f, mt.strftime(fmtm)))
        print('%s modified %s' %(f, mt.strftime(fmtm)))

# transfers a file edited within the last 24 hours
def transferFiles(f):
    global working
    global moved_files
    global edited
    nf = working + f
    t = os.path.getmtime(nf)
    mt = datetime.fromtimestamp(t)
    if mt > yesterday:
        shutil.move(working + f, edited)
        moved_files.append('%s moved to %s' %(f, edited))
        print('%s moved to %s' %(f, edited))


# views all files modified within the last 24 hours.
def viewWorking():
    global working
    global files
    for f in os.listdir(working):
        modTime(f)

# transfers all working files modified within the last 24 hours, and displays where they went
def transferWorking():
    global edited
    global working
    global moved_files
    for f in os.listdir(working):
        transferFiles(f)


class Mywin(wx.Frame):
    global working
    global edited

    def __init__(self, parent, title = 'MyWin'):
        super(Mywin, self).__init__(parent, title = title)
        self.fileTransferGUI()
        self.Centre()
        self.Show()
        self.SetSize((600,500))

    def fileTransferGUI(self):
        global working
        global edited

        panel = wx.Panel(self)

        self.SetTitle('Daily File Transfers')
        self.Show(True)

        # Menu Bar Stuff....
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        menuBar.Append(fileButton, 'File')
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Exit the program')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # View/Set Working Directory Box....

        workingDirectory = wx.StaticBox(panel, -1, 'Working File Directory:')
        workingSizer = wx.StaticBoxSizer(workingDirectory, wx.VERTICAL)

        workingBox = wx.BoxSizer(wx.HORIZONTAL)

        workingText = wx.StaticText(panel, -1, "Location:")
        self.workingLocation = wx.TextCtrl(panel, -1, working, size = (300,20))
        self.workingLocation.SetBackgroundColour(wx.Colour(255,255,255))
        self.workingLocation.SetForegroundColour(wx.Colour(0,0,0))
        workingButton = wx.Button(panel, -1, "Change Directory")

        workingBox.Add(workingText, 0, wx.ALL|wx.CENTER, 5)
        workingBox.Add(self.workingLocation, 0, wx.ALL|wx.CENTER, 5)
        workingBox.Add(workingButton, 0, wx.ALL|wx.CENTER, 5)
        workingSizer.Add(workingBox, 0, wx.ALL|wx.CENTER, 10)


        # View/Set Transfer Directory Box....

        tansferDirectory = wx.StaticBox(panel, -1, 'Transfer File Directory:')
        transferSizer = wx.StaticBoxSizer(tansferDirectory, wx.VERTICAL)

        transferBox = wx.BoxSizer(wx.HORIZONTAL)

        transferText = wx.StaticText(panel, -1, "Location")
        self.transferLocation = wx.TextCtrl(panel, -1, edited, size = (300,20))
        self.transferLocation.SetBackgroundColour(wx.Colour(255,255,255))
        self.transferLocation.SetForegroundColour(wx.Colour(0,0,0))
        transferButton = wx.Button(panel, -1, "Change Directory")

        transferBox.Add(transferText, 0, wx.ALL|wx.CENTER, 5)
        transferBox.Add(self.transferLocation, 0, wx.ALL|wx.CENTER, 5)
        transferBox.Add(transferButton, 0, wx.ALL|wx.CENTER, 5)
        transferSizer.Add(transferBox, 0, wx.ALL|wx.CENTER, 10)


        # View and Submit(Transfer) Edited Files...

        submitDirectory = wx.StaticBox(panel, -1, 'View and Transfer Files:')
        submitSizer = wx.StaticBoxSizer(submitDirectory, wx.VERTICAL)

        submitBox = wx.BoxSizer(wx.HORIZONTAL)

        viewButton = wx.Button(panel, -1, 'View Files')
        submitButton = wx.Button(panel, -1, 'Transfer Files')

        submitBox.Add(viewButton, 0, wx.ALL|wx.LEFT, 10)
        submitBox.Add(submitButton, 0, wx.ALL|wx.LEFT, 10)
        submitSizer.Add(submitBox, 0, wx.ALL|wx.LEFT, 10)

        # View previous transfer date using SQL
        
        previousStaticBox = wx.StaticBox(panel, -1, 'Most Recent File Transfer:')
        previousSizer = wx.StaticBoxSizer(previousStaticBox, wx.VERTICAL)

        pBox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.previousTDate = wx.StaticText(panel, -1, label = recentDate, size = (200,20))
        self.previousTDate.SetBackgroundColour(wx.Colour(255,255,255))
        self.previousTDate.SetForegroundColour(wx.Colour(0,0,0))

        pBox.Add(self.previousTDate, 0, wx.ALL|wx.CENTER, 5)
        previousSizer.Add(pBox, 0, wx.ALL|wx.CENTER, 10)
        
        # Add all three sections to main box...

        vbox.Add(workingSizer,0, wx.ALL|wx.CENTER, 5)
        vbox.Add(transferSizer,0, wx.ALL|wx.CENTER, 5)
        vbox.Add(submitSizer, 0, wx.ALL|wx.CENTER, 5)
        vbox.Add(previousSizer, 0, wx.ALL|wx.CENTER, 5)

        # Button Event Bindings....
        workingButton.Bind(wx.EVT_BUTTON, self.showWorkingDirectory)
        transferButton.Bind(wx.EVT_BUTTON, self.showTransferDirectory)
        viewButton.Bind(wx.EVT_BUTTON, self.showWorkingFiles)
        submitButton.Bind(wx.EVT_BUTTON, self.showTransferedFiles)

        panel.SetSizer(vbox)

    def showWorkingDirectory(self, e):
        global working
        dialog = wx.DirDialog(None, "Please choose your working directory:", defaultPath = working, pos = (10,10))
        if dialog.ShowModal() == wx.ID_OK:
            working = dialog.GetPath() + "\\"
            self.workingLocation.SetValue(working)
            return working
        else:
            app.Close()
            dialog.Destroy()
            return _userCancel


    # Set the transfer directory
    def showTransferDirectory(self, e):
        global edited
        dialog = wx.DirDialog(None, "Please choose your transfer directory:", defaultPath = edited, pos = (10,10))
        if dialog.ShowModal() == wx.ID_OK:
            edited = dialog.GetPath() + "\\"
            self.transferLocation.SetValue(edited)
            return edited
        else:
            app.Close()
            dialog.Destroy()
            return _userCancel

    # Displays all files edited in a pop up window
    def showWorkingFiles(self, e):
        global files
        global working
        global edited
        viewWorking()
        wx.MessageBox('Files edited in the last 24 hours: %s' %(files), 'Working Files', wx.OK)

    # Transfers and displays all transfered files in a pop up window
    def showTransferedFiles(self, e):
        global moved_files
        global recentDate
        global files
        global edited
        global working
        transferWorking()
        dateEntry()
        readDate()
        self.previousTDate.SetLabel('{}'.format(recentDate))
        wx.MessageBox('Files transfered: %s' %(moved_files), 'Transfered Files', wx.OK)

    # Closes things
    def Quit(self, e):
        self.Close()


def main():
    createTable()
    app = wx.App()
    Mywin(None)
    app.MainLoop()

main()
