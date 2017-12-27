#!/bin/bash
BRANCH=$1
echo 'start to sync remote branch:' $BRANCH

git fetch --all
git reset --hard origin/$BRANCH
supervisorctl restart flasks
echo 'update success to remote branch:' $BRANCH