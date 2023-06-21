import unittest
import pep8
import console
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """Testing the console for bugs"""

    def test_pep8_console(self):
        """Checks if console.py conforms to pep8 style"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors and style warnings")

    def test_pep8_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(
            len(console.__doc__) >= 1, "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(
            HBNBCommand.__doc__, None, "No docstring in HBNBCommand class")
        self.assertTrue(
            len(HBNBCommand.__doc__) >= 1,
            "No docstring in HBNBCommand class")
