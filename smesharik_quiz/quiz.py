class SmesharikQuiz:
    def __init__(self):
        self.smesharik = None

    def ask_question(self, question):
        answer = input(question + " (Да/Нет): ").strip().lower()
        return answer == 'да'

    def start_quiz(self):
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
                else:
                    self.smesharik = "Совунья"
            else:
                if self.ask_question("У вас есть рога?"):
                    self.smesharik = "Лосяш"
                else:
                    self.smesharik = "Капатыч"