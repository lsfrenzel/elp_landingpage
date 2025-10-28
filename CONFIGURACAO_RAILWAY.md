# Configuração do Railway para ELP Consultoria

## Variáveis de Ambiente Necessárias

Para que o projeto funcione corretamente no Railway, você precisa configurar as seguintes variáveis de ambiente:

### 1. SESSION_SECRET (Obrigatório)
**Descrição**: Chave secreta para gerenciar sessões do Flask de forma segura.

**Como gerar**:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Onde configurar no Railway**:
1. Acesse o projeto no Railway
2. Vá em "Variables"
3. Adicione a variável:
   - Nome: `SESSION_SECRET`
   - Valor: Cole a chave gerada acima

---

### 2. RESEND_API_KEY (Obrigatório para emails)
**Descrição**: Chave da API do Resend para envio de emails do formulário de contato.

**Como obter**:
1. Acesse [resend.com](https://resend.com)
2. Crie uma conta ou faça login
3. Vá em "API Keys"
4. Clique em "Create API Key"
5. Copie a chave gerada

**Onde configurar no Railway**:
1. Acesse o projeto no Railway
2. Vá em "Variables"
3. Adicione a variável:
   - Nome: `RESEND_API_KEY`
   - Valor: Cole a chave da API do Resend

---

### 3. RESEND_FROM_EMAIL (Recomendado)
**Descrição**: Email remetente para os emails enviados pelo sistema.

**Valor recomendado**: 
- Para testes: `onboarding@resend.dev`
- Para produção: Seu domínio verificado no Resend (ex: `contato@elpconsultoria.eng.br`)

**Como configurar domínio no Resend**:
1. No painel do Resend, vá em "Domains"
2. Adicione seu domínio (elpconsultoria.eng.br)
3. Configure os registros DNS conforme instruções
4. Aguarde a verificação

**Onde configurar no Railway**:
1. Acesse o projeto no Railway
2. Vá em "Variables"
3. Adicione a variável:
   - Nome: `RESEND_FROM_EMAIL`
   - Valor: `onboarding@resend.dev` (para testes) ou `contato@elpconsultoria.eng.br` (para produção)

---

## Checklist de Configuração

- [ ] Gerar e configurar `SESSION_SECRET`
- [ ] Criar conta no Resend.com
- [ ] Obter `RESEND_API_KEY`
- [ ] Configurar `RESEND_FROM_EMAIL`
- [ ] (Opcional) Verificar domínio no Resend para produção
- [ ] Fazer deploy no Railway
- [ ] Testar formulário de contato

---

## Verificação

Após configurar as variáveis:
1. Faça um novo deploy no Railway
2. Acesse a página de Contato
3. Preencha e envie o formulário
4. Verifique se o email foi enviado para comercial@elpconsultoria.eng.br

---

## Troubleshooting

### Email não está sendo enviado
1. Verifique se as variáveis estão configuradas corretamente no Railway
2. Confirme que a `RESEND_API_KEY` é válida
3. Verifique os logs do Railway para mensagens de erro
4. Se usar domínio próprio, confirme que ele está verificado no Resend

### Botão fica em "Enviando..."
- Isso indica que há um erro no servidor
- Verifique os logs do Railway
- Provavelmente a `RESEND_API_KEY` está faltando ou inválida

---

## Suporte

Para mais informações:
- Documentação do Resend: https://resend.com/docs
- Documentação do Railway: https://docs.railway.app
