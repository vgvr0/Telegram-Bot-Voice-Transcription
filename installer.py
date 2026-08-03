import subprocess
import sys


def setup(token: str) -> None:
    print("creating venv...")
    subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)

    pip = "venv/bin/pip"
    python = "venv/bin/python"

    print("installing requirements.txt...")
    subprocess.run([pip, "install", "-r", "requirements.txt"], check=True)

    print("installing ollama...")
    subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True, check=True)

    print("downloading llama3.2:3b model (this may take a while)...")
    subprocess.run(["ollama", "pull", "llama3.2:3b"], check=True)

    with open("config.py", "w", encoding="utf-8") as file:
        file.write(f"token = '{token}'\n")

    print("\nSetup complete!")
    print("Start the bot with:")
    print("  source venv/bin/activate")
    print("  python main.py")
    print("Or:")
    print(f"  {python} main.py")


if __name__ == "__main__":
    token = input("Enter token (from BotFather in Telegram): ").strip()
    if not token:
        print("Token is required.")
        sys.exit(1)

    setup(token)
