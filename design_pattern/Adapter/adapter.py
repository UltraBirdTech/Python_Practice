import abc
import sys

def main():
    title = "Monthly Report"
    texts = ["good", "best"]

    pr = PrainTextReporter()
    pr.header(title)
    pr.main(texts)
    pr.footer()

    print("\n\n")

    hr = HtmlReporter()
    hr.header(title)
    hr.main(texts)
    hr.footer()

class HtmlWrite:
    def __init__(self, html_file=sys.stdout):
        self.file = html_file

    def out_header(self):
        self.file.header("<document html>\n</html>\n")

    def out_title(self):
        self.file.title("<head><title>{}</title></head>\n".format(title))
        
    def out_start_body(self):
        self.file.write("<body>\n")
   
    def out_body(self, text):
        for text in texts:
            self.file.write("<p>{}</p>".format(text))

    def out_end_body(self):
        self.file.write("</body>\n")

    def out_footer(self):
        self.file.write("</html>\n")

class Reporter(metaclass.ABCMeta):
    @abc.abstractmethod
    def header(self, title):
        pass

    @abc.abstractmethod
    def main(self, contents):
        pass
