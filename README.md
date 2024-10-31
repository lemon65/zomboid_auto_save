# Zomboid Auto Save - "ZAS" ![alt text](/images/pz_logo.png "Project Zomboid")
This is a script that runs along side project zomboid and saves/backup your game as you play. you can change variables in the script_config.py file to change the save location "BACKUP_SAVE_PATH" and interval "SAVE_INTERVAL_SEC"

* BACKUP_SAVE_PATH == defaults the saves to -- "C:\Users\\<CURRENT_USER>\Zomboid\zas_backup_saves\"
* SAVE_INTERVAL_SEC == defaults to 300sec/5mins before it will save.
* COMPRESS_FOLDERS == defaults to 0, to .ZIP the saves to save on space.

** added functions by mikrostiff:
* MAX_BACKUPS == defaults to 10, which will back up max 10 files for each save, oldest ones will be replaced by newest ones.
* Only backs up when changes are detected in the SAVE file.

NOTE - The script will auto create the backup folders if they are not present

### Usage:
```
$ py zomboid_auto_save.py
All saves are in: 'C:\Users\aaron\Zomboid\zas_backup_saves'
08/10/22 01:05:30 -- Archiving 'fire_man_save', into: 'C:\Users\aaron\Zomboid\zas_backup_saves\Survivor\1660118730_fire_man_save'
08/10/22 01:05:35 -- Archiving 'fire_man_save', into: 'C:\Users\aaron\Zomboid\zas_backup_saves\Survivor\1660118741_fire_man_save'
08/10/22 01:05:40 -- Archiving 'fire_man_save', into: 'C:\Users\aaron\Zomboid\zas_backup_saves\Survivor\1660119052_fire_man_save'
Hope you killed some Zeds my friend!
```

## Screenshot of ZAS
![alt text](/images/zas_example.png "Example using ZAS to save your game")

## How to Install
Clone the repo and run the python script

## Requirements
python 3.9.6 or Greater

## Credit
I do not own or take any credit for the game Project Zomboid, please buy the game here - https://store.steampowered.com/app/108600/Project_Zomboid/ 
