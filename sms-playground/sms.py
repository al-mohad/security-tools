from twilio.rest import Client

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACed0f52e410d6e696a880494846262ba7'
auth_token = '72001ac0396011ff8dacfefaeb913e91'
client = Client(account_sid, auth_token)
my_message = '''Dear Sir/Madam,
We have logged your IP-address on more than 40 illegal Websites.
Important: Please answer our questions! The list of questions are attached.
Yours faithfully,
Ibrahim Magu
Economic and Financial Crimes Commission -EFCC-
No. 5, Fomella Street, Off Adetokunbo Ademola Crescent,:
Wuse II,: Abuja,: Nigeria.
0903 330 3026'''

message = client.messages \
                .create(
                    body=my_message,
                    from_='+12057495430',
                    to='+23408058533393'
                )

print(message.sid)
