Ansible Role atop
====================

This role installs and configures atop, a process periodically saving a top like snapshot.

Example Play
============

```yaml
- hosts: foo
  vars:
    atop_log_interval: 120
  roles:
    - blunix.role-atop
```

License
-------

Apache

Author Information
------------------

Service and support for orchestrated hosting environments, continuous integration/deployment/delivery and various Linux and open-source technology stacks are available from:

```
Blunix GmbH - Professional Linux Service
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: mailto:service@blunix.org
```
