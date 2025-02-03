# Zomboid Auto Save - "ZAS" ![alt text](/images/pz_logo.png "Project Zomboid")
This is a script that runs along side project zomboid and saves/backup your game as you play. you can change variables in the script_config.py file to change the save location "BACKUP_SAVE_PATH" and interval "SAVE_INTERVAL_SEC" as well as the total maximum amount of saves "MAX_SAVES" you want to keep at one time.

* BACKUP_SAVE_PATH == defaults the saves to -- "C:\Users\\<CURRENT_USER>\Zomboid\zas_backup_saves\"
* SAVE_INTERVAL_SEC == defaults to 300sec/5mins before it will save.
* COMPRESS_FOLDERS == defaults to 0, to .ZIP the saves to save on space.
* MAX_SAVES == defaults to 10, The total amount of saves you can have saved, it will start removing the oldest after it hits this limit.

NOTEs About Running:
- The script will auto create the backup folders if they are not present
- Don't leave the script running or it can overwrite all your backups with the same save data (5mins - 10saves == 50min time frame)

### Usage:
```
$ py zomboid_auto_save.py
Configured for Max Saves of: 10
All saves are in: 'C:\Users\CURRENT_USER\Zomboid\zas_backup_saves'
02/02/25 10:22:56 -- Archiving '2025-01-20_11-41-01', into: 'C:\Users\CURRENT_USER\Zomboid\zas_backup_saves\Sandbox\1738563776_2025-01-20_11-41-01'
MaxSaves = 10, Removing the oldest save file: 1737956008_2025-01-20_11-41-01.zip
Hope you killed some Zeds my friend!
```

### Restore a Save:
* Turn off the game
* Go into your configured backup save folder - 'C:\Users\CURRENT_USER\Zomboid\zas_backup_saves'
* Unzip the file, using - https://www.7-zip.org/
* Remove the Epoch time at the front of the folder name.
    * "/1737956008_2025-01-20_11-41-01" >> "/2025-01-20_11-41-01"
* Overwrite the old save folder with the backup save in - 'C:\Users\CURRENT_USER\Zomboid\Saves'
* Launch the game and enjoy

## Screenshot of ZAS
![alt text](/images/zas_example.png "Example using ZAS to save your game")

## How to Install
Clone the repo and run the python script

## Requirements
python 3.9.6 or Greater

## Credit
I do not own or take any credit for the game Project Zomboid, please buy the game here - https://store.steampowered.com/app/108600/Project_Zomboid/ 
