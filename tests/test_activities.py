def test_get_activities_returns_all_activities(client):
    # Arrange - pre-loaded in-memory data contains activities on startup

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0


def test_get_activities_each_entry_has_required_fields(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    for name, details in response.json().items():
        assert required_fields.issubset(details.keys()), (
            f"Activity '{name}' is missing required fields"
        )


def test_get_activities_participants_is_a_list(client):
    # Arrange - no extra setup; just verify data types in the response

    # Act
    response = client.get("/activities")

    # Assert
    for name, details in response.json().items():
        assert isinstance(details["participants"], list), (
            f"Activity '{name}' participants should be a list"
        )
