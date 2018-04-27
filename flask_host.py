from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def test():
    if request.method == "POST":
        print(request.data)
        return request.data
    return 'test'


if __name__ == "__main__":
    app.debug = True
    app.run()
