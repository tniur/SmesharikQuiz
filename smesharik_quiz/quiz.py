# smesharik_quiz/quiz.py
class SmesharikQuiz:
    def __init__(self):
        self.smesharik = None

    def greet_user(self):
        print("Добро пожаловать в тест 'Какой вы Смешарик'! Удачного прохождения теста!")

    def thank_user(self):
        print("Спасибо за прохождение теста! Надеемся, вам было интересно.")

    def ask_question(self, question):
        while True:
            answer = input(question + " (Да/Нет): ").strip().lower()
            if answer in ['да', 'нет']:
                return answer == 'да'
            else:
                print("Пожалуйста, введите 'Да' или 'Нет'.")

    def start_quiz(self):
        self.greet_user()
        if self.ask_question("Вы ребенок?"):
            if self.ask_question("Вы летали в космос?"):
                if self.ask_question("Вы коллекционируете кактусы?"):
                    self.smesharik = "Ежик"
                elif self.ask_question("Вы любите морковку?"):
                    self.smesharik = "Крош"
                elif self.ask_question("Вы робот?"):
                    self.smesharik = "Би-би"
            else:
                if self.ask_question("Вы пишете стихи?"):
                    self.smesharik = "Бараш"
                elif self.ask_question("Душу за шоколад продадите?"):
                    self.smesharik = "Нюша"
        else:
            if self.ask_question("Вы птица?"):
                if self.ask_question("Вы умеете играть на пианино?"):
                    self.smesharik = "Кар-Карыч"
                elif self.ask_question("Вы живете в дупле?"):
                    self.smesharik = "Совунья"
                elif self.ask_question("Вы умеете управлять самолетом?"):
                    self.smesharik = "Пин"
            else:
                if self.ask_question("У вас есть рога?"):
                    self.smesharik = "Лосяш"
                elif self.ask_question("У вас есть огород?"):
                    self.smesharik = "Капатыч"

        self.display_result()
        self.thank_user()

    def display_result(self):
        if self.smesharik:
            print(f"Вы - {self.smesharik}!")
        else:
            print("Не удалось определить вашего персонажа.")
