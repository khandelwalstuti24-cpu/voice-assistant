import speech_recognition as sr
#Initialize recognizer
recognizer = sr.Recognizer()

#Load audio file
import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Order.wav')
with sr.AudioFile(path) as source:
    audio_data = recognizer.record(source)
    print("Transcribing")
    
    #Google Speech Recognition
    try:
        text = recognizer.recognize_google(audio_data)
        print("\nTranscription:")
        print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not\ understand the audio. ")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")    