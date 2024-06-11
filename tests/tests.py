from smesharik_quiz.quiz import SmesharikQuiz

def test_pin():
    quiz = SmesharikQuiz()
    assert quiz.check_smesharik() == False
