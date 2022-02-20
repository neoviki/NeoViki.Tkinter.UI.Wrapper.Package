#!/bin/bash
for d in examples/* ; do
    cd $d
    ./run.sh
    cd ../../
done 
