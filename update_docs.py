import os
import time
from datetime import datetime
from mistralai import Mistral
from markdown import markdown
from xhtml2pdf import pisa 


MISTRAL_API_KEY = "JmNoW35BSmQA7UJPpCCiqiru1m1MbODu"  # chave API do Mistral
client = Mistral(api_key=MISTRAL_API_KEY)


def gerar_documentacao_qvs(conteudo: str, nome_arquivo: str) -> str:
    """Gera documentação para um arquivo QVS usando a API Mistral."""
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    prompt = f"""
Você é um gerador de documentação formal e clara.

Gere uma explicação detalhada e bem organizada para o script QVS abaixo,
no formato de um documento formal, mas que seja fácil de entender mesmo por
pessoas que não têm conhecimento técnico.

O texto deve ser:
- Escrito em português claro e acessível.
- Com tom formal e objetivo.
- Sem termos técnicos complexos ou siglas sem explicação.
- Organizado em seções e tópicos para facilitar a leitura.
- Explicar o que o script faz, para que serve e como funciona de forma simplificada.
- Incluir exemplos ilustrativos quando necessário.
- Não sugerir alterações ou melhorias no código.

Script:
{conteudo}
    """

    try:
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}]
        )
        conteudo_gerado = response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Erro ao chamar API Mistral: {e}")
        conteudo_gerado = ""

    cabecalho = (
        f"# Documentação Técnica\n\n"
        f"**Arquivo:** `{nome_arquivo}`  \n"
        f"**Última atualização:** {data_hora}\n\n"
        f"{conteudo_gerado}\n"
    )
    return cabecalho


def salvar_documentacao_em_md_e_pdf(conteudo_doc: str, nome_arquivo: str):
    """Salva a documentação em Markdown e converte para PDF usando xhtml2pdf."""
    nome_base = os.path.splitext(nome_arquivo)[0]
    nome_md = nome_base + "_documentacao.md"
    nome_pdf = nome_base + "_documentacao.pdf"

    try:
        # Salva como Markdown
        with open(nome_md, "w", encoding="utf-8") as f:
            f.write(conteudo_doc)
        print(f"Markdown salvo: {nome_md}")

        # Converte Markdown para HTML
        html_content = markdown(conteudo_doc)

        # Converte HTML para PDF usando xhtml2pdf
        with open(nome_pdf, "wb") as f:
            pisa.CreatePDF(html_content, dest=f)
        print(f"PDF gerado com sucesso: {nome_pdf}")
    except Exception as e:
        print(f"Erro ao salvar PDF: {e}")


def atualizar_documentacao_qvs(diretorio: str):
    """Atualiza a documentação de todos os arquivos .qvs no diretório informado."""
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.lower().endswith(".qvs"):
                caminho = os.path.join(root, file)

                with open(caminho, "r", encoding="utf-8") as f:
                    conteudo = f.read()

                # Remove comentários/documentação antiga do topo
                linhas = conteudo.splitlines()
                while linhas and linhas[0].strip().startswith("//"):
                    linhas.pop(0)
                conteudo_sem_doc = "\n".join(linhas)

                print(f"Atualizando documentação: {caminho}")
                nova_doc = gerar_documentacao_qvs(conteudo_sem_doc, file)

                # Atualiza o .qvs inserindo a documentação no início
                with open(caminho, "w", encoding="utf-8") as f:
                    f.write(nova_doc + "\n" + conteudo_sem_doc)

                # Exportações
                salvar_documentacao_em_md_e_pdf(nova_doc, file)

                # Evita sobrecarga de requisições
                time.sleep(15)


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
# Faça uma documentação bem explicativa, analise o script QVS abaixo e gere uma documentação clara e formal 
# explicando o conteúdo do script, sem dar sugestões, em português, 
# contendo:
# - Resumo do que o script faz
# - Principais etapas (em tópicos)

# Arquivo: {nome_arquivo}
# Data e Horário: {data_hora}

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
