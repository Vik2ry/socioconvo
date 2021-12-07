from flask import Flask, request
import requests

from pymessenger import Bot

app =  Flask(__name__)

# FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = "SocioConvo"

PAGE_ACCESS_TOKEN = "EABF39VKqWLsBAOZAbjkdGZAo09CkjvwUCF2rPswcfWaQocYi73EFYnwiWrP5m8PnaniCawrZBxMGZCsmsCdp9Tx5kWHKSP7eA0N3NkbkOJZCL7StqCiZCNWFiFl3U3aOT0uCgsC58Y0zdsoJTQwnklpuoAdled5UvqlwzhzM6zlPuLDRXLEQWm"

def get_API(messaged):
	bot = Bot(PAGE_ACCESS_TOKEN)

	url = 'http://localhost:8118/predict/'
	r = requests.get(url + messaged)

	data = r.json() # as its a rest api you can directly access the json object 
	
	print(data)
	return(data["text"])

def process_message(text):
	formatted_message = text.lower()
	if formatted_message != "stop" or formatted_message == "start":
		response = get_API(text)
	else:
		response = 'You are now been transferred to a manual responder. To start chit-chat again send "START". Please help give us feedback on this bot while waiting to be transferred at bit.ly/...'
	return response

@app.route('/', methods=["POST", "GET"])
def webhook():
	if request.method == "GET":
		if request.args.get("hub.verify_token") == VERIFY_TOKEN:
			return request.args.get("hub.challenge")
		else:
			return "Hello Youtube! - Not connected to Facebook."
	elif request.method == "POST":
		payload = request.json
		event = payload['entry'][0]['messaging']
		#print(event)
		for msg in event:
			text = msg['message']['text']
			sender_id = msg['sender']['id']
			#print(text)
			response = process_message(text)
			bot.send_text_message(sender_id, response)
		return "message received"
	else:
		# print(request.data)
		return "200"
	
if __name__ == '__main__':
	app.run()