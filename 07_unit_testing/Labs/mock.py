""" from unittest.mock import patch

with patch('os.rename') as rename:
    backup_file()
    rename.assert_called_with('datafile.csv', 'datafile.csv.bak')
    print('backup_file() correctly called rename!')

from unittest.mock import Mock

mymock = Mock()
mymock.somemethod()

try:
    mymock.somemethod.assert_called()
    print('somemethod() was called')
except AssertionError:
    print('somemethod() was not called!') """

