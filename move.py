import os
import platform
import shutil

def clearScreen():
    operatingSys = platform.system()
    if operatingSys == 'Windows':
        os.system('cls')
    elif operatingSys == 'Darwin' or operatingSys == 'Linux':
        os.system('clear')

def createFolderAndMoveFiles():
  path = os.path.join("", "new_folder/")
  
  # Create the directory
  # 'new_folder' in
  # '/home / User / Documents'
  try:
    os.mkdir(path)
    print("Directory '% s' created" % directory)
  except:
    print ("Directory already exist")
  filelist = open('files.txt').readlines()
  for filename in filelist:
    print('Processing : ' + filename.strip())
    new_path = path + filename.strip()
    if os.path.isfile(filename.strip()):
      print('Moved to ' + new_path.strip())
      shutil.move(filename.strip(), new_path)

clearScreen()
print("File movement started");
createFolderAndMoveFiles()
print("File movement ended");
