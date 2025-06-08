# FEA.dev GO! - Canal Digital da Diretoria de Governança e Operações

## 📋 Visão Geral do Projeto

O **FEA.dev GO!** (Governança e Operações) é um aplicativo Streamlit desenvolvido para servir como canal digital interno da Diretoria de Governança e Operações da FEA.dev. O objetivo é centralizar informações, otimizar processos e promover transparência e eficiência organizacional.

## 🎯 Objetivos

- **Centralização**: Unificar todas as informações e ferramentas operacionais
- **Transparência**: Facilitar acesso a relatórios, OKRs e calendários
- **Eficiência**: Otimizar processos como reserva de espaços e organização de eventos
- **Engajamento**: Manter membros informados e conectados
- **Cultura de Dados**: Visualizar progresso de OKRs e métricas importantes
- **Inovação**: Demonstrar compromisso com tecnologia na gestão

## 🏗️ Arquitetura do Sistema

### Tecnologias Utilizadas
- **Frontend/Backend**: Python + Streamlit
- **Dados**: CSV/Excel, Google Sheets, SQLite
- **Integrações**: APIs Google Calendar, Google Drive
- **Visualização**: Plotly, Matplotlib, Streamlit Charts

### Estrutura de Dados
```
data/
├── newsletters/
├── okrs/
├── eventos/
├── reservas/
├── squads/
└── contatos/
```

## 📱 Funcionalidades Principais

### 1. Dashboard Inicial
- **Boas-vindas**: Mensagem da Diretoria de GO
- **Destaques Rápidos**:
  - Última newsletter publicada
  - Próximos eventos importantes
  - Progresso geral dos OKRs
  - Notícias e comunicados urgentes

### 2. Seção Governança

#### 2.1 Newsletters e Comunicados
- Lista cronológica de newsletters
- Filtros por mês/ano
- Visualização direta no app
- Download de arquivos
- Seção de comunicados urgentes

#### 2.2 Relatórios das RD's (Reuniões de Diretoria)
- Lista organizada por data
- Resumos executivos
- Pesquisa por tópicos
- Acesso aos detalhes completos

#### 2.3 Acompanhamento de OKRs
- **Diretorias monitoradas**:
  - RH
  - Marketing
  - Tecnologia
  - Product Manager
  - Governança e Operações
  - Presidência

- **Métricas por OKR**:
  - Status (em andamento, concluído, em atraso)
  - Progresso percentual
  - Gráficos de progresso
  - Timeline de execução

#### 2.4 Calendário da Entidade
- Integração com Google Calendar público
- Eventos, reuniões, prazos de projetos
- Filtros por tipo e diretoria
- Alertas de eventos próximos

### 3. Seção Operações

#### 3.1 Reserva de Espaços
- **Funcionalidades**:
  - Formulário de solicitação
  - Calendário de ocupação
  - Regras e diretrizes
  - Sistema de aprovação
  - Notificações automáticas

#### 3.2 Eventos Pontuais
- **Informações dos eventos**:
  - Datas e locais
  - Detalhes logísticos
  - Formulários RSVP
  - Voluntariado para organização
  - Galeria de eventos passados

#### 3.3 Squads e Grupos de Trabalho
- **Para cada squad**:
  - Informações do projeto
  - Lista de membros
  - Product Owner/Gerente responsável
  - Links para ferramentas (Trello, Notion)
  - Status do projeto

#### 3.4 Canais de Comunicação
- Links para grupos WhatsApp oficiais
- Acesso ao Google Drive organizado
- Diretrizes de uso
- Manual FEA.dev digital

### 4. Recursos e Ferramentas

#### 4.1 Contatos das Diretorias
- **Informações disponíveis**:
  - Presidente: Gabriel Braz
  - Vice-presidente: Julia Cerqueira
  - Diretora de RH: Júlia Toledo
  - Demais diretores e vice-diretores

