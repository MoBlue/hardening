# Windows Local GPO Hardening

Simple python script to remotely deploy security settings via local GPO, using Microsoft LGPO tool.

## Getting Started
Download deploy.py, edit relevant options and run.

### Prerequisites
Tested only on Windows 10, should work on any LGPO supported system.

The following files should be hosted on internal/external site, available for download by the script:<br/><br/>
 * LGPO.exe — Microsoft Local Group Policy Object Utility
 * GPO.zip — Password protected zip of GPO backup folder — may be produced by AD GPMC backup, SCM and more. The zip is expected to host 'GPO' directory, holding the GPO {ID} folder tree and manifest.<br/>
 GPO.zip_<br/>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|GPO_<br/>
	     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|{GPO GUID}_<br/>
	     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|manifest.xml<br/>
 * ADMX.zip — Password protected zip of ADMX and ADML files — may be downloaded from various sources. The zip is expected to host 'ADMX' directory, hodling under it the ADMX files and 'en-us' ADML folder.<br/>
 ADMX.zip_<br/>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|ADMX_<br/>
	     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|/en-us/*.adml<br/>
	     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|*.admx<br/>

### Configurable options:
The following settings should be modified in 'deployment.py':
 * rootpath = r'C:/Installs/' # local root path for files and folders
 * win10path = os.path.join(rootpath, 'WIN10/') # optional Version folder under local root path
 * admxFlag = 1 # 0 or 1 for ADMX download and deploy
 * lgpoURL = 'https://{SITE}/LGPO.exe' # Microsoft LGPO download link
 * win10gpoURL = 'https://{SITE}/GPO.zip' # Encrypted Zipped GPO backup download link
 * win10admxURL = 'https://{SITE}/ADMX.zip' # Encrypted Zipped ADMX/ADML download link
 * zipPWD = "{ZIP PASSWORD}" # Encrypted zip password. Note! use the same password for all zip files.

## Notes and Limitations
The script makes use of ZipFile library, posing the following limitations:
 1. The zipfile module does not support ZIP files with appended comments, or multi-disk ZIP files. It does support ZIP files larger than 4 GB that use the ZIP64 extensions.
 2. zipfile only supporting traditional PKWARE encryption method, if you try a WinZip AES-256 encrypted zip, zipfile.extractall raises a RuntimeError "Bad password for file" when given the correct password.

Zip files encryption:
1. Same password should be used for all files. 
2. Zip encryption is mostly used as integrity control, due to the PKWARE encryption method limitation, it should not be relied upon for protection of sensitive data.

## To Do:
1. Allow multiple passwords for different zip files
2. Cleanup procedure of local resources
3. GPO Update procedure
4. GPO Compare & Report procedure

## License
The code may be used by anyone and everyone for any purpose.

## Acknowledgments
Inspired by Comodo ITSM Procedures.
