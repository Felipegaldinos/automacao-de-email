import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import tkinter as tk
from tkinter import messagebox, filedialog

caminho_pdf = None

def selecionar_pdf():
    """Abre uma janela para o usuário selecionar o arquivo PDF."""
    global caminho_pdf
    caminho_pdf = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if caminho_pdf:
        messagebox.showinfo("Arquivo Selecionado", f"PDF selecionado: {caminho_pdf}")

def enviar_email():
    email_usuario = entrada_email_usuario.get()
    senha = entrada_senha.get()
    assunto = entrada_assunto.get()
    conteudo = entrada_conteudo.get("1.0", tk.END)
    emails_destinatarios = entrada_destinatarios.get().split(",")  
    
    servidor_smtp = "smtp.gmail.com"
    porta_smtp = 587

    mensagem = MIMEMultipart()
    mensagem['From'] = email_usuario
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(conteudo, 'plain'))

    if caminho_pdf:
        try:
            with open(caminho_pdf, "rb") as pdf_file:
                anexo_pdf = MIMEApplication(pdf_file.read(), _subtype="pdf")
                anexo_pdf.add_header('Content-Disposition', 'attachment', filename=caminho_pdf.split("/")[-1])
                mensagem.attach(anexo_pdf)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível anexar o PDF: {e}")
            return

    try:
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()
        servidor.login(email_usuario, senha)
        
        
        servidor.sendmail(email_usuario, emails_destinatarios, mensagem.as_string())
        messagebox.showinfo("Sucesso", "E-mails enviados com sucesso!")
        
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar os e-mails: {e}")
    
    finally:
        servidor.quit()

janela = tk.Tk()
janela.title("Automação de Envio de E-mails")
janela.geometry("400x500")

tk.Label(janela, text="Seu E-mail:").pack()
entrada_email_usuario = tk.Entry(janela, width=40)
entrada_email_usuario.pack()

tk.Label(janela, text="Senha do E-mail:").pack()
entrada_senha = tk.Entry(janela, show="*", width=40)
entrada_senha.pack()

tk.Label(janela, text="Destinatários (separados por vírgula):").pack()
entrada_destinatarios = tk.Entry(janela, width=40)
entrada_destinatarios.pack()

tk.Label(janela, text="Assunto do E-mail:").pack()
entrada_assunto = tk.Entry(janela, width=40)
entrada_assunto.pack()

tk.Label(janela, text="Conteúdo do E-mail:").pack()
entrada_conteudo = tk.Text(janela, width=40, height=10)
entrada_conteudo.pack()

botao_pdf = tk.Button(janela, text="Selecionar PDF", command=selecionar_pdf)
botao_pdf.pack(pady=5)

botao_enviar = tk.Button(janela, text="Enviar E-mail", command=enviar_email)
botao_enviar.pack(pady=10)

janela.mainloop()