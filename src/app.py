from flask import Flask
import sys
import os

app = Flask(__name__)

# append path apps root folders
app_dir = os.path.join(os.path.dirname(__file__), "apps")
for dir in os.listdir(app_dir):
    sys.path.append(os.path.abspath(os.path.join(app_dir + '/' + dir)))

sys.path.append(os.path.join(os.path.dirname(__file__), "common"))

from resources import resources_apps
app.register_blueprint(resources_apps)

if __name__ == "__main__":    
    app.run(debug=True, host='0.0.0.0', port=3200)
