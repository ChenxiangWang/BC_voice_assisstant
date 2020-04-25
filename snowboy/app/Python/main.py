# encoding: utf-8
import snowboydecoder
import sys
import signal
import speech_recognition as sr
import os
import asr
import jd
"""
This demo file shows you how to use the new_message_callback to interact with
the recorded audio after a keyword is spoken. It uses the speech recognition
library in order to convert the recorded audio into text.

Information on installing the speech recognition library can be found at:
https://pypi.python.org/pypi/SpeechRecognition/
"""


interrupted = False



# TODO
def audioRecorderCallback(fname):
    print('Recognizing...\n')
    rsp = asr.baidu_asr(fname)
    rst = rsp.split('[', 1)[1]
    rst = rst.split(']', 1)[0]
    print (rst)
    print (jd.classify(rst))
    os.remove(fname)


#TODO  - feedback
def detectedCallback():
    snowboydecoder.play_audio_file()
    sys.stdout.write("recording audioo...\n")
  
    sys.stdout.flush()

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 0:
    print "Usage: python main.py"
    sys.exit(-1)

model = 'resources/nihao.pmdl'

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.38)
print "Listening... Press Ctrl+C to exit"

# main loop
detector.start(detected_callback=detectedCallback,
               audio_recorder_callback=audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()




