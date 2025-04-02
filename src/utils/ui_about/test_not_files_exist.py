import os
import tempfile
import unittest
from unittest.mock import patch

from files_exist import check_readme

class TestFilesExist(unittest.TestCase):
    def setUp(self):
        # Use tempfile for safer temporary directory handling
        self.test_dir = tempfile.TemporaryDirectory()
        self.base_path = self.test_dir.name
        
        # Standard expected filenames
        self.expected_json = 'README_parsed.json'
        self.expected_md = 'README_parsed.md'

    def tearDown(self):
        # Automatic cleanup with tempfile
        self.test_dir.cleanup()

    def create_file(self, filename, content=""):
        """Helper to create files in test directory"""
        path = os.path.join(self.test_dir.name, filename)
        with open(path, 'w') as f:
            f.write(content)
        return path

    def test_unexpected_files(self):
        """Test various unexpected file scenarios"""
        test_cases = [
            ('extra.txt', 'text file'),
            ('.hidden', 'hidden file'),
            ('README.json', 'similar JSON'),  # Wrong naming pattern
            ('data.csv', 'csv data')
        ]

        for filename, content in test_cases:
            with self.subTest(filename=filename):
                self.create_file(filename, content)
                self.create_file(self.expected_json)
                self.create_file(self.expected_md)

                with self.assertRaises(ValueError) as cm:
                    check_readme('dummy', folder_path=self.test_dir.name)
                
                self.assertIn(filename, str(cm.exception))
                self.assertIn("should only contain", str(cm.exception))

    def test_valid_files(self):
        """Test acceptable file combinations"""
        test_cases = [
            [self.expected_json, self.expected_md],  # Both files
            [self.expected_json],  # Only JSON
            [self.expected_md]  # Only MD
        ]

        for files in test_cases:
            with self.subTest(files=files):
                for f in files:
                    self.create_file(f)
                
                result = check_readme('dummy', folder_path=self.test_dir.name)
                self.assertIsInstance(result, dict)

    def test_empty_directory(self):
        """Test empty target directory"""
        with self.assertRaises(ValueError) as cm:
            check_readme('dummy', folder_path=self.test_dir.name)
        
        self.assertIn("No README files found", str(cm.exception))

    def test_non_directory_path(self):
        """Test invalid directory path"""
        with self.assertRaises(ValueError) as cm:
            check_readme('dummy', folder_path='/non/existent/path')
        self.assertIn("is not a valid directory", str(cm.exception))

    def test_file_permissions_error(self):
        """Test read-protected directory"""
        os.chmod(self.test_dir.name, 0o000)  # Remove all permissions
        try:
            with self.assertRaises(PermissionError):
                check_readme('dummy', folder_path=self.test_dir.name)
        finally:
            os.chmod(self.test_dir.name, 0o755)  # Restore permissions

if __name__ == "__main__":
    unittest.main(failfast=True)