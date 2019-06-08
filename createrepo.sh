#!/bin/bash

function createrepo(){
    python createrepo.py $1
    cd ~/Documentos/proyectos
    mkdir $1
    cd $1
    git init
    touch README.md
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/diegoara96/$1.git
    git push -u origin master
    code .
}
