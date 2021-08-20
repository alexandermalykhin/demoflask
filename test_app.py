import os
import tempfile

import pytest

from app import index


@pytest.fixture
def app():
    app = index()
    return app