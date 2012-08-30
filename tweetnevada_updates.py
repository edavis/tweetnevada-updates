import subprocess
from munin.mongodb import MuninMongoDBPlugin

class TweetNevadaUpdates(MuninMongoDBPlugin):
    title = "TweetNevada"
    category = "TweetNevada"
    vlabel = "updates per ${graph_period}"
    scale = False
    period = "hour"

    @property
    def fields(self):
        return [
            ("untrusted",
             dict(label="untrusted updates", info="number of untrusted updates", type="COUNTER")),

            ("trusted",
             dict(label="trusted updates", info="number of trusted updates", type="COUNTER")),

            ("keepalive",
             dict(label="keepalives", info="number of keepalive notices", type="COUNTER"))]

    def execute(self):
        db = self.connection['tweetnv']
        print "trusted.value %d" % db.trusted_updates.find().count()
        print "untrusted.value %d" % db.untrusted_updates.find().count()

        log = '/var/log/supervisor/tweetnevada.log'
        cmd = ["grep", "-c", "keepalive", log]
        status = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        (stdout, stderr) = status.communicate()
        keepalive_count = int(stdout.strip())
        print "keepalive.value %d" % keepalive_count

def main():
    TweetNevadaUpdates().run()
