from pathlib import Path
from tqdm import tqdm
import sys
import random
rate=0.2

if __name__ == '__main__':
    args = sys.argv
    in_dir=Path(args[1])
    out_dir=Path(args[2])
    out_dir.mkdir(exist_ok=True)
    dirs=list(in_dir.iterdir())
    for sub_dir in tqdm(dirs):
        save_dir=(out_dir/sub_dir.name)
        save_dir.mkdir(exist_ok=True)

        imgs=list(sub_dir.iterdir())
        get_num=max(1,int(len(imgs)*rate))

        mv_imgs=random.sample(imgs,get_num)
        for img in mv_imgs:
            img.rename(str(save_dir/img.name))


