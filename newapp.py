from flask import Flask,request,jsonify,render_template
app=Flask(__name__)
keyword_responses={
 "hi":"hello there",
 "how are you":"i am fine",
 "what are you doing":"checking mails",
 "planning to meet":"yes sure"

 }
@app.route("/")
def home():
    return render_template("index.html")

default_response="i am not sure about it"
@app.route("/chat",methods=["post"])
def chat():
    user_input=request.json.get("message","").lower().strip()
    if not user_input:
        return jsonify({"error":"no message providd"}),400
    
    reply=default_response
    for keyword in keyword_responses:
        if keyword in user_input:
            reply=keyword_responses[keyword]
            break

    return jsonify({"reply":reply})
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)






