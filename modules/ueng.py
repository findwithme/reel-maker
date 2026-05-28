import os
import sys
import logging
from instagrapi import Client

logging.getLogger("instagrapi").setLevel(logging.ERROR)
logging.getLogger("moviepy").setLevel(logging.ERROR)
logging.getLogger("proglog").setLevel(logging.ERROR)

os.environ["IMAGEIO_LOGLEVEL"] = "error"

cl = Client()

t_path = os.path.abspath(os.path.join("tumb", "cover.jpg"))


class SilenceOutput:
    def __enter__(self):
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        sys.stdout = open(os.devnull, "w")
        sys.stderr = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = self._stdout
        sys.stderr = self._stderr


def snd(usr, password, caption, video_path):
    v_path = os.path.abspath(video_path)

    while True:
        try:
            cl.login(usr, password)
            break
        except:
            pass

    with SilenceOutput():
        cl.clip_upload(
            path=v_path,
            caption=caption,
            thumbnail=t_path
        )