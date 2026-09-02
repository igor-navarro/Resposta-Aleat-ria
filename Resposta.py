import random
import time

print("🎱 Bem-vindo à Bola 8 Mágica!")
input("Faça uma pergunta de 'sim ou não' para o universo: ")

print("\nConsultando os astros...")
time.sleep(2)  # Pausa dramática de 2 segundos

respostas = [
    "Com certeza!",
    "Sem dúvida alguma.",
    "As perspectivas são boas.",
    "Sim.",
    "Concentre-se e pergunte novamente.",
    "Minhas fontes dizem que não.",
    "Muito duvidoso.",
    "Não conte com isso."
]

print(f"🔮 Resposta: {random.choice(respostas)}")