

import os
import time
from datetime import datetime
import google.generativeai as genai

# Inicializa o cliente Gemini com sua chave de API
genai.configure(api_key="AIzaSyANW3dk0XXkTwx2Pip0lqRes-CYv0IvjdA")

# Carrega o modelo
model = genai.GenerativeModel("gemini-1.5-pro")

def gerar_documentacao_qvs(conteudo: str, nome_arquivo: str) -> str:
    """Gera documentação para um arquivo QVS usando a API Google Gemini."""
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    prompt = f"""
Você é especialista em QlikView e documentação técnica.

Analise o script QVS abaixo e gere uma documentação clara e formal em português, contendo:
- Nome do arquivo
- Data da última atualização
- Resumo do que o script faz
- Principais etapas (em tópicos)

Considere as linhas iniciadas por "//", "#" ou "/*" como comentários.

Arquivo: {nome_arquivo}
Data: {data_hora}

Script:
{conteudo}
    """

    try:
        response = model.generate_content(prompt)
        conteudo_gerado = response.text.strip()
    except Exception:
        conteudo_gerado = "// Erro: nenhuma resposta gerada pela API.\n"

    cabecalho = (
        f"// Documentação Técnica\n"
        f"// Arquivo: {nome_arquivo}\n"
        f"// Última atualização: {data_hora}\n"
        f"{conteudo_gerado}\n\n"
    )
    return cabecalho


def atualizar_documentacao_qvs(diretorio: str):
    """Atualiza a documentação de todos os arquivos .qvs no diretório informado."""
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.lower().endswith(".qvs"):
                caminho = os.path.join(root, file)

                with open(caminho, "r", encoding="utf-8") as f:
                    conteudo = f.read()

                # Remove cabeçalho anterior (linhas iniciais com "//")
                linhas = conteudo.splitlines()
                while linhas and linhas[0].strip().startswith("//"):
                    linhas.pop(0)
                conteudo_sem_doc = "\n".join(linhas)

                print(f"Atualizando documentação: {caminho}")
                nova_doc = gerar_documentacao_qvs(conteudo_sem_doc, file)

                with open(caminho, "w", encoding="utf-8") as f:
                    f.write(nova_doc + conteudo_sem_doc)

                # Espera entre requisições para evitar sobrecarga
                time.sleep(5)


if __name__ == "__main__":
    atualizar_documentacao_qvs(".")
    print("Documentação atualizada para todos os arquivos .qvs")



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


