"""import pyttsx3
friend = pyttsx3.init()
friend.say("You are dashing smart . I love you. I miss you, and you are such a blessing to my world")
friend.runAndWait()"""


import pyttsx3
friend = pyttsx3.init()
speech = input ("Say Something: ")
friend.say(speech)
friend.runAndWait()

