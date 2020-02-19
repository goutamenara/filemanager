from fileSrch import filelist
import os
f = filelist.files(os.getcwd(),'*.py')
print(f)