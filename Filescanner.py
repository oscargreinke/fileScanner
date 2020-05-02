import os

os.chdir("/Users/oscargreinke/Desktop/OmniFolder/Personal/RandomPrograms/FileScanner/files/")
for filename in os.listdir("/Users/oscargreinke/Desktop/OmniFolder/Personal/RandomPrograms/FileScanner/files/"):
    file = open(filename, "rt",encoding='us-ascii')
    print(filename)
    for line in file:
        if "no no no" in line or "yes no" in line or "no yes" in line:
           print(line)
           #line = "no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no "
    file.close()
