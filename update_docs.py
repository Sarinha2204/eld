import os
import time
from datetime import datetime
import google.generativeai as genai
from fpdf import FPDF

genai.configure(api_key="AIzaSyANW3dk0XXkTwx2Pip0lqRes-CYv0IvjdA")
model = genai.GenerativeModel("gemini-1.5-flash")


def gerar_documentacao_qvs(conteudo: str, nome_arquivo: str) -> str:
    """Gera documentação para um arquivo QVS usando a API Google Gemini."""
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    prompt = f"""
Você é especialista em QlikView e documentação técnica.

Faça uma documentação estilo de sulfite a4 enalise o script QVS abaixo e gere uma documentação clara e formal explicando o conteúdo do script, sem dar sugestões, em português, 
contendo:
- Resumo do que o script faz
- Principais etapas (em tópicos)

Script:
{conteudo}
    """

    try:
        response = model.generate_content(prompt)
        if hasattr(response, "text"):
            conteudo_gerado = response.text.strip()
        elif hasattr(response, "candidates") and len(response.candidates) > 0:
            conteudo_gerado = response.candidates[0].output.strip()
        else:
            conteudo_gerado = ""
    except Exception as e:
        print(f"Erro ao chamar API Gemini: {e}")
        conteudo_gerado = ""

    cabecalho = (
        f"Documentação Técnica\n"
        f"Arquivo: {nome_arquivo}\n"
        f"Última atualização: {data_hora}\n\n"
        f"{conteudo_gerado}\n"
    )
    return cabecalho


def salvar_documentacao_em_pdf(conteudo_doc: str, nome_arquivo: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(25, 20, 20)
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_font("Arial", size=12)

    for linha in conteudo_doc.splitlines():
        pdf.cell(0, 8, txt=linha, ln=True)

    nome_pdf = os.path.splitext(nome_arquivo)[0] + "_documentacao.pdf"
    pdf.output(nome_pdf)
    print(f"Documentação exportada para PDF: {nome_pdf}")


def salvar_documentacao_em_md(conteudo_doc: str, nome_arquivo: str):
    nome_md = os.path.splitext(nome_arquivo)[0] + "_documentacao.md"
    try:
        with open(nome_md, "w", encoding="utf-8") as f:
            f.write("# Documentação Técnica\n\n")
            f.write(conteudo_doc)
        print(f"Documentação exportada para Markdown: {nome_md}")
    except Exception as e:
        print(f"Erro ao salvar .md: {e}")


def atualizar_documentacao_qvs(diretorio: str):
    """Atualiza a documentação de todos os arquivos .qvs no diretório informado."""
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.lower().endswith(".qvs"):
                caminho = os.path.join(root, file)

                with open(caminho, "r", encoding="utf-8") as f:
                    conteudo = f.read()

                linhas = conteudo.splitlines()
                while linhas and linhas[0].strip().startswith("//"):
                    linhas.pop(0)
                conteudo_sem_doc = "\n".join(linhas)

                print(f"Atualizando documentação: {caminho}")
                nova_doc = gerar_documentacao_qvs(conteudo_sem_doc, file)

                with open(caminho, "w", encoding="utf-8") as f:
                    f.write(nova_doc + "\n" + conteudo_sem_doc)

                salvar_documentacao_em_pdf(nova_doc, file)
                salvar_documentacao_em_md(nova_doc, file)

                time.sleep(5)


if __name__ == "__main__":
    atualizar_documentacao_qvs(".")
    print("Documentação atualizada para todos os arquivos .qvs e exportada para PDF e Markdown.")


# import time
# import os
# from datetime import datetime
# from openai import OpenAI

# client = OpenAI(api_key="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")

# def gerar_documentacao_qvs(conteudo: str, nome_arquivo: str) -> str:
#     """Gera documentação para um arquivo QVS usando a API OpenAI."""
#     data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#     prompt = f"""
# Você é um especialista em QlikView e documentação técnica.
# Analise o script QVS abaixo e gere uma documentação bem explicativa e formal em português, utilizando explicações 
# em resumo e em tópicos, considere as linhas que começam com "//" como comentários.
# contendo:
# - Nome do arquivo
# - Data e hora da última atualização: {data_hora}
# - Descrição do que o script faz
# - Lista resumida dos principais componentes e etapas

# Arquivo: {nome_arquivo}

# Script:
# {conteudo}
#     """
#     resposta = client.chat.completions.create(
#         model="gpt-4o-mini", 
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.3
#     )

#     cabecalho = (
#         f"// Documentação Técnica\n"
#         f"// Arquivo: {nome_arquivo}\n"
#         f"// Última atualização: {data_hora}\n"
#         f"{resposta.choices[0].message.content.strip()}\n\n"
#     )
#     return cabecalho

# def atualizar_documentacao_qvs(diretorio: str):
#     """Percorre todos os arquivos .qvs e atualiza a documentação no topo."""
#     for root, _, files in os.walk(diretorio):
#         for file in files:
#             if file.lower().endswith(".qvs"):
#                 caminho = os.path.join(root, file)

#                 with open(caminho, "r", encoding="utf-8") as f:
#                     conteudo = f.read()

#                 # Remove doc antiga (primeiros 15 linhas se começarem com "//")
#                 linhas = conteudo.splitlines()
#                 while linhas and linhas[0].strip().startswith("//"):
#                     linhas.pop(0)
#                 conteudo_sem_doc = "\n".join(linhas)

#                 print(f"Atualizando  documentação: {caminho}")
#                 nova_doc = gerar_documentacao_qvs(conteudo_sem_doc, file)

#                 with open(caminho, "w", encoding="utf-8") as f:
#                     f.write(nova_doc + conteudo_sem_doc)
#                 time.sleep(25)


# if __name__ == "__main__":
#     atualizar_documentacao_qvs(".")
#     print("Documentação atualizada para todos os arquivos .qvs")


