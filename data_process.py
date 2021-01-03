"""
This is a standalone script that calls routines to process email
and clean up text. The input
"""
import os
from nlp_code.email_processor import process_email, read_email_file, write_processed_email
import config
import pathlib


def process_data(file_list_name, output_folder):
    with open(file_list_name,'r') as f:

        for data_file_path in f.readlines():
            try:
                data_file_path = data_file_path.strip()
                print("Reading email file:" + data_file_path)
                email_str=read_email_file(data_file_path)
                print("Processing email file:" + data_file_path)
                processed_email_str=process_email(email_str)
                print("Processed string")
                print(processed_email_str)
                #from the original path strip the leading `data/`
                p = pathlib.Path(data_file_path)
                output_file_name=pathlib.Path(*p.parts[1:])
                processed_file_name = os.path.join(output_folder,output_file_name)
                os.makedirs(os.path.dirname(processed_file_name), exist_ok = True)
                print("Writing email file:" + data_file_path)
                write_processed_email(processed_file_name, processed_email_str)
            except Exception as exc:
                print(exc)

if __name__=="__main__":
    # Input list file created typically using a utility like find
    file_list_name = config.DATA_FILE_LIST_PATH
    # The output folder where the cleaned up data should be stored
    output_folder = config.PROCESSED_OUTPUT_FOLDER
    process_data(file_list_name, output_folder)