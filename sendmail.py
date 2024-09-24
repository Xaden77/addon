import yagmail
import  os
from dotenv import load_dotenv
load_dotenv()

sender = "hridhay.vjec@gmail.com"
reciever="046bh5s02g@spymail.one"
subject="test mail"
contents= '''
    this is content
'''
yag=yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
yag.send(to=reciever,subject=subject,contents=contents)
print("sent")

