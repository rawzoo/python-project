#This programe rename all the files from current directory and remove Number or digits from their
#names 


import os
def rename_files():
       #replace your own Directory address
       file_list = os .listdir(r"home/ved/hello")
       saved_path = os.getcwd()
       print("Current Dir is %s" %saved_path)
       os.chdir(r"home/ved/hello")

       for file_name in file_list:
           os.rename(file_name,file_name.translate(None, "0123456789"))
           os.chdir(saved_path)
rename_files()
