from pathlib import Path
import cv2
import numpy as np
import sys
from tqdm import tqdm

#画像を結合する
#python conect.py res
#でres内のディレクトリごとに同じ名前の画像を結合．
#サイズが違うかったら無視

def path_sort(path_list):
    path_str=[]
    for path in path_list:
        if path.is_dir():
            path_str.append(str(path))
    path_str.sort()
    new_path_list=[]
    for path in path_str:
        new_path_list.append(Path(path))
    return new_path_list

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

def delete_dir(path):
    file_list=list(path.iterdir())
    for file in file_list:
        file.unlink()
    path.rmdir()
    return None

def reshape(imgs,row=3):
    l=len(imgs)
    margin=imgs[0]*0
    new_imgs=[]
    k=0
    for i in range(-(-l//row)):
        row_imgs=[]
        for j in range(row):
            if k < l:
                row_imgs.append(imgs[k])
                k=k+1
            else:
                row_imgs.append(margin)
        new_imgs.append(row_imgs)

    return new_imgs




if __name__ == '__main__':
    args = sys.argv
    name=args[1]
    res_dir='res'
    path=Path(name)
    res=path/res_dir
    if res.exists():
        delete_dir(res)

    dir_list=list(path.iterdir())
    dir_list=path_sort(dir_list)
    file_list=list(dir_list[0].iterdir())

    res.mkdir(exist_ok=True) 
    for file in tqdm(file_list):
        imgs=[]
        flag=False
        img=cv2.imread(str(file))
        h,w,c=img.shape
        #imgs.append(img[:h,:w//2])
        file_name=file.name
        for dir in dir_list:
            dir_name=dir/file_name
            img=cv2.imread(str(dir_name))

            if type(img)==type(None):
                print(dir_name)
                flag=True
                break
            img=cv2.resize(img,dsize=(w,h))
            imgs.append(img)
        if flag:
            continue
        img_name=str(res/file_name)
        tile_num=3
        if len(imgs)==2 or len(imgs)==4:
            tile_num=2
        tile_num=7
        imgs=reshape(imgs,tile_num)
        try:
            conect= concat_tile(imgs)
            cv2.imwrite(img_name,conect)
        except:
            print(file)
    print(dir_list)
