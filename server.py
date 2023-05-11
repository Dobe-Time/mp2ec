from flask import Flask
from flask import request
import stress

app = Flask(__name__)

class seed_storage():
    seed = 0

seed_box = seed_storage()

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        seed_in = request.json
        seed_in = int(seed_in['num'])
        seed_box.seed = seed_in
        return str(seed_box.seed)
    else:
        return str(seed_box.seed)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80, debug = True)