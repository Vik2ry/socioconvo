from flask import Flask, request
import requests

app =  Flask(__name__)

# FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = "Socioconvo"
PAGE_ACCESS_TOKEN = "EABF39VKqWLsBAOZAbjkdGZAo09CkjvwUCF2rPswcfWaQocYi73EFYnwiWrP5m8PnaniCawrZBxMGZCsmsCdp9Tx5kWHKSP7eA0N3NkbkOJZCL7StqCiZCNWFiFl3U3aOT0uCgsC58Y0zdsoJTQwnklpuoAdled5UvqlwzhzM6zlPuLDRXLEQWm"
@app.route('/', methods=['GET'])
def webhook():
	if request.method == "GET":
		if request.args.get("hub.verify_token") == VERIFY_TOKEN:
			return request.args.get("hub.challenge")
		else:
			return "Hello Youtube! - Not connected to Facebook."
	else:
		# print(request.data)
		return "200"
if __name__ == '__main__':
	app.run()