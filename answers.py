answers = {
	"hello": "Hello!",
	"what`s up": "Fine, you?",
	"Bye": "Miss you"
}

def get_answer(question, answers):
	return answers.get(question)

def ask_user(answers):
	while True:
		user_input = input("Please, say someone: ")
		answer = get_answer(user_input, answers)
		print(answer)

		if user_input == "Bye":
			break