from openai import OpenAI
import os
import base64

TEAM_API_KEY = "sk-KkfSNYD468LsWAALZtAObg"
PROXY_ENDPOINT = "https://nova-litellm-proxy.onrender.com"

client = OpenAI(
   base_url=PROXY_ENDPOINT,
   api_key=TEAM_API_KEY
)


def genText():
    THIS_MODEL = "gpt-4o-mini"
    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Getting the base64 string
    base64_image = encode_image("ImageInputs/photo.jpg")

    # Send the request to the API
    response = client.chat.completions.create(
            model=THIS_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": [
                        {"type": "text",
                        "text": "Using american sign language symbols, identify the american sign language symbol in the image in ONE word. If you cannot recognize an american sign language symbol then just print a blank space."
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type":"text",
                            "text": "What is in this image?"
                        },
                        {
                            "type": "image_url",
                            "image_url": 
                                {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                        }
                    ]
                }
            ],
            max_tokens=300
        )
    print(f"response: {response}")
    #print(response);
    # Extract the description
    description = response.choices[0].message.content
    print(description)
    #print(f"Desription: {description}")