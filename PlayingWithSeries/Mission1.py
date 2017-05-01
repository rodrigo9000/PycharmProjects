# check if file exist, if not, create
# Write some computer config on it, close file
# check if folder backup exist, if not, create it
# copy files to this folder in zip format
# when crateing another backup, increment 1 at the end if file exist
from os import path
from sys import platform
import re
import shutil

file1 = "missionfile.txt"

print "Text Item exists: " + str(path.exists(file1))

if path.exists(file1):
    session = open(file1, "a+")
    session.write ("Mission 1 \n")
    session.write("Your system is a: \n" + platform)
else:
    session = open(file1, "w+")
    session.write ("Mission 1 \n")
    session.write("Your system is a: \n" + platform)

# Close file if Open
if not session.closed:
    session.close()
# backup Folder
fname = "backup.zip"
print "Zip File Exist: " + str(path.isfile(fname))
# if not path.isfile(fname):
#     src = path.realpath(file1)
#     root_dir, tail = path.split(src)
#     shutil.make_archive("backup", "zip", root_dir)
def availablename(fname):
    while path.isfile(fname):
        head, tail = fname.split('.')
        var = re.search(r'(\d+$)', head)
        if var:
            num = int(var.group()) + 1
            fname = re.sub(var.group(), str(num), fname)
        else:
            fname = head + "1" + '.' + tail
    return fname

fname = availablename(fname)
print "Next backup legal name:", fname