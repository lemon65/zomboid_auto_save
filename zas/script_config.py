import os

# This is a configuration file for the script

# This is how often the script will back up your saves 300sec == 5mins
SAVE_INTERVAL_SEC = 5*60

# The save location where you want to save the backups, note this needs to be the "FULL PATH" to the target folder
BACKUP_SAVE_PATH = os.path.expanduser('~\\Zomboid\\') + "Saves_ZAS_backup"

# Example of Setting a manual save path for the script
# BACKUP_SAVE_PATH = "C:\Users\<CURRENT_USER>\Documents\Game_Saves"

# This Setting will configure the script to .ZIP and compress the saves or to just copy the folders
# 0 == .ZIP the folder, 1 = Just copy the folder 
COMPRESS_FOLDERS = 0

# this determines how many save files are kept on your disc. Newest one will override oldest one. 
# Only works when COMPRESS_FOLDERS = 0
MAX_BACKUPS = 5