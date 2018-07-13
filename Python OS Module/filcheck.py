import os,time
arr = os.listdir('.')
print(arr)
for file in arr:
    print("Name:",file)
    print("Is file:",os.path.isfile(file))
    print("is Link",os.path.islink(file))
    print("is Dir",os.path.isdir(file))
    print("path",os.path.realpath(file))
    print("Relative Path:",os.path.relpath(file))
    print("size:",os.path.getsize(file))
    print("split:",os.path.split(os.path.realpath(file)))
    print("split dir:",os.path.splitdrive(os.path.realpath(file)))


    print("-----")
