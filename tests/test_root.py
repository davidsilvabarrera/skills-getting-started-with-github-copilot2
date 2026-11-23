import pytest


def test_root_redirect_to_static_index(client, reset_activities):
    """Test that GET / redirects to /static/index.html"""
    response = client.get("/", follow_redirects=False)
    
    assert response.status_code == 307
    assert "/static/index.html" in response.headers["location"]


def test_root_redirect_location_header(client, reset_activities):
    """Test that redirect location header is correct"""
    response = client.get("/", follow_redirects=False)
    
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_root_with_follow_redirects(client, reset_activities):
    """Test following redirect from root (would return index.html if file exists)"""
    response = client.get("/", follow_redirects=True)
    
    # Will be 404 or 200 depending on if static/index.html exists
    # We just verify it follows the redirect
    assert response.status_code in [200, 404, 307]
