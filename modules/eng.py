import ollama
import re
from ollama import Client
client = Client(timeout=90.0)
def sct(usr, sys):
    try:
        res = client.chat(
            model='llama3',
            messages=[
                {'role': 'system', 'content': sys},
                {'role': 'user', 'content': usr}
            ]
        )
        return res.get('message', {}).get('content', '')
    except Exception as e:
        print(f"Error in model connection generating: {e}")
        return None
def script(req):
    sys = """
    You are an expert Instagram Reel scriptwriter. You write highly informative, rapid-fire scripts entirely in clean, professional English.

    CRITICAL DISCIPLINE RULES:
    ZERO CHITCHAT. Do NOT say Hello, Sure, Here is, This script is, or any greeting lines.
    Start IMMEDIATELY with the first spoken word. End IMMEDIATELY with the last spoken word.
    No titles, headers, scene markers, brackets, or markdown blocks.
    Do NOT include bullet points, numbering, list characters, dashes, or symbols of any kind.
    Speak in a continuous, rapid-fire, direct tone. Connect the details seamlessly using quick transitions like First, Next, The main advantage, The downside is.
    """
    usr = f"""
    Create a highly informative, rapid-fire voice-over script in English for an INSTAGRAM REEL about: "{req}"
    Target these exact aspects cleanly, one after the other in a fast-paced continuous conversational flow:
    Cover what it is and how it works.
    Cover a real world use case.
    Cover the biggest advantage.
    Cover the biggest disadvantage.
    Cover how beginners can start right now.
    Cover its future scope.
    STRICT FORMAT TEMPLATE:
    Output ONLY the raw spoken text merged into a continuous 30 to 45 second script paragraph. Do not write bullet characters, numbers, or section titles. Just type the speech directly.
    """
    vs = sct(usr, sys)
    if vs:
        vs = vs.strip()
        vs = re.sub(r'^```[a-zA-Z]*', '', vs, flags=re.MULTILINE)
        vs = re.sub(r'```$', '', vs, flags=re.MULTILINE)
        vs = re.sub(r'^[\s\-\•\*\\>#]+', '', vs, flags=re.MULTILINE)
        vs = re.sub(r'^\d+\s*[\.\)\-]?\s*', '', vs, flags=re.MULTILINE)
        vs = re.sub(r'[\*\#\[\]\(\)]', '', vs)
        patterns = [
            r'^(hello\s*,?\s*)?here\s+is\s+the\s+script.*', 
            r'^this\s+script\s+is\s+for\s+.*',
            r'^sure\s*,?\s*here\s+is\s+.*',
            r'^here\s+are\s+the\s+scripts.*',
            r'^welcome\s+back.*',
            r'^instagram\s+reel\s+script.*',
            r'^here\s+are\s+the\s+points.*'            
        ]
        for pat in patterns:
            vs = re.sub(pat, '', vs, flags=re.IGNORECASE | re.MULTILINE)
        return vs.strip()
    else:
        return "Error in msg passing"
def caption(req):
    sys = """
    You are an expert Instagram caption writer.
    Write highly engaging Instagram Reel captions in clean English.
    RULES:
    No greetings.
    No markdown.
    No quotation marks.
    Keep it short and viral.
    Use emojis naturally.
    Add a strong CTA.
    Add relevant hashtags at the end.
    """
    usr = f"""
    Create an Instagram Reel caption for: "{req}"
    Make it engaging, modern, and social-media friendly.
    """
    cap = sct(usr, sys)
    if cap:
        cap = cap.strip()
        cap = re.sub(r'^```[a-zA-Z]*', '', cap, flags=re.MULTILINE)
        cap = re.sub(r'```$', '', cap, flags=re.MULTILINE)
        cap = re.sub(r'[\*\[\]\(\)]', '', cap)
        patterns = [
            r'^here\s+is\s+the\s+caption.*',
            r'^instagram\s+caption.*',
            r'^caption\s*:',
            r'^sure\s*,?\s*'
        ]
        for pat in patterns:
            cap = re.sub(pat,'',cap,flags=re.IGNORECASE | re.MULTILINE)
        return cap.strip()
    return "Follow for more 🚀"
def msg(req):
    s = script(req)
    c = caption(req)
    return {
        "script": s,
        "caption": c
    }