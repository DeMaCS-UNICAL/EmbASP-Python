from embasp.languages.predicate import Predicate


class Edge(Predicate):
    predicate_name = "edge"

    def __init__(self, source=None, destination=None):
        Predicate.__init__(self, [("source"), ("destination")])
        self.source = source
        self.destination = destination

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def set_source(self, source):
        self.source = source

    def set_destination(self, destination):
        self.destination = destination

    def __str__(self):
        return "edge(" + str(self.source) + "," + str(self.destination) + ")."
