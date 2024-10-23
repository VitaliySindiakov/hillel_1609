import pytest

from homework_10 import log_event
from datetime import datetime


@pytest.mark.parametrize("username, status, current_time", [
    ("Andrew", "success", datetime.now().time()),
    ("Karl", "expired", datetime.now().time()),
    ("Anna", "failed", datetime.now().time())
])
def test_logger(username: str, status: str, current_time: datetime):
    log_event(username, status, current_time)
    with open('login_system.log', 'r') as log_file:
        content = log_file.read()
        lines = content.splitlines()
        last_line: str = lines[len(lines) - 1]
        assert str(current_time) in last_line and username in last_line and status in last_line
