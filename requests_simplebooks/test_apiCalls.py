from data import postOrder, patchOrder
from simplebooks import RestAPIMethods


def test_get_request_status_code():
    obj = RestAPIMethods()
    obj.token(url="api-clients/")
    response = obj.get_req("books")
    assert response.status_code == 200


def test_post_request_status_code():
    obj = RestAPIMethods()
    obj.token(url="api-clients/")
    response = obj.post_req("/orders", postOrder())
    assert response.status_code == 201


def test_get_request_after_post():
    obj = RestAPIMethods()
    obj.token(url="api-clients/")
    obj.post_req("/orders", postOrder())
    response = obj.get_req("orders")
    assert response.status_code == 200


def test_patch_request_status_code():
    obj = RestAPIMethods()
    obj.token(url="api-clients/")
    obj.post_req("/orders", postOrder())
    orderId = obj.post_req("/orders", postOrder()).json().get('orderId')
    update_url = 'orders/' + orderId
    response = obj.update_req(update_url, patchOrder())
    assert response.status_code == 204


def test_get_request_after_patch():
    obj = RestAPIMethods()
    obj.token(url="api-clients/")
    obj.post_req("/orders", postOrder())
    orderId = obj.post_req("/orders", postOrder()).json().get('orderId')
    update_url = 'orders/' + orderId
    obj.update_req(update_url, patchOrder())
    response = obj.get_req(update_url)
    assert response.status_code == 200


def test_delete_request_status_code():
    obj = RestAPIMethods()
    obj.token(url="api-clients/")
    obj.post_req("/orders", postOrder())
    orderId = obj.post_req("/orders", postOrder()).json().get('orderId')
    update_url = 'orders/' + orderId
    response = obj.delete_req(update_url)
    assert response.status_code == 200
