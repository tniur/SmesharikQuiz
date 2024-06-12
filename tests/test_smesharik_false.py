from smesharik_quiz.quiz import SmesharikQuiz


def test_smesharik_false():
    quiz = SmesharikQuiz()
    assert quiz.check_smesharik() is False
