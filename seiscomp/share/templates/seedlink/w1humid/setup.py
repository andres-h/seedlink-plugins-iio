import os

'''
Plugin handler for the 1-Wire humidity sensor (DS2438+HIH-5030) plugin.
'''
class SeedlinkPluginHandler:
    def __init__(self):
        pass

    def push(self, seedlink):
        try: seedlink.param('sources.w1humid.device')
        except: seedlink.setParam('sources.w1humid.device', '26-000000000000')

        try: seedlink.param('sources.w1humid.sampleRate')
        except: seedlink.setParam('sources.w1humid.sampleRate', '0.1')

        try: seedlink.param('sources.w1humid.proc')
        except: seedlink.setParam('sources.w1humid.proc', 'w1humid10s')

        return seedlink.param('sources.w1humid.device')

    def flush(self, seedlink):
        pass

