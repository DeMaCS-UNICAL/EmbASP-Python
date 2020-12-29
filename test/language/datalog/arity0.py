from embasp.languages.predicate import Predicate


class Arity0(Predicate):

    predicate_name = "a"

    def __init__(self):
        super(Arity0, self).__init__([])

    def __str__(self):
        return "a"
