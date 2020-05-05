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
import json
import threading
"""
This demo file shows you how to use the new_message_callback to interact with
the recorded audio after a keyword is spoken. It uses the speech recognition
library in order to convert the recorded audio into text.

Information on installing the speech recognition library can be found at:
https://pypi.python.org/pypi/SpeechRecognition/
"""


interrupted = False
def recognize_text(fname):

    thread1 = threading.Thread(target = snowboydecoder.play_audio_file,args=('audio/8.wav',))
    thread1.start()
    
    r_baidu = asr.baidu_asr(fname)
    sentence = json.loads(r_baidu)['result'][0]
    print(sentence)
    #get result from JD.
    r_jd = json.loads(jd.classify_T(sentence))['result']
    #status code
    status = r_jd['status']
    #threand1: play the welcome vedio
    thread1.join()
    snowboydecoder.RCD = True
    try:
        garbage_info = r_jd['garbage_info']
        cate_name = garbage_info[0]['cate_name']
        ps = garbage_info[0]['ps']
        #print (cate_name)
        if cate_name == '可回收物':
            snowboydecoder.play_audio_file('audio/2.wav')
        elif cate_name == '湿垃圾':
            snowboydecoder.play_audio_file('audio/3.wav')
        elif cate_name == '干垃圾':
            snowboydecoder.play_audio_file('audio/4.wav')
        elif cate_name == '有害垃圾':
            snowboydecoder.play_audio_file('audio/5.wav')
    except:
        snowboydecoder.play_audio_file('audio/7.wav')
        
def audioRecorderCallback(fname):
    print('Recognizing...\n')
    recognize_text(fname)
    os.remove(fname)
    
#def audioRecorderCallback2(fname):
#    print('Recognizing...\n')    
#    print(jd.classify_V(fname))
#    os.remove(fname)

#TODO - feedback
def detectedCallback():
    # play 'welcome' audio.
    snowboydecoder.play_audio_file('audio/1.wav')
    sys.stdout.flush()
    #sys.stdout.write("recording audio...\n")

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


