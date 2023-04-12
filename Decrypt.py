print ('Welcome')

print("decryption")
message=input("enter your message to decrypt:")
key=int(input("enter the key(1-94):"))
decryption_text=" "

for i in range(len(message)):
    # print(i)
    temp=(ord(message[i])-key)

    if temp<32:
        temp=temp+127-32

    decryption_text+=chr(temp)
print("your decrypted text is:"+(decryption_text))


