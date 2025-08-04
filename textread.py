#Text reader 
from gtts import gTTS
file=open("demo.txt","r").read()
language="en"
speech=gTTS(text=str(file),lang=language,slow=False)
speech.save('hello.mp3')