choice=input("do you want to decode or encode pass")
if 'encode' in choice:
    password = input("enter the password with no space").strip()




    print(len(password))
    if len(password)>3:
        hashpass=password[1:]+password[0]
        print(hashpass)
    # now i am suppsoe to reverse it to make it unpredictable
        finalhash=hashpass[::-1]
        print(f'this is the real password {finalhash}')
else:
    print("decoding is active")
    hashpass=input("enter here hash password").strip()
    finalhashpass=hashpass[1:]+hashpass[0]
    reversehash=finalhashpass[::-1]
    
    print(f'this is your real plane password {reversehash}')
