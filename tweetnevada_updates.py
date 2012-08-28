from munin.mongodb import MuninMongoDBPlugin

class TweetNevadaUpdates(MuninMongoDBPlugin):
    title = "Number of Updates"
    category = "TweetNevada"
    vlabel = "updates"

    @property
    def fields(self):
        return [
            ("untrusted",
             dict(label="untrusted", info="number of untrusted updates", type="GUAGE")),

            ("trusted",
             dict(label="trusted", info="number of trusted updates", type="GUAGE"))]

    def execute(self):
        db = self.connection['tweetnv']
        print "trusted.value %d" % db.trusted_updates.find().count()
        print "untrusted.value %d" % db.untrusted_updates.find().count()

def main():
    TweetNevadaUpdates().run()
