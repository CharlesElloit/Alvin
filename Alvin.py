from ai import AI
from skills.Joke import joke
from skills.getDate import getDate

alvin = AI()
 
command = ""
wakeWord = "alvin"

while True and command != "goodbye":
  command = alvin.listen()
  print("command was:", command)
  
  JOKES_STRS = ["tell me a joke", "tell me another joke", "another one"]
  for phrase in JOKES_STRS:
    if phrase in command:
      joke()
  
  TIME_STRS = ["what's the time", "what is the time", "the current time please"]
  for phrase in TIME_STRS:
    if phrase in command:
      getDate()

alvin.speak("Goodbye")