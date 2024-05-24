import speech_recognition as sr

mic = sr.Recognizer()
def recognizeSpeech():
    with sr.Microphone() as source:
        
        mic.adjust_for_ambient_noise(source)
        print("Fale alguma coisa")
        audio = mic.listen(source)
        try:
            frase = mic.recognize_google(audio,language='pt-BR')
            return frase
    
        except sr.UnknownValueError:
            return "Nao entendi"

while False:
    with sr.Microphone() as source:
        
        mic.adjust_for_ambient_noise(source)
        print("Fale alguma coisa")
        audio = mic.listen(source)
        try:
            frase = mic.recognize_google(audio,language='pt-BR')
            print("Voce disse: " + frase)
    
        except sr.UnknownValueError:
            print("Nao entendi")