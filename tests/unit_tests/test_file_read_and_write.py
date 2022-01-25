

import unittest
from unittest.mock import patch, mock_open
from text_file import TextFile


class TestTextFiles(unittest.TestCase):
   
    def test_creating_TextFile_object(self):
        s = TextFile('text.txt')
        assert ('text.txt') == (s._path)


    def test_file_writer(self):
        fake_file_path = "path.txt"
        content = "Message to write on file to be written"
        foo=TextFile(fake_file_path)
        with patch('text_file.TextFile.write_sorted_names', mock_open()) as mocked_file:
            foo.write_sorted_names(content, 'w')
            # assert if opened file on write mode 'w'
            mocked_file.assert_called_once_with(content, 'w')
    
    def test_read_file(self):
        fake_file_path = "path.txt"
        content = "hello , apple , ball"
        foo=TextFile(fake_file_path)
        with patch('text_file.TextFile.read_and_sort_file', mock_open()) as mocked_file:
            foo.read_and_sort_file(content, 'r')
            # assert if opened file on write mode 'r'
            mocked_file.assert_called_once_with(content, 'r')
    

    def test_file_extension(self):
        with self.assertRaises(Exception):
            fake_file_path = "path"
            content = "Message to write on file to be written"
            foo=TextFile(fake_file_path)
            with patch('text_file.TextFile.write_sorted_names', mock_open()) as mocked_file:
                 foo.write_sorted_names(content, 'w')
              
    