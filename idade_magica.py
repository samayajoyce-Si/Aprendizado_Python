# idade_magica.py

print("Quantos anos você tem?")
idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Você é uma criança mágica! 🧒✨")
elif 12 <= idade < 18:
    print("Você é um jovem aprendiz! 🧙‍♂️📚")
elif 18 <= idade < 60:
    print("Você é um mago experiente! 🧠🪄")
else:
    print("Você é um sábio do reino! 👑📜")
