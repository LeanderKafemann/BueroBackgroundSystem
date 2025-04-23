import os, shutil, zipfile
from tkinter.filedialog import askopenfilename
import pyautogui as py

py.alert("Systemupdatevorgang wird gestartet...\nSie nutzen Systemupdate 6!\nVielen Dank!", "Systemupdate")

pfad = askopenfilename(title="Zip-Datei mit Update auswählen", filetypes=[("Zip comprimized folder", "*.zip")])
versio = pfad[pfad.find("system", len(pfad)-20):len(pfad)].rstrip(".zip").lstrip("system")
tempfile = "./programdata/update"
with zipfile.ZipFile(pfad, 'r') as zip_ref:
    zip_ref.extractall(tempfile)

os.remove("./update.py")
shutil.move(tempfile + "/update.py", "./update.py")
os.remove("./fehleranalyse.py")
shutil.move(tempfile + "/fehleranalyse.py", "./fehleranalyse.py")

with open("./programdata/buero/versioninfo_System.txt", "w") as f:
    f.write(versio)

py.alert("Die Operation war erfolgreich.", "Ende")
