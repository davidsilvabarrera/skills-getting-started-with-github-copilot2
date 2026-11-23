import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to initial state before each test"""
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Team": {
            "description": "Join our competitive soccer team and compete in regional tournaments",
            "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["alex@mergington.edu"]
        },
        "Basketball League": {
            "description": "Play basketball and develop your skills with our experienced coaches",
            "schedule": "Tuesdays and Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["maya@mergington.edu", "noah@mergington.edu"]
        },
        "Volleyball Team": {
            "description": "Practice volleyball skills and compete in friendly matches",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 14,
            "participants": []
        },
        "Track and Field": {
            "description": "Train for running, jumping, and throwing events",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": []
        },
        "Drama Club": {
            "description": "Perform in plays and musicals, develop acting and theatrical skills",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["isabella@mergington.edu"]
        },
        "Photography Club": {
            "description": "Learn photography techniques and create visual stories",
            "schedule": "Fridays, 3:30 PM - 4:30 PM",
            "max_participants": 15,
            "participants": []
        },
        "Creative Writing Workshop": {
            "description": "Write stories and poetry, and share work with fellow writers",
            "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
            "max_participants": 16,
            "participants": []
        },
        "Art Studio": {
            "description": "Explore painting, drawing, sculpture, and other visual arts",
            "schedule": "Mondays and Wednesdays, 3:30 PM - 4:30 PM",
            "max_participants": 18,
            "participants": ["grace@mergington.edu", "leo@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop public speaking and critical thinking through competitive debate",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["ryan@mergington.edu"]
        },
        "Math Club": {
            "description": "Solve challenging problems and explore mathematical ideas",
            "schedule": "Mondays, 3:30 PM - 4:30 PM",
            "max_participants": 18,
            "participants": []
        },
        "History Society": {
            "description": "Explore historical events through research and discussion",
            "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
            "max_participants": 18,
            "participants": []
        },
        "Science Club": {
            "description": "Conduct experiments and explore STEM through hands-on projects",
            "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
            "max_participants": 25,
            "participants": ["ava@mergington.edu", "ethan@mergington.edu", "liam@mergington.edu"]
        }
    }

    activities.clear()
    activities.update(original_activities)
    yield
    activities.clear()
    activities.update(original_activities)
