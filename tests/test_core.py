import unittest
from agent_arch.core import DemoAgentCore

class TestCore(unittest.TestCase):
    def setUp(self):
        self.agent = DemoAgentCore()
    
    def test_query(self):
        response = self.agent.query('测试问题')
        self.assertIsInstance(response, str)