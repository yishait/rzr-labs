#!/usr/bin/env python3

import boto3
from simple_term_menu import TerminalMenu

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('yishaitamir-logging')
objects = []

for object_summary in my_bucket.objects.filter(Prefix="logs/"):
    objects.append(object_summary.key)

def main():
    terminal_menu = TerminalMenu(objects)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {objects[menu_entry_index]}!")
    s3_obj = s3.Object(bucket_name="yishaitamir-logging", key=objects[menu_entry_index])
    body = s3_obj.get()['Body']
    log = body.read()
    if log:
        print(log.decode("utf-8") )

if __name__ == "__main__":
    main()