import requests
import re
import tkinter as tk

# Define a função que é chamada ao clicar no botão "Buscar"
def buscar_vulnerabilidades():
    # Obtém a URL informada no campo de texto
    url = url_field.get()

    # Realiza a requisição HTTP/HTTPS ao site
    response = requests.get(url)

    # Verifica se o site está online e acessível
    if response.status_code == 200:
        result_label.config(text="Site está online e acessível!")
        # Obtem o corpo da resposta HTTP/HTTPS do site
        body = response.text
        
        # Procura por vulnerabilidades de injeção de SQL
        if "error in your SQL syntax" in body:
            result_label.config(text="Possível vulnerabilidade de injeção de SQL")
        
        # Procura por vulnerabilidades de Cross-Site Scripting (XSS)
        if "<script>" in body:
            result_label.config(text="Possível vulnerabilidade de Cross-Site Scripting (XSS)")
        
        # Procura por vulnerabilidades de Cross-Site Request Forgery (CSRF)
        if "<form" in body:
            if re.search(r'method=["\']?POST["\']?', body, re.IGNORECASE):
                result_label.config(text="Possível vulnerabilidade de Cross-Site Request Forgery (CSRF)")
        
        # Aqui você pode adicionar mais verificações para outras vulnerabilidades
    else:
        result_label.config(text="Site pode estar offline ou indisponível.")

# Cria a janela principal
root = tk.Tk()
root.title("Verificador de Vulnerabilidades")

# Cria o campo de texto para a URL
url_field = tk.Entry(root, width=50)
url_field.pack(pady=10)

# Cria o botão para buscar as vulnerabilidades
buscar_button = tk.Button(root, text="Buscar", command=buscar_vulnerabilidades)
buscar_button.pack()

# Cria a label para mostrar o resultado
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Inicia a janela principal
root.mainloop()