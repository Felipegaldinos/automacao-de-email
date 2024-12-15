# Automação de Envio de E-mails com Anexo

Este projeto é uma aplicação simples desenvolvida em Python usando `tkinter` para a interface gráfica e `smtplib` para envio de e-mails. Ele permite que o usuário envie e-mails com um arquivo PDF anexado para vários destinatários.

# Funcionalidades

- Interface gráfica para facilitar o envio de e-mails.
- Seleção de arquivos PDF para anexar aos e-mails.
- Envio de e-mails para múltiplos destinatários separados por vírgula.
- Campos para personalizar o e-mail: remetente, destinatários, assunto e mensagem.

# Requisitos

Certifique-se de ter o Python 3 instalado e as seguintes bibliotecas disponíveis:

- `tkinter` (para interface gráfica)
- `smtplib` (para envio de e-mails)
- `email` (para formatação do e-mail)

Caso alguma biblioteca esteja ausente, ela pode ser instalada com o gerenciador de pacotes padrão do Python.

# Como Usar

1. Configurar Permissões no Gmail: Certifique-se de que sua conta do Gmail está configurada para permitir o uso de "Aplicativos menos seguros" ou tenha gerado uma senha de aplicativo.


2. Executar o Código:

Salve o código em um arquivo envio_email.py.

Execute o script com o comando:

python envio_email.py



3. Preencher os Campos:

Insira seu e-mail e senha.

Adicione os destinatários separados por vírgula.

Escreva o assunto e o conteúdo do e-mail.

Opcionalmente, selecione um PDF para anexar.



4. Enviar o E-mail:

Clique em "Enviar E-mail".




# Melhorias Futuras

Suporte a outros tipos de anexos além de PDFs.

Armazenar configurações de login para evitar entrada repetitiva.

Validação de entradas para verificar se os campos obrigatórios estão preenchidos.

Interface aprimorada com bibliotecas como PyQt ou Kivy.


# Observação

Certifique-se de que as permissões de envio pelo SMTP do Gmail estão habilitadas. Acesse a documentação oficial do Gmail para mais informações sobre configurações de segurança
