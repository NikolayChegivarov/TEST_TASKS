def get_user_input(prompt: str) -> str:
    return input(prompt).strip()


def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(get_user_input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число.")


def yes_no_question(question: str) -> bool:
    while True:
        answer = get_user_input(question).lower()
        if answer in ["да", "yes"]:
            return True
        elif answer in ["нет", "no"]:
            return False
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'.")
