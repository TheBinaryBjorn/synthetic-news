"""
This Module is in charge of testing the file llm_service,
including GeminiService class.
"""
from unittest.mock import Mock

import pytest
from google import genai

from backend.services.exceptions import LlmMessageException
from backend.services.llm_service import GeminiService

DEFAULT_MODEL = "gemini-2.5-flash"
CUSTOM_MODEL = "gemini-1.5-pro"
NOT_ALLOWED_MODEL = "deepseek-r1"
VALID_MESSAGE = "Hello, this is a test message!"
MOCK_RESPONSE_MESSAGE = "Mocked LLM response."


def test_constructor_with_valid_input():
    """
    Test ID: TC-013
    Objective: Verify that the constructor works
    well with valid input.
    """
    # Arrange
    mock_client = Mock(spec=genai.Client)
    model = DEFAULT_MODEL

    # Act
    llm_service_object = GeminiService(mock_client, model)

    # Assert
    assert llm_service_object.client is mock_client
    assert llm_service_object.model == model


def test_constructor_with_only_client_specified():
    """
    Test ID: TC-014
    Objective: Verify that the constructor sets the
    model to the default model when not specified.
    """
    # Arrange
    mock_client = Mock(spec=genai.Client)

    # Act
    llm_service_object = GeminiService(mock_client)

    # Assert
    assert llm_service_object.client is mock_client
    assert llm_service_object.model == DEFAULT_MODEL


def test_constuctor_with_not_allowed_model():
    """
    Test ID: TC-015
    Objective Verify that the constructor throws a value error
    when the given model is not in the allowed models list
    """
    # Arrange
    mock_client = Mock(spec=genai.Client)
    custom_model = NOT_ALLOWED_MODEL

    # Act and Assert
    with pytest.raises(ValueError):
        GeminiService(mock_client, custom_model)


def test_constructor_raises_type_error_on_invalid_client():
    """
    Test ID: TC-016
    Objective: Verify that the constructor raises
    a TypeError on invalid client
    """
    # Assert
    with pytest.raises(TypeError):
        GeminiService([])

    with pytest.raises(TypeError):
        GeminiService(-1)

    with pytest.raises(TypeError):
        GeminiService("string")


def test_constructor_raises_type_error_on_invalid_model():
    """
    Test ID: TC-017
    Objective: Verify that the constructor raises a type
    error when using non string model
    """
    # Arrange
    client = Mock(spec=genai.Client)
    with pytest.raises(TypeError):
        GeminiService(client, -1)
    with pytest.raises(TypeError):
        GeminiService(client, [1, 2, 3])
    with pytest.raises(TypeError):
        GeminiService(client, None)


def test_constructor_raises_value_error_on_model_empty_string():
    """
    Test ID: TC-018
    Objective: verify that the constructor raises a value error
    when an empty string model is entered.
    """
    # Arrange
    client = Mock(spec=genai.Client)
    model = ""
    with pytest.raises(ValueError):
        GeminiService(client, model)


def test_constructor_raises_value_error_on_whitespace_string():
    """
    Test ID: TC-019
    Objective: verify that the constructor raises a value error
    when an empty string model is entered.
    """
    # Arrange
    client = Mock(spec=genai.Client)
    model = " "
    with pytest.raises(ValueError):
        GeminiService(client, model)


def test_send_message_to_llm_with_valid_text():
    """
    Test ID: TC-020
    Objective: Verify that the method send message to llm
    works with good input.
    """
    # Arrange
    mock_client = Mock(spec=genai.Client)
    mock_response = Mock()
    mock_response.text = MOCK_RESPONSE_MESSAGE

    mock_client.models.generate_content.return_value = mock_response

    llm_service_object = GeminiService(mock_client)

    # Act
    response = llm_service_object.send_message_to_llm(VALID_MESSAGE)

    mock_client.models.generate_content.assert_called_once_with(
        model=DEFAULT_MODEL, contents=VALID_MESSAGE
    )

    assert response == MOCK_RESPONSE_MESSAGE


def test_send_message_to_llm_raises_llm_message_exception_when_fails():
    """
    Test ID: TC-021
    Objective: Verify that the method send message to llm
    raises a LlmMessageException when it fails to send
    a message to the llm.
    """
    # Arrange
    mock_client = Mock(spec=genai.Client)
    mock_client.models.generate_content.side_effect = LlmMessageException
    llm_service_objcet = GeminiService(mock_client)

    # Act and Assert
    with pytest.raises(LlmMessageException):
        llm_service_objcet.send_message_to_llm(VALID_MESSAGE)

def test_send_message_to_llm_with_invalid_text_raises_type_error():
    """
    Test ID: TC-021
    Objective: Verify that the method send message to llm
    works throws a type error on non string input.
    """
    # Arrange
    mock_client = Mock(spec=genai.Client)
    llm_service_object = GeminiService(mock_client)

    # Act
    with pytest.raises(TypeError):
        llm_service_object.send_message_to_llm([])

    with pytest.raises(TypeError):
        llm_service_object.send_message_to_llm(-1)
    
    with pytest.raises(TypeError):
        llm_service_object.send_message_to_llm(None)

def test_send_message_to_llm_with_empty_string_text_raises_value_error():
    """
    Test ID: TC-021
    Objective: Verify that the method send message to llm
    works throws a value error on empty string input.
    """
    # Arrange
    mock_client = Mock(spec=genai.Client)
    llm_service_object = GeminiService(mock_client)

    # Act
    with pytest.raises(ValueError):
        llm_service_object.send_message_to_llm("")

def test_send_message_to_llm_with_whitespace_string_text_raises_value_error():
    """
    Test ID: TC-021
    Objective: Verify that the method send message to llm
    works throws a value error on empty string input.
    """
    # Arrange
    mock_client = Mock(spec=genai.Client)
    llm_service_object = GeminiService(mock_client)

    # Act
    with pytest.raises(ValueError):
        llm_service_object.send_message_to_llm("   ")

def test_send_message_to_llm_throws_llm_message_error_on_bad_response():
    """
    Test ID: TC-023
    Objective: Verify that the method send message to llm
    raises an LlmMessageError on bad response
    """
    # Arrange
    mock_client = Mock(spec=genai.Client)
    mock_client.models.generate_content.return_value = None
    llm_service_object = GeminiService(mock_client)

    with pytest.raises(LlmMessageException, match="Failed to extract response."):
        llm_service_object.send_message_to_llm(VALID_MESSAGE)

def test_send_message_to_llm_throws_llm_message_error_on_empty_response():
    """
    Test ID: TC-023
    Objective: Verify that the method send message to llm
    raises an LlmMessageError on bad response
    """
    # Arrange
    mock_client = Mock(spec=genai.Client)
    mock_response = Mock()
    mock_response.text = ""
    mock_client.models.generate_content.return_value = mock_response
    llm_service_object = GeminiService(mock_client)

    with pytest.raises(LlmMessageException, match="Error: Empty LLM response."):
        llm_service_object.send_message_to_llm(VALID_MESSAGE)