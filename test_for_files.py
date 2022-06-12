import pytest
import shutil
from functions import get_function

prettify_html_file = get_function()


@pytest.fixture(autouse=True)
def clean_file():
    shutil.copy('fixtures/before.html', 'fixtures/before2.html')
    shutil.copy('fixtures/after.html', 'fixtures/after2.html')
    yield


def open_and_read_file(with_links_path):
    with open(with_links_path, encoding='utf8') as f:
        html = f.read()
    return html


def test_format_html():
    assert open_and_read_file('fixtures/before2.html') != open_and_read_file('fixtures/after2.html')
    prettify_html_file('fixtures/before2.html')
    assert open_and_read_file('fixtures/before2.html') == open_and_read_file('fixtures/after2.html')
