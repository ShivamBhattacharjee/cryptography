print('Welcome')
print("Rules: Dont open it")


message=input ('Enter message you want to encrypt :')
key = int(input("Enter a key(1-94): "))
encrypt =''

print("encryption")
for i in range(len(message)):
    # print(i)
    temp=(ord(message[i])+key)

    if temp>126:
       temp=temp-127+32
    encrypt+=chr(temp)
print ('Encrypted Message: '+ (encrypt) )
    






