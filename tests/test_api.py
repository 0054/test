
def test_200_root(client):
    response = client.get("/")
    assert response.status_code == 200

def test_200_repo_dotfiles(client):
    response = client.get("/repo/dofiles")
    assert response.status_code == 200

def test_200_events(client):
    response = client.get("/check")
    assert response.status_code == 200
