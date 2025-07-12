import os
import time
import subprocess

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
 ____              _  ___            ____ _     _ 
/ ___|  __ _ _   _| |/ (_)_ __ ___  / ___| |__ (_)
\___ \ / _` | | | | ' /| | '_ ` _ \| |   | '_ \| | 
 ___) | (_| | |_| | . \| | | | | | | |___| | | | |
|____/ \__,_|\__, |_|\_\_|_| |_| |_|\____|_| |_|_|
             |___/                                
          
    [S][A][Y][K][I][M][C][H][I][!][!]
    [+] Author   : cybermad
    [+] Version  : 1.0
    [*] Github   : https://github.com/madanokr001   
    [*] Telegram : https://t.me/cybermads   
""")

def php(port):
    print(f"""
 ____              _  ___            ____ _     _ 
/ ___|  __ _ _   _| |/ (_)_ __ ___  / ___| |__ (_)
\___ \ / _` | | | | ' /| | '_ ` _ \| |   | '_ \| |
 ___) | (_| | |_| | . \| | | | | | | |___| | | | |
|____/ \__,_|\__, |_|\_\_|_| |_| |_|\____|_| |_|_|
             |___/                                                                                           
          
[+] Starting php server...
[*] 127.0.01:{port}
""")
    os.system(f"php -S 127.0.0.1:{port} > /dev/null 2>&1 &")
    time.sleep(1)

def ngrok(port):
    print(f"""
 ____              _  ___            ____ _     _ 
/ ___|  __ _ _   _| |/ (_)_ __ ___  / ___| |__ (_)
\___ \ / _` | | | | ' /| | '_ ` _ \| |   | '_ \| |
 ___) | (_| | |_| | . \| | | | | | | |___| | | | |
|____/ \__,_|\__, |_|\_\_|_| |_| |_|\____|_| |_|_|
             |___/                                                               
          
[+] Starting ngrok server...
[*] http:{port}
""")
    os.system(f"ngrok http {port} > /dev/null 2>&1 &")
    time.sleep(5)

def fetch():
    try:
        result = subprocess.check_output("curl -s http://127.0.0.1:4040/api/tunnels", shell=True).decode()
        for line in result.split('"'):
            if line.startswith("https://"):
                return line
    except:
        return None

def main():
    banner()
    port = input("[+] Port? > ").strip() or "8000"

    php(port)
    ngrok(port)

    url = fetch()
    if url:
        print(f"""
 ____              _  ___            ____ _     _ 
/ ___|  __ _ _   _| |/ (_)_ __ ___  / ___| |__ (_)
\___ \ / _` | | | | ' /| | '_ ` _ \| |   | '_ \| |
 ___) | (_| | |_| | . \| | | | | | | |___| | | | |
|____/ \__,_|\__, |_|\_\_|_| |_| |_|\____|_| |_|_|
             |___/                                                                                           
          
[+] Starting ngrok server...
[*] Link: {url}
              """)
    else:
        print("[-] https://dashboard.ngrok.com/get-started/your-authtoken")
        print("[-] ngrok config add-authtoken YOURTOKENHERE")

    print("[*] Ctrl+C")

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        os.system("pkill php")
        os.system("pkill ngrok")
        print(":(")

if __name__ == "__main__":
    main()
