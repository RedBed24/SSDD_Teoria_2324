import importlib.util
import os.path
import time
import Ice
import sys

if importlib.util.find_spec("ssdd") is None:
    slice_path = os.path.join(os.path.dirname(__file__), "icedrive.ice")

    if not os.path.exists(slice_path):
        raise ImportError("Cannot find icedrive.ice for loading IceDrive module")

    Ice.loadSlice(slice_path)

import ssdd

ID = "05735354M"
FULLNAME = "Samuel Espejo Gil"

CRIS_PROXY_STRING = "Cristian -t -e 1.1:tcp -h 93.189.90.58 -p 4000 -t 60000"
SYNC_PROXY_STRING = "SyncReport -t -e 1.1:tcp -h 93.189.90.58 -p 4000 -t 60000"

class Client(Ice.Application):
    def run(self, argv):
        proxy = self.communicator().stringToProxy(CRIS_PROXY_STRING)
        cris_server = ssdd.CristianPrx.checkedCast(proxy)
        proxy = self.communicator().stringToProxy(SYNC_PROXY_STRING)
        sync_server = ssdd.SyncReportPrx.checkedCast(proxy)
        if not cris_server or not sync_server:
            raise RuntimeError('Invalid proxy')

        tc1 = time.time()
        ts = cris_server.getServerTime(ID, tc1)
        tc2 = time.time()

        serverTime = ts + (tc2 - tc1) / 2
        error = (tc2 - tc1) / 2

        sync_server.notifyTime(ID, FULLNAME, tc2, serverTime, error)

        return 0

if __name__ == '__main__':
    client = Client()
    sys.exit(client.main(sys.argv))
