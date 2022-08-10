import os

# This is a configuration file for the script

# This is how often the script will back up your saves 300sec == 5mins
SAVE_INTERVAL_SEC = 300

# The save location where you want to save the backups, note this needs to be the "FULL PATH" to the target folder
BACKUP_SAVE_PATH = os.path.expanduser('~\\Zomboid\\') + "zas_backup_saves"

# Example of Setting a manual save path for the script
# BACKUP_SAVE_PATH = "C:\Users\<CURRENT_USER>\Documents\Game_Saves"
