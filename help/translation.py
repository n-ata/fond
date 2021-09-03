from help.models import *
from modeltranslation.translator import register, TranslationOptions

@register(Menu)
class MenuTranslationOptions(TranslationOptions):
	fields = ('name',)

@register(Home)
class HomeTranslationOptions(TranslationOptions):
	fields = ('title', 'text')

@register(About)
class AboutTranslationOptions(TranslationOptions):
	fields = ('title', 'text')

@register(Helping)
class HelpingTranslationOptions(TranslationOptions):
	fields = ('title', 'text')

@register(Fond)
class FondTranslationOptions(TranslationOptions):
	fields = ('title', 'text')

@register(Blogs)
class BlogsTranslationOptions(TranslationOptions):
	fields = ('title', 'text')

@register(BlogDetailsOther)
class BlogDetailsOtherTranslationOptions(TranslationOptions):
	fields = ('blogdetails', 'newsletter', 'enteremail', 'subscribe', 'recentposts')

@register(Others)
class OthersTranslationOptions(TranslationOptions):
	fields = ('makeadonation', 'aboutus', 'discoverme', 'helpingtoday', 'howwehelppeople', 'programs', 'ourdonationprograms', 'news', 'latestblog', 'footertext', 'navigation', 'contactus', 'address', 'support', 'supporttext', 'donate', 'copyright', 'goal', 'raised', 'email', 'readmore')