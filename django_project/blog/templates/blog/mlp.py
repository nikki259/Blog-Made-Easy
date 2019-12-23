import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

document1="""Text summarization refers to the technique of shortening long␣
, →pieces of text. The intention is to create a coherent and fluent summary␣ , →having only the main points outlined in the document. Automatic text␣ , →summarization is a common problem in machine learning and natural language␣ , →processing (NLP)."""
print(document1)
parser = PlaintextParser.from_string(document1, Tokenizer("english"))
summarizer = LexRankSummarizer()
summary = summarizer(parser.document,1)
print(summary)
for sentence in summary:
    print(sentence)
