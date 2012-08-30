from munin.mongodb import MuninMongoDBPlugin

class TweetNevadaUpdates(MuninMongoDBPlugin):
    title = "Number of Updates"
    category = "TweetNevada"
    vlabel = "updates"
    scale = False
    period = "hour"

    @property
    def fields(self):
        return [
            ("untrusted",
             dict(label="Untrusted updates", info="number of untrusted updates", type="COUNTER")),

            ("trusted",
             dict(label="Trusted updates", info="number of trusted updates", type="COUNTER"))]

    def execute(self):
        db = self.connection['tweetnv']
        print "trusted.value %d" % db.trusted_updates.find().count()
        print "untrusted.value %d" % db.untrusted_updates.find().count()

def main():
    TweetNevadaUpdates().run()
