import os

# This is a configuration file for the script

# This is how often the script will back up your saves 300sec == 5mins
SAVE_INTERVAL_SEC = 300

# The save location where you want to save the backups, note this needs to be the "FULL PATH" to the target folder
BACKUP_SAVE_PATH = os.path.expanduser('~\\Zomboid\\') + "zas_backup_saves"

# Example of Setting a manual save path for the script
# BACKUP_SAVE_PATH = "C:\Users\<CURRENT_USER>\Documents\Game_Saves"

# This Setting will configure the script to .ZIP and compress the saves or to just copy the folders
# 0 == .ZIP the folder, 1 = Just copy the folder 
COMPRESS_FOLDERS = 0

# This is the max amount of saves that will be backed up by the system
MAX_SAVES = 10