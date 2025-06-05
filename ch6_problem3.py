# a spam comment is defined as a text containing following keywords 
# make a lot of money , buy now , subscribe this , click this , WAP to detect these spams 

spam1 = "make a lot of money "
spam2 = "buy now"
spam3 = "subcribe now"
spam4 = "click this"

message = input("enter your comment: ")

if((spam1 in message) or (spam2 in message) or (spam3 in message) or (spam4 in message)):
    print("SPAM ALERT")

else:
    print("Comment:",message)
    
