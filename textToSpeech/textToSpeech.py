from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    # Create a text-to-speech object
    tts = gTTS(text=text, lang=lang)

    # Save the audio file
    tts.save("output.mp3")

    # Play the audio file
    os.system("start output.mp3")  # For Windows
    # os.system("afplay output.mp3")  # For macOS
    # os.system("mpg123 output.mp3")  # For Linux (requires mpg123 to be installed)

if __name__ == "__main__":
    # Get input text from the command line
    input_text = input("Enter the text you want to convert to speech: ")

    # Convert text to speech
    text_to_speech(input_text)
