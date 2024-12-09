import zipfile
import pathlib

def make_archive(filepath,dest_dir):
    dest_path = pathlib.Path(dest_dir,'compressed.zip')
    with zipfile.ZipFile(dest_path,'w') as archive:
        for fp in filepath:
            fp = pathlib.Path(fp)
            archive.write(fp,arcname=fp.name)


#if __name__ == "__main__":
#    make_archive(filepath = ['functions.py'],dest_dir = 'temp')