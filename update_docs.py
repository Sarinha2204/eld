import os
from datetime import datetime
from openai import OpenAI

# Inicializa cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_documentacao(conteudo, nome_arquivo):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    prompt = f"""
Você é um especialista em QlikView e documentação técnica.
Analise o script abaixo e gere um cabeçalho de documentação em português,
com a data e hora de atualização ({data_hora}).

Arquivo: {nome_arquivo}

Script:
{conteudo}
    """
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return f"// Documentação gerada automaticamente\n// Última atualização: {data_hora}\n{resp.choices[0].message.content}\n\n"

def atualizar_arquivos():
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".qvs"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                doc = gerar_documentacao(conteudo, file)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(doc + conteudo)
                print(f"✅ Documentação atualizada: {path}")

if __name__ == "__main__":
    atualizar_arquivos()
