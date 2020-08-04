from twilio.rest import Client 

 
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  #use the account_sid from the Twilio app
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  #use the auth_token from the Twilio app
client = Client(account_sid, auth_token) 
 
def send_love_message():
  message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Good Night by ZAN 😍',    
                              to='whatsapp:+91{YOUR_NUMBER}' 
                          ) 
 
  print(message.sid)
