# coding: utf-8 

import sys
import os
import shutil

def add_path (name_dir1, index1):
    if index1 == 2:
        try:
            for i in range(1, index1):
                os.mkdir(name_dir1)
        except FileExistsError:
            print("Эти директории уже созданы!")
    
    else:
        try:
            for i in range(1, index1):
                os.mkdir(name_dir1 + str(i))
            print(os.listdir(os.getcwd()))
        except FileExistsError:
            print("Эти директории уже созданы!", "\n", os.listdir(os.getcwd()))
            

def remove_path (name_dir2, index2):
    if index2 == 2:
        try:
            for i in range(1, index2):
                os.removedirs(name_dir2)
        except OSError:
            print("Эти директории уже удалены!")

    else:
        try:
            for i in range(1,index2):
                os.removedirs(name_dir2 + str(i))
            print("Директории удалены", "\n", os.listdir(os.getcwd()))
        except OSError:
            print("Эти директории уже удалены!", "\n", os.listdir(os.getcwd()))