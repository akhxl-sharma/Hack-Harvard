from flask import Flask, jsonify
import pickle as pkl 
import subprocess

app = Flask(__name__)

@app.route('/run_my_script', methods=['GET'])
def run_my_script():
    try:
        # Run your script and capture the output
        result = subprocess.check_output(['python', '/Users/akhil/Downloads/Hack-Harvard/ai/recommenders/recommender.py'], universal_newlines=True)

        return jsonify({'output': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)