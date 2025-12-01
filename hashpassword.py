password = input("enter the password").strip()
realpass="".join(password.split())


print(len(realpass))
if len(realpass)>3:
    hashpass=realpass[1:]+realpass[0]
    print(hashpass)
    # now i am suppsoe to reverse it to make it unpredictable
    finalhash=hashpass[::-1]
    print(f'this is the real password {finalhash}')