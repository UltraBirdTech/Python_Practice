import abc

def main():
    html = Director.construct(HTMLBuilder())
    text = Director.construct(TextBuilder())
    print(html)
    print('=' * 20)
    print(text)

class Director():
    def construct(self, builder):
        all_str = ""
        all_str += builder.build_title("Monthly Report")
        all_str += builder.build_header("------")
        all_str += builder.build_contents(["Monday: 20", "Tuesday: 30"])
        all_str += builder.build_footer("------")
        return all_str
        
class AbstractBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def build_title(self, title):
        pass
    
