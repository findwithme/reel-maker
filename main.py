from modules import msg
from modules import v_engine
from modules import v2_engine
from modules import snd

import re
import json
import os

FILE = "users.json"
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        users = json.load(f)
else:
    users = []

os.system("cls")
print("\033[92m+-----------------------------------------------+")
print("|                  \033[1;95mREEL-MAKER\033[92m                   |")
print("+-----------------------------------------------+")
print("|                                               |")
print("+-----------------------------------------------+")
f_msg = input("\033[4;2H\033[33mENTER THE TOPIC : ")

folder = re.sub(r'[^A-Za-z0-9]','_',f_msg)
base_path = f"output/{folder}"
os.makedirs(base_path,exist_ok=True)
audio_path = (f"{base_path}/{folder}.wav")
video_path = (f"{base_path}/{folder}.mp4")
os.system("cls")
print("\033[92m+-----------------------------------------------+")
print(f"|             \033[1;95mREEL-MAKER\033[94m({f_msg})\033[92m               ")
print("\033[2;49H|")
print("+-----------------------------------------------+")
print("|                                               |")
print("|                                               |")
print("|                                               |")
print("|                                               |")
print("|                                               |")
print("|                                               |")
print("+-----------------------------------------------+")
msg_out = msg(f_msg)
script = msg_out["script"]
caption = msg_out["caption"]

script = re.sub(r'[^A-Za-z0-9\u0C00-\u0C7F\s]','',script)
print("\033[94m\033[4;2H[+] VOICE GENERATING...")
v_engine(
    script,
    audio_path
)
print("\033[1;94m\033[5;2H[+] VOICE GENERATION COMPLETE...")
print("\033[1;94m\033[6;2H[+] VIDEO GENRATION STRATED...")

v2_engine(
    script=script,
    output=video_path,
    font_path="fonts/Orbitron-VariableFont_wght.ttf",
    background_folder="backgrounds",
    voice_file=audio_path
)
print("\033[1;94m\033[7;2H[+] VIDEO GENERATION COMPLETE...")
data = users[0]
print(f"\033[1;94m\033[8;2H[+] UPLOADING ON INSTAGRAM [{data['user']}]")
snd(data["user"],data["pass"],caption,video_path)
print(f"\033[1;94m\033[9;2H[+]VIDEO UPLOADED AT [{data['user']}]")
