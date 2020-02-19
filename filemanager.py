#!/usr/bin/python3
import os
import fnmatch

class filemanager:

    def __init__(self,path):
        self.path = path
    

    def get_files(self,pattern):
        files = []
        for root, dirs, fs in os.walk(self.path):
            if fs:
                for f in fs:
                    if fnmatch.fnmatch(f, pattern):
                        files.append(os.path.join(root,f))
        return files