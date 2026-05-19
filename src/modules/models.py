"""function get_models()"""
def get_models(api: str) -> str:
	"""
	Returns the AI model that we are going to use for the specified LLM API Key.
	Edit this file to test other models

	Arguments:
	api (str): The LLM that we are testing

	Returns:
	str: model related with the LLM that we are testing.
	"""
	model = None
	if api == "openai":
		model = "gpt-4o" # "gpt-4o-mini"
	elif api == "anthropic":
		model = "claude-opus-4-7"
	elif api == "xai":
		model = "grok-4.3"
	elif api == "deepseek":
		model = "deepseek-reasoner"
	elif api == "gemini":
		model = "gemini-2.5-flash"

	return model
