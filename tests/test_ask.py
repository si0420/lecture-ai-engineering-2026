"""第1回スクリプトの検証。"""

from types import SimpleNamespace
from unittest.mock import patch

from app.ask import ask


def test_ask_prints_input_and_output_token_counts(capsys):
    response = SimpleNamespace(
        text="応答本文",
        usage_metadata=SimpleNamespace(
            prompt_token_count=12,
            candidates_token_count=34,
        ),
    )

    with (
        patch("app.ask.get_api_key", return_value="test-key"),
        patch("app.ask.genai.Client") as client,
    ):
        client.return_value.models.generate_content.return_value = response

        assert ask("質問") == "応答本文"

    assert capsys.readouterr().out == "[tokens] input=12, output=34\n"
