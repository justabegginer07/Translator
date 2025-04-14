import numpy
import whisper
import sounddevice as sd
import soundfile as sf

model=whisper.load_model('turbo')

def speech_to_text(audio_path):
    result=model.transcribe(audio_path)
    return result


print(speech_to_text('harvard.wav'))






