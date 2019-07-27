global idd
global pas
idd="sahil"
pas="lisha10l"

print("For setup enter ADMIN Credentials")
admin_id=input("ADMIN_ID:")
ad_pass=input("ADMIN_PASSOWRD:")

if admin_id==idd and ad_pass==pas:
    print("Please Enter your one time USERID and PASSWORD and your business Email Address")
    USERID=input("USERID:")
    PASSWORD=input("PASSWORD:")
    EMAIL=input("EMAIL:")
    print("Credetials saved successfully")
    idd=USERID
    pas=PASSWORD
else:
    print("CONTACT ADMIN FOR FUTHER SUPPORT!")

if __name__=="__main__":
    main()

