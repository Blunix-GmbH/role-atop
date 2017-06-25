Ansible Role atop
====================

This role installs and configures atop, a process periodically saving a top like snapshot.

What is `atop`?
===============
`atop` which aggregates process statistics of all running processes and saves it to `/var/log/atop/${timestamp}.log`. The logs can later be viewed in a `top` style way. You can use it to find the exact process that "caused high load last sunday".

**Upstream:** [atoptool.nl](http://www.atoptool.nl/)

Example Play
============

```yaml
- hosts: foo
  vars:
    atop_log_interval: 120
  roles:
    - blunix.role-atop
```

`atop` Usage
============
You can generate reports via `atopsar` or browse through the log with the regular `atop`. In my opinion
the best way to use it is by browsing through the log file via the normal `atop` interface. To view todays logs use the following command while using `t` to jump forward and `T` to skip backward in time.
```
atop -r /var/log/atop/atop_$(date +%Y%m%d)
```

Use the following keys to navigate - see `man atop` for further instructions.
```
t - Skips forwards in time to next snapshot
T - When viewing the contents of a raw file, this key can be used to show the previous sample from the file.
P - Enter search string - http / postgres etc....
b - [Enter time] - When viewing the contents of a raw file, this key can be used to jump to a certain timestamp within the file (either forwards or backwards).
r - skip back to start of file with current filter applied
```

For a more advanced example refer to this link and scroll down to "scripts":
[atoptoopnl/extras.php](http://atoptool.nl/extras.php)
[atoptoolnl/download/atopscripts-1.1.tgz](http://atoptool.nl/download/atopscripts-1.1.tgz)


atopsar Usage
-------------
You can also use `atopsar` to generate reports (not that helpful in everyday work my opinion). With the flag `-A` in the following example all available reports are generated, starting from 13:00 (optional flag `-b`) till 13:35 (optional flag `-e`) reading today's raw file as written by the `atop` command (default): 
```
atopsar -A -b 13:00 -e 13:35
```

Also refer to [atoptool.nlsystemreports.php](http://www.atoptool.nl/systemreports.php)


Logfile format
--------------
You can view the logfile "raw" by using `atop -r /var/log/atop/atop_$(date +%Y%m%d) -P PRG`. [This thread on stackexchange.com](http://unix.stackexchange.com/questions/75764/can-i-extract-the-full-command-line-from-an-atop-1-23-data-file) shows some BASH magic to extract it without using the `atop` executable:
```
# Install zlib-flate
xxd -p < /var/log/atop/atop_$(date +%Y%m%d).log |
  fold -w4 |
  awk -v cmd='xxd -r -p | zlib-flate -uncompress | strings' '
    /789c/{if (x) close(cmd); x=1}; x {print | cmd}' |
  grep your-command
```

Quote: "The idea being to detect the zlib header (starting with 789c) and pass that to zlib-flate -uncompress. Not
guaranteed bulletproof and not the most efficient way to do it, but does the trick for me. Alternatives to
zlip-flate -uncompress (part of qpdf) include openssl zlib -d and pigz -zd."



License
=======

Apache

Author Information
==================

Service and support for orchestrated hosting environments, continuous integration/deployment/delivery and various Linux and open-source technology stacks are available from:

```
Blunix GmbH - Professional Linux Service
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: mailto:service@blunix.org
```
