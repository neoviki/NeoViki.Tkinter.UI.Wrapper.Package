#!/bin/bash
for d in examples/* ; do
    cd $d
    ./run.py2.sh
    cd ../../
done
