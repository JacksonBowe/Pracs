class ProgrammingLanguage:
    def __init__(self, language='none', typing='none', reflection=0, year=0):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    # def is_dynamic(self):

    def __str__(self):
        return '{}, {} Typing, Reflection={}, First appeared in {}'.format(self.language, self.typing, self.reflection, self.year)
