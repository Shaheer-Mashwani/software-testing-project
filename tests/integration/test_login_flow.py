from src.login import login

def test_login_flow():
    """
    Integration Test:
    Check full login flow with valid credentials
    """
    result = login("admin", "1234")
    assert result == "Login successful"

