from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import pyodbc
import sqlalchemy
import spacy
from chatterbot.languages import ENG

# Conexão ao SQL Server usando SQLAlchemy
DATABASE_URI = 'mssql+pyodbc://user:password@server/database?driver=ODBC+Driver+17+for+SQL+Server'

# Carregar o modelo SpaCy explicitamente
spacy_model = spacy.load("en_core_web_sm")

# Configurar o chatbot
chatbot = ChatBot(
    'SQLServerBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=DATABASE_URI,
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    tagger_language=ENG
)

# Treinador
trainer = ListTrainer(chatbot)

# Adicionar conteúdo para treinar o chatbot
conversations = [
    [
        "Olá",
        "Olá! Como posso ajudar você hoje?"
    ],
    [
        "Qual é o seu nome?",
        "Meu nome é ChatBot."
    ],
    [
        "O que você faz?",
        "Eu respondo a perguntas com base nos dados que eu tenho."
    ]
]

# Treinar com a lista de conversas
trainer.train(conversations)

# Treinar com corpus de dados padrão do ChatterBot
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train("chatterbot.corpus.portuguese")

# Função para interagir com o chatbot
def ask_bot(question):
    response = chatbot.get_response(question)
    return response

# Testando o chatbot
if __name__ == "__main__":
    while True:
        question = input("Você: ")
        response = ask_bot(question)
        print(f"Bot: {response}")
