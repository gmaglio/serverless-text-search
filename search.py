SEARCH_INDEX = dict()
def populateSearchIndexDecorator(func):
    def wrapper(search_str):
        if len(SEARCH_INDEX.keys()) > 0:
            print("Search Index is already populated")
            return func(search_str)
        else:
            print("Populating the Search Index")
            Result = SearchService.addSearchableWords("word-dict.txt")
            print(Result)
            return func(search_str)
    return wrapper
  
class SearchService:
    @staticmethod
    def addSearchableWords(filename):
        f = open(filename, "rb");
        wordCount = 0
        for _searchable in f:
            searchable = _searchable.decode(errors = "ignore").rstrip()
            term = ""
            for c in searchable:
                term += c
                if term not in SEARCH_INDEX:
                    SEARCH_INDEX[term] = list() 
                SEARCH_INDEX[term].append(searchable)
            wordCount += 1
        return {
                "wordCount": wordCount,
                "termsCount": len(SEARCH_INDEX.keys())
        }

    @staticmethod
    @populateSearchIndexDecorator
    def search(search_str):
        if search_str not in SEARCH_INDEX:
            return
        return SEARCH_INDEX[search_str]
