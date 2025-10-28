# Diagnóstico - Envio de Email via Resend no Railway

## Melhorias Implementadas

O código foi melhorado para capturar todos os erros e registrar logs detalhados quando o formulário de contato for enviado. Agora você poderá ver exatamente onde está o problema nos logs do Railway.

## Como Verificar os Logs no Railway

1. Acesse seu projeto no Railway
2. Vá na aba **Deployments** (Implantações)
3. Clique no deployment mais recente (ativo)
4. Vá na aba **Logs**
5. Teste o formulário de contato no site
6. Observe os logs em tempo real

## O Que Procurar nos Logs

Quando alguém preencher o formulário e clicar em "Solicitar Contato", você verá logs similares a:

### ✅ Se Funcionar Corretamente:
```
INFO - Contact form submitted - Name: João Silva, Email: joao@example.com, Phone: (11) 99999-9999
INFO - Attempting to send email via Resend...
INFO - Getting Resend credentials...
INFO - Resend credentials obtained. From email: xxx@xxx.xxx
INFO - Sending email to: comercial@elpconsultoria.eng.br, from: ELP Consultoria - Website <xxx@xxx.xxx>, subject: Novo Contato - João Silva
INFO - Resend API response status: 200
INFO - Resend API response body: {"id":"xxxxx-xxxxx-xxxxx"}
INFO - Email sent successfully! Response: {'id': 'xxxxx-xxxxx-xxxxx'}
```

### ❌ Se Houver Erro:
```
ERROR - ERRO ao enviar email via Resend: [MENSAGEM DE ERRO DETALHADA]
```

## Problemas Comuns e Soluções

### 1. Variável de Ambiente Não Configurada
**Log:**
```
RESEND_API_KEY environment variable not found. Please configure Resend credentials in Railway.
```

**Solução:**
- Vá em **Variables** no Railway
- Verifique se `RESEND_API_KEY` está configurada
- Verifique se `RESEND_FROM_EMAIL` está configurada

### 2. API Key Inválida
**Log:**
```
Resend API error - Status 401: {"message":"Invalid API key"}
```

**Solução:**
- A chave API está incorreta ou expirada
- Gere uma nova chave em https://resend.com/api-keys
- Atualize a variável `RESEND_API_KEY` no Railway

### 3. Email Remetente Não Verificado
**Log:**
```
Resend API error - Status 403: {"message":"Domain not verified"}
```

**Solução:**
- O email em `RESEND_FROM_EMAIL` precisa ser de um domínio verificado no Resend
- Opção 1: Use `onboarding@resend.dev` (email de teste do Resend)
- Opção 2: Verifique seu domínio no Resend em https://resend.com/domains

### 4. Formato de Email Inválido
**Log:**
```
Invalid email format: [email] - Error: ...
```

**Solução:**
- O email digitado no formulário está inválido
- Isso é uma validação normal, não é um erro do sistema

## Variáveis de Ambiente Necessárias

No Railway, você DEVE ter:

```
RESEND_API_KEY=re_xxxxxxxxxxxxxxxxxxxxx
RESEND_FROM_EMAIL=contato@seudominio.com.br
```

OU para testes:

```
RESEND_API_KEY=re_xxxxxxxxxxxxxxxxxxxxx
RESEND_FROM_EMAIL=onboarding@resend.dev
```

## Como Obter a API Key do Resend

1. Acesse https://resend.com
2. Faça login
3. Vá em **API Keys**
4. Clique em **Create API Key**
5. Dê um nome (ex: "ELP Website Production")
6. Copie a chave (começa com `re_`)
7. Cole no Railway em **Variables** → `RESEND_API_KEY`

## Como Configurar o Email Remetente

### Opção 1: Usar o Email de Teste (Mais Rápido)
```
RESEND_FROM_EMAIL=onboarding@resend.dev
```
✅ Funciona imediatamente
❌ Emails podem ir para spam
❌ Não é profissional

### Opção 2: Usar Seu Próprio Domínio (Recomendado)
1. No Resend, vá em **Domains**
2. Clique em **Add Domain**
3. Digite seu domínio (ex: `elpconsultoria.eng.br`)
4. Adicione os registros DNS solicitados no seu provedor de domínio
5. Aguarde a verificação (pode levar alguns minutos)
6. Configure no Railway:
```
RESEND_FROM_EMAIL=contato@elpconsultoria.eng.br
```

## Testando Localmente (Opcional)

Se quiser testar localmente antes de fazer deploy no Railway:

1. Crie um arquivo `.env` na raiz do projeto:
```
SESSION_SECRET=seu_secret_aqui
RESEND_API_KEY=re_xxxxxxxxxxxxxxxxxxxxx
RESEND_FROM_EMAIL=onboarding@resend.dev
```

2. Instale python-dotenv:
```bash
pip install python-dotenv
```

3. No início do `app.py`, adicione:
```python
from dotenv import load_dotenv
load_dotenv()
```

4. Execute localmente:
```bash
python main.py
```

## Próximos Passos

1. **Faça deploy no Railway** com as alterações de código
2. **Verifique os logs** após fazer deploy
3. **Teste o formulário** e observe os logs em tempo real
4. **Compartilhe os logs** se ainda houver problemas

## Suporte

Se após seguir estas instruções o problema persistir, envie:
1. Os logs completos do Railway (copie e cole)
2. Confirmação de que as variáveis de ambiente estão configuradas
3. O email configurado em `RESEND_FROM_EMAIL`
