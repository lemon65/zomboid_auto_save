""" This is a project zomboid script that will auto save you game every interval """
import os
import sys
import time
import shutil
import datetime

def get_config_path():
    """Get path to config file whether running as script or exe"""
    if getattr(sys, 'frozen', False):
        # Running as exe
        return os.path.join(os.path.dirname(sys.executable), 'script_config.py')
    else:
        # Running as script
        return os.path.join(os.path.dirname(__file__), 'script_config.py')

import importlib.util
config_path = get_config_path()
spec = importlib.util.spec_from_file_location("script_config", config_path)
CONF = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CONF)

class ZAS():
    "This is a class that run the Zomboid Auto Save system"
    def __init__(self):
        self.SAVE_PATH = os.path.expanduser('~\\Zomboid\\Saves')
        self.next_save_time = time.time() + CONF.SAVE_INTERVAL_SEC # Changed to current time for immediate save
        self.MAX_BACKUPS = CONF.MAX_BACKUPS  # Add max backups constant
        self.mkfolder_system()
        self.last_modified_times = {} # Add dictionary to store last modified times
    
    def mkfolder_system(self):
        """ Checks to see if we need to make the folders where we put the backup Zips"""
        FOLDERS = os.listdir(self.SAVE_PATH) # FOLDERS are different game mode. Apocalypse/Survivor/etc.,
        if not os.path.isdir(CONF.BACKUP_SAVE_PATH):
            print("Created a folder to save backups: '%s'" % CONF.BACKUP_SAVE_PATH)
            os.mkdir(CONF.BACKUP_SAVE_PATH)
            for folder in FOLDERS:
                os.mkdir(CONF.BACKUP_SAVE_PATH + "\\" + folder)
        else:
            print("All saves are in: '%s'" % CONF.BACKUP_SAVE_PATH)

    def check_for_changes(self, save_path):
        """Returns True if files have changed since last check"""
        current_mod_time = os.path.getmtime(save_path)
        last_mod_time = self.last_modified_times.get(save_path, 0)
        # Update stored modification time
        self.last_modified_times[save_path] = current_mod_time
        return current_mod_time > last_mod_time

    def back_up_saves(self):
        """ Step the save folders and backups all saves """
        FOLDERS = os.listdir(self.SAVE_PATH)  # Get all the folder names in the saves folder ['Multiplayer', 'Sandbox', 'Survivor']
        for folder_name in FOLDERS:
            base_save_path = self.SAVE_PATH + "\\" + folder_name
            save_folders = os.listdir(base_save_path)
            for save in save_folders:  # Get all the sub folder, save = each individual save game.
                full_save_path = base_save_path + "\\" + save
                backup_dir = os.path.join(CONF.BACKUP_SAVE_PATH, folder_name,save)
                # Only backup if changes detected
                if self.check_for_changes(full_save_path):
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    zip_name = timestamp + "_" + save
                    full_backup_path = os.path.join(backup_dir,zip_name) # store saved zip file in respective game save folder
                    now = datetime.datetime.now()
                    current_time = now.strftime("%m/%d/%y %I:%M:%S")
                    print("%s archiving '%s', into: '%s'" % (current_time, save, backup_dir))
                    self.archive_saves(full_backup_path, full_save_path)
                else:
                    print(f"No changes detected in {save}")
                self.cleanup_old_backups(backup_dir)
                    
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
                current_time = time.time()
                time_remaining = int(self.next_save_time - current_time)
                if current_time >= self.next_save_time:
                    self.back_up_saves()
                    self.next_save_time = time.time() + CONF.SAVE_INTERVAL_SEC
                print(f"Next save in {time_remaining} seconds", end='\r')
                time.sleep(min(10,CONF.SAVE_INTERVAL_SEC))
                
        except KeyboardInterrupt:
            print("\nHope you killed some Zeds my friend!")
            sys.exit(0)
        except ValueError as e:
            print("ERROR: %s" % e)
            sys.exit(1)
            
    def cleanup_old_backups(self, backup_dir):
        """Keep only the most recent MAX_BACKUPS files"""
        files = os.listdir(backup_dir)
        if len(files) > self.MAX_BACKUPS:
            files.sort()  # Sort by timestamp since filenames start with unix timestamp
            files_to_remove = files[:-self.MAX_BACKUPS]  # Keep last 10 files
            for old_file in files_to_remove:
                full_path = os.path.join(backup_dir, old_file)
                if os.path.exists(full_path):
                    if os.path.isfile(full_path):
                        os.remove(full_path)
                    elif os.path.isdir(full_path):
                        shutil.rmtree(full_path)
                    
zas = ZAS()
zas._save_poller()
