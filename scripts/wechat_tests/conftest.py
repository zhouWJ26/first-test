import pytest
from .utils import launch_driver


@pytest.fixture(scope="session")
def driver() -> "AppiumDriver":
    driver = launch_driver()
    yield driver
    driver.quit()