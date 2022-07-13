#!/bin/bash

aws s3api list-objects --bucket jaydenstaticwebsite --query 'Contents[].{Key: Key, Size: Size}' --output text