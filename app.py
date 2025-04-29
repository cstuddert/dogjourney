from flask import Flask, render_template, request, jsonify
import os

# app = Flask(__name__)
# app.config['TEMPLATES_AUTO_RELOAD'] = True

# Dynamically set the template and static folders to the current project
CURRENT_PROJECT_PATH = os.path.join(os.path.dirname(__file__), "current_project")
TEMPLATES_PATH = os.path.join(CURRENT_PROJECT_PATH, "templates")
STATIC_PATH = os.path.join(CURRENT_PROJECT_PATH, "static")

# Initialize Flask app with dynamic template and static folder paths
app = Flask(__name__, template_folder=TEMPLATES_PATH, static_folder=STATIC_PATH)
app.config['TEMPLATES_AUTO_RELOAD'] = True


### MARS
@app.route('/')
def dogjourney():
    return render_template('test_breeds.html')


if __name__ == '__main__':
    app.run(debug=True)
