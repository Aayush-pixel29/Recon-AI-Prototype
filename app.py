import os
import io
import base64
import requests
from flask import Flask, request, render_template, jsonify, send_from_directory
from PIL import Image
from openai import OpenAI

# Initialize Flask App
app = Flask(__name__)

# Mock data for demonstration
MOCK_API_RESPONSE = """
Based on the visual comparison, the following damage has been identified:

- **Urgent (High Priority):** Complete collapse of one residential structure at approximately [52.1234, -1.5678].
- **Significant (Medium Priority):** At least two buildings have severe roof damage and debris is scattered in the surrounding area.
- **Moderate (Low Priority):** General debris and downed trees are visible throughout the affected zone.

A human-in-the-loop review is recommended for all high-priority areas before deployment.
"""

# Replace with your OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def process_images_with_vision(image1_base64, image2_base64):
    """
    Simulates calling the OpenAI Vision API to compare two images.
    In a real-world scenario, this would send the images to the API.
    For this demo, we use a mock response.
    """
    # Replace this mock logic with your actual API call
    if openai_api_key == "YOUR_OPENAI_API_KEY":
        return {"response": MOCK_API_RESPONSE, "status": "mocked"}
    else:
        # Correctly format the messages with images
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "I need to perform a before and after damage assessment. The first image shows a residential area before a disaster. The second image shows the same area after. Please identify and describe any structural damage to the buildings or infrastructure."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image1_base64}"
                        }
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image2_base64}"
                        }
                    }
                ]
            }
        ]

        # Call the OpenAI API
        try:
            response = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=messages,
                max_tokens=300
            )
            return {"response": response.choices[0].message.content, "status": "live"}
        except Exception as e:
            return {"response": f"Error calling OpenAI API: {e}", "status": "error"}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'before_image' not in request.files or 'after_image' not in request.files:
            return jsonify({'error': 'Missing image files'}), 400

        before_image = request.files['before_image']
        after_image = request.files['after_image']

        before_image_base64 = base64.b64encode(before_image.read()).decode('utf-8')
        after_image_base64 = base64.b64encode(after_image.read()).decode('utf-8')

        # Process the images with our simulated AI
        api_response = process_images_with_vision(before_image_base64, after_image_base64)
        
        # In a real app, you would process this further with DALL-E or GPT-4,
        # but for this demo, we'll just return the vision model's output.

        return jsonify({'result': api_response['response'], 'status': api_response['status']})
    
    return render_template('index.html')

@app.route('/assets/<path:filename>')
def serve_static(filename):
    """Serve static files from the assets directory."""
    return send_from_directory('assets', filename)

if __name__ == '__main__':
    app.run(debug=True)
