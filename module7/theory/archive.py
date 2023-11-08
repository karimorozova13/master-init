import shutil

archive = shutil.make_archive('binary.bit', 'zip') # you can archivate file

print(archive) #full path to archive

shutil.unpack_archive(archive, 'theory')

# archive = shutil.make_archive('backup', 'zip', 'paht/to/folder/or/file')  you archivate the folder, add the pass