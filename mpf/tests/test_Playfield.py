from mpf.tests.MpfTestCase import MpfTestCase


class TestPlayfield(MpfTestCase):

    def get_config_file(self):
        return 'test_playfield.yaml'

    def getMachinePath(self):
        return 'tests/machine_files/playfield/'

    # nothing to test currently
