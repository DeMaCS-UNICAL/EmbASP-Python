from .idlv.idlv_parser_visitor_implementation import IDLVParserVisitorImplementation


class DatalogSolversParser(object):

    @staticmethod
    def parse_idlv(models, atomsList, two_stageParsing):
        IDLVParserVisitorImplementation.parse(
            models, atomsList, two_stageParsing)
