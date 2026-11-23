import pytest


def test_get_activities_returns_all_activities(client, reset_activities):
    """Test that GET /activities returns all activities"""
    response = client.get("/activities")
    
    assert response.status_code == 200
    activities = response.json()
    
    assert len(activities) == 15
    assert "Chess Club" in activities
    assert "Soccer Team" in activities
    assert "Science Club" in activities


def test_get_activities_contains_required_fields(client, reset_activities):
    """Test that each activity has required fields"""
    response = client.get("/activities")
    activities = response.json()
    
    for activity_name, activity_data in activities.items():
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
        assert isinstance(activity_data["participants"], list)


def test_get_activities_participants_data(client, reset_activities):
    """Test that activity participants are correctly populated"""
    response = client.get("/activities")
    activities = response.json()
    
    chess_club = activities["Chess Club"]
    assert len(chess_club["participants"]) == 2
    assert "michael@mergington.edu" in chess_club["participants"]
    assert "daniel@mergington.edu" in chess_club["participants"]
    
    programming_class = activities["Programming Class"]
    assert len(programming_class["participants"]) == 2
    assert "emma@mergington.edu" in programming_class["participants"]
    
    volleyball_team = activities["Volleyball Team"]
    assert len(volleyball_team["participants"]) == 0


def test_get_activities_multiple_calls_consistent(client, reset_activities):
    """Test that multiple calls to /activities return consistent data"""
    response1 = client.get("/activities")
    response2 = client.get("/activities")
    
    assert response1.json() == response2.json()
