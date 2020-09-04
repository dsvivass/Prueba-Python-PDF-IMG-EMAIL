#!/usr/bin/env python3

import os
import datetime
import reports
import emails



def parrafo():
    print(os.listdir())
    parag = ''
    for doc in os.listdir():
        with open(doc, encoding = 'utf-8') as f:
            for i,line in enumerate(f):
                if i < 2:
                    parag = parag + line + '<br/>'
                else:
                    parag = parag + '<br/>'
                    break
    print(parag)
    return parag

def main():
    os.chdir('supplier-data/descriptions/')
    parag = parrafo()
    os.chdir('../../')
    reports.generate("processed.pdf", "Processed Update on {}".format(datetime.date.today()),
                     parag)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "processed.pdf")
    emails.send_email(message)

if __name__ == '__main__':
    main()



