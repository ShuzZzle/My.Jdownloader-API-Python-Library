import unittest
import main


class TVSTest(unittest.TestCase):

    def setUp(self):
        """"Call before every Testcase."""
        self.tvtracker = main.TrackKeeper()

    def tearDown(self):
        """"behaves like __del__(self)"""

    def test_get_episode_data(self):
        for k, v in main.SHOW_TRACKER.iteritems():
            self.assertTrue(self.tvtracker.get_episode_data(k))

if __name__ == '__main__':
    unittest.main()
