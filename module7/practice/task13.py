import shutil

def create_backup(path, file_name, employee_residence):
    with open(f'{path}/{file_name}', 'wb') as fh:
        for key,val in employee_residence.items():
            encode_str = f'{key} {val}\n'.encode('utf-8')
            fh.write(encode_str)
    archive_name = shutil.make_archive('backup_folder', 'zip', path)
    return archive_name
print(create_backup('strings_module','backup_folder',{'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'} ))