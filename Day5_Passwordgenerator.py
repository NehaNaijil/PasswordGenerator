import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
LETTERS=[x.upper() for x in letters]
num=[1,2,3,4,5,6,7,8,9,0]
sym=['!','@','#','$','%','^','&','*','(',')']
password=""
print("Welcome to password generator")
totalLength=int(input("What is the length of password required?"))
numberOfCapitals=int(input("How many capital letters are needed?"))
numberOfSmallLetters=int(input("How many small letters are needed?"))
numberOfnumbers=int(input("How many numbers are needed?"))
numberOfsymbols=int(input("How many symbols are needed?"))
if(totalLength!=(numberOfCapitals+numberOfnumbers+numberOfSmallLetters+numberOfsymbols)):
    print("Request mismatched, try again later")
count_LETTERS=0
count_letters=0
count_num=0
count_sym=0
lists=[letters,LETTERS,num,sym]
x=0
while x<totalLength:
    
    l=random.choice(lists)
   
    if(l==letters):
        if(count_letters<numberOfSmallLetters):
            password+=random.choice(letters)
            
        else:
            lists.remove(letters)
    elif(l==LETTERS):
        if(count_LETTERS<numberOfCapitals):
            password+=random.choice(LETTERS)
           
        else:
            lists.remove(LETTERS)
    elif(l==num):
        if(count_num<numberOfnumbers):
            password+=str(random.choice(num))
            
        else:
            lists.remove(num)
    else:
        if(count_sym<numberOfsymbols):
            password+=random.choice(sym)
           
        else:
            lists.remove(sym)
    x=len(password)

print(f"The password generated is: {password}")
    
        

        


