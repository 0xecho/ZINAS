import speech_recognition as sr

from os import path,system
from voice import voicedata

def analyse_from_file(file="out.wav"):
    if file[:-3] == "amr":
        os.system('ffmpeg -y -i '+file+' -ar 22050 out.wav')


    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), file)

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
    try:
        d=r.recognize_sphinx(audio)
        print(d)
        for i in voicedata:
            if d in voicedata[i]:
                return i
    except sr.UnknownValueError:
        print("ALGEBAGNM,EBAKWO ENDEGENA YINAGERU")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    return "not found"
