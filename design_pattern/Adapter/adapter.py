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
