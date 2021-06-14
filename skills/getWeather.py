import pyjokes
from ai import AI

alvin = AI()

def joke():
  funnyJoke = pyjokes.get_joke()
  print(funnyJoke)
  alvin.speak(funnyJoke)