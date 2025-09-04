"""
This module is in charge of test the Gemini Writer
Service class.
"""

from unittest.mock import Mock

import pytest

from ..services.llm_service import LlmService
from ..services.script_writer_service import GeminiWriterService


# Test constructor
def test_constructor_works_with_valid_input():
    """
    Test ID: TC-024
    Objective: Verify that the GeminiWriterService
    constructor functions well with good input.
    """
    # Arrange
    mock_llm_service = Mock(spec=LlmService)

    # Act
    script_writer_service = GeminiWriterService(mock_llm_service)

    # Assert
    assert script_writer_service.llm_service is mock_llm_service


def test_constructor_returns_type_error_with_non_llm_service_object():
    """
    Test ID: TC-025
    Objective: Verify that the GeminiWriterService constructor
    raises a TypeError when instansiated with non LlmService object.
    """
    with pytest.raises(TypeError):
        GeminiWriterService([1, 2, 3])

    with pytest.raises(TypeError):
        GeminiWriterService(-1)

    with pytest.raises(TypeError):
        GeminiWriterService("String")


def test_llm_service_of_object_is_an_llm_service():
    """
    Test ID: TC-026
    Objective: Verify that the given LllmService object
    remains an LlmService object in the field llm_service
    of the class
    """
    # Arrange
    mock_llm_service = Mock(spec=LlmService)

    # Act
    script_writer_service = GeminiWriterService(mock_llm_service)

    # Assert
    assert isinstance(script_writer_service.llm_service, LlmService)

VALID_TOPIC = "Artificial Intelligence"
VALID_RESEARCH_TEXT = """
Here's a summary of the most recent Artificial Intelligence news from the last week, with a focus on today, August 21, 2025:

**Breaking News (August 21, 2025):**

*   **OpenAI's Valuation Soars Amid GPT-5 Launch:** OpenAI is reportedly in talks to sell $6 billion in shares,
    potentially pushing its valuation to over $500 billion. This comes after the launch of their flagship model, GPT-5, and the open-weight models, GPT-OSS.
    However, GPT-5 has received mixed reviews, with some users criticizing its new "friendly" tone as less efficient. (Source: Dwealth.news, Medium)
*   **Nvidia Shares Slip Amid AI Boom Concerns:** Nvidia's stock has dipped, with analysts warning of a potential "AI bubble."
This caution is fueled by the lukewarm reception of GPT-5 and broader concerns about overheating markets. (Source: Dwealth.news)
*   **Chinese Startup DeepSeek Releases Upgraded AI Model:** Reuters reported today that Chinese startup DeepSeek has released an upgraded AI model. (Source: Reuters)

**Other Recent AI News (Last Week):**

*   **Meta Pauses AI Hiring:** Meta has reportedly paused AI hiring after aggressively recruiting top researchers from rivals like OpenAI and Google.
The company is restructuring its AI division into four specialized units, aiming to build "superintelligence" systems.
This move comes amidst broader tech market volatility and investor concerns about compensation costs. (Source: Ainvest.com)
*   **AI Funding and Innovation:**
    *   AI crawler Firecrawl raised $14.5 million and is still looking to hire agents as employees.
    *   Eight Sleep raised $100 million to expand its AI-powered sleep technology.
    *   OpenAI launched a sub-$5 ChatGPT plan in India.
    *   Anthropic bundled Claude Code into its enterprise plans. (Source: TechCrunch)

This week has seen significant developments in the AI landscape,
with major players like OpenAI and Meta making headlines regarding their valuations, product launches, and strategic shifts.
The market is also showing signs of caution, particularly concerning the rapid growth and investment in the AI sector.
"""
VALID_PODCAST_SCRIPT = """
Hello there. Welcome to Synthetic News.
I am your host Cynthia. That is Cynthia with an S.
Today we are talking all about artificial intelligence. You know, it is really a big topic right now.

First up, let's talk about OpenAI. They are talking about selling a lot of shares. About six billion dollars worth, actually.
This could make their company worth over five hundred billion dollars. That is a huge number, you know. This news comes after they launched their main model.
It is called G P T five. They also launched other models. These are called G P T hyphen O S S. However, G P T five has gotten mixed reviews.
Some users are saying its new friendly tone is not as good. They say it is less efficient.

Next, let's look at Nvidia shares. Their stock has dipped a bit. Experts are warning about a possible artificial intelligence bubble.
This caution is fueled by G P T five not being totally loved. It is also because of broader worries about the markets heating up too much.

Also, we have news from a Chinese startup. This company is called DeepSeek.
They have released an upgraded artificial intelligence model. That is big news today.

Now, let's look at some other artificial intelligence news from the last week.

Meta has paused its artificial intelligence hiring. They were really aggressive before. They hired top researchers from companies like OpenAI and Google.
Now, Meta is changing things. They are dividing their artificial intelligence division. It will have four specialized units.
Their goal is to build super intelligence systems. This move comes when the tech market is a bit shaky.
Investors are also worried about how much they are paying people.

Finally, let's talk about artificial intelligence funding and new things.

An artificial intelligence company called Firecrawl raised fourteen point five million dollars. They are actually still looking to hire more people.

Another company, Eight Sleep, raised one hundred million dollars. They want to expand their artificial intelligence powered sleep technology. That sounds interesting.
OpenAI launched a new C H A T G P T plan in India. It costs less than five dollars. That is very affordable.
And Anthropic bundled their Claude Code into its business plans. This is for their bigger customers.

This week has really seen big things happen in artificial intelligence. Major companies like OpenAI and Meta are making headlines. This is about their company worth.
It is about new products. It is about big changes they are making. The market is also showing some caution. This is especially true about the fast growth.
It is about all the money going into the artificial intelligence area.

That is your update for today. See you tomorrow.
"""


# Test Generate Podcast Method:
def test_generate_podcast_script_method_works_with_valid_input():
    """
    Test ID: TC-027
    Objective: Verify that the method generates a podcast script
    with valid topic and text
    """
    # Arrange
    mock_llm_service = Mock(spec=LlmService)
    gemini_writer_service = GeminiWriterService(mock_llm_service)
    mock_llm_service.send_message_to_llm.return_value = VALID_PODCAST_SCRIPT

    # Act
    podcast_script = gemini_writer_service.generate_podcast_script(VALID_TOPIC, VALID_RESEARCH_TEXT)

    # Assert
    assert podcast_script == VALID_PODCAST_SCRIPT
