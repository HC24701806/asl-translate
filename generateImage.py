from pathlib import Path
from PIL import Image
from openai import OpenAI
import requests
import time

TEAM_API_KEY = "sk-KkfSNYD468LsWAALZtAObg"
PROXY_ENDPOINT = "https://nova-litellm-proxy.onrender.com"

def example_image_generation():
    """ 
    Examples of image generation from the proxy
    """

    client = OpenAI(
        api_key=TEAM_API_KEY,
        base_url=PROXY_ENDPOINT
    )

    file = open("./TextFiles/output.txt","r")
    initialInput = file.read()
    input = initialInput.split()
    output = [0]*len(input)
    count = 0

    for word in input:
        output[count] = client.images.generate(
            prompt="Generate basic sketch of American Sign Language Symbol for word:" + word,
            model="dall-e-3",
        )
        count = count + 1

    n = 0
    for image in output:
        print(image)
        url = image.data[0].url
        path = "imageFiles/example_image_generation" + str(n) + ".png"
        open(path, "wb").write(requests.get(url).content)
        img = Image.open(path)
        time.sleep(1)
        img.show()
        n = n + 1

if __name__ == "__main__":
    example_image_generation()