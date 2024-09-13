import smtplib


my_email = "senderbirthday@gmail.com"
my_password ="fjne bveu tbtr lwjm"
that_email = 'tedrecieve@yahoo.com'

#Create a new connection object 
with  smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    #Starting the transport security, we are securing our connection to the server. Message will be encrypted
    connection.starttls()
    #Time to log in
    connection.login(user=my_email, password=my_password)
    #Lets send a mail
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=that_email,
        msg="Subject: GoodBye again \n\n This is the body, take it in memory of you"
        )
