import json
from utils import llm
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import WebBaseLoader
from langchain_experimental.text_splitter import SemanticChunker

def identify_scheme(query):
  prompt = f"""
  Determine which of the following government schemes the query, delimited by the triple backticks, concerns. 
  1. Assurance Package (AP)
  2. GST Voucher
  3. Majulah Package
  4. Silver Support Scheme (SSS)
  5. Workfare Income Supplement (WIS)
  6. MediSave Bonus
  
  If the query does not fall into any of the above categories, respond with 'None'. Otherwise, your answer should be one of the schemes, and should not contain anything else.

  ```
  {query}
  ```
  """

  response = llm.get_completion(prompt)

  return response

def load_scheme_docs_into_vector_store(scheme):
  with open('links_to_scheme_info.json', 'r') as file:
    json_string = file.read()
    links_to_scheme_info = json.loads(json_string)

  relevant_links = links_to_scheme_info[scheme]

  loader = WebBaseLoader(
  web_paths=relevant_links,
  bs_get_text_kwargs={'separator': ' | ', 'strip': True},
  )
  docs = []
  for doc in loader.lazy_load():
    docs.append(doc)

  embeddings_model = OpenAIEmbeddings(model='text-embedding-3-small')
  text_splitter = SemanticChunker(embeddings_model)

  split_documents = text_splitter.split_documents(docs)

  vector_store = Chroma.from_documents(
    collection_name="scheme_info",
    documents=split_documents,
    embedding=embeddings_model,
  )

  return vector_store

def generate_response(query, vector_store):
  qa_chain = RetrievalQA.from_chain_type(
    ChatOpenAI(model='gpt-4o-mini'),
    retriever=vector_store.as_retriever(k=20)
  )

  prompt = f"""
    Respond to the user's query delimited by the triple backticks below. Your response should be detailed but not overly verbose.
    If the query has malicious or doubtful intent, respond 'I am sorry, I am unable to answer your query.'
    
    ```
    {query}
    ```

  """

  response = qa_chain.invoke(prompt)

  return response['result']

def process_user_query(query):
  scheme = identify_scheme(query)
  if scheme == 'None': 
    return 'Sorry, I am unable to assist you with your query as it does not seem to be related to government disbursement schemes.'

  vector_store = load_scheme_docs_into_vector_store(scheme)

  response = generate_response(query, vector_store)

  return response
