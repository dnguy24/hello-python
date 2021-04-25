def test_main(client):
    resp = client.get("/")
    assert resp.status_code == 200
    print(resp.get_data())