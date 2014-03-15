import os

print("PATH shortener v.01")
print("something something GNU GPL v3 license (no but really do whatever with this)")
print("\n")

path = os.getenv('PATH')
print("Writing old PATH to pathBackup.txt in this directory..")
with open('backup.txt', 'w+') as fileBackup:
	fileBackup.write(path);
path = path.split(";")
oldLength = len(path)
path = list(set(path))
print(path)
print(str(oldLength - len(path)) + " extraneous vars removed")
path = ';'.join(path)

os.putenv("PATH",path)

print("If you see no change in the PATH variable, that means you didn't run this with administrative privileges. Try again.")