#### 4.2 Sistema de Suporte
- FAQ (Perguntas Frequentes)
- Formulário de feedback
- Sistema de tickets/sugestões
- Canal direto com Diretoria GO

## 🎨 Interface do Usuário

### Navegação Principal
- **Sidebar** com menu principal
- **Tabs** para seções secundárias
- **Dashboard** como página inicial
- **Breadcrumbs** para navegação

### Componentes Visuais
- **Cards informativos** para destaques
- **Gráficos interativos** para OKRs
- **Calendários visuais** para eventos
- **Tabelas filtráveis** para dados
- **Formulários intuitivos** para interações

## 📊 Métricas e Analytics

### KPIs do Sistema
- Taxa de utilização do app
- Frequência de acesso às seções
- Número de reservas de espaços
- Engagement com newsletters
- Progresso dos OKRs

### Relatórios Automáticos
- Relatório mensal de atividades
- Dashboard de métricas em tempo real
- Exportação de dados para análise

## 🔒 Segurança e Acesso

### Controle de Acesso
- Autenticação por credenciais FEA.dev
- Níveis de permissão por seção
- Logs de acesso e atividades

### Backup e Recuperação
- Backup automático diário
- Versionamento de dados importantes
- Plano de recuperação de desastres

## 📈 Roadmap de Desenvolvimento

### Fase 1 - MVP (4 semanas)
- [ ] Dashboard inicial
- [ ] Seção de newsletters
- [ ] Acompanhamento básico de OKRs
- [ ] Sistema de contatos

### Fase 2 - Operações (6 semanas)
- [ ] Sistema de reserva de espaços
- [ ] Gestão de eventos
- [ ] Integração com Google Calendar
- [ ] FAQ e suporte

### Fase 3 - Avançado (8 semanas)
- [ ] Analytics avançados
- [ ] Integrações com ferramentas externas
- [ ] Sistema de notificações
- [ ] Mobile responsivo

### Fase 4 - Otimização (4 semanas)
- [ ] Performance optimization
- [ ] Testes de usabilidade
- [ ] Documentação completa
- [ ] Treinamento dos usuários

## 🚀 Implementação e Deploy

### Ambiente de Desenvolvimento
```bash
# Instalação das dependências
pip install streamlit pandas plotly google-api-python-client

# Execução local
streamlit run app.py
```

### Ambiente de Produção
- Deploy em Streamlit Cloud
- Configuração de domínio personalizado
- Monitoramento de performance
- Backup automático

## 📝 Documentação Técnica

### Estrutura do Código
```
feadev_go/
├── app.py                 # Aplicação principal
├── pages/                 # Páginas do aplicativo
│   ├── dashboard.py
│   ├── governanca.py
│   └── operacoes.py
├── components/            # Componentes reutilizáveis
├── data/                  # Dados e configurações
├── utils/                 # Funções utilitárias
└── requirements.txt       # Dependências
```

### APIs e Integrações
- Google Calendar API
- Google Drive API
- Google Sheets API
- WhatsApp Business API (futuro)

## 🎓 Benefícios Esperados

### Para a Organização
- **Redução de 40%** no tempo de busca por informações
- **Aumento de 60%** na transparência organizacional
- **Melhoria de 50%** na eficiência de processos
- **Centralização** de 100% das informações operacionais

### Para os Membros
- Acesso rápido e fácil a informações
- Maior engajamento com atividades da entidade
- Melhor compreensão dos objetivos organizacionais
- Canal direto de comunicação com liderança

## 🔧 Manutenção e Suporte

### Atualizações Regulares
- Atualizações mensais de conteúdo
- Melhorias baseadas em feedback
- Adição de novas funcionalidades
- Correções de bugs

### Suporte aos Usuários
- Manual do usuário online
- Vídeos tutoriais
- Suporte via chat/email
- Treinamentos presenciais

---

**Desenvolvido com ❤️ para a FEA.dev**  
*Diretoria de Governança e Operações*