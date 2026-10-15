# Envio de E-mails com PDF

Aplicação desktop em Python para compor uma mensagem, selecionar um PDF opcional e enviar e-mails a vários destinatários pelo SMTP do Gmail. O envio é iniciado manualmente na interface.

## Funcionalidades

- Interface gráfica com Tkinter.
- Campos de remetente, destinatários separados por vírgula, assunto e corpo.
- Seleção de arquivo PDF em janela de arquivos.
- Composição MIME e conexão SMTP com STARTTLS.
- Notificações de sucesso ou erro na interface.

## Tecnologias

Python 3, Tkinter e módulos padrão smtplib e email.

## Como executar

Instale Python 3 com Tkinter disponível. Confira a interface gráfica:

```sh
python -m tkinter
```

Clone o projeto e execute o arquivo existente:

```sh
git clone https://github.com/Felipegaldinos/automacao-de-email.git
cd automacao-de-email
python email.py
```

Caso ocorra conflito de importação com o pacote padrão `email`, renomeie o script para `envio_email.py` e execute `python envio_email.py`. Isso é uma solução manual; o arquivo atual do repositório se chama `email.py`.

O servidor está definido no código como `smtp.gmail.com`, porta 587, com STARTTLS. A implementação usa login por senha e não oferece OAuth. Para contas elegíveis, consulte as condições de verificação em duas etapas e senhas de app na [documentação oficial do Google](https://support.google.com/accounts/answer/185833?hl=pt-BR). Não use orientações antigas sobre ativar aplicativos menos seguros. `smtplib` e `email` fazem parte do Python; Tkinter depende da instalação do Python/sistema, não de um simples `pip install tkinter`.

## Organização do código

- `email.py` — interface, seleção do PDF, composição da mensagem e envio SMTP.

## Roteiro de demonstração

Primeiro confira o Tkinter e o possível conflito do nome do arquivo. Para testar o envio, use uma conta de teste e um destinatário seu; clicar em Enviar E-mail realiza um envio real. Teste uma mensagem simples e depois um PDF pequeno.

## Limitações atuais

Não há agendamento de envios ou fila. A chamada SMTP ocorre na interface e pode bloquear a janela durante a conexão. Se a criação do objeto SMTP falhar, o bloco finally tenta executar servidor.quit() sem uma instância válida, causando um erro adicional. O nome email.py também coincide com o pacote padrão email e pode causar conflito de importação; renomear o arquivo é uma melhoria de código separada desta documentação.

## Competências demonstradas

Interface desktop, composição MIME, anexos e comunicação SMTP.

## Autoria

Projeto disponível no perfil de [Felipe Galdino](https://github.com/Felipegaldinos). Consulte os arquivos do repositório para verificar os termos de licença aplicáveis.
