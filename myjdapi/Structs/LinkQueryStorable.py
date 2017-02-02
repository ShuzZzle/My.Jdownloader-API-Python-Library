from Struct import Struct


class LinkQueryStorable(Struct):

    def __init__(self, bytesTotal=False, comment=False, status=False, enabled=False, maxResults=-1, startAt=0,
                 packageUUIDs=None, host=False, url=False, bytesLoaded=False, speed=False, eta=False, finished=False,
                 priority=False, running=False, skipped=False, extractionStatus=False):
        Struct.__init__(self)
        self.bytesTotal = bytesTotal
        self.comment = comment
        self.status = status
        self.enabled = enabled
        self.maxResults = maxResults
        self.startAt = startAt
        self.packageUUIDs = packageUUIDs
        self.host = host
        self.url = url
        self.bytesLoaded = bytesLoaded
        self.speed = speed
        self.eta = eta
        self.finished = finished
        self.priority = priority
        self.running = running
        self.skipped = skipped
        self.extractionStatus = extractionStatus
        # Save for later
        self.struct_hack = locals()
        del self.struct_hack["self"]