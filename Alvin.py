from ai import AI
import pyjokes

alvin = AI()

def joke():
  funnyJoke = pyjokes.get_joke()
  print(funnyJoke)
  alvin.speak(funnyJoke)
  
command = ""

while True and command is not "goodbye":
  command = alvin.listen()
  print("command was:", command)
  
  if command == "tell me a joke":
    joke()

alvin.speak("Goodbye")