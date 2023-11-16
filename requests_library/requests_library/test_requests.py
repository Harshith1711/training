import requests
import pytest

@pytest.mark.get
def test_get():
    """
    Test the GET request to retrieve a single post from the JSONPlaceholder API.
    """
    # Sending a simple GET request
    get_request = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    # Accessing response content
    print("GET request test:", get_request.text)
    print("GET request json body:", get_request.json())
    print("GET request status code:", get_request.status_code)

    assert get_request.status_code == 200


@pytest.mark.get
def test_get_all():
    """
    Test the GET request to retrieve all posts from the JSONPlaceholder API.
    """
    # Sending a simple GET request
    get_request = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Accessing response content
    print("GET request test:", get_request.text)
    print("GET request json body:", get_request.json())
    print("GET request status code:", get_request.status_code)

    assert get_request.status_code == 200


@pytest.mark.post
def test_post():
    """
    Test the POST request to create a new post on the JSONPlaceholder API.
    """
    # Sending a simple POST request
    post_request = requests.post("https://jsonplaceholder.typicode.com/posts")

    print("POST response:", post_request.json())
    print("POST status:", post_request.status_code)
    print("POST request text:", post_request.text)
    assert post_request.status_code == 201


@pytest.mark.patch
def test_patch():
    """
    Test the PATCH request to update a post on the JSONPlaceholder API.
    """
    # Sending a simple PATCH request
    payload = {'body': "a new body after Patch Request", 'title': "Hello"}
    patch_request = requests.patch("https://jsonplaceholder.typicode.com/posts/1", payload)

    print("PATCH response:", patch_request.json())
    print("PATCH status code:", patch_request.status_code)
    print("PATCH text:", patch_request.text)

    assert patch_request.status_code == 200


@pytest.mark.delete
def test_delete():
    """
    Test the DELETE request to delete a post on the JSONPlaceholder API.
    """
    # Deleting the PATCH request by Delete method
    delete_request = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

    print("DELETE request status code:", delete_request.status_code)
    print("DELETE request json:", delete_request.json())
    print("DELETE request text:", delete_request.text)

    assert delete_request.status_code == 200
