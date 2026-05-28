import os
import re
import textwrap
import numpy as np

from PIL import (Image,ImageDraw,ImageFont,ImageFilter)
from moviepy.video.VideoClip import VideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.audio.io.AudioFileClip import AudioFileClip

WIDTH = 1080
HEIGHT = 1920
VIDEO_SIZE = (WIDTH,HEIGHT)
FPS = 30
def ease_out_cubic(x):
    return 1 - pow(1 - x,3)
def split_script(script):
    script = str(script).strip()
    if not script:
        return []
    script = script.replace("\n", " ")
    script = re.sub(r'\s+', ' ', script)
    words = script.split()
    chunks = []
    current = []
    for word in words:
        current.append(word)
        if len(current) >= 5:
            chunk = " ".join(current)
            if len(chunk) >= 15:
                chunks.append(chunk)
            current = []
    if current:
        chunks.append(
            " ".join(current)
        )
    return chunks
def make_frame(text,t,duration,bg_path,font_path,font_size,text_color):
    bg = Image.open(bg_path)
    bg = bg.resize(VIDEO_SIZE)
    zoom = 1 + (0.05 * (t / duration))
    zw = int(WIDTH * zoom)
    zh = int(HEIGHT * zoom)
    bg = bg.resize((zw,zh))
    left = (zw - WIDTH) // 2
    top = (zh - HEIGHT) // 2
    bg = bg.crop((left,top,left + WIDTH,top + HEIGHT))
    bg = bg.filter(ImageFilter.GaussianBlur(2))
    overlay = Image.new("RGBA",VIDEO_SIZE,(0,0,0,110))
    bg = bg.convert("RGBA")
    bg.alpha_composite(overlay)
    img = bg.convert("RGB")
    draw = ImageDraw.Draw(img)
    progress = min(t / 0.5,1)
    scale = 0.9 + (0.1 * ease_out_cubic(progress))
    current_size = int(font_size * scale)
    font = ImageFont.truetype(font_path,current_size)
    wrapped = textwrap.fill(text,width=16)
    bbox = draw.multiline_textbbox((0,0),wrapped,font=font,spacing=20)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (WIDTH - text_width) // 2
    y = (HEIGHT - text_height) // 2
    draw.multiline_text((x + 4,y + 4),wrapped,font=font,fill=(0,0,0),spacing=20,align="center")
    draw.multiline_text((x,y),wrapped,font=font,fill=text_color,spacing=20,align="center")
    return np.array(img)
def v2_engine(script,output="output.mp4",font_path="fonts/Orbitron-VariableFont_wght.ttf",font_size=85,text_color=(255,255,255),background_folder="backgrounds",voice_file=None):

    backgrounds = [
        os.path.join(background_folder,file)
        for file in os.listdir(background_folder)
        if file.endswith((".jpg",".png",".jpeg"))
    ]
    lines = split_script(script)
    audio = None
    if voice_file:
        audio = AudioFileClip(voice_file)
        total_audio_duration = audio.duration
    else:
        total_audio_duration = len(lines) * 3
    clips = []
    total_words = sum(len(line.split())for line in lines)
    for i, line in enumerate(lines):
        line_words = len(line.split())
        duration = (line_words / total_words) * total_audio_duration
        bg_path = backgrounds[i % len(backgrounds)]
        def frame_function(t,current_line=line,current_duration=duration,current_bg=bg_path):
            return make_frame(current_line,t,current_duration,current_bg,font_path,font_size,text_color)
        clip = VideoClip(frame_function,duration=duration)
        clips.append(clip)
    final = concatenate_videoclips(clips,method="compose")
    if audio:
        final = final.set_audio(audio)
    final.write_videofile(output,fps=FPS,codec="libx264",bitrate="8000k",preset="medium",logger=None)