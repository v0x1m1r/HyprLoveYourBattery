#!/usr/bin/env python3

# SPDX-License-Identifier: MIT
# Copyright (c) 2025 v0x1m1r

# imports
import time
import os
import subprocess

# Locations of the power status and hyprland config
POWER_PATH = "/sys/class/power_supply/AC/online"
HYPR_CONFIG = os.path.expanduser("~/.config/hypr/hyprland.conf")

# the actual code
def is_plugged_in(): # checks for status, no need to really touch this
    try:
        with open(POWER_PATH, "r") as f:
            return f.read().strip() == "1"
    except Exception:
        return False

# config updating, if you only need to toggle blur and shadows you should be fine with the code bellow
def update_config(plugged): 
    with open(HYPR_CONFIG, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if "blur {" in line:
            blur_block = True
        if "shadow {" in line:
            shadow_block = True

        if "blur {" in line or "shadow {" in line:
            new_lines.append(line)
            continue

        if "blur {" in line or "shadow {" in line:
            blur_block = False
            shadow_block = False

        if "enabled = " in line and "blur" in "".join(new_lines[-3:]):
            new_lines.append(f"        enabled = {'true' if plugged else 'false'}\n")
        elif "enabled = " in line and "shadow" in "".join(new_lines[-3:]):
            new_lines.append(f"        enabled = {'true' if plugged else 'false'}\n")
        else:
            new_lines.append(line)

    with open(HYPR_CONFIG, "w") as f:
        f.writelines(new_lines)

    # make hyprland reload
    subprocess.run(["hyprctl", "reload"], check=False)


def main():
    last_state = None
    while True:
        plugged = is_plugged_in()
        if plugged != last_state:
            print(f"Power state changed: {'Plugged In' if plugged else 'On Battery'}")
            update_config(plugged)
            last_state = plugged
        time.sleep(5)

if __name__ == "__main__":
    main()
