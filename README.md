# メモ

## copy.py
```python copy.py from_dir to_dir ```

でfrom_dir内の全てのEXTSのファイルをto_dirに移動できる．
ファイル名は相対パスの/を無くしたもの

## conect.py
```python conect.py dir```

でdir内の画像を結合できる．想定している構造は
```
dir
├── 0_resA
│   ├── img1.png
│   └── img2.png
├── 1_resB
│   ├── img1.png
│   └── img2.png
└── 2_resC
    ├── img1.png
    └── img2.png
```

このようなもので，resA,B,Cの順番で横に並んで結合された画像が出てくる．
出力先は```dir/res```.

## rename.py
```aaaa.jpg__.exe.png```などのめんどくさい構造のファイル名を最後の拡張子だけにしてくれる．この場合は```aaaa.png```
```python rename.py dir ```

## makereg.py
ディレクトリの何割かのファイルを構造を維持して（2層）移動させる
```python copy.py from_dir to_dir ```