import pyttsx3
import speech_recognition as sr

class AI():
  __name = ""
  __skills = []
  
  def __init__(self, name=None):
    self.engine = pyttsx3.init()
    self.r = sr.Recognizer()
    self.m = sr.Microphone()
    
    if name is not None:
      self.__name = name
    
    print("Listening...")
    with self.m as source:
      self.r.adjust_for_ambient_noise(source)
      
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, value):
    sentence = f"Hello, my name is {self.__name}"
    self.__name = value
    self.engine.say(sentence)
    self.engine.runAndWait()
  
  
  def speak(self, sentence):
    self.engine.say(sentence)
    self.engine.runAndWait()
   
   
  def listen(self):
    print("Say something")
    with self.m as source:
      audio = self.r.listen(source)
    
    try:
      phrase = self.r.recognize_google(audio, show_all=False, language="en_USA")
      sentence = f"Have got it, you said {phrase}"
      self.engine.say(sentence)
      self.engine.runAndWait()
    except e as error:
      print(e)
      sentence = "Sorry i didn't catch that. Try again."
      self.engine.say(sentence)
      self.engine.runAndWait()
    return phrase