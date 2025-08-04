#Convert PDF to AUDIO
import PyPDF2
from gtts import gTTS
file=open("virtual Environment.pdf","rb")
reader=PyPDF2.PdfReader(file)
text=''
for page in reader.pages:
    page_text=page.extract_text()
if page_text:
    text+=page_text+'\n'
speech=gTTS(text,lang='en')
speech.save('output_audio.mp3') 
file.close()
print("Audio file 'output_audio.mp3' has been created successfully:")   