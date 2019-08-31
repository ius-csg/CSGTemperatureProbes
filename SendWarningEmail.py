from __future__ import print_function
import smtplib
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
"""Get a list of Labels from the user's mailbox.
"""

from apiclient import errors
gmail_user = 'iuscompsec@gmail.com'
gmail_password = 'IUSh@Ck3r$'

# sent_from = gmail_user
# to = ['zbouvier@iu.edu']
# subject = '*** TESTING PLEASE IGNORE ***'
body = "We\'ll be putting temperature stuff here eventually. #HopefullyBeforeAugust"

# email_text = """\
# From: %s
# To: %s
# Subject: %s

# %s
# """ % (sent_from, ", ".join(to), subject, body)

# try:
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login(gmail_user, gmail_password)
#     server.sendmail(sent_from, to, email_text)
#     server.close()

#     print("Email sent!")
# except Exception as itBroke:
#     print(itBroke)
#     print('Something went wrong...')








# # If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# def main():
#     """Shows basic usage of the Gmail API.
#     Lists the user's Gmail labels.
#     """
#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     service = build('gmail', 'v1', credentials=creds)

#     # Call the Gmail API
#     results = service.users().labels().list(userId='me').execute()
#     labels = results.get('labels', [])

#     if not labels:
#         print('No labels found.')
#     else:
#         print('Labels:')
#         for label in labels:
#             print(label['name'])

# if __name__ == '__main__':
#     main()
