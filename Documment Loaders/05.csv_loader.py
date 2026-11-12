from langchain_community.document_loaders.csv_loader import CSVLoader

# CSV file load karein (har row ek alag Document ban jayegi)
loader = CSVLoader(file_path="ai_models.csv")
docs = loader.load()

print(f"Total rows loaded: {len(docs)}")
print("\nPehli row ka data:")
print(docs[0].page_content)
