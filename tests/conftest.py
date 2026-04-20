import copy
import pytest
from fastapi.testclient import TestClient

import src.app as app_module
from src.app import app


@pytest.fixture
def client():
    return TestClient(app, follow_redirects=False)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activities dict after every test to ensure isolation."""
    original = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(original)
