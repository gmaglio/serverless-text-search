from search import SearchService
import sys, json

def handler(event, context):
    SearchString = event["searchString"]
    Results = SearchService.search(SearchString)
    return Results
