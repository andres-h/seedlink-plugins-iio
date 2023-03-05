import os

'''
Plugin handler for the ADXL355 accelerometer plugin.
'''
class SeedlinkPluginHandler:
    def __init__(self):
        pass

    def push(self, seedlink):
        try: seedlink.param('sources.adxl.device')
        except: seedlink.setParam('sources.adxl.device', 'adxl355')

        try: seedlink.param('sources.adxl.sampleRate')
        except: seedlink.setParam('sources.adxl.sampleRate', '500')

        try: seedlink.param('sources.adxl.proc')
        except: seedlink.setParam('sources.adxl.proc', 'adxl500')

        return seedlink.param('sources.adxl.device')

    def flush(self, seedlink):
        pass

