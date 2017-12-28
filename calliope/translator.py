import json
import urllib2
from urllib import quote
import textwrap

import settings


class Translator:
    """"""

    def __init__(self, lang_from='en', lang_to='zh'):
        """"""
        self.lang_from = lang_from
        self.lang_to = lang_to


    def translate(self, text):
        """"""
        if self.lang_from == self.lang_to:
            return text

        self.text_list = textwrap.wrap(text, 1000, replace_whitespace=False)
        return ' '.join(self._translate_from_webapi(s) for s in self.text_list)


    def _translate_from_webapi(self, text):
        """"""
        text = quote(text, '')
        url = settings.TRANSLATOR_URL % (text, self.lang_from, self.lang_to)
        request = urllib2.Request(url=url, headers=settings.TRANSLATOR_HEADERS)
        content = urllib2.urlopen(request).read().decode('utf-8')
        return json.loads(content)['responseData']['translatedText']


if __name__ == '__main__':
    translator = Translator()
    word = translator.translate("This is a pen.")
    print word
