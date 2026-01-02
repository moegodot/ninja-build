
import os
import sys
import platform
import copy

ninja_root_dir = os.path.abspath(os.path.dirname(__file__))

def get_ninja():
    ninja = None
    plat = platform.machine().lower()
    is_x64 = plat.startswith("amd") or plat.startswith("x86") or plat.startswith("x64")

    if sys.platform.lower().startswith("win"):
        if is_x64:
            ninja = f"{ninja_root_dir}/win/"
        else:
            ninja = f"{ninja_root_dir}/win-arm64/"
    elif sys.platform.lower().startswith("linux"):
        if is_x64:
            ninja = f"{ninja_root_dir}/linux/"
        else:
            ninja = f"{ninja_root_dir}/linux-aarch64/"
    elif sys.platform.lower().startswith("darwin"):
        if is_x64:
            return None
        else:
            ninja = f"{ninja_root_dir}/mac/"
    else:
        return None
    
    return ninja

