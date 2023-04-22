from flask import Flask, render_template, request
import requests

app = Flask(__name__)

PROJECT_ID = "PROJECT-ID"
API_KEY = "API KEY"
BASE_URL = f"https://firestore.googleapis.com/v1/projects/projetexe-db2ce/databases/(default)/documents"


def get_firestore_data():
    doc_url = f"{BASE_URL}/google-map/Maps?key={API_KEY}"
    response = requests.get(doc_url)

    if response.status_code == 200:
        doc_data = response.json()
        return doc_data['fields']
    else:
        print("Error getting document:", response.text)
        return None


@app.route('/', methods=['GET'])
def home():
    doc_data = get_firestore_data()
    if doc_data:
        google_links = {}
        for i in range(1, 9):
            map_key = f"map{i}"
            if map_key in doc_data:
                google_links[map_key] = doc_data[map_key]['stringValue']
        return render_template('home.html', google_links=google_links)
    else:
        return "Error retrieving data from Firestore", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
