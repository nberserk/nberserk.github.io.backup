import sys
import os

home="/Users/darren/projects/nberserk.github.io/_posts/"
fileName=sys.argv[1].split(".")[0] + ".html"
src=home+fileName

with open(src) as f:
    content = f.readlines()
    for l in content:
        if "date:" in l:
            date=l.split(":")[1].strip()            
            dest=home+date+"-"+fileName
            print "renaming %s -> %s " % (src,dest)   
            os.rename(src, dest)
            break



# for o in sys.argv:
#     print o
