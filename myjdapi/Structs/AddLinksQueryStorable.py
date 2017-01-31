from Struct import Struct


class AddLinksQueryStorable(Struct):

    def __init__(self, autostart=False, deepDecrypt=False, autoExtract=False, overwritePackagizerRules=False,
                 links=None, dataURLs=[], packageName=None,  extractPassword=None, sourceUrl=None,
                 downloadPassword=None, destinationFolder=None, assignJobID=None
                 ):
        """

        :param deepDecrypt:
        :param autoExtract:
        :param overwritePackagizerRules:
        :param links:
        :param dataURLs:
        :param packageName:
        :param extractPassword:
        :param sourceUrl:
        :param downloadPassword:
        :param destinationFolder:
        :param assignJobID:
        :type autostart: object
        """
        Struct.__init__(self)  # Even though this is not needed
        self.autostart = autostart
        self.deepDecrypt = deepDecrypt
        self.autoExtract = autoExtract
        self.overwritePackagizerRules = overwritePackagizerRules
        self.links = links
        self.dataURLs = dataURLs
        self.packageName = packageName
        self.extractPassword = extractPassword
        self.sourceUrl = sourceUrl
        self.downloadPassword = downloadPassword
        self.destinationFolder = destinationFolder
        self.assignJobID = assignJobID
        # Save for later
        self.struct_hack = locals()
        del self.struct_hack["self"]
