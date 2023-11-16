```markdown
# API Testing with requests and pytest

This project contains automated tests using the `requests` library and `pytest` for testing various HTTP methods on the JSONPlaceholder API.

## Description

This project demonstrates how to use Python's `requests` library along with `pytest` for testing different HTTP methods on the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API. The tests cover GET, POST, PATCH, and DELETE requests.

## Usage

Run the tests using pytest. To run specific markers, use the `-k` option:

```bash
pytest -k "get"
```

Replace `"get"` with the marker you want to run.