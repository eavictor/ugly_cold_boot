# Windows only cold boot tool

### Warning: DO NOT touch KeyBoard & Mouse while running

### How to Use:
1. Setup boot schedule in BIOS

Note: usually locate at `power management` section

2. Copy this folder to target system (no specific folder)

3. Double click `install.exe` to generate auto shutdown trigger

4. Reboot manually

### How to Uninstall:
1. Close cmd window when pop up

2. Double click `uninstall.exe`

3. Delete tool folder

### If cannot run:
##### stuck at: `Try launching set_time_and_shutdown.exe`
1. Open `images` folder

2. Capture those images again (with same name)

3. Put new images to `images` folder (overwrite)

### Build:
1. Execute command `pip install -Ur requirements.txt`

2. Double click `build.bat`

3. Copy exe files from `dist` folder to project root folder

4. Delete all `.py` and `.spec` files

5. Delete `build` and `dist` folder


