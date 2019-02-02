from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
@app.route("/save", methods=["post"])
def save():
    print("working")
    user = str(request.json['user'])
    text = str(request.json['text'])
    password = str(request.json['password'])
    try:
        with open("writable.txt", 'r') as writable:
            wr = int(writable.read())
        if wr:
            with open(user+"_password.txt", "r") as password_file:

                if password == password_file.read():
                    with open(user+"_vote.txt", "w") as saved_file:
                        saved_file.write(text)
                        return(jsonify({"error":"none", "type":"encryption"}))
                else:
                    return(jsonify({"error":"password"}))
        else:
            with open(user+"_vote.txt", "r") as saved_file:
                output = str(saved_file.read())
                return(jsonify({"error":"none", "type":"decryption","text":output}))
    except Exception as E:
        print("Error:", E)
        return(jsonify({"error":"error"}))
@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    #context = ('cert.pem', 'key.pem')
    #app.run(host="0.0.0.0", port="443", ssl_context=context)
    app.run(host="127.0.0.1", port=5000)