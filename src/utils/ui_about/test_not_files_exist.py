import os
import shutil
import unittest


from files_exist import check_readme

class TestFilesExist(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = os.path.join(os.path.dirname(__file__), 'test_temp_dir')
        os.makedirs(self.test_dir, exist_ok=True)

        # Update the file paths to use the temporary directory
        self.json_file_path = os.path.join(self.test_dir, 'README_parsed.json')
        self.md_file_path = os.path.join(self.test_dir, 'README_parsed.md')

    def tearDown(self):
        # Clean up the temporary directory after each test
        shutil.rmtree(self.test_dir)

    def test_unexpected_file_raises_value_error(self):
        # Create an unexpected file in the directory
        unexpected_file_path = os.path.join(self.test_dir, 'unexpected_file.txt')
        with open(unexpected_file_path, 'w') as f:
            f.write("This is an unexpected file.")

        # Check if ValueError is raised
        with self.assertRaises(ValueError) as context:
            check_readme('dummy_path', folder_path=self.test_dir)

        self.assertIn("Unexpected file found in the folder", str(context.exception))
        self.assertIn("It should only contain JSON or MD archives.", str(context.exception))

    def test_no_unexpected_file(self):
        # Create expected JSON and MD files
        with open(self.json_file_path, 'w') as f:
            f.write("{}")
        with open(self.md_file_path, 'w') as f:
            f.write("{}")

        # Check if no error is raised
        result = check_readme('dummy_path', folder_path=self.test_dir)
        self.assertIsInstance(result, dict)

if __name__ == "__main__":
    unittest.main()