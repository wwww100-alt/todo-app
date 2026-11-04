"""Бизнес-логика: дела, статусы, операции над списком."""

class Task:
    def __init__(self, title: str, deadline: str, done: bool = False):
        self.title = title
        self.deadline = deadline
        self.done = done

    def mark_done(self):
        self.done = True

    def __str__(self) -> str:
        status = "выполнено" if self.done else "не выполнено"
        return f"{self.title} (до {self.deadline}) — {status}"