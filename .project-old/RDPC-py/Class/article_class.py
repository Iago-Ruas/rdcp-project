import uuid
from schemas import ArticleCreator


class Article(ArticleCreator):
    def __init__(self):

        self._id = uuid.uuid4()
        self.user_id = None

        self._title_pt = None
        self._title_en = None
        self._title_es = None

        self._summary_pt = None
        self._summary_en = None
        self._summary_es = None

        self.two_sentences__summary_pt = None
        self.two_sentences__summary_en = None
        self.two_sentences__summary_es = None

        self._key_word_pt = None
        self._key_word_en = None
        self._key_word_es = None

        self._full_article_pt = None
        self._full_article_en = None
        self._full_article_es = None

        self.doc_full_article: bytes = None


class ArticleBuider:

    def __init__(self):
        self._article: Article = Article()

    # Id
    def UserId(self, user_id: str):
        if user_id is None or user_id is "":
            raise "User ID is null"

    # Title:
    def SetTitlePt(self, title: str):
        if title is None or title == "":
            raise "Title PT is Empty or is Null."

        self._article._title_pt = title
        return self

    def SetTitleEn(self, title: str):
        if title is None or title == "":
            raise "Title EN is Empty or is Null."

        self._article._title_en = title
        return self

    def SetTitleEs(self, title: str):
        if title is None or title == "":
            raise "Title ES is Empty or is Null."
        self._article._title_es = title
        return self

    # summary:
    def SetsummaryPt(self, summary: str):
        if summary is None or summary == "":
            raise "summary in PT is Empty or is Null."

        self._article._summary_pt = summary
        return self

    def SetsummaryEn(self, summary: str):
        if summary is None or summary == "":
            raise "summary in EN  is Empty or is Null."

        self._article._summary_en = summary
        return self

    def SetsummaryEs(self, summary: str):
        if summary is None or summary == "":
            raise "summary in ES is Empty or is Null."

        self._article._summary_es = summary
        return self

    # Two sentences summary
    def SetTwoSentencessummaryPT(self, summary: str):
        if summary is None or summary == "":
            raise "Two sentences summary in PT is Empty or is Null."
        self._article.two_sentences__summary_pt = summary
        return self

    def SetTwoSentencessummaryEn(self, summary: str):
        if summary is None or summary == "":
            raise "Two sentences summary in PT is Empty or is Null."
        self._article.two_sentences__summary_en = summary
        return self

    def SetTwoSentencessummaryEs(self, summary: str):
        if summary is None or summary == "":
            raise "Two sentences summary in PT is Empty or is Null."
        self._article.two_sentences__summary_es = summary
        return self

    # Keywords
    def SetKeyWordPt(self, key: str):
        if key is None or key == "":
            raise "Keyword in PT is Empty or is Null."
        self._article._key_word_pt = key
        return self

    def SetKeyWordEn(self, key: str):
        if key is None or key == "":
            raise "Keyword in EN is Empty or is Null."
        self._article._key_word_en = key
        return self

    def SetKeyWordEs(self, key: str):
        if key is None or key == "":
            raise "Keyword in ES is Empty or is Null."
        self._article._key_word_es = key
        return self

    # Full article
    def SetFullArticlePt(self, article: str):
        if article is None or article == "":
            raise "Article in PT is Empty or is Null."
        self._article._full_article_pt = article
        return self

    def SetFullArticleEn(self, article: str):
        if article is None or article == "":
            raise "Article in EN is Empty or is Null."
        self._article._full_article_en = article
        return self

    def SetFullArticleEs(self, article: str):
        if article is None or article == "":
            raise "Article in ES is Empty or is Null."
        self._article._full_article_es = article
        return self

    # Biuld
    def Build(self):
        return self._article
