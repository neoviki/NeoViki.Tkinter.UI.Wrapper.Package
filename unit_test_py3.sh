#!/bin/bash
for d in examples/* ; do
    cd $d
    ./run_py3.sh
    cd ../../
done
