# Configuração do Railway para ELP Consultoria

## Arquivos de Configuração

O projeto já está configurado com os seguintes arquivos necessários para o Railway:

- ✅ `requirements.txt` - Dependências Python (incluindo gunicorn)
- ✅ `railway.json` - Configuração de build e deploy
- ✅ `Procfile` - Comando de inicialização
- ✅ `runtime.txt` - Versão do Python (3.11.0)

---

## Variáveis de Ambiente Necessárias

Configure as seguintes variáveis no Railway (Settings → Variables):

### 1. SESSION_SECRET ✅ (Já configurada)
```
wI5igJ7HyH1FDE7fv9qvKGFN7ngPJUkNVE_HPhe7Ua-CT4MscKGs8GlGHne1wTTI67QDReFAyqNhsZl6oxM0dg
```

### 2. RESEND_API_KEY (Obrigatório)
**Como obter:**
1. Acesse [resend.com](https://resend.com)
2. Faça login ou crie uma conta
3. Vá em "API Keys" → "Create API Key"
4. Copie a chave gerada

**No Railway:**
- Nome: `RESEND_API_KEY`
- Valor: Cole a chave da API

### 3. RESEND_FROM_EMAIL (Opcional, mas recomendado)
**Valores possíveis:**
- Para testes: `onboarding@resend.dev`
- Para produção: `contato@elpconsultoria.eng.br` (após verificar domínio no Resend)

**No Railway:**
- Nome: `RESEND_FROM_EMAIL`
- Valor: `onboarding@resend.dev` (ou seu email verificado)

### 4. PORT (Automático)
O Railway define automaticamente a variável `PORT`. **Não é necessário configurar.**

---

## Passo a Passo para Deploy

### 1. Preparar o Repositório
Faça commit e push de todos os arquivos para o GitHub:

```bash
git add .
git commit -m "Configuração para Railway"
git push origin main
```

### 2. Criar Projeto no Railway

1. Acesse [railway.app](https://railway.app)
2. Faça login
3. Clique em "New Project"
4. Escolha "Deploy from GitHub repo"
5. Selecione seu repositório

### 3. Configurar Variáveis de Ambiente

No painel do Railway:
1. Vá em "Variables"
2. Adicione as variáveis:
   - `SESSION_SECRET`: wI5igJ7HyH1FDE7fv9qvKGFN7ngPJUkNVE_HPhe7Ua-CT4MscKGs8GlGHne1wTTI67QDReFAyqNhsZl6oxM0dg
   - `RESEND_API_KEY`: [sua chave do Resend]
   - `RESEND_FROM_EMAIL`: onboarding@resend.dev

### 4. Deploy Automático

O Railway vai:
1. Detectar que é um projeto Python (através do `requirements.txt`)
2. Instalar as dependências automaticamente
3. Executar o comando do `Procfile` ou `railway.json`
4. Seu site estará no ar! 🚀

---

## Verificação Pós-Deploy

Após o deploy bem-sucedido:

1. ✅ Acesse a URL fornecida pelo Railway
2. ✅ Navegue até a página de Contato
3. ✅ Preencha e envie o formulário
4. ✅ Verifique se o email chegou em comercial@elpconsultoria.eng.br

---

## Logs e Troubleshooting

### Visualizar Logs no Railway
1. No painel do projeto, vá em "Deployments"
2. Clique no deployment ativo
3. Vá em "View Logs"

### Problemas Comuns

#### 1. "gunicorn: command not found" ❌ RESOLVIDO
- **Causa:** requirements.txt não foi processado corretamente
- **Solução:** Arquivo já corrigido! Faça redeploy.

#### 2. Email não está sendo enviado
- Verifique se `RESEND_API_KEY` está configurada
- Confirme que a chave é válida no painel do Resend
- Veja os logs para mensagens de erro específicas

#### 3. Erro 500 ao acessar o site
- Verifique se `SESSION_SECRET` está configurada
- Veja os logs do Railway para detalhes do erro

---

## Domínio Customizado (Opcional)

Para usar seu próprio domínio:

1. No Railway, vá em "Settings" → "Domains"
2. Clique em "Custom Domain"
3. Digite seu domínio (ex: elpconsultoria.eng.br)
4. Configure os registros DNS conforme instruções
5. Aguarde a propagação do DNS (até 48h)

---

## Email com Domínio Próprio (Produção)

Para usar email profissional no Resend:

1. No painel do Resend, vá em "Domains"
2. Clique em "Add Domain"
3. Digite: `elpconsultoria.eng.br`
4. Configure os registros DNS (SPF, DKIM, DMARC)
5. Aguarde verificação
6. Atualize `RESEND_FROM_EMAIL` no Railway para: `contato@elpconsultoria.eng.br`

---

## Checklist Final

Antes de considerar o deploy completo:

- [x] Código commitado e pushed para GitHub
- [ ] Projeto criado no Railway
- [ ] Variável `SESSION_SECRET` configurada
- [ ] Variável `RESEND_API_KEY` configurada
- [ ] Variável `RESEND_FROM_EMAIL` configurada
- [ ] Deploy bem-sucedido
- [ ] Site acessível via URL do Railway
- [ ] Formulário de contato testado e funcionando
- [ ] Email recebido em comercial@elpconsultoria.eng.br

---

## Suporte

- **Railway Docs:** https://docs.railway.app
- **Resend Docs:** https://resend.com/docs
- **Flask Docs:** https://flask.palletsprojects.com

---

## Resumo das Correções Aplicadas

✅ Limpeza do `requirements.txt` (removidas duplicatas)  
✅ Atualização do `railway.json` (configuração explícita do builder)  
✅ Código Python compatível com Railway e Replit  
✅ Formulário de contato funcionando com Resend  
✅ Tratamento de erros e mensagens ao usuário

**Status:** Pronto para deploy! 🚀
