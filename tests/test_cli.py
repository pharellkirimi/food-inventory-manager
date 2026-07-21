from unittest.mock import patch
import cli


@patch("builtins.input", return_value="7")
def test_exit_cli(mock_input):
    cli.main()