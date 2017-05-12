import subprocess

import hexchat

__module_name__ = 'DeaDBeeF'
__module_version__ = '0.0.1'
__module_description__ = 'DeaDBeef currently playing script'


def now_playing(*dummy):
    proc = subprocess.check_output(['deadbeef',
                                    '--nowplaying', '"%a - %t 「%b」 %e/%l"'])
    hexchat.command('SAY np: ' + proc.decode('utf-8').strip('"'))
    return hexchat.EAT_ALL


def unload_callback(dummy):
    hexchat.prnt('RIP deadbeef wp script')

hexchat.hook_command('wp', now_playing, help='"/wp" to display currently playing deadbeef track')
hexchat.hook_unload(unload_callback)
hexchat.prnt('hexchat.wp.deadbeef.py loaded')
