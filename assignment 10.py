#!/usr/bin/env python
# coding: utf-8

# 1. How do you distinguish between shutil.copy() and shutil.copytree()?

# In[ ]:


shutil. copy() will copy a single file and
shutil. copytree() will copy an entire folder and every folder and file contained in it.


# 2. What function is used to rename files??

# In[ ]:


rename() method in Python is used to rename a file or directory.


# 3. What is the difference between the delete functions in the send2trash and shutil modules?

# In[ ]:


The send2trash functions will move a file or folder to the recycle bin 
while shutil functions will permanently delete files and folders.


# 4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is
#    equivalent to File objects’ open() method?

# In[ ]:


The zipfile. ZipFile() function is equivalent to the open() function


# 5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf
#    or .jpg). Copy these files from whatever location they are in to a new folder.

# In[ ]:


import os, shutil

def selectiveCopy(folder, extension, destFolder):
    folder = os.path.abspath(folder)
    destFolder = os.path.abspath(destFolder)
    print('Looking in', folder, 'for files with extensions of', ', '.join(extension))
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extension:
                fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.pdf', '.jpg']
folder = 'randomFolder'
destFolder = 'selectiveFolder'
selectiveCopy(folder, extensions, destFolder)


# In[ ]:





# In[ ]:




