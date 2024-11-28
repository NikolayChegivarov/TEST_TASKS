def get_user_input(prompt: str) -> str:
    """Функция для получения и очистки пользовательского ввода."""
    return input(prompt).strip()


def get_int_input(prompt: str) -> int:
    """Функция для получения целочисленного ввода с проверкой."""
    while True:
        try:
            return int(get_user_input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число.")


def yes_no_question(question: str) -> bool:
    """Функция для обработки вопросов да/нет."""
    while True:
        answer = get_user_input(question).lower()
        if answer in ["да", "yes"]:
            return True
        elif answer in ["нет", "no"]:
            return False
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'.")
