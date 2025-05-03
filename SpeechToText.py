import numpy
import whisper
import os
import pydub
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
                                
ffmpeg_path=os.path.abspath('/workspaces/Translator')
os.environ['PATH']=ffmpeg_path+os.pathsep+os.environ.get('PATH','')

model=whisper.load_model('base')

#def audio_recording(filename,duration=5,fs=44100):
def audio_recording(duration=5,fs=44100):
    print('recording....')
    audio=sd.rec(int(duration*fs),samplerate=fs,channels=2)
    #sf.write(filename,audio,fs)
    speech_to_text(audio)

def speech_to_text(audio_path):
    result=model.transcribe(audio_path)
    #print(result['text'])
    return result['text']

audio_recording()
#print(speech_to_text('harvard.wav'))






