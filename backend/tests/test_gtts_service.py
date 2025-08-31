"""
This module contains unit tests for the gTTS_Service class.
It verifies the correct behavior of the constructor and its effects on the file system.
"""

import os

import pytest

from backend.services.tts_service import GoogleTtsService


def test_constructor_creates_gtts_service_object(tmp_path, monkeypatch):
    """
    Test ID: TC-001
    Test Objective: Verify that the constructor successfully creates an object.
    """
    # Temporarily change the current working directory to isolate the test.
    monkeypatch.chdir(tmp_path)
    # Create instance of the class
    gtts_service = GoogleTtsService()

    # Assert that the created object is an instance of the class gTTS_Service.
    assert isinstance(gtts_service, GoogleTtsService)


def test_constructor_creates_generated_audio_dir(tmp_path, monkeypatch):
    """
    Test ID: TC-002
    Test Objective: Verify that the constructor successfully creates a
    'generated_audio' directory.
    """
    monkeypatch.chdir(tmp_path)

    # Check that no dir by the name generated_audio exists
    assert not os.path.isdir("generated_audio")

    # Create an instance of gTTS_Service()
    GoogleTtsService()

    # Assert that the generated_audio directory was created.
    assert os.path.isdir("generated_audio")


def test_convert_text_to_speech_returns_exception_on_non_string(tmp_path, monkeypatch):
    """
    Test ID: TC-003
    Test Objective: Verify that the method convert_text_to_speech
    throws a TypeError when receiving a non string argument.
    """
    monkeypatch.chdir(tmp_path)

    google_tts_service = GoogleTtsService()

    with pytest.raises(TypeError):
        google_tts_service.convert_text_to_speech(-1)

    with pytest.raises(TypeError):
        google_tts_service.convert_text_to_speech(None)

    with pytest.raises(TypeError):
        google_tts_service.convert_text_to_speech([1, 2, 3])

def test_convert_text_to_speech_returns_valid_gTTS_object(tmp_path, monkeypatch):
    """
    Test ID: TC-004
    Test Objective: Verify that the method convert_text_to_speech
    returns a valid gTTS object.
    """
    pass

def test_create_mp3_file_creates_mp3_file(tmp_path, monkeypatch):
    pass
