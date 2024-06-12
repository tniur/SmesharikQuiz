from smesharik_quiz.quiz import SmesharikQuiz


def test_result():
    quiz = SmesharikQuiz()
    assert quiz.display_result() is False
