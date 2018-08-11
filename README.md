# Windows Local GPO Hardening

Simple python script to remotely deploy security settings via local GPO, using Microsoft LGPO tool.

## Getting Started
Download deploy.py, edit relevant options and run.

### Prerequisites
Tested only on Windows 10, should work on any LGPO supported system.

The following files should be hosted on internal/external site, available for download by the script:<br/><br/>
<b>Note! Same password should be used for all zip files. Zip encryption is mostly used as integrity control.</b>
 * LGPO.exe — Microsoft Local Group Policy Object Utility
 * GPO.zip — Password protected zip of GPO backup folder — may be produced by AD GPMC backup, SCM and more. The zip is expected to host 'GPO' directory, holding the GPO {ID} folder tree and manifest.
 * ADMX.zip — Password protected zip of ADMX and ADML files — may be downloaded from various sources. The zip is expected to host 'ADMX' directory, hodling under it the ADMX files and 'en-us' ADML folder.


### Configurable options:
The following settings should be modified in 'deployment.py':
 * rootpath = r'C:/Installs/' # local root path for files and folders
 * win10path = os.path.join(rootpath, 'WIN10/') # optional Version folder under local root path
 * lgpoURL = 'https://{SITE}/LGPO.exe' # Microsoft LGPO download link
 * win10gpoURL = 'https://{SITE}/GPO.zip' # Encrypted Zipped GPO backup download link
 * win10admxURL = 'https://{SITE}/ADMX.zip' # Encrypted Zipped ADMX/ADML download link
 * zipPWD = "{ZIP PASSWORD}" # Encrypted zip password. Note! use the same password for all zip files.

## To Do:
1. Allow multiple passwords for different zip files
2. Cleanup procedure of local resources
3. GPO Update procedure
4. GPO Compare & Report procedure

## License
The code may be used by anyone and everyone for any purpose.

## Acknowledgments
Inspired by Comodo ITSM Procedures.
