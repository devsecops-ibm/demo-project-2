#!/bin/bash
MYDIR="/Users/jaydenaung/git/demo/demo-project-2/aws-python"
if [ ! -f $MYDIR/logs.txt ]; then
   cd $MYDIR
   mkdir contents
   cd contents
   wget http://jaydenstaticwebsite.s3-website-ap-southeast-1.amazonaws.com/logs.txt
else
  break
fi