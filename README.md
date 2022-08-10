# Zomboid Auto Save
This is a script that runs along side project zomboid and saves/backup your game as you play. you can change varables in the script_config.py file to change the save location "BACKUP_SAVE_PATH" and interval "SAVE_INTERVAL_SEC"

The script defaults the saves to -- "C:\Users\<CURRENT_USER>\Zomboid\zas_backup_saves\"

NOTE - The script will auto create the backup folders if they are not present

### Usage:
```
$ py zomboid_auto_save.py
All saves are in: 'C:\Users\<CURRENT_USER>\Zomboid\zas_backup_saves\'
08/09/22 09:36:00 -- Zipping 'fire_man_save', into Archive: 'C:\Users\<CURRENT_USER>\Zomboid\zas_backup_saves\Survivor\1660106160_fire_man_save'
08/09/22 09:41:01 -- Zipping 'fire_man_save', into Archive: 'C:\Users\<CURRENT_USER>\Zomboid\zas_backup_saves\Survivor\1660106461_fire_man_save'
08/09/22 09:46:02 -- Zipping 'fire_man_save', into Archive: 'C:\Users\<CURRENT_USER>\Zomboid\zas_backup_saves\Survivor\1660106762_fire_man_save'
```

## How to Install
Clone the repo and run the python script

## Requirements
python 3.9.6 or Greater