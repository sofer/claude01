"""Tests for the fac CLI."""

import pytest
from io import StringIO
import sys
from unittest.mock import patch

from fac.cli import main


def test_main_outputs_hello():
    """Test that the main function outputs 'hello'."""
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', new=captured_output):
        main()
    
    # Get the printed output
    output = captured_output.getvalue().strip()
    
    # Assert output is 'hello'
    assert output == 'hello'