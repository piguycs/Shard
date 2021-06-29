from json import load

class setCfg():
    '''
    @param config file
    '''
    def __init__(self, config):
        self.file = config
        with open(config) as f:
            self.cfg = load(f)

    def test(self):
        return self.file

    def getField(self, field):
        return self.cfg[field]
    
    def getAll(self, field, xindex=None):
        try:
            allfields = []
            for x in self.cfg[field]:
                if xindex:
                    allfields.append(x[xindex])
                else:
                    allfields.append(x)
            return allfields
        except IndexError:
            return None

    def pushField(self):
        with open(self.file) as f:
            file = load(f)
        return file
