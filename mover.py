import os
import shutil
from Tkinter import IntVar
import dataset


class DbMigrationThing:
    def __init__(self, old_folder_path, new_folder_path):
        self.old_folder_path = old_folder_path
        self.new_folder_path = new_folder_path
        self.number_of_folders = IntVar()
        self.progress_of_folders = IntVar()

    def do_migrate(self):
        shutil.copy(os.path.abspath(self.old_folder_path), os.path.abspath(self.old_folder_path) + ".bak")
        shutil.copy(os.path.abspath(self.new_folder_path), os.path.abspath(self.new_folder_path) + ".bak")

        new_database_connection = dataset.connect('sqlite:///' + self.new_folder_path)
        old_database_connection = dataset.connect('sqlite:///' + self.old_folder_path)

        new_folders_table = new_database_connection['folders']
        old_folders_table = old_database_connection['folders']
        self.number_of_folders = old_folders_table.count(folder_is_active="True")
        self.progress_of_folders = 0
        for line in old_folders_table.find(folder_is_active="True"):
            print(line)
            new_folders_table.insert(dict(folder_name=line['folder_name'],
                                          copy_to_directory=line['copy_to_directory'],
                                          folder_is_active=line['folder_is_active'],
                                          alias=line['alias'],
                                          process_backend_copy=line['process_backend_copy'],
                                          process_backend_ftp=line['process_backend_ftp'],
                                          process_backend_email=line['process_backend_email'],
                                          ftp_server=line['ftp_server'],
                                          ftp_folder=line['ftp_folder'],
                                          ftp_username=line['ftp_username'],
                                          ftp_password=line['ftp_password'],
                                          email_to=line['email_to'],
                                          email_origin_address=line['email_origin_address'],
                                          email_origin_username=line['email_origin_username'],
                                          email_origin_password=line['email_origin_password'],
                                          email_origin_smtp_server=line['email_origin_smtp_server'],
                                          process_edi=line['process_edi'],
                                          convert_to_format=line['convert_to_format'],
                                          calculate_upc_check_digit=line['calculate_upc_check_digit'],
                                          include_a_records=line['include_a_records'],
                                          include_c_records=line['include_c_records'],
                                          include_headers=line['include_headers'],
                                          filter_ampersand=line['filter_ampersand'],
                                          tweak_edi=line['tweak_edi'],
                                          pad_a_records=line['pad_a_records'],
                                          a_record_padding=line['a_record_padding'],
                                          email_smtp_port=line['email_smtp_port'],
                                          reporting_smtp_port=line['reporting_smtp_port'],
                                          ftp_port=line['ftp_port'],
                                          email_subject_line=line['email_subject_line']))
            self.progress_of_folders += 1
