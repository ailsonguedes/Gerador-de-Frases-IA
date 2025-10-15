from ai_cliente import gerar_frase_motivacional

def main():
    tema = input("Texting a theme (ex: overcoming adversity, focus, courage): ")
    print("Generating quote... (loading)")
    frase = gerar_frase_motivacional(tema)
    print(f"\nMotivacional Quoting:\n{frase}")

if __name__ == "__main__":
    main()
