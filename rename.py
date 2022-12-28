from pathlib import Path
import shutil
import re
import sys
from tqdm import tqdm
EXTS = [".jpg", ".png", ".JPG", ".jpeg", ".tif",".gif" ,".tiff", ".TIF"]

def reGet(path):
    files=[]
    for path_i in path.iterdir():
        if path_i.is_dir():
            files.extend(reGet(path_i))
        else:
            files.append(path_i)
    return files

def rename_cp(file_path):
    if file_path.suffix in EXTS:
        toPath=re.sub('\..*\.','.',str(file_path))
        file_path.rename(toPath)


if __name__ == '__main__':
    args = sys.argv
    in_dir=Path(args[1])
    files=reGet(in_dir)
    for file in tqdm(files):
        rename_cp(file)

