import re
from os import path
# line = "Cats are smarter than dogs";
#
# matchObj = re.match( r'dogs', line, re.M|re.I)
# if matchObj:
#    print "match --> matchObj.group() : ", matchObj.group()
# else:
#    print "No match!!"
#
# searchObj = re.search( r'dogs', line, re.M|re.I)
# if searchObj:
#    print "search --> searchObj.group() : ", searchObj.group()
# else:
#    print "Nothing found!!"

# string = "backup.zip"
#
# def availablename(fname):
#     while path.isfile(fname):
#         head, tail = fname.split('.')
#         var = re.search(r'(\d+$)', head)
#         if var:
#             num = int(var.group()) + 1
#             fname = re.sub(var.group(), str(num), fname)
#         else:
#             fname = head + "1" + '.' + tail
#     return fname
# print availablename(string)

file = open("LinksRegex.txt", "r")
for line in file:
    print "-" * 20
    print line
    # URL Regex
    regex = re.search(r'^(https|http|ftp):[\/]{2}([\w\.\-#&amp]+\.[a-zA-Z]{2,4})(:[0-9]+)?', line, flags = re.IGNORECASE|re.MULTILINE)
    print "Entire regex", regex.group()
    print "[Protocol]: ", regex.group(1)
    print "[Domain Name]: ", regex.group(2)
    print "[Port number]: ", regex.group(3)

