def test_root_redirects_to_index(client):
    # Arrange - no additional setup needed; root endpoint requires no parameters

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code in (301, 302, 307, 308)
    assert response.headers["location"].endswith("/static/index.html")
