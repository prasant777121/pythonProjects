while True:
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak anything:")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('you said:{}'.format(text))
        except:
            print("sorry could not reconize your voice")



    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(r.recognize_google(audio))