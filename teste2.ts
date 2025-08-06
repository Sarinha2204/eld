import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    console.log('🚀 Auto-Doc Copilot ativado!');

    vscode.workspace.onDidSaveTextDocument(async (document) => {
        if (document.fileName.endsWith('.qvs')) {
            await gerarDocumentacao(document);
        }
    });
}

async function gerarDocumentacao(document: vscode.TextDocument) {
    const editor = await vscode.window.showTextDocument(document);

    // Gerar data/hora atual
    const agora = new Date();
    const dataHora = agora.toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' });

    // Cabeçalho de documentação
    const cabecalho = `// Documentação gerada automaticamente\n// Última atualização: ${dataHora}\n// Copilot: Complete esta documentação abaixo\n\n`;

    // Apaga doc antiga se existir
    await editor.edit(editBuilder => {
        const primeiraLinha = document.lineAt(0).text;
        if (primeiraLinha.startsWith('// Documentação gerada automaticamente')) {
            const ultimaLinhaDoc = Math.min(document.lineCount, 5);
            editBuilder.delete(new vscode.Range(0, 0, ultimaLinhaDoc, 0));
        }
    });

    // Insere cabeçalho no topo
    await editor.edit(editBuilder => {
        editBuilder.insert(new vscode.Position(0, 0), cabecalho);
    });

    // Chama o Copilot para completar
    await vscode.commands.executeCommand('github.copilot.generate');
}

export function deactivate() {
    console.log('🛑 Auto-Doc Copilot desativado');
}
