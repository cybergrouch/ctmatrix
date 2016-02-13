def makeInverseIndex(strlist):
  # 1. Convert list<String> to list<(document number, set of words in document)>
  documentWordsList = [ (k, set(v.lower().split())) for (k,v) in list(enumerate(strlist)) ] 
  
  # 2. Iterate through list<(document number, set of words in document)> and consider item<(document number, set of words in document)>
  #    2.1. for each word, create an element (word, document number) and add to list
  #    2.2. You'll now have list<list<(word, document number)>>
  # 3. Merge the list<list<(word, document number)>> to a single list<(word, document number)>
  # 4. Iterate through each element in list<(word, document number)> and assemble results into a map<(word, set<document number>)
  wordToDocumentsMap = {}
  for documentNumber, documentWordSet in documentWordsList:
      for documentWord in documentWordSet:
          wordToDocumentsMap[documentWord] = wordToDocumentsMap[documentWord] | {documentNumber} if documentWord in wordToDocumentsMap else {documentNumber}
  
  # 5. Return map<(word, set<document number>)
  return wordToDocumentsMap
  
def orSearch(inverseIndex, query):
    documentSearchResult = set({})
    
    listOfSets = [ inverseIndex[queryWord] for queryWord in query if queryWord in inverseIndex ]
    
    for setElement in listOfSets:
        documentSearchResult = documentSearchResult | setElement
            
    return documentSearchResult
  
  
def andSearch(inverseIndex, query):
    documentSearchResult = set({})
        
    for queryWord in query:
        wordDocumentSet = inverseIndex[queryWord] if queryWord in inverseIndex else set({})
            
        if not documentSearchResult:
            documentSearchResult = wordDocumentSet
        else:
            documentSearchResult = documentSearchResult & wordDocumentSet
                        
    return documentSearchResult
