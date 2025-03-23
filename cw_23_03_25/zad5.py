class SimpleChatbot:
    def __init__(self, questions: list):
        self.questions = questions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.questions):
            question = self.questions[self.index]
            self.index += 1
            return question
        else:
            raise StopIteration



class StopIteration(Exception):
    pass


bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?", "Ile masz lat?"])

for question in bot:
    print(question)
    response = input()