import subprocess
import time

user = subprocess.run('whoami', shell=True, capture_output=True, text=True).stdout.strip()
path = subprocess.run('pwd', shell=True, capture_output=True, text=True).stdout.strip()
file_path = '/etc/systemd/system/telegram_bot.service'


def is_admin():
    """Check if the current user has root privileges."""
    return user == 'root'


def setup(default_user):
    """Set up the Telegram bot as a systemd service."""
    try:
        config = f"""[Unit]
Description=Telegram Assist Bot
After=network.target

[Service]
Type=simple
User={default_user}
Environment=PYTHONPATH={path}
WorkingDirectory={path}
ExecStart={path}/venv/bin/python3 {path}/main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
"""

        with open(file_path, 'w') as file:
            file.write(config)

        subprocess.run('sudo systemctl daemon-reload', shell=True, check=True)
        subprocess.run('sudo systemctl enable telegram_bot.service', shell=True, check=True)

        print('Setup complete!')
        print('The computer will reboot in a few seconds and the bot will start automatically.')

        time.sleep(3)
        subprocess.run('sudo reboot', shell=True)

    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    if is_admin():
        default_user = input('Enter username (e.g., pi): ').strip()
        setup(default_user)
    else:
        print('Run script with sudo')