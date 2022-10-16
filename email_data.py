# import os
# import win32com.client as win32

# olApp = win32.Dispatch('Outlook.Application')
# olNS = olApp.GetNameSpace('MAPI')

# def send_email(email_address):
#     print(email_address)
#     mail_item = olApp.CreateItem(0)
#     mail_item.Subject = 'Home Buyer Report'
#     mail_item.BodyFormat = 1
#     mail_item.Body = 'This report includes a .csv file with the home buyer data and two images showing a breakdown of approvals and disapprovals.'
#     mail_item.To = email_address
#     mail_item.Attachments.Add(os.path.join(os.getcwd(), 'homebuyerinfo.csv'))
#     mail_item.Attachments.Add(os.path.join(os.getcwd(), 'approved_percent.png'))
#     mail_item.Attachments.Add(os.path.join(os.getcwd(), 'whynotapproved.png'))

#     mail_item.Send()

