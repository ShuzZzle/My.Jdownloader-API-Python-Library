class Struct:

    def __init__(self):
        pass

    def to_dict(self):
        struct_dict = dict()
        for key, value in self.struct_hack.iteritems():
            struct_dict[key] = value
        return struct_dict
