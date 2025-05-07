from typing import Union, Callable
from sklearn.base import BaseEstimator, TransformerMixin


class TextPreprocessor(BaseEstimator, TransformerMixin):
    preprocessing_stages: list[Callable[[str], str]] = []
    numbers: list[str] = [str(x) for x in range(0,10)]

    def __init__(self, lowercase: bool = True, exclude_stopwords: bool = True, clean_numbers: bool = True, strip_whitespaces: bool = True, reduce_whitespaces: bool = True):
        if lowercase:
            self.preprocessing_stages.append(self.lowercase)
        if exclude_stopwords:
            self.preprocessing_stages.append(self.exclude_stopwords)
        if clean_numbers:
            self.preprocessing_stages.append(self.clean_numbers)
        if strip_whitespaces:
            self.preprocessing_stages.append(self.strip_whitespaces)
        if reduce_whitespaces:
            self.preprocessing_stages.append(self.reduce_whitespaces)
        ...

    def lowercase(self, text: str) -> str:
        return text.lower()
    
    def exclude_stopwords(self, text: str) -> str:
        return " ".join([word for word in text.split() if word not in self.stopwords])
    
    def clean_numbers(self, text: str) -> str:
        for char in self.numbers:
            text = text.replace(char, ' ')
        return text
    
    def reduce_whitespaces(self, text: str) -> str:
        return ' '.join(text.split())
    
    def strip_whitespaces(self, text: str) -> str:
        return text.rstrip()
    
    def __call__(self, text: Union[str, list[str]]) -> list[str]:
        if isinstance(text, str):
            text = [text]
        
        processed_documents = []
        for document in text:
            for stage in self.preprocessing_stages:
                document = stage(document)
            processed_documents.append(document)

        return processed_documents
    
    def fit(self, text: Union[str, list[str]]) -> list[str]:
        return self(text)
    
    def fit_transform(self, text: Union[str, list[str]], y=None) -> list[str]:
        return self(text)
    
    # def transform(self, text: Union[str, list[str]], y=None) -> list[str]:
    #     return self(text)

print(TextPreprocessor())