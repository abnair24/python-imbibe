import click.testing
import pytest
import requests

from python_imbibe import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem",
        "extract": "Ipsum",
    }
    return mock


def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_mock_title(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert "Lorem" in result.output


def test_main_mock_invokes_request(runner, mock_requests_get):
    runner.invoke(console.main)
    assert mock_requests_get.called
