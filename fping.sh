#!/usr/bin/env bash
echo "127.0.0.1" > fping_hosts
for ping in $(cat fping_prefixes);
  do sudo fping -c 1 -r 0 -i 1 -a -g "$ping" >> fping_hosts 2>&1
done