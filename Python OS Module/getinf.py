import os,time

print('my Filename: ' , "gitignore.jpg")
print('modified time: ' , time.ctime(os.path.getmtime('gitignore.jpg')))
print('access time: ', time.ctime(os.path.getatime('gitignore.jpg')))
print('created time:' , time.ctime(os.path.getctime('gitignore.jpg')))
print('Size is:',os.path.getsize('gitignore.jpg'))
