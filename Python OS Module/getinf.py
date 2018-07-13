import os,time
print('Filename: ' , "ram.txt")
print('modified time: ' , time.ctime(os.path.getmtime('ram.txt')))
print('access time: ', time.ctime(os.path.getatime('ram.txt')))
print('created time:' , time.ctime(os.path.getctime('ram.txt')))
print('Size:',os.path.getsize('ram.txt'))
