from modules.email_processor import process_email, read_email_file, write_processed_email
import os

parent_folder='processed_files'
with open('file_list','r') as f:

    for data_file_path in f.readlines():
        try:
            data_file_path = data_file_path.strip()
            print("Reading email file:" + data_file_path)
            email_str=read_email_file(data_file_path)
            print("Processing email file:" + data_file_path)
            processed_email_str=process_email(email_str)
            print("Processed string")
            print(processed_email_str)
            processed_file_name = parent_folder + '/' + data_file_path
            os.makedirs(os.path.dirname(processed_file_name), exist_ok = True)
            print("Writing email file:" + data_file_path)
            write_processed_email(processed_file_name, processed_email_str)
        except Exception as exc:
            print( exc)