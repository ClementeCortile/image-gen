import os
import requests
import json
from header.constants import ad_variables, API_ENDPOINT

# Function to generate image using DALL-E API
def generate_image(prompt, api_key, api_endpoint):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "image-alpha-001",
        "prompt": prompt,
        "num_images": 1,
        "size": "512x512",
        "response_format": "url",
    }

    response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        image_url = result["data"][0]["url"]
        return image_url
    else:
        raise Exception(f"Error generating image: {response.status_code} - {response.text}")


def main():
    # Get API key from environment variable
    API_KEY = os.environ["OPENAI_API_KEY"]

    # Compose the prompt based on the ad_variables dictionary
    prompt = f"{ad_variables['brand_name']} {ad_variables['product_type']} with {ad_variables['logo_description']} - {ad_variables['color']} {ad_variables['gender']} {ad_variables['catchphrase']} - {ad_variables['discount']}"

    # Generate image using the DALL-E API
    try:
        image_url = generate_image(prompt, API_KEY, API_ENDPOINT)
        print(f"Generated image URL: {image_url}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
