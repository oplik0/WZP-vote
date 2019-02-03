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
            wr = int(str(writable.read()).replace("\n", ""))
        if wr:
            with open("passwords/"+user+"_password.txt", "r") as password_file:

                if password == str(password_file.read()).replace("\n", ""):
                    with open("votes/"+user+"_vote.txt", "w") as saved_file:
                        saved_file.write(text)
                        return(jsonify({"error":"none", "type":"encryption"}))
                else:
                    if password=="":
                        try:
                            with open("votes/"+user+"_vote.txt", "r") as saved_file:
                            output = str(saved_file.read())
                            return(jsonify({"error":"none", "type":"decryption","text":output}))
                        except:
                            return(jsonify({"error":"password"}))
                    else:
                        return(jsonify({"error":"password"}))
        else:
            with open("votes/"+user+"_vote.txt", "r") as saved_file:
                output = str(saved_file.read())
                return(jsonify({"error":"none", "type":"decryption","text":output}))
    except Exception as E:
        print("Error:", E)
        return(jsonify({"error":"error"}))
@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    #usuń/schowaj w komentarz te dwie linie jeśli nie używasz tls
    context = ('cert.pem', 'key.pem')
    app.run(host="0.0.0.0", port="443", ssl_context=context)
    #Odkomentuj jeśli nie używasz szyfrowania:
    #app.run(host="0.0.0.0", port="80")
    #odkomentuj do testowania lokalnego:
    #app.run(host="127.0.0.1", port=5000) 
