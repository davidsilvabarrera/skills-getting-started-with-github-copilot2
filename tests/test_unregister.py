import pytest


def test_unregister_successful(client, reset_activities):
    """Test successful unregistration from an activity"""
    email = "michael@mergington.edu"
    response = client.delete(f"/activities/Chess Club/unregister?email={email}")
    
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert email in data["message"]
    assert "Chess Club" in data["message"]


def test_unregister_removes_participant(client, reset_activities):
    """Test that unregister actually removes participant from activity"""
    email = "michael@mergington.edu"
    client.delete(f"/activities/Chess Club/unregister?email={email}")
    
    response = client.get("/activities")
    activities = response.json()
    
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_nonexistent_activity(client, reset_activities):
    """Test unregister from non-existent activity raises 404"""
    response = client.delete("/activities/Fake Club/unregister?email=test@mergington.edu")
    
    assert response.status_code == 404
    data = response.json()
    assert "not found" in data["detail"]


def test_unregister_student_not_signed_up(client, reset_activities):
    """Test unregister for student not in activity raises error"""
    response = client.delete("/activities/Chess Club/unregister?email=notmember@mergington.edu")
    
    assert response.status_code == 400
    data = response.json()
    assert "not signed up" in data["detail"]


def test_unregister_from_empty_activity(client, reset_activities):
    """Test unregister from activity with no participants raises error"""
    response = client.delete("/activities/Volleyball Team/unregister?email=test@mergington.edu")
    
    assert response.status_code == 400
    data = response.json()
    assert "not signed up" in data["detail"]


def test_unregister_multiple_participants(client, reset_activities):
    """Test that unregister only removes the specified student"""
    email_to_remove = "michael@mergington.edu"
    email_to_keep = "daniel@mergington.edu"
    
    client.delete(f"/activities/Chess Club/unregister?email={email_to_remove}")
    
    response = client.get("/activities")
    activities = response.json()
    
    assert email_to_remove not in activities["Chess Club"]["participants"]
    assert email_to_keep in activities["Chess Club"]["participants"]
    assert len(activities["Chess Club"]["participants"]) == 1


def test_unregister_then_resign_up(client, reset_activities):
    """Test that a student can sign up again after unregistering"""
    email = "test@mergington.edu"
    activity = "Track and Field"
    
    client.post(f"/activities/{activity}/signup?email={email}")
    client.delete(f"/activities/{activity}/unregister?email={email}")
    signup_response = client.post(f"/activities/{activity}/signup?email={email}")
    
    assert signup_response.status_code == 200
    
    response = client.get("/activities")
    activities = response.json()
    assert email in activities[activity]["participants"]


def test_unregister_response_message_format(client, reset_activities):
    """Test that unregister response has proper format"""
    response = client.delete("/activities/Science Club/unregister?email=ava@mergington.edu")
    
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Unregistered ava@mergington.edu from Science Club"


def test_unregister_case_sensitivity_activity(client, reset_activities):
    """Test that activity name case matters for unregister"""
    response = client.delete("/activities/chess club/unregister?email=michael@mergington.edu")
    
    assert response.status_code == 404
