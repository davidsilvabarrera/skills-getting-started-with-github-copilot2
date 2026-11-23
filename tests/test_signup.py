import pytest


def test_signup_successful(client, reset_activities):
    """Test successful signup for an activity"""
    response = client.post("/activities/Chess Club/signup?email=test@mergington.edu")
    
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "test@mergington.edu" in data["message"]
    assert "Chess Club" in data["message"]


def test_signup_adds_participant_to_activity(client, reset_activities):
    """Test that signup actually adds participant to activity"""
    email = "newstudent@mergington.edu"
    client.post(f"/activities/Soccer Team/signup?email={email}")
    
    response = client.get("/activities")
    activities = response.json()
    
    assert email in activities["Soccer Team"]["participants"]


def test_signup_duplicate_raises_error(client, reset_activities):
    """Test that signing up twice raises an error"""
    email = "michael@mergington.edu"
    
    response = client.post(f"/activities/Chess Club/signup?email={email}")
    
    assert response.status_code == 400
    data = response.json()
    assert "already signed up" in data["detail"]


def test_signup_nonexistent_activity(client, reset_activities):
    """Test signup for non-existent activity raises 404"""
    response = client.post("/activities/Fake Club/signup?email=test@mergington.edu")
    
    assert response.status_code == 404
    data = response.json()
    assert "not found" in data["detail"]


def test_signup_multiple_students_same_activity(client, reset_activities):
    """Test multiple students can sign up for same activity"""
    activity = "Track and Field"
    email1 = "student1@mergington.edu"
    email2 = "student2@mergington.edu"
    
    client.post(f"/activities/{activity}/signup?email={email1}")
    client.post(f"/activities/{activity}/signup?email={email2}")
    
    response = client.get("/activities")
    activities = response.json()
    
    assert email1 in activities[activity]["participants"]
    assert email2 in activities[activity]["participants"]
    assert len(activities[activity]["participants"]) == 2


def test_signup_different_activities_same_student(client, reset_activities):
    """Test a student can sign up for multiple activities"""
    email = "versatile@mergington.edu"
    
    client.post(f"/activities/Chess Club/signup?email={email}")
    client.post(f"/activities/Drama Club/signup?email={email}")
    
    response = client.get("/activities")
    activities = response.json()
    
    assert email in activities["Chess Club"]["participants"]
    assert email in activities["Drama Club"]["participants"]


def test_signup_case_sensitivity(client, reset_activities):
    """Test that signup handles case properly for activity names"""
    response = client.post("/activities/chess club/signup?email=test@mergington.edu")
    
    assert response.status_code == 404


def test_signup_response_message_format(client, reset_activities):
    """Test that signup response has proper format"""
    response = client.post("/activities/Photography Club/signup?email=photo@mergington.edu")
    
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Signed up photo@mergington.edu for Photography Club"
