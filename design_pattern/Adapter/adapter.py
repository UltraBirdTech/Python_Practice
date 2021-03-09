import abc
import sys

def main():
    title = "Monthly Report"
    texts = ["good", "best"]

    pr = PlainTextReporter()
    pr.header(title)
    pr.main(texts)
    pr.footer()

    print("\n\n")

    hr = HtmlReporter()
    hr.header(title)
    hr.main(texts)
    hr.footer()

class HtmlWriter:
    def __init__(self, html_file=sys.stdout):
        self.file = html_file

    def out_header(self):
        self.file.write("<document html>\n</html>\n")

    def out_title(self):
        self.file.write("<head><title>{}</title></head>\n".format(title))
        
    def out_start_body(self):
        self.file.write("<body>\n")
   
    def out_body(self, text):
        for text in texts:
            self.file.write("<p>{}</p>".format(text))

    def out_end_body(self):
        self.file.write("</body>\n")

    def out_footer(self):
        self.file.write("</html>\n")

class Reporter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def header(self, title):
        pass

    @abc.abstractmethod
    def main(self, contents):
        pass

    @abc.abstractmethod
    def footer(self):
        pass

class PlainTextReporter(Reporter):
    def __init__(self, file=sys.stdout):
        self.file = file

    def header(self, title):
        self.file.write("**{}**\n".format(title))

    def main(self, texts):
        for text in texts:
            self.file.write("**{}**\n".format(text))
    
    def footer(self):
        pass

class HtmlReporter(Reporter, HtmlWriter):
    def __init__(self, file=sys.stdout):
        self.file = file

    def header(self, title):
        self.out_header()
        self.out_title(title)
        self.out_start_body()

    def main(self, texts):
        for test in tests:
            self.file.out_body(text)

    def footer(self):
        self.out_end_body()
        self.out_footer()

class HtmlReporter(Reporter):
    def __init__(self, file=sys.stdout):
        self._htmlwriter = HtmlWriter(file)

    def header(self, title):
        self._htmlwriter.out_header()
        self._htmlwriter.out_title()
        self._htmlwirter.out_start_body()

    def main(self):
        self._htmlwriter.out_body(texts)

    def footer(self):
        self._htmlwriter.out_end_body()
        self._htmlwriter.out_footer()
 
if __name__ == "__main__":
    main()
