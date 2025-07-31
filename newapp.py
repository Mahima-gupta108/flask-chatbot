from flask import Flask,request,jsonify,render_template
app=Flask(__name__)
keyword_responses = {
    "hi": "hello there",
    "hello": "hey! how can I help you?",
    "how are you": "I am fine, thank you!",
    "what are you doing": "Just checking some mails",
    "planning to meet": "Yes sure, let’s plan it!",
    "what is your name": "I’m your friendly AI chatbot!",
    "who created you": "I was created by a team of developers!",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "what can you do": "I can chat with you, answer questions, and help you with tasks!",
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
    "what is ai": "AI stands for Artificial Intelligence. It's the simulation of human intelligence by machines.",
    "open google": "Sorry, I can't open websites yet. 😅",
    "weather today": "I don't have live weather data, but it’s always sunny in our chat!",
    "your favorite color": "I like all the colors, but pink looks cute on me 💖"
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






