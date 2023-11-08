import requests
import bibtexparser

##
##
### Pergunta principal:
### Quais Autores estão indexados tanto na base de dados da scopus e da UN Library?
### Segundo Passo:
### Encontrar os autores que estão dentro dos documentos em PDF disponíveis pela biblioteca da UN Library
##
##

searchTerm = 'Pachauri, R.K.'


scopus = requests.get('https://api.elsevier.com/content/search/scopus?query=TITLE-ABS-KEY('+ searchTerm +')&apiKey=0e8d1539414402446bf8ed45e92dffda')


onu = requests.get('https://digitallibrary.un.org/search?ln=en&p=Pachauri%2C+R.K.&f=&rm=&sf=&so=d&rg=50&c=Resource+Type&c=UN+Bodies&c=&of=btex&fti=0&fti=0')


# scopus = requests.get('https://api.elsevier.com/content/search/scopus?query=all(ipcc)&apiKey=349f8bf67249f00e2365499e4ac9ab57&httpAccept=application%2Fjson')

scopusJson = scopus.json();

print("Scopus results: " + scopusJson['search-results']['opensearch:totalResults'])

print(onu.text)
# print(scopusJson);
