from zipfile import ZipFile
from tqdm import tqdm

file_name = r"***ENTER YOUR ZIP FILE's ADDRESS HERE***"
file_path = r"***FOLDER NAME TO EXTRACT TO***"

wordlist = open(r"***PATH TO WORD LIST***", "r", encoding="latin-1")
passwords = wordlist.read()
passwords = passwords.split()

with ZipFile(file_name, 'r') as zip:
    zip.printdir() 
    print('Trying extraction ...')

#    passwords=["123", "123456", "12345678"]

    for password in tqdm(passwords):

#        print("Trying with password: ",password)
    
        try:
            zip.extractall(path=file_path, members=None, pwd=password.encode('utf-8'))
            break
        except RuntimeError:
            continue
#            print("Wrong Password Maybe?")
        except Exception as e:
            continue
#            print(f"An unexpected error occurred with password: {password} - {e}")

    print("***********************************")
    print('Correct Password: ', password)
    print("***********************************")
