# ❤️🔋 HyprLoveYourBattery

A simple background script that helps your laptop battery last longer by **automatically disabling Hyprland visual effects** (like blur and shadows) when running on battery power — and turning them back on when plugged in.

---

## ✨ Features

- 📡 Monitors laptop AC power status in real time
- ⚡ Disables power-hungry visual effects when on battery
- ✅ Automatically updates `hyprland.conf`
- 🔁 Reloads Hyprland without restarting your session
- 🧘‍♂️ Runs silently in the background (no windows, no popups)

---

## 📦 Requirements

- **Python 3.x**
- **Hyprland**
- `hyprctl` must be available in your `PATH`

> Optional (for advanced users):
> - `inotify_simple` (to use an event-driven version instead of polling / requires modfication)

---

## 📁 File Structure
HyprLoveYourBattery/
├── hypr-power-daemon.py # Main script
├── LICENSE # MIT License
└── README.md # You're reading this!

## ⚙️ Installation

1. **Clone this repo**:
   ```bash
   git clone https://github.com/yourusername/HyprLoveYourBattery.git

2. Move the script to your Hyprland config:
   ```bash
   mkdir -p ~/.config/hypr/scripts
   cp HyprLoveYourBattery/hypr-power-daemon.py ~/.config/hypr/scripts/
   chmod +x ~/.config/hypr/scripts/hypr-power-daemon.py

3. Add to Hyprland autostart:
Edit ~/.config/hypr/hyprland.conf and add:
   ```bash
    exec-once = ~/.config/hypr/scripts/hypr-power-daemon.py

## 🧠 How It Works

    Reads from:
    /sys/class/power_supply/AC/online

        1 = Plugged In → Enables blur and shadow

        0 = On Battery → Disables them to save power

Modifies your ~/.config/hypr/hyprland.conf accordingly:

    blur {
        enabled = false  # toggled
    }
    shadow {
        enabled = false  # toggled
    }

Applies changes using:

    hyprctl reload

## 🧪 Optional Improvements

Want to make it even more power-efficient?

   * 💤 Event-driven version: Replace polling with inotify for zero CPU wakeups

   * ⏲️ Adjust poll interval: Increase the sleep time to 30s or 60s if using polling

   * 🔋 Integrate with tlp or power-profiles-daemon for smarter management

#  🛡️ License

This project is licensed under the MIT License — free to use, modify, and redistribute.
🤝 Contributing

Pull requests, issues, and suggestions welcome!
This project is intentionally minimal — feel free to build on it.
