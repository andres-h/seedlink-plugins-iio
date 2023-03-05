import os

'''
Plugin handler for the DPS310 barometer plugin.
'''
class SeedlinkPluginHandler:
    def __init__(self):
        pass

    def push(self, seedlink):
        try: seedlink.param('sources.dps.device')
        except: seedlink.setParam('sources.dps.device', 'dps310')

        try: seedlink.param('sources.dps.sampleRate')
        except: seedlink.setParam('sources.dps.sampleRate', '1')

        try: seedlink.param('sources.dps.proc')
        except: seedlink.setParam('sources.dps.proc', 'dps1')

        return seedlink.param('sources.dps.device')

    def flush(self, seedlink):
        pass

