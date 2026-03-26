import pandas as pd
from twilio.rest import Client
import time
acc_SID="********************"
auth_token="********************"
client=Client(acc_SID,auth_token)
df=pd.read_excel("*****.xlsx")
for i in range(len(df)):
    name=df.loc[i,"NAME"]
    desig=df.loc[i,"DESIGNATION"]
    number=df.loc[i,"NUMBER"]


    messages={'Staff':"good morning",
              'Student':"hi daa",
              'Corpenter':"study well",
              'Docter':"hiiiiii ",
              'Engineer':"Become A Innovator",
              'Manager':"helllllllooooo"}
    msg=messages.get(desig.lower(),"hello")
    final_message=f"{name} {msg}"
    client.messages.create(
        from_='whatsapp:+14155238886',
        body=final_message,
        to=f'whatsapp:{number}'
         )
    print(f"sent to{name}")
    time.sleep(1)