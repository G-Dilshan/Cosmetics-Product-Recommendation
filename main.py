import base64
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
import json
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils import user_prompt

# Define the system message to set the assistant's behavior
system_message = SystemMessagePromptTemplate.from_template("""
You are a skincare expert assistant. Given a user's skin/facial concerns, recommend most appropriate skincare products.
""")

# Create the chat prompt template
prompt = ChatPromptTemplate.from_messages([system_message, user_prompt.human_message])

load_dotenv()

client = OpenAI()

app = Flask(__name__)
CORS(app)

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Server is running"})

@app.route('/product_recommend', methods=['POST'])
def product_recommend():
    try:
        # Get JSON data from request
        data = request.get_json()

        if not data or 'image_path' not in data:
            return jsonify({"error": "Missing 'image_path' in request body"}), 400

        image_path = data['image_path']

        # Check if file exists
        if not os.path.exists(image_path):
            return jsonify({"error": f"Image file not found: {image_path}"}), 404

        encoded_image = encode_image(image_path)

        response = client.responses.create(
            model="gpt-4.1",
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text",
                         "text": user_prompt.vision_prompt},
                        {
                            "type": "input_image",
                            "image_url": f"data:image/jpeg;base64,{encoded_image}",
                        },
                    ],
                }
            ],
        )

        concern_output = response.output_text

        llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
        chain = prompt | llm | StrOutputParser()

        result = chain.invoke({"concerns": concern_output})

        # return result
        return jsonify({"result": result,
                        "concerns": concern_output}), 200

    except AttributeError as e:
        return jsonify({"error": f"AttributeError - OpenAI client issue: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.route('/product_recommend_upload', methods=['POST'])
def product_recommend_upload():
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # Save uploaded file temporarily
        temp_path = f"temp_{file.filename}"
        file.save(temp_path)

        try:
            encoded_image = encode_image(temp_path)

            response = client.responses.create(
                model="gpt-4.1",
                input=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_text",
                             "text": user_prompt.vision_prompt},
                            {
                                "type": "input_image",
                                "image_url": f"data:image/jpeg;base64,{encoded_image}",
                            },
                        ],
                    }
                ],
            )

            concern_output = response.output_text

            llm = ChatOpenAI(
                model="gpt-4o",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
            )
            chain = prompt | llm | StrOutputParser()

            result = chain.invoke({"concerns": concern_output})

            # return result
            return jsonify({"result": result,
                        "concerns": concern_output}), 200

        finally:
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)

    except Exception as e:
        return jsonify({"error": f"Error processing upload: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)