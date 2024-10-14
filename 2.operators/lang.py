from googletrans import Translator


def translate_test(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text


if __name__ == "__main__":
    input_text = "hello kiran"
    source_language = "en"
    target_language = "es"
    translated_test = translate_test(input_text, source_language, target_language)

    print(f"originl test : {input_text}")
    print(f"translated text : {translated_test}")
