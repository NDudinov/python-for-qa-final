import json

import pytest
import requests
from hamcrest import assert_that
from hamcrest import is_
from hamcrest.library.text.stringcontains import contains_string

from api.constants_api import HttpCodes
from api.constants_api import Type
from api.constants_api import local_url as url


@pytest.fixture
def add_test_book():
    print("Precondition")
    payload = {
        "type": Type.Action_and_Adventure.value,
        "title": "Conan the Barbarian",
        "creation_date": "1934-03-03"
    }
    response_post = requests.post(url + 'manipulation', json=payload)
    return json.loads(response_post.text).get("id")


@pytest.fixture
def delete_test_book(add_test_book):
    yield "Clear up"
    requests.delete(url + f'manipulation?id={add_test_book}')


class TestBookIds:
    """Class for testing BookIds(Resource) endpoint"""
    @pytest.mark.parametrize('b_type',
                             [Type.Romance, Type.Science_Fiction, Type.Satire, Type.Drama, Type.Action_and_Adventure])
    def test_get_by_type(self, b_type):
        response = requests.get(url + f'ids?book_type={b_type.value}')
        assert_that(response.status_code, is_(HttpCodes.ok))


class TestBookLatest:
    """Class for testing BookLatest(Resource) endpoint"""
    def test_get_latest(self, add_test_book, delete_test_book):
        response = requests.get(url + 'latest?limit=1')
        assert_that(response.status_code, is_(HttpCodes.ok))


class TestBookInfo:
    """Class for testing BookInfo(Resource) endpoint"""
    def test_get_by_id(self, add_test_book, delete_test_book):
        response = requests.get(url + f'info?id={add_test_book}')
        text_response = json.loads(response.text)
        assert_that(response.status_code, is_(HttpCodes.ok))
        assert_that(text_response.get("type"), is_(Type.Action_and_Adventure.value))
        assert_that(text_response.get("title"), is_("Conan the Barbarian"))
        assert_that(text_response.get("creation_date"), is_("1934-03-03"))

    def test_get_none_id(self):
        response = requests.get(url + 'info?id=1234')
        text_response = json.loads(response.text)
        assert_that(response.status_code, is_(HttpCodes.not_found))
        assert_that(text_response.get("message"), is_("There is no such book | books."))


class TestBookManipulation:
    """Class for testing BookManipulation(Resource) endpoints"""
    def test_post_manipulation(self):
        payload = {
            "type": Type.Action_and_Adventure.value,
            "title": "Captain Blood: His Odyssey",
            "creation_date": "2020-03-03"
        }
        response = requests.post(url + 'manipulation', json=payload)
        id_to_check = json.loads(response.text).get("id")
        assert_that(response.status_code, is_(HttpCodes.ok))
        assert_that(get_status_code_for_search_by_id(id_to_check), is_(HttpCodes.ok))

    def test_post_not_valid_manipulation(self):
        payload = {
        }
        response = requests.post(url + 'manipulation', json=payload)
        message = json.loads(response.text).get("message")
        assert_that(response.status_code, is_(HttpCodes.bad_request))
        assert_that(message, is_("The request is not valid."))

    def test_delete_manipulation(self, add_test_book, delete_test_book):
        response = requests.delete(url + f'manipulation?id={add_test_book}')
        assert_that(response.status_code, is_(HttpCodes.ok))
        assert get_status_code_for_search_by_id(add_test_book) == HttpCodes.not_found

    def test_delete_fail_manipulation(self):
        response = requests.delete(url + f'manipulation?id={add_test_book}')
        assert_that(response.status_code, is_(HttpCodes.not_found))

    def test_put_manipulation(self, add_test_book, delete_test_book):
        payload = {
            "type": Type.Science_Fiction.value,
            "title": "Starship Troopers"
        }
        response = requests.put(url + f'manipulation?id={add_test_book}', json=payload)
        assert_that(response.status_code, is_(HttpCodes.ok))
        assert get_status_code_for_search_by_id(add_test_book) == HttpCodes.ok

    def test_get_manipulation(self):
        response = requests.get(url + 'manipulation')
        assert_that(response.text, contains_string("No implementation for `GET` method"))


def get_status_code_for_search_by_id(id_to_find):
    response = requests.get(url + f'info?id=' + id_to_find)
    return response.status_code
