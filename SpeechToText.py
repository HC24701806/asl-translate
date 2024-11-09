from openai import OpenAI

TEAM_API_KEY = "sk-KkfSNYD468LsWAALZtAObg"
PROXY_ENDPOINT = "https://nova-litellm-proxy.onrender.com"


def example_audio_transcription():
    """ 
    Examples of audio transcription from the proxy
    """
    client = OpenAI(
        api_key=TEAM_API_KEY, # set this!!!
        base_url=PROXY_ENDPOINT # and this!!!
    )

    audio_file= open("./AudioFiles/input.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
    )
    f = open("./TextFiles/output.txt", "w")   # 'r' for reading and 'w' for writing
    f.write(transcription.text)    # Write inside file 
    f.close()

    print(transcription.text)


if __name__ == "__main__":
    example_audio_transcription()