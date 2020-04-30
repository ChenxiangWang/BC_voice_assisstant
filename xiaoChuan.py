"""
Main changes:
	1. Set a default model 'nihao.pmdl'
	2. DetectedCallBack would invoke a welcome
        3. AudioRecorderCallback, use baidu ASR-API.
        4. sensitivity chenged to 0.75
Modified from demo4.by Chenxiang Wang , 2020-4-25
"""

from wake_up import snowboydecoder as snowboydecoder
import sys
import signal
#import speech_recognition as sr
import os
import bd_api.asr as asr
import jd_api.jd as jd
import shutil
"""
This demo file shows you how to use the new_message_callback to interact with
the recorded audio after a keyword is spoken. It uses the speech recognition
library in order to convert the recorded audio into text.

Information on installing the speech recognition library can be found at:
https://pypi.python.org/pypi/SpeechRecognition/
"""


interrupted = False

#TODO - ARS
def audioRecorderCallback(fname):
    print('Recognizing...\n')
    rsp = asr.baidu_asr(fname)
    rst = rsp.split('[', 1)[1]
    rst = rst.split(']', 1)[0]
    print (rst)
    print (jd.classify_T(rst))
    
    #print(jd.classify_V(fname))
    os.remove(fname)

#TODO - feedback
def detectedCallback():
    sys.stdout.flush()
    snowboydecoder.play_audio_file()
    sys.stdout.write("recording audio...\n")

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

model = 'resources/nihao.pmdl'

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print ("Listening... Press Ctrl+C/Z to exit")

# main loop
detector.start(detected_callback=detectedCallback,
               audio_recorder_callback=audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()




