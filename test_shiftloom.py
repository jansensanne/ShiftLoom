# test_shiftloom.py
"""
Tests for ShiftLoom module.
"""

import unittest
from shiftloom import ShiftLoom

class TestShiftLoom(unittest.TestCase):
    """Test cases for ShiftLoom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShiftLoom()
        self.assertIsInstance(instance, ShiftLoom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShiftLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
