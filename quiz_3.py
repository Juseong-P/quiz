class Word:
    def __init__(self, New_word, ex1, ex2, answer):
        self.New_word = New_word
        self.ex1 = ex1
        self.ex2 = ex2
        self.answer = answer

    def show_question (self):
        print("""
\"{0}\"의 뜻은?
1. {1}
2. {2}""".format(self.New_word, self.ex1, self.ex2))

    def check_answer(self, choose_answer):

        if choose_answer == self.answer:
            print("정답입니다.")
        else:
            print("오답입니다.")

word = Word("얼죽아", "얼어 죽어도 아이스 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer(int(input("= > ")))
