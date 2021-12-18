def install_module(module):
    import subprocess, os
    subprocess.call(["pip", "install", module], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
try:
    import rich,colored,requests
except:
    install_module('rich')
    install_module('colored')
    install_module('requests')
    import rich,colored,requests