import requests

URL = "https://asked.kr/query.php?query=0"
URL2 = "https://asked.kr/"

def isUser(id):
	length = len(requests.get(URL2+id).text)
	if length > 200:
		return True
	else:
		return False
	
def ask(id, question):
	a = {'id': id, 'content': question, 'makarong_bat':'-1', 'show_user':'0'}
	post = requests.post(URL, data=a)
	code = post.status_code
	if isUser(id):
		if code == 200:
			try:
				print("success!")
				print("id : ",id,"\nquestion : ",question)
			except Exception as e:
				print(e)
		else:
			print('error! -> status_code : ',code)
	else:
		print("error! -> invalid user!")
