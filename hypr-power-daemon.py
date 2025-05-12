#!/usr/bin/env python3

# SPDX-License-Identifier: MIT
# Copyright (c) 2025 v0x1m1r


# Toggle what gets changed to true/false [1 = enabled = 0 disabled]
TOGGLE_SHADOW = 1
TOGGLE_BLUR = 0

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

# the actual code
def update_config(plugged):
    with open(HYPR_CONFIG, "r") as f:
        lines = f.readlines()

    new_lines = []
    inside_blur = False
    inside_shadow = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("blur {"):
            inside_blur = True
            new_lines.append(line)
            continue
        elif stripped.startswith("shadow {"):
            inside_shadow = True
            new_lines.append(line)
            continue
        elif stripped.startswith("}"):
            inside_blur = False
            inside_shadow = False
            new_lines.append(line)
            continue

        if "enabled = " in stripped:
            if inside_blur and TOGGLE_BLUR:
                new_lines.append("        enabled = {}\n".format("true" if plugged else "false"))
                continue
            elif inside_shadow and TOGGLE_SHADOW:
                new_lines.append("        enabled = {}\n".format("true" if plugged else "false"))
                continue

        new_lines.append(line)

    with open(HYPR_CONFIG, "w") as f:
        f.writelines(new_lines)

    subprocess.run(["hyprctl", "reload"], check=False)
# checks for status, no need to really touch this
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
