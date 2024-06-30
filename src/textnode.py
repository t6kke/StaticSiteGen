
class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, tn):
        if self.text == tn.text and self.text_type == tn.text_type and self.url == tn.url:
            return True
        return False

    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type}, {self.url})")
