import pytest
import requests
from flask import Flask

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, get_city_suggestions


# Function to create a test client for the Flask app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Mock function for the Geoapify API call
def mock_get_city_suggestions(query):
    return ['Baku', 'Bari', 'Barcelona', 'Barnaul']


# Test the get_city_suggestions function directly
def test_get_city_suggestions(monkeypatch):
    # Use the mock function instead of the real API call
    monkeypatch.setattr('app.get_city_suggestions', mock_get_city_suggestions)

    result = get_city_suggestions('Ba')
    assert result == ['Baku', 'Bari', 'Barcelona', 'Barnaul']


# Test the autocomplete endpoint
def test_autocomplete(client, monkeypatch):
    # Use the mock function instead of the real API call
    monkeypatch.setattr('app.get_city_suggestions', mock_get_city_suggestions)

    response = client.get('/autocomplete?q=Ba')
    assert response.status_code == 200
    assert response.json == ['Baku', 'Bari', 'Barcelona', 'Barnaul']