import base64
import zipfile, urllib
from zipfile import *
import os, sys
import ctypes
import subprocess
import traceback
import logging
import shutil

rootpath = r'C:/Installs/' # root path for deployment
win10path = os.path.join(rootpath, 'WIN10/') # optional Version folder

lgpoURL = 'https://{SITE}/LGPO.exe' # Microsoft LGPO link
win10gpoURL = 'https://{SITE}/GPO.zip' # Encrypted Zipped GPO backup in folder named 'GPO' - GPO.zip => /GPO/{GPO Backup Files}
win10admxURL = 'https://{SITE}/ADMX.zip' # Encrypted Zipped ADMX + ADML in folder named 'ADMX' - => /ADMX/{ADMX Files}/en-us/{ADML Files}

zipPWD = "{ZIP PASSWORD}" # Encrypted zip password. Note! use the same password for all zip files. 

if not os.path.exists(rootpath):
    os.makedirs(rootpath)
    
if not os.path.exists(win10path):
    os.makedirs(win10path)

class disable_file_system_redirection:
    _disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
    _revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
    def __enter__(self):
        self.old_value = ctypes.c_long()
        self.success = self._disable(ctypes.byref(self.old_value))
    def __exit__(self, type, value, traceback):
        if self.success:
            self._revert(self.old_value)


with disable_file_system_redirection():
    def downloadLGPO():
        lgpopath = os.path.join(rootpath, 'LGPO.exe')
        if os.path.exists(lgpopath):
                os.remove(lgpopath)
        try:
            with open(lgpopath, 'wb') as f:
                f.write(urllib.urlopen(lgpoURL).read())
            if os.path.isfile(lgpopath):
                return '{} - {}KB'.format(lgpopath, os.path.getsize(lgpopath)/1000)
        except Exception as e:
            return e.message

with disable_file_system_redirection():
    def downloadWIN10():
        win10GPOpath = os.path.join(win10path, 'GPO.zip')
        if os.path.exists(win10GPOpath):
            os.remove(win10GPOpath)

        try:
            with open(win10GPOpath, 'wb') as f:
                f.write(urllib.urlopen(win10gpoURL).read())
            if os.path.isfile(win10GPOpath):
                return unzipWIN10(win10GPOpath)
        except Exception as e:
            return e.message

with disable_file_system_redirection():
    def unzipWIN10(zip_file):
        try:
            zf=zipfile.ZipFile(zip_file, "r")
            zf.extractall(path = win10path, pwd = zipPWD)
            zf.close()
            return 'download & unzip WIN10 completed'
        except Exception as e:
            return e.message

with disable_file_system_redirection():
    def downloadADMX():
        win10ADMXpath = os.path.join(win10path, 'ADMX.zip')
        if os.path.exists(win10ADMXpath):
            os.remove(win10ADMXpath)
        try:
            with open(win10ADMXpath, 'wb') as f:
                f.write(urllib.urlopen(win10admxURL).read())
            if os.path.isfile(win10ADMXpath):
                return unzipADMX(win10ADMXpath)
        except:
            return 'Check ADMX URL or Download Path!'

with disable_file_system_redirection():
    def unzipADMX(zip_file):
        try:
            zf=zipfile.ZipFile(zip_file, "r")
            zf.extractall(path=win10path,pwd=zipPWD)
            zf.close()
            return 'download & unzip ADMX completed'
        except Exception as e:
            return e.message

with disable_file_system_redirection():
    def copyADMX():
        win10ADMXdpath = os.path.join(win10path, 'ADMX/')
        if not os.path.exists(win10ADMXdpath):
            return 'cant find ADMX'
        try:
            src_files = os.listdir(win10ADMXdpath)
            for file_name in src_files:
                full_file_name = os.path.join(win10ADMXdpath, file_name)
                if (os.path.isfile(full_file_name)):
                    shutil.copy(full_file_name, r'C:/Windows/PolicyDefinitions/')
            return 'ADMX Success'
        except Exception as e:
            return e.message
with disable_file_system_redirection():
    def copyADML():
        win10ADMLdpath = os.path.join(win10path, 'ADMX/en-us/')
        if not os.path.exists(win10ADMLdpath):
            return 'cant find ADML'
        try:
            src_files = os.listdir(win10ADMLdpath)
            for file_name in src_files:
                full_file_name = os.path.join(win10ADMLdpath, file_name)
                if (os.path.isfile(full_file_name)):
                    shutil.copy(full_file_name, r'C:/Windows/PolicyDefinitions/en-US/')
            return 'ADML Success'
        except Exception as e:
            return e.message

with disable_file_system_redirection():
    def ImplementGPO():
        lgpopath = os.path.join(rootpath, 'LGPO.exe')
        win10GPOpath = os.path.join(win10path, 'GPO/')
        if not os.path.exists(lgpopath):
            return "Can't find LGPO"                
        if not os.path.exists(win10GPOpath):
            return "Can't find GPO dir"
        cmd = lgpopath + ' /g ' + win10GPOpath
        try:
            o=os.popen(cmd).read()
            return o
        except Exception as e:
            return e.message

    if __name__=='__main__':
        print ('Download LGPO:')
        print downloadLGPO()
        print ('download & unzip WIN10 gpo:')
        print downloadWIN10()
        print ('download & unzip ADMX:')
        print downloadADMX()
        print ('copyADMX:')
        print copyADMX()
        print ('copyADML:')
        print copyADML()
        print ('ImplementGPO:')
        print ImplementGPO()
        print ('Completed')
