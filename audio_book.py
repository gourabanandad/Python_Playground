from gtts import gTTS
import os

def create_audiobook(text_file, output_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
        
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f"File saved as {output_file}")
    
    
text_file = input("Enter the text file path: ")       # Input the path where the text file is. 
output_file = input("Enter the output file name in .mp3 format: ") # Enter the path of the folder you store the music

create_audiobook(text_file, output_file)
os.system(f"Start {output_file}")