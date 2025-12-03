pipeline_config = {
    "steps": {
        "tokenization": {"enabled": True, "method": "word"},
        "stopwords": {"enabled": True, "language": "english", "custom_words": []},
        "stemming": {"enabled": False, "algorithm": "porter"},
        "normalization": {"enabled": True, "lowercase": True, "remove_punct": True}
    },
    "input_encoding": "utf-8",
    "output_format": "tokens"
}