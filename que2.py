import os
import zipfile
 

def zip_files(search_directory, selected_extensions, output_path):
    file_zip = zipfile.ZipFile('.\\my_stuff\\my_stuff.zip', 'w')
    for folder, subfolders, files in os.walk('.\\my_stuff'):
 
        for file in files:
            if file.endswith('*.jpeg') or file.endswith('*.txt') :
                file_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), '.my_stuff'), compress_type = zipfile.ZIP_DEFLATED)
 
    file_zip.close()
                    
if __name__ == '__main__':
    zip_files('.\\my_stuff', ['.jpg','.txt'], 'my_stuff.zip')