
import os
import sys
import platform
import copy

ninja_root_dir = os.path.abspath(os.path.dirname(__file__))

def internal_add_ninja(envs = None):

    plat = platform.machine().lower()
    is_x64 = plat.startswith("amd") or plat.startswith("x86") or plat.startswith("x64")

    if envs is None:
        envs = copy.deepcopy(os.environ)

    if sys.platform.lower().startswith("win"):
        if is_x64:
            envs["PATH"] = f"{ninja_root_dir}/win/;{envs["PATH"]}"
        else:
            envs["PATH"] = f"{ninja_root_dir}/win-arm64/;{envs["PATH"]}"
    elif sys.platform.lower().startswith("linux"):
        if is_x64:
            envs["PATH"] = f"{ninja_root_dir}/linux/:{envs["PATH"]}"
        else:
            envs["PATH"] = f"{ninja_root_dir}/linux-aarch64/:{envs["PATH"]}"
    elif sys.platform.lower().startswith("darwin"):
        if is_x64:
            return None
        else:
            envs["PATH"] = f"{ninja_root_dir}/mac/:{envs["PATH"]}"
    else:
        return None
    
    return envs

def add_ninja(envs = None):
    result = internal_add_ninja(envs)

    if result is not None:
        print(f"add ninja to PATH:{result}")
    else:
        print("failed to apply ninja")
        raise RuntimeError("failed to apply ninja")
