import pytest
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def equation_roots_url():
    base_url = os.environ.get("BASE_URL").rstrip("/")
    return f"{base_url}/equation/roots"
