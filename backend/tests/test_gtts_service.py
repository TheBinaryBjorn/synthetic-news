from backend.services.tts_service import gTTS_Service
import os

def test_constructor_creates_gtts_service_object(tmp_path,monkeypatch):
    """
        Test ID: TC-001
        Test Objective: Verify that the constructor successfully creates an object.
    """
    # Temporarily change the current working directory to isolate the test.
    monkeypatch.chdir(tmp_path)
    # Create instance of the class
    gtts_service = gTTS_Service()

    # Assert that the created object is an instance of the class gTTS_Service.
    assert isinstance(gtts_service, gTTS_Service)

def test_constructor_creates_generated_audio_dir(tmp_path,monkeypatch):
    """
        Test ID: TC-002
        Test Objective: Verify that the constructor successfully creates a 'generated_audio' directory.
    """
    monkeypatch.chdir(tmp_path)

    # Check that no dir by the name generated_audio exists
    assert not os.path.isdir("generated_audio")

    # Create an instance of gTTS_Service()
    service = gTTS_Service()

    # Assert that the generated_audio directory was created.
    assert os.path.isdir("generated_audio")
