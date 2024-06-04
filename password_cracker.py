import hashlib  #imports the hash library
commonPasswords = []
hashPasswords = []
hashTemp = ""
userPasswords = []
userTemp = [ ]
user_hash_dict = {} #initialises all necessary variables

with open('common_passwords.txt', 'r') as f:
    commonPasswords = f.read().splitlines() #takes all of the passwords in text file and puts it into a list

with open('username_hashes.txt', 'r') as g:
    text = g.read().splitlines()   #takes all of the username and hash password pairs and puts it into a list
    for user_hash in text:
        username = user_hash.split(":")[0]
        usernameHash = user_hash.split(":")[1] #splits the username and hash password pairs into their own separate lists
        user_hash_dict[username] = usernameHash #converts the 2 lists into a dictionary

for i in range(len(commonPasswords)):
    hashTemp = hashlib.sha256(commonPasswords[i].encode('utf-8'))
    hashPasswords.append(hashTemp.hexdigest())  #passes each password into a hash function and stores the output into a separate list


for password in hashPasswords: #iterates over each common password hash and compares it to the username hashed passwords
    for userHash in user_hash_dict.values():
        if password == userHash: #then uses the dictionary value to access the username which is then equal to the un-hashed value of the password
            print(list(user_hash_dict.keys())[list(user_hash_dict.values()).index(password)] + " is equal to " + commonPasswords[hashPasswords.index(password)])