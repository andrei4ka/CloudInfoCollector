#!/bin/bash

set -x

df -ha
df -i

lsblk

blkid

lsof

for u in $(ls /sys/block); do udevadm info --query=property --export --name=${u}; done

