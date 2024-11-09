from pathlib import Path
from openai import OpenAI

TEAM_API_KEY = "sk-KkfSNYD468LsWAALZtAObg"
PROXY_ENDPOINT = "https://nova-litellm-proxy.onrender.com"

def example_tts():
    """
    Examples of text-to-speech from the proxy
    """
    client = OpenAI(
        api_key=TEAM_API_KEY, # set this!!!
        base_url=PROXY_ENDPOINT # and this!!!
    )

    myFile = open("./TextFiles/input.txt","r")
    content = myFile.read()
    
    speech_file_path = Path(__file__).parent / "./AudioFiles/output.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
    input=content
    )

    response.stream_to_file(speech_file_path)

if __name__ == "__main__":
    example_tts()
