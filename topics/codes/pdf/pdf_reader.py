import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from PyPDF2 import PdfReader, PdfWriter
import os

# Função para processar o PDF principal e dividir por colaboradores
def processar_pdfs_por_colaborador(pdf_path, output_dir):
    try:
        # Abrindo o PDF principal
        pdf_reader = PdfReader(pdf_path)
        total_paginas = len(pdf_reader.pages)
        colaboradores = {}

        # Iterar por cada página e buscar um colaborador correspondente (simulado)
        for i in range(total_paginas):
            pagina = pdf_reader.pages[i]
            texto = pagina.extract_text()

            # Simulação para obter o colaborador (ex: buscar por "Colaborador: [Nome]")
            colaborador = obter_colaborador_do_texto(texto)
            if colaborador not in colaboradores:
                colaboradores[colaborador] = []
            colaboradores[colaborador].append(i)

            # Atualizando a barra de progresso
            barra_progresso["value"] = (i + 1) * (100 / total_paginas)
            root.update_idletasks()  # Atualiza a interface gráfica

        # Criando PDFs separados para cada colaborador
        for colaborador, paginas in colaboradores.items():
            pdf_writer = PdfWriter()

            for num_pagina in paginas:
                pdf_writer.add_page(pdf_reader.pages[num_pagina])

            output_filename = f"{colaborador}.pdf"
            output_path = os.path.join(output_dir, output_filename)
            with open(output_path, "wb") as output_pdf:
                pdf_writer.write(output_pdf)

        messagebox.showinfo("Concluído", "Separação das NFEs por colaborador concluída!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função que será chamada ao clicar no botão para iniciar o processamento
def iniciar_processamento():
    # Escolher o arquivo PDF principal
    pdf_path = filedialog.askopenfilename(title="Selecione o PDF com as NFEs", filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        return

    # Escolher o diretório de saída para salvar os PDFs separados
    output_dir = filedialog.askdirectory(title="Selecione o diretório para salvar os PDFs separados")
    if not output_dir:
        return

    # Desativar o botão para evitar cliques enquanto processa
    botao_iniciar.config(state=tk.DISABLED)

    # Criar uma thread para rodar o processamento dos PDFs
    thread = threading.Thread(target=processar_pdfs_por_colaborador, args=(pdf_path, output_dir))
    thread.start()

    # Verificar quando a thread terminar
    verificar_thread(thread)

# Função para verificar se a thread terminou
def verificar_thread(thread):
    if thread.is_alive():
        # Se a thread ainda está rodando, verifica novamente após 100 ms
        root.after(100, lambda: verificar_thread(thread))
    else:
        # Reativar o botão quando o processamento terminar
        botao_iniciar.config(state=tk.NORMAL)

# Função fictícia para obter o colaborador a partir do texto da página
# Isso deve ser adaptado conforme a estrutura do texto do PDF
def obter_colaborador_do_texto(texto):
    # Simulação para pegar o nome do colaborador (ex: "Colaborador: [Nome]")
    if "Colaborador: " in texto:
        return texto.split("Colaborador: ")[1].split("\n")[0].strip()
    return "Desconhecido"

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Separação de PDFs de NFEs por Colaborador")
root.geometry("400x200")

# Barra de progresso
barra_progresso = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
barra_progresso.pack(pady=20)

# Botão para iniciar o processamento
botao_iniciar = tk.Button(root, text="Iniciar Processamento", command=iniciar_processamento)
botao_iniciar.pack(pady=10)

# Iniciar o loop principal
root.mainloop()