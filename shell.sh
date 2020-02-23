#!/usr/bin/bash

function create() {
    # python test.py
    # echo $1
    python ./create.py $1 $2 $3 $4
    cd $3\\$4
    git init
    git remote add origin https://github.com/$1/$4.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
    read -p "Press Enter to Exit..."
}
create $1 $2 $3 $4