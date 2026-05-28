import numpy as np
import soundfile as sf
from kokoro import KPipeline
import warnings
import os
import logging

logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def tts(txt,out = "audio.wav",voice = "af_heart",speed = 1):
    pl = KPipeline(
    lang_code='a',
    repo_id="hexgrad/Kokoro-82M"
)
    txt = str(txt)
    txt = txt.replace("\n",".")
    gen = pl(text=txt, voice=voice, speed=speed, split_pattern=r'[.!?]+')
    ac = []
    for i, (graphemes,phonemes,audio) in enumerate(gen):
        if audio is not None and len(audio) > 0:
            ac.append(audio)
    if not ac:
        return None
    fa = np.concatenate(ac)
    sf.write(out, fa, 24000)
    return out
def v_engine(msg_out, output):
    return tts(
        txt=msg_out,
        out=output,
        voice="af_heart",
        speed=1.0
    )