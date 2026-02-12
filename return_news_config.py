import os

def return_news_config(app_const, lang):
    """
    The entry point for the news config retrieval. It receives the launch request.
        lang(string): "en" or "zh"
    """
    
    BASE_PATH = app_const['BASE_PATH']
    
    base = BASE_PATH or ''
    news_config_path = os.path.join(base, f'{lang}_news_config.json')
    
    if not os.path.exists(news_config_path):
        raise FileNotFoundError(f"News config file not found: {news_config_path}")
    
    try:
        with open(news_config_path, 'r', encoding='utf-8') as f:
            news_config = f.read()
    except Exception as e:
        raise RuntimeError(f"Failed to read news config file: {e}")
    
    return {"data": news_config, "message": "Successfully retrieved news config"}

if __name__ == "__main__":
    sample_lang = 'zh'
    result = return_news_config({}, sample_lang)
    print(result)