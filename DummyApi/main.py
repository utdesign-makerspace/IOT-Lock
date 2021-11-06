from flask import Flask,jsonify

app = Flask(__name__)

validIds = {"0852729982"}

@app.route('/<string:id>/')
def verifyUser(id):
    successResponse = {"success":"true"}
    failResponse = {"success":"false"}
    
    if id in validIds:
        return jsonify(successResponse)
    else:
        return jsonify(failResponse)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
