#!/bin/bash
chmod +x ./examples/button_1/run.sh
cp ./examples/button_1/run.sh run.sh
for d in examples/* ; do
    echo "copy run.sh $d/run.sh"
    cp run.sh $d/run.sh
done 
rm run.sh
rm src/NeoViki_UI_Tk.pyc 2> /dev/null 1> /dev/null
