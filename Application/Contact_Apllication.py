contact={}
def Add_contact(name,ph_no):
    if(name in contact.keys()):
        print(name,"Conact Already Exits...!!!")
    else:
        
        contact[name]=ph_no
        print("Contact Added/Saved Sucessfully....!!!!")
def Display_contact():
    i=0
    if(len(contact)==0):
        print("Contacts is Emty...!!!")
    else:
        if(i<len(contact)):
            for name,phone in contact.items():
                print(i+1,".Name=",name,", phoneNumber=",phone)
                i=i+1                
def Delete_contact(name):
    if(name in contact.keys()):
        contact.pop(name)
        print(name,"Deleted Sucessfully...!!")
    else:
        print(name,"Does not  exits in contact list...!!!")
def Update_contact(name,ph_no):
    if(name in contact.keys()):
        contact[name]=ph_no
        print("Contact Updated Sucessfully...!!!")
    else:
        print("contact not exits...!!!")
def Search_contact(name):
    if(name in contact.keys()):
        print("name=",name,"phoneNumber=",contact[name])
    else:
        print(name,"Don't exits ...!!!")       
        