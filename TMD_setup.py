import subprocess
import json
import os
import shutil

def install_psreadline():
    # Install PSReadLine module
    subprocess.run(["powershell.exe", "-Command", "Install-Module -Name PSReadLine -Scope CurrentUser -Force -SkipPublisherCheck"])

def update_terminal_config():
    # Rename the existing configuration file if it exists
    old_config_path = os.path.expanduser("~/.terminal_settings.json")
    if os.path.exists(old_config_path):
        new_config_path = old_config_path.replace(".json", "_old.json")
        shutil.move(old_config_path, new_config_path)
        print(f"Existing configuration file renamed to: {new_config_path}")

    # Update Windows Terminal configuration
    config = {
        "$schema": "https://aka.ms/terminal-profiles-schema",
        "defaultProfile": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
        "profiles": {
            "list": [
                {
                    "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
                    "name": "TMD",
                    "commandline": "cmd.exe /K powershell.exe -NoExit -Command Set-ExecutionPolicy RemoteSigned -Scope Process -Force; Import-Module PSReadLine",
                    "icon": "ms-appx:///ProfileIcons/powershell.png",
                    "startingDirectory": "cwd",
                    "colorScheme": "MyCustomScheme"
                }
            ]
        },
        "schemes": [
            {
                "name": "MyCustomScheme",
                "background": "#1E1E1E",
                "black": "#0C0C0C",
                "blue": "#0037DA",
                "cyan": "#3A96DD",
                "foreground": "#CCCCCC",
                "green": "#13A10E",
                "purple": "#881798",
                "red": "#C50F1F",
                "white": "#CCCCCC",
                "yellow": "#C19C00",
                "brightBlack": "#767676",
                "brightBlue": "#3B78FF",
                "brightCyan": "#61D6D6",
                "brightGreen": "#16C60C",
                "brightPurple": "#B4009E",
                "brightRed": "#E74856",
                "brightWhite": "#F2F2F2",
                "brightYellow": "#F9F1A5"
            }
        ],
        "globals": {
            "commandline": {
                "startingDirectory": "%USERPROFILE%",
                "frame": "{{directory}}"
            }
        }
    }

    with open(os.path.expanduser("~/.terminal_settings.json"), "w") as f:
        json.dump(config, f)

    print("Terminal configuration updated.")

def main():
    install_psreadline()
    update_terminal_config()

if __name__ == "__main__":
    main()
