# Configuração do Railway para ELP Consultoria

## ✅ Correção Aplicada para o Erro "gunicorn: command not found"

O projeto agora inclui o arquivo **`nixpacks.toml`** que garante que o Railway instale todas as dependências corretamente antes de executar o gunicorn.

---

## Arquivos de Configuração do Railway

O projeto possui os seguintes arquivos de configuração:

- ✅ **`nixpacks.toml`** - Configuração oficial do Nixpacks (garante instalação correta das dependências)
- ✅ **`requirements.txt`** - Lista de dependências Python
- ✅ **`railway.json`** - Configurações de deploy
- ✅ **`Procfile`** - Comando de inicialização (fallback)
- ✅ **`runtime.txt`** - Versão do Python (3.11.0)

---

## Variáveis de Ambiente Necessárias

Configure no Railway (Settings → Variables):

### 1. SESSION_SECRET ✅
```
wI5igJ7HyH1FDE7fv9qvKGFN7ngPJUkNVE_HPhe7Ua-CT4MscKGs8GlGHne1wTTI67QDReFAyqNhsZl6oxM0dg
```

### 2. RESEND_API_KEY ⚠️ (Obrigatório)
1. Acesse [resend.com](https://resend.com)
2. Faça login ou crie conta
3. Vá em **API Keys** → **Create API Key**
4. Copie a chave e adicione no Railway:
   - **Nome:** `RESEND_API_KEY`
   - **Valor:** [sua chave]

### 3. RESEND_FROM_EMAIL 📧 (Recomendado)
- **Para testes:** `onboarding@resend.dev`
- **Para produção:** `contato@elpconsultoria.eng.br` (após verificar domínio)

No Railway:
- **Nome:** `RESEND_FROM_EMAIL`
- **Valor:** `onboarding@resend.dev`

---

## Passo a Passo: Deploy no Railway

### 1️⃣ Fazer commit dos arquivos atualizados

```bash
git add .
git commit -m "Adiciona configuração nixpacks.toml para Railway"
git push origin main
```

**Importante:** Certifique-se de que estes arquivos foram commitados:
- `nixpacks.toml`
- `requirements.txt`
- `railway.json`

### 2️⃣ Criar/Atualizar projeto no Railway

Se já tem um projeto:
1. No Railway, vá no seu projeto
2. Em **Settings**, clique em **Redeploy**

Se é novo:
1. Acesse [railway.app](https://railway.app)
2. Clique em **New Project**
3. Escolha **Deploy from GitHub repo**
4. Selecione seu repositório

### 3️⃣ Configurar variáveis de ambiente

No painel do Railway:
1. Vá em **Variables**
2. Adicione:
   ```
   SESSION_SECRET=wI5igJ7HyH1FDE7fv9qvKGFN7ngPJUkNVE_HPhe7Ua-CT4MscKGs8GlGHne1wTTI67QDReFAyqNhsZl6oxM0dg
   RESEND_API_KEY=[sua chave do Resend]
   RESEND_FROM_EMAIL=onboarding@resend.dev
   ```

### 4️⃣ Aguardar deploy

O Railway vai:
1. ✅ Detectar `nixpacks.toml`
2. ✅ Instalar Python 3.11
3. ✅ Executar `pip install --upgrade pip`
4. ✅ Instalar dependências do `requirements.txt`
5. ✅ Iniciar com `gunicorn --bind 0.0.0.0:$PORT --workers 4 main:app`

---

## Como o nixpacks.toml Resolve o Problema

O arquivo `nixpacks.toml` define explicitamente as fases de build:

```toml
[phases.setup]
nixPkgs = ["python311", "pip"]          # Instala Python e pip

[phases.install]
cmds = [
    "pip install --upgrade pip",        # Atualiza pip
    "pip install -r requirements.txt"   # Instala gunicorn e outras deps
]

[start]
cmd = "gunicorn --bind 0.0.0.0:$PORT --workers 4 main:app"
```

Isso garante que o **gunicorn seja instalado ANTES** de tentar executá-lo.

---

## Verificação Pós-Deploy

Após deploy bem-sucedido:

1. ✅ Acesse a URL do Railway
2. ✅ Teste a página inicial
3. ✅ Navegue para a página de **Contato**
4. ✅ Preencha e envie o formulário
5. ✅ Verifique se o email chegou em **comercial@elpconsultoria.eng.br**

---

## Visualizar Logs

Para ver o que está acontecendo:

1. No Railway, vá em **Deployments**
2. Clique no deployment ativo
3. Vá em **View Logs**
4. Você deve ver:
   ```
   Installing dependencies from requirements.txt...
   Successfully installed gunicorn-23.0.0 Flask-3.1.2 ...
   Starting gunicorn 23.0.0
   Listening at: http://0.0.0.0:XXXXX
   ```

---

## Troubleshooting

### ❌ Ainda vendo "gunicorn: command not found"

**Verifique:**
1. O arquivo `nixpacks.toml` foi commitado?
   ```bash
   git status
   git add nixpacks.toml
   git commit -m "Add nixpacks config"
   git push
   ```

2. O Railway detectou o `nixpacks.toml`?
   - Nos logs de build, deve aparecer "Using nixpacks.toml"

3. Tente fazer redeploy manual:
   - Settings → Redeploy

### ⚠️ Email não está sendo enviado

**Verifique:**
1. `RESEND_API_KEY` está configurada?
2. A chave é válida? (teste no painel do Resend)
3. Veja os logs para mensagens de erro

### 🔴 Erro 500

**Verifique:**
1. `SESSION_SECRET` está configurada?
2. Veja os logs para detalhes do erro

---

## Configuração de Email Profissional (Produção)

Para usar `contato@elpconsultoria.eng.br`:

### No Resend:
1. Vá em **Domains** → **Add Domain**
2. Digite: `elpconsultoria.eng.br`
3. Configure os registros DNS fornecidos:
   - **SPF**: Record TXT
   - **DKIM**: Record TXT
   - **DMARC**: Record TXT
4. Aguarde verificação (até 24h)

### No Railway:
1. Atualize a variável:
   ```
   RESEND_FROM_EMAIL=contato@elpconsultoria.eng.br
   ```

---

## Domínio Customizado

Para usar `elpconsultoria.eng.br`:

1. No Railway: **Settings** → **Domains** → **Custom Domain**
2. Digite seu domínio
3. Configure DNS conforme instruções:
   - **CNAME** ou **A Record**
4. Aguarde propagação (até 48h)

---

## Checklist de Deploy

- [ ] Arquivos commitados no GitHub:
  - [ ] `nixpacks.toml`
  - [ ] `requirements.txt`
  - [ ] `railway.json`
- [ ] Projeto criado/atualizado no Railway
- [ ] Variáveis configuradas:
  - [ ] `SESSION_SECRET`
  - [ ] `RESEND_API_KEY`
  - [ ] `RESEND_FROM_EMAIL`
- [ ] Build concluído sem erros
- [ ] Site acessível
- [ ] Formulário testado
- [ ] Email recebido

---

## Resumo das Correções

✅ **Criado `nixpacks.toml`** - Garante instalação correta das dependências  
✅ **Limpeza do `requirements.txt`** - Removidas duplicatas  
✅ **Configuração explícita** - Python 3.11 + pip + gunicorn  
✅ **Código compatível** - Funciona em Replit e Railway  

**Status:** Pronto para deploy! 🚀

---

## Suporte

- **Nixpacks:** https://nixpacks.com/docs
- **Railway:** https://docs.railway.app
- **Resend:** https://resend.com/docs
- **Flask:** https://flask.palletsprojects.com
