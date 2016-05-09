import shutil, os


src = 'C:\Users\Jimmy Wilcox\Desktop\src\\'
dst = 'C:\Users\Jimmy Wilcox\Desktop\dst\\'


for f in os.listdir(src):
    if f.endswith(".txt"):
        shutil.move(src + f, dst)
        print "Moved " + f + " to " + dst
        
print "All .txt files have been moved from: " + src + "\n to: " + dst
