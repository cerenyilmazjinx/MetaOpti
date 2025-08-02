# test_metaopti.py
"""
Tests for MetaOpti module.
"""

import unittest
from metaopti import MetaOpti

class TestMetaOpti(unittest.TestCase):
    """Test cases for MetaOpti class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaOpti()
        self.assertIsInstance(instance, MetaOpti)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaOpti()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
