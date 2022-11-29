from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")
speak.Speak("hello guys whats up yeh i know there cyling ")


