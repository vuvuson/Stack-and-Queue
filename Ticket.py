class Ticket:
    def __init__(self, number, issue):
        self.number = number
        self.issue = issue
    def __str__(self):
        return f"#{self.number} {self.issue}"
    