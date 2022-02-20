#!/bin/bash
chmod +x ./examples/0001_filemanager/run.sh
cp ./examples/0001_filemanager/run.sh run.sh
for d in examples/* ; do
    echo "copy run.sh $d/run.sh"
    cp run.sh $d/run.sh
done 
rm run.sh
rm src/NeoViki_UI_Tk.pyc 2> /dev/null 1> /dev/null
