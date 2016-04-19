from bs4 import BeautifulSoup4
import urllib

langCode={
    "arabic":"ar", "bulgarian":"bg", "chinese":"zh-CN",
    "croatian":"hr", "czech":"cs", "danish":"da", "dutch":"nl",
    "english":"en", "finnish":"fi", "french":"fr", "german":"de",
    "greek":"el", "hindi":"hi", "italian":"it", "japanese":"ja",
    "korean":"ko", "norwegian":"no", "polish":"pl", "portugese":"pt",
    "romanian":"ro", "russian":"ru", "spanish":"es", "swedish":"sv" }

def setUserAgent(userAgent):
    urllib.FancyURLopener.version = userAgent
    pass

def translate(text, fromLang, toLang):
    setUserAgent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008070400 SUSE/3.0.1-0.1 Firefox/3.0.1")
    try:
        postParameters = urllib.urlencode({"langpair":"%s|%s" %(langCode[fromLang.lower()],langCode[toLang.lower()]), "text":text,"ie":"UTF8", "oe":"UTF8"})
    except KeyError, error:
        print "Currently we do not support %s" %(error.args[0])
        return

    page = urllib.urlopen("http://translate.google.com/translate_t", postParameters)
    content = page.read()
    page.close()

    htmlSource = BeautifulSoup(content)
    translation = htmlSource.find('span', title=text )
    return translation.renderContents()

print translate("Good morning to you friend!", "English", "German")
print translate("Good morning to you friend!", "English", "Italian")
print translate("Good morning to you friend!", "English", "Spanish")
print translate("Good morning to you friend!", "English", "Russian")
print translate("Good morning to you friend!", "English", "Greek")