from unittest import TestCase
from handlers import pulls


class TestPulls(TestCase):

    def setUp(self):
        """Init"""

    def test_pulls(self):
        """Test if known pulls in estimated pulls"""
        t_accepted = {
            'num': 12,
            'title': 'Homework1: Anton Antanovich',
            'link': 'https://api.github.com/repos/alenaPy/devops_lab/pulls/12'
        }
        t_open = {
            'num': 7,
            'title': 'Homework1: Raman Rohau',
            'link': 'https://api.github.com/repos/alenaPy/devops_lab/pulls/7'
        }
        t_closed = {
            'num': 1,
            'title': 'Test PR',
            'link': 'https://api.github.com/repos/alenaPy/devops_lab/pulls/1'
        }
        t_needs_work = {
            'num': 22,
            'title': 'Homework2: Yaroslav Kurapov',
            'link': 'https://api.github.com/repos/alenaPy/devops_lab/pulls/22'
        }
        self.assertEqual(pulls.get_pulls('open').count(t_open), 1)
        self.assertEqual(pulls.get_pulls('closed').count(t_closed), 1)
        self.assertEqual(pulls.get_pulls('accepted').count(t_accepted), 1)
        self.assertEqual(pulls.get_pulls('needs work').count(t_needs_work), 1)

    def tearDown(self):
        """Finish"""
