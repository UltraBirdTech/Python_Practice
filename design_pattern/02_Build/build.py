import abc

def main():
    html = Director.construct(HTMLBuilder())
    text = Director.construct(TextBuilder())
    print(html)
    print('=' * 20)
    print(text)
