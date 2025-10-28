# Configuração para Deploy no Railway

## Arquivos de Configuração

O projeto já está configurado com os seguintes arquivos necessários para o Railway:

- **requirements.txt**: Lista de dependências Python que o Railway instalará automaticamente
- **runtime.txt**: Especifica a versão do Python (3.11.0)
- **Procfile**: Define o comando para iniciar o servidor (gunicorn)
- **railway.json**: Configurações específicas do Railway

## Variáveis de Ambiente Necessárias

Para que o projeto funcione corretamente no Railway, configure as seguintes variáveis de ambiente:

### 1. SESSION_SECRET (Obrigatório)
Chave secreta para sessões do Flask. Gere uma chave aleatória segura.

```bash
SESSION_SECRET=sua-chave-secreta-aqui
```

**Como gerar uma chave segura:**
```python
import secrets
print(secrets.token_urlsafe(64))
```

### 2. RESEND_API_KEY (Obrigatório)
Chave de API do Resend para envio de emails.

```bash
RESEND_API_KEY=re_SuaChaveDoResendAqui
```

**Como obter:**
1. Acesse https://resend.com/
2. Faça login ou crie uma conta
3. Vá em "API Keys"
4. Crie uma nova API key

### 3. RESEND_FROM_EMAIL (Opcional)
Email de origem para os emails enviados. Se não configurado, usa o padrão do Resend.

```bash
RESEND_FROM_EMAIL=onboarding@resend.dev
```

**Nota:** Para usar um domínio personalizado, você precisa verificá-lo no Resend primeiro.

### 4. RAILWAY_ENVIRONMENT (Automático)
O Railway define essa variável automaticamente quando o app está em produção.

## Passos para Configurar no Railway

1. Acesse o dashboard do Railway
2. Selecione seu projeto
3. Vá em "Variables"
4. Adicione cada variável:
   - Clique em "New Variable"
   - Digite o nome da variável
   - Digite o valor
   - Clique em "Add"

5. Após adicionar todas as variáveis, faça um novo deploy ou reinicie o serviço

## Verificação

Após configurar as variáveis, o formulário de contato deve:
- Enviar emails para comercial@elpconsultoria.eng.br
- Exibir mensagens de sucesso/erro apropriadas
- Registrar logs de envio

## Troubleshooting

### Erro: "SESSION_SECRET environment variable must be set"
- Adicione a variável SESSION_SECRET no Railway

### Erro: "RESEND_API_KEY environment variable not found"
- Adicione a variável RESEND_API_KEY no Railway com sua chave do Resend

### Emails não estão sendo enviados
- Verifique se a RESEND_API_KEY está correta
- Verifique os logs do Railway para mensagens de erro
- Confirme que sua conta Resend está ativa
