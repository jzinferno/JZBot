#!/usr/bin/env bash

case "$1" in
  arch )
    uname -m
    ;;
  os )
    if [ -f '/etc/os-release' ]; then
      awk -F '=' '/PRETTY_NAME/ { print $2 }' /etc/os-release | tr -d \"
    else
      uname -sm
    fi
    ;;
  ip )
    echo $(curl -s 'http://ident.me' || printf '127.0.0.1')
    ;;
  uptime )
    boot=$(date -d"$(uptime -s)" +%s)
    now=$(date +%s)
    s=$((now - boot))

    d="$((s / 60 / 60 / 24)) days"
    h="$((s / 60 / 60 % 24)) hours"
    m="$((s / 60 % 60)) mins"

    ((${d/ *} == 1)) && d=${d/s}
    ((${h/ *} == 1)) && h=${h/s}
    ((${m/ *} == 1)) && m=${m/s}

    ((${d/ *} == 0)) && unset d
    ((${h/ *} == 0)) && unset h
    ((${m/ *} == 0)) && unset m

    uptime=${d:+$d, }${h:+$h, }$m
    uptime=${uptime%', '}
    echo ${uptime:-$s secs}
    ;;
  cpu )
    awk -F '\\s*: | @' '/model name|Hardware|Processor/ {print $2; exit(0)}' /proc/cpuinfo
    ;;
  gpu )
    lspci 2>/dev/null | awk -F '\\s*: | @' '{f=0} /Display|3D|VGA/ {print $2; f=1; exit(0)} END {if (f==0) exit(1)}' || echo 'Unknown'
    ;;
  neofetch )
    neofetch --stdout | grep ':'
    ;;
  * )
    true
    ;;
esac
