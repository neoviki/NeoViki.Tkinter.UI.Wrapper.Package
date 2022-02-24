#!/bin/bash
chmod +x ./examples/0001_filemanager/run.sh
cp ./examples/0001_filemanager/run.sh run.sh
cp ./examples/0001_filemanager/run_py3.sh run_py3.sh
for d in examples/* ; do
    echo "copy run.sh $d/run.sh"
    cp run.sh $d/run.sh
    cp run_py3.sh $d/run_py3.sh
done 
rm run.sh
rm run_py3.sh
rm src/NeoViki_UI_Tk.pyc 2> /dev/null 1> /dev/null
rm src/__pycache__ 2> /dev/null 1> /dev/null
