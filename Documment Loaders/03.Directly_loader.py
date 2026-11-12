# ager hum na mutiple file yeh pdf ko ikhate load karna hai toh hum directly loader use kare ga 
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
loader=DirectoryLoader(
    path="books",
    # yeh ap paaten bata rahe hoo kis tarah ki file load karni hai 
    glob="*.pdf",
    # humhe yeh bhi batana hai ka ap ka loader jo hai wo kon si class hai 
    loader_cls=PyPDFLoader
)
docs=loader.load()
# lazy loader aik documnet ko load saare pdf ko ikhate nhi karte hai aur yeh hume jab use karna chahye jab hume 100 padf load is sa load hone matime nhi lage ga
# ab hum lazy load chalye ga 
docs1=loader.lazy_load()
print(docs)
print(len(docs))
print(docs[0].metadata)
print(docs[0].page_content)
# ab hum loop chalaye ga
for document in docs1:
    print(document.metadata)