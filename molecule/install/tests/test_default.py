import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    assert host.package('atop').is_installed


def test_etc_default_atop(host):
    f = host.file('/etc/default/atop')

    assert f.exists
    assert f.contains('INTERVAL="600"')
    assert f.contains('LOGPATH="/var/log/atop"')
    assert f.contains('OUTFILE="$LOGPATH/daily.log"')


def test_service(host):
    s = host.service('atop')

    assert s.is_enabled
    assert s.is_running
