from document_server.storage import BlobStorage

storage = BlobStorage()

documents = storage.list_documents()

for doc in documents:
    print(doc)
