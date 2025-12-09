from flask import Flask, request, jsonify, send_file
import json
import os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from your frontend

JSON_FILE = 'submissions.json'

def load_submissions():
    """Load submissions from JSON file"""
    if not os.path.exists(JSON_FILE):
        return []
    
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_submissions(submissions):
    """Save submissions to JSON file"""
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(submissions, f, indent=2, ensure_ascii=False)

@app.route('/api/submit', methods=['POST'])
def submit_form():
    """Handle form submission"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'company', 'email', 'phone']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Generate submission ID
        submission_id = f"MERAY-{datetime.now().strftime('%Y%m%d')}-{len(load_submissions()) + 1:04d}"
        
        # Create submission object
        submission = {
            'id': submission_id,
            'name': data['name'].strip(),
            'company': data['company'].strip(),
            'email': data['email'].strip(),
            'phone': data['phone'].strip(),
            'message': data.get('message', '').strip(),
            'timestamp': datetime.now().isoformat(),
            'status': 'new'
        }
        
        # Load existing submissions
        submissions = load_submissions()
        
        # Add new submission
        submissions.append(submission)
        
        # Save to file
        save_submissions(submissions)
        
        return jsonify({
            'success': True,
            'message': 'Submission received',
            'submission_id': submission_id
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/submissions', methods=['GET'])
def get_submissions():
    """Get all submissions"""
    submissions = load_submissions()
    return jsonify(submissions)

@app.route('/api/download-json', methods=['GET'])
def download_json():
    """Download JSON file"""
    if not os.path.exists(JSON_FILE):
        return jsonify({'error': 'No submissions yet'}), 404
    
    return send_file(JSON_FILE, as_attachment=True)

if __name__ == '__main__':
    # Create empty JSON file if it doesn't exist
    if not os.path.exists(JSON_FILE):
        save_submissions([])
    
    print("Meray Server running on http://localhost:5000")
    print(f"Submissions will be saved to: {os.path.abspath(JSON_FILE)}")
    app.run(debug=True, port=5000)