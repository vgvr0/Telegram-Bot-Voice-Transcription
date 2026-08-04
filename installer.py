import subprocess
import sys


from utils.passToHash import toHash



# python -c "import secrets; print(secrets.token_hex(32))" ДЛЯ SECRET

"""
def setup(token, login, password):
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


    with open("config.py", "w", encoding="utf-8") as file:
        hashed_login = toHash(login)
        file.write(f"LOGIN = '{hashed_login}'\n")


    with open("config.py", "w", encoding="utf-8") as file:
        hashed_password = toHash(password)
        file.write(f"LOGIN = '{hashed_password}'\n")



    print("\nSetup complete!")
    print("Start the bot with:")
    print("  source venv/bin/activate")
    print("  python main.py")
    print("Or:")
    print(f"  {python} main.py")

"""
if __name__ == "__main__":
    #token = input("Enter token (from BotFather in Telegram): ").strip()
    #login = input('Enter login for admin panel: ')
    #password = input('Enter password for admin panel: ')

    #if not token or not login or not password:
        #print("Token is required.")
        #sys.exit(1)

    print("installer don't work! ")


    #setup(token, login, password)



