from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template(
        "index.html",
        girlfriends="lin has no litmited."
    )

@app.route('/test')
def test():
    return "TEST"

@app.route('/data', methods=["POST"])
def data():
    print(request.values)
    return request.values.get("msg")

if __name__ == '__main__':
    app.run(debug=True)