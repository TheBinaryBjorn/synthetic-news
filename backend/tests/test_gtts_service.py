"""
This module contains unit tests for the gTTS_Service class.
It verifies the correct behavior of the constructor and its effects on the file system.
"""

import os
import re

import pytest
from gtts import gTTS

from ..services.tts_service import GoogleTtsService


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


def test_convert_text_to_speech_returns_valid_gtts_object(tmp_path, monkeypatch):
    """
    Test ID: TC-004
    Test Objective: Verify that the method convert_text_to_speech
    returns a valid gTTS object.
    """
    # Arrange
    monkeypatch.chdir(tmp_path)

    google_tts_service = GoogleTtsService()

    # Act
    gtts_object = google_tts_service.convert_text_to_speech("Test String")

    # Assert
    assert isinstance(gtts_object, gTTS)


def test_create_mp3_file_creates_mp3_file(tmp_path, monkeypatch):
    """
    Test ID: TC-005
    Test Objective: Verify that the method create_mp3_file
    creates an mp3 file.
    """

    # Arrange
    monkeypatch.chdir(tmp_path)
    google_tts_service = GoogleTtsService()

    # Act
    filepath = google_tts_service.create_mp3("Test Topic", "Test Text")

    # Assert
    assert os.path.exists(filepath)


def test_create_mp3_with_existing_file_returns_same_path(tmp_path, monkeypatch):
    """
    Test ID: TC-006
    Test Objective: Verify that calling create_mp3 twice returns the same path
    without recreating the file.
    """
    # Arange
    monkeypatch.chdir(tmp_path)
    google_tts_service = GoogleTtsService()

    # Act
    first_filepath = google_tts_service.create_mp3("Test Topic", "Test Text")
    second_filepath = google_tts_service.create_mp3("Test Topic", "Test Text")

    # Assert
    assert first_filepath == second_filepath


def test_create_mp3_generates_expected_filename_format(tmp_path, monkeypatch):
    """
    Test ID: TC-007
    Test Objective: Verify the filename follows the expected pattern with
    timestamp.
    """
    # Arange
    monkeypatch.chdir(tmp_path)
    google_tts_service = GoogleTtsService()

    # Act
    filepath = google_tts_service.create_mp3("Test Topic", "Test Text")
    filename = os.path.basename(filepath)

    # Assert
    assert re.fullmatch(r"Test Topic - \[(\d{1,2}-\d{4})\] - Audio\.mp3", filename)


def test_convert_text_to_speech_with_empty_string(tmp_path, monkeypatch):
    """
    Test ID: TC-008
    Test Objective: Verify behavior with empty string input.
    """
    # Arrange
    monkeypatch.chdir(tmp_path)
    google_tts_service = GoogleTtsService()

    # Act & Assert
    with pytest.raises(ValueError):
        google_tts_service.convert_text_to_speech("")


def test_create_mp3_raises_exception_on_non_string_topic(tmp_path, monkeypatch):
    """
    Test ID: TC-009
    Test Objective: Verify that the method create mp3 raises a type error
    on non string inputs for topic
    """
    # Arange
    monkeypatch.chdir(tmp_path)
    google_tts_service = GoogleTtsService()

    # Act & Assert
    with pytest.raises(TypeError):
        google_tts_service.create_mp3(-1, "Test String")

    with pytest.raises(TypeError):
        google_tts_service.create_mp3(None, "Test String")

    with pytest.raises(TypeError):
        google_tts_service.create_mp3([1, 2, 3], "Test String")


def test_create_mp3_raises_exception_on_non_string_text(tmp_path, monkeypatch):
    """
    Test ID: TC-010
    Test Objective: Verify that the method create mp3 raises a type error
    on non string inputs for text
    """
    # Arange
    monkeypatch.chdir(tmp_path)
    google_tts_service = GoogleTtsService()

    # Act & Assert
    with pytest.raises(TypeError):
        google_tts_service.create_mp3("Test Topic", -1)

    with pytest.raises(TypeError):
        google_tts_service.create_mp3("Test Topic", None)

    with pytest.raises(TypeError):
        google_tts_service.create_mp3("Test Topic", [1, 2, 3])


def test_create_mp3_raises_value_error_on_empty_topic(tmp_path, monkeypatch):
    """
    Test ID: TC-011
    Test Objective: Verify that the method create_mp3 raises a ValueError
    on empty string input for topic
    """
    # Arange
    monkeypatch.chdir(tmp_path)
    google_tts_service = GoogleTtsService()
    # Act
    with pytest.raises(ValueError):
        google_tts_service.create_mp3("", "Test Text")


def test_create_mp3_raises_value_error_on_empty_text(tmp_path, monkeypatch):
    """
    Test ID: TC-012
    Test Objective: Verify that the method create_mp3 raises a ValueError
    on empty string input for text
    """
    # Arange
    monkeypatch.chdir(tmp_path)
    google_tts_service = GoogleTtsService()
    # Act & Assert
    with pytest.raises(ValueError):
        google_tts_service.create_mp3("Test Topic", "")
