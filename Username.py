#Name=str(input("User Name"))
#print(Name)
import re
pattern="[A-Za-z]{3}"
user=str(input("User Name"))
if(re.search(pattern, user)):
    print("User Name is replaced by proper name")
    print(user)
else:
    print(user+ "Did not match")
