from flask import Flask, jsonify, render_template, request
import json
import os


app = Flask(__name__)


#Correct pathing to api_result
with open(os.path.join("data", "api_results.json")) as f:
    materials = json.load(f)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/api/materials')
def get_materials():
    query = request.args.get('q', '').lower().strip()

    if query:
        filtered = [
            m for m in materials
            if query in m.get('pretty_formula', '').lower() or
               query in m.get('material_id', '').lower() or
               query in (m.get('magnetic_ordering') or '').lower()
        ]
        return jsonify(filtered)
    return jsonify(materials)


#Routing to get the material info
@app.route('/material/<material_id>')
def details(material_id):
    return render_template('details.html')



#For flask to run routing.py
if __name__ == '__main__':
    app.run(debug=True)
