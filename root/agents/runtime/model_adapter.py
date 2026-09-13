from typing import Any, Dict, Optional


class LocalModelAdapter:
    """A lightweight local adapter that can use transformers when available.

    It is intentionally repository-local and never imports an external AI
    agent implementation. If the transformers stack is not available, the
    adapter safely falls back to a deterministic placeholder response.
    """

    def __init__(self, model_name: str = "distilgpt2", provider: Optional[str] = None):
        self.model_name = model_name
        self.provider = provider or "local-placeholder"
        self._pipeline = None

    def _load_pipeline(self):
        try:
            from transformers import pipeline
        except Exception:
            return None

        try:
            if self._pipeline is None:
                self._pipeline = pipeline(
                    "text-generation",
                    model=self.model_name,
                    tokenizer=self.model_name,
                    device=-1,
                )
            return self._pipeline
        except Exception:
            return None

    def generate(self, prompt: str, **kwargs: Any) -> str:
        """Generate a response through an optional local transformers pipeline,
        otherwise return a deterministic placeholder phrase.
        """
        normalized = prompt.strip()
        if not normalized:
            return "I need a clearer request."

        try:
            pipeline = self._load_pipeline()
            if pipeline is not None:
                generated = pipeline(
                    normalized,
                    max_new_tokens=16,
                    do_sample=False,
                    num_return_sequences=1,
                )
                if generated and isinstance(generated, list):
                    return generated[0].get("generated_text", normalized)
        except Exception:
            pass

        return (
            f"Model={self.model_name} provider={self.provider} processed request: "
            f"{normalized[:180]}"
        )
