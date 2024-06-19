from flask import Flask, request, render_template
import openai
import json
import re
from dotenv import load_dotenv
import os
import threading  \

load_dotenv()
print(os.getenv('OPENAI_API_KEY'))
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

def rank_links_by_prompt(json_data, prompt):
    data = json_data
    ranked_links = []

    def process_link(link, materials):
        materials_list = [f"{material[:-1]}: {value:.1f}%" for material, value in materials.items()]
        material_text = ", ".join(materials_list)
        combined_text = f"{prompt} This clothing is made of {material_text}."

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Rate the material composition for the given purpose from -1.0 to 1.0:\n\nPurpose: {prompt}\nMaterials: {material_text}\n\nprovide only the decimal score (not even score written (very important))",
            max_tokens=10,
            temperature=0.9
        )
        response_text = response.choices[0].text.strip()
        response_text = re.sub(r'[^\d.-]', '', response_text) 
        print(response_text)

        try:
            suitability_score = float(response_text)
            ranked_links.append((link, suitability_score))
        except ValueError:
            print(f"Failed to convert score text '{response_text}' to float.")
            suitability_score = None

    threads = []
    for link, materials in data.items():
        thread = threading.Thread(target=process_link, args=(link, materials))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    ranked_links.sort(key=lambda x: x[1] if x[1] is not None else float('-inf'), reverse=True)
    return [link for link, _ in ranked_links[:5]]  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rank_links', methods=['POST'])
def rank_links():
    prompt = request.form['prompt']
    file_path = 'socks.json'

    try:
        with open(file_path, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        return "Error: File 'socks.json' not found."
    except json.JSONDecodeError as e:
        return f"Error decoding JSON in file 'socks.json': {e}"

    sorted_links = rank_links_by_prompt(json_data, prompt)
    return render_template('index.html', links=sorted_links)

if __name__ == '__main__':
    app.run(debug=True)


