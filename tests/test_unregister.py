def test_unregister_removes_participant_from_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # already present in seed data

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity}"}
    participants = client.get("/activities").json()[activity]["participants"]
    assert email not in participants


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_non_registered_participant_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "notregistered@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
