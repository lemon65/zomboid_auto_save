""" This is a project zomboid script that will auto save you game every interval """
import os
import sys
import time
import shutil
import datetime
import script_config as CONF

class ZAS():
    "This is a class that run the Zomboid Auto Save system"
    def __init__(self):
        self.SAVE_PATH = os.path.expanduser('~\\Zomboid\\Saves')  # Finds the local path to the users zomboid saves
        self.next_save_time = time.time() + CONF.SAVE_INTERVAL_SEC
        self.mkfolder_system()

    def mkfolder_system(self):
        """ Checks to see if we need to make the folders where we put the backup Zips"""
        FOLDERS = os.listdir(self.SAVE_PATH)
        if not os.path.isdir(CONF.BACKUP_SAVE_PATH):
            print("Created a folder to save backups: '%s'" % CONF.BACKUP_SAVE_PATH)
            os.mkdir(CONF.BACKUP_SAVE_PATH)
            for folder in FOLDERS:
                os.mkdir(CONF.BACKUP_SAVE_PATH + "\\" + folder)
        else:
            print("All saves are in: '%s'" % CONF.BACKUP_SAVE_PATH)

    def back_up_saves(self):
        """ Step the save folders and backups all saves """
        FOLDERS = os.listdir(self.SAVE_PATH)  # Get all the folder names in the saves folder ['Multiplayer', 'Sandbox', 'Survivor']
        for folder_name in FOLDERS:
            base_save_path = self.SAVE_PATH + "\\" + folder_name
            save_folders = os.listdir(base_save_path)
            for save in save_folders:  # Get all the sub folder saves
                full_save_path = base_save_path + "\\" + save
                zip_name = str(int(time.time())) + "_" + save
                full_backup_path = CONF.BACKUP_SAVE_PATH + "\\" + folder_name + "\\" + zip_name
                now = datetime.datetime.now()
                current_time = now.strftime("%m/%d/%y %I:%M:%S")
                print("%s -- Archiving '%s', into: '%s'" % (current_time, save, full_backup_path))
                self.archive_saves(full_backup_path, full_save_path)

    def archive_saves(self, path_to_backup, target_save_path):
        """ depending on the settings it will archive the saves as a .ZIP of the targeted folder or just copy the folders """
        if CONF.COMPRESS_FOLDERS == 0:
            shutil.make_archive(path_to_backup, 'zip', target_save_path)
        elif CONF.COMPRESS_FOLDERS == 1:
            shutil.copytree(target_save_path, path_to_backup)
        else:
            raise ValueError("Please check the value for COMPRESS_FOLDERS, it needs to be a [1 or 0]")

    def _save_poller(self):
        """ Every SAVE_INTERVAL_SEC it will review the folders created and backup your save files """
        try:
            while True:
                if time.time() >= self.next_save_time:
                    self.back_up_saves()
                    self.next_save_time = time.time() + CONF.SAVE_INTERVAL_SEC  # Reset the next save time
                time.sleep(10)
        except KeyboardInterrupt:
            print("Hope you killed some Zeds my friend!")
            sys.exit(0)
        except ValueError as e:
            print("ERROR: %s" % e)
            sys.exit(1)

zas = ZAS()
zas._save_poller()