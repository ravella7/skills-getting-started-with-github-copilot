"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database with additional activities
activities = {
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
    # Sports related activities
    "Soccer Team": {
        "description": "Join the school's soccer team to train and compete in matches",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": []
    },
    "Basketball Club": {
        "description": "Participate in basketball training sessions and friendly matches",
        "schedule": "Fridays, 5:00 PM - 7:00 PM",
        "max_participants": 15,
        "participants": []
    },
    # Artistic activities
    "Painting Class": {
        "description": "Explore various painting techniques and create your own artworks",
        "schedule": "Tuesdays, 3:00 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Drama Club": {
        "description": "Engage in acting workshops and prepare for performances",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 20,
        "participants": []
    },
    # Intellectual activities
    "Debate Team": {
        "description": "Enhance your critical thinking by engaging in structured debates",
        "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Robotics Club": {
        "description": "Learn about robotics and participate in building and coding challenges",
        "schedule": "Fridays, 2:30 PM - 4:30 PM",
        "max_participants": 12,
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities

# Validate student is not already signed up for the activity
@app.get("/activities/{activity_name}")
def get_activity(activity_name: str):
    """Get details of a specific activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Check if student is already signed up
    if "email" in activity and activity["email"] in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")

    return activity

# @app.post("/activities/{activity_name}/signup")
# def signup_for_activity(activity_name: str, email: str):
#     """Sign up a student for an activity"""
#     # Validate activity exists
#     if activity_name not in activities:
#         raise HTTPException(status_code=404, detail="Activity not found")

#     # Get the specificy activity
#     activity = activities[activity_name]

#     # Add student
#     activity["participants"].append(email)
#     return {"message": f"Signed up {email} for {activity_name}"}
