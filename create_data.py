from openai import OpenAI

PROXY_ENDPOINT = "sk-KkfSNYD468LsWAALZtAObg"
TEAM_API_KEY = "3b575cb7-9ade-4037-977f-6075bd73f02d"

client = OpenAI(
   base_url=PROXY_ENDPOINT,
   api_key=TEAM_API_KEY
)


response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
   {
   "role": "user",
   "content": [
       {"type": "text", "text": "What’s in this image?"},
       {
       "type": "image_url",
       "image_url": {
           "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
       },
       },
   ],
   }
],
max_tokens=300,
)


print(response.choices[0])