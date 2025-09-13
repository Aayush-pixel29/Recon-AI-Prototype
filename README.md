Recon AI: Rapid Disaster Damage Assessment

Project Description
Recon AI is an AI-powered platform designed to provide real-time, actionable intelligence to first responders and aid organizations following a natural disaster. Our solution addresses the critical problem of slow and dangerous manual damage assessments by providing a rapid, data-driven overview of a disaster zone.

For the people affected, especially those in remote areas, this technology ensures that aid is properly prioritized and deployed, ultimately saving lives and minimizing suffering.

Core Technology: Powered by OpenAI
Our solution is built on a modular and powerful AI architecture that integrates several of OpenAI's APIs in a unique workflow:

GPT-4 Vision: The core of our system. It compares pre- and post-disaster images from satellites or drones to automatically identify and describe structural damage.

DALL·E 3: A creative solution for data gaps. When a high-quality "before" image is unavailable, DALL·E 3 generates a plausible representation based on a text description, ensuring the assessment can still be completed.

GPT-4: This model acts as the intelligence layer, taking the raw visual data from GPT-4 Vision and translating it into concise, actionable text reports for rescue teams, complete with prioritized action items.

How to Run the Demo Locally
This demo is built as a single-file Flask application to make it easy to set up and run.

Prerequisites
Python 3.8+

An OpenAI API Key (you will need to replace the placeholder in app.py).

Step-by-Step Guide
Clone the Repository:

git clone [repository_url]
cd Recon-AI-Prototype

Set up the Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Dependencies:

pip install -r requirements.txt

Update Your API Key:

Open the app.py file.

Find the openai.api_key line and replace the placeholder with your actual key: openai.api_key = "YOUR_OPENAI_API_KEY"

Run the Application:

python app.py

View the Demo:

Open your web browser and navigate to http://127.0.0.1:5000.

Future Roadmap
This prototype is the first step toward a fully-featured, open-source platform. Our future plans include:

Scaling Data Ingestion: Expanding to handle multiple data sources and a larger volume of imagery.

Integrating Real-time Feeds: Connecting with live satellite or drone feeds for instant post-disaster analysis.

Community Contribution: Open-sourcing the project to allow developers and researchers to contribute to the codebase and mission.

License: MIT License
