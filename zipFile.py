# importing the 
import zipfile 
from tqdm import tqdm 

# password list path 
wordlist = "rockyou.txt"

# take input from user for which zip file they would like to crack 
zip_file = input(zipfile.ZipFile)

# intialization of the zip file object 
zip_file = zipfile.ZipFile(zip_file)

# count the number of words in this wordlist 
n_words = len(list(open(wordlist, "rb")))

# print the total number of passwords 
print("Number of passwords to test:", n_words)

# open the wordlist and read it word by word as it tries to guess the password of the file
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
                continue
        else:
                print("[+] Password recovered:", word.decode().strip())
                print("[+] Extracted contents were placed in the current directory.")
                exit(0)
print("[!] Password could not be recovered.")




