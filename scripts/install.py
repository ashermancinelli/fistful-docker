#!/usr/bin/env python3
import sys, os
from pathlib import Path
sys.path.insert(0, Path(__file__).parent)
import sh
def run(cmd, *args, **_kwargs):
    kwargs = dict(_out=sys.stdout, _err=sys.stderr)
    kwargs.update(**_kwargs)
    cmd = cmd.bake(*args, **kwargs)
    print(cmd)
    return cmd()

try:
    d = sh.Command('docker')
    dc = sh.Command('docker-compose')
    run(d, '--version')
    run(dc, '--version')
except Exception:
    print('Needs docker and docker-compose.')
    sys.exit(1)

root = Path(__file__).parent.parent
data = root / 'fof-data'
if not data.exists():
    data.mkdir()
    run(sh.chmod, '777', data)

os.environ['SRCDS_PORT'] = '27015'
os.environ['SRCDS_TOKEN'] = '0'
run(dc, 'up')
