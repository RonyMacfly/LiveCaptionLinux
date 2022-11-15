import pyaudio
import wave
import json
from os.path import dirname

def getText(text):
	res = json.loads(text)
	return res["text"]

from LiveCaptionLinux.voskLocal import Model, KaldiRecognizer, SetLogLevel
import subprocess

def start():
    pathModel = dirname(__file__) + "/vosk-model-en-us-daanzu-20200905-lgraph"
    voskModel = Model(pathModel)
    rec       = KaldiRecognizer(voskModel, 16000)
    
    CHUNK    = 16000
    FORMAT   = pyaudio.paInt16
    CHANNELS = 1
    RATE     = 16000
    RECORD_SECONDS = 60*60*24
    data = b""
    HOW_MANY_SECONDS_TO_RECOGNIZE = 3

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    for i in range(1, int(RATE / CHUNK * RECORD_SECONDS)+1):
        data += stream.read(CHUNK)
        
        rec.AcceptWaveform(data)
        print(getText(rec.FinalResult()))
        
        if((i % HOW_MANY_SECONDS_TO_RECOGNIZE) == 0): data = b""
        
    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
