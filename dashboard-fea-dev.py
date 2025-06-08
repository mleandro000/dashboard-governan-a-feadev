import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

# Configuração da página
st.set_page_config(
    page_title="FEA.dev GO! - Governança e Operações",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado com identidade visual moderna
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(255, 221, 0, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 221, 0, 0.08) 0%, transparent 50%),
            linear-gradient(45deg, transparent 30%, rgba(255, 221, 0, 0.03) 50%, transparent 70%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        border: 1px solid rgba(255, 221, 0, 0.2);
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="circuit" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M0,10 L5,10 M10,0 L10,5 M10,15 L10,20 M15,10 L20,10" stroke="rgba(255,221,0,0.1)" stroke-width="0.5" fill="none"/></pattern></defs><rect width="100" height="100" fill="url(%23circuit)"/></svg>') repeat;
        opacity: 0.3;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        padding: 2rem 1.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
        border: 1px solid rgba(255, 221, 0, 0.3);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 221, 0, 0.1), transparent);
        transition: left 0.6s ease;
    }
    
    .metric-card:hover::before {
        left: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(255, 221, 0, 0.2);
        border-color: rgba(255, 221, 0, 0.6);
    }
    
    .okr-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.9) 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #FFDD00;
        margin: 0.8rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .okr-card:hover {
        transform: translateX(5px);
        box-shadow: 0 12px 35px rgba(255, 221, 0, 0.2);
    }
    
    .event-card {
        background: linear-gradient(135deg, rgba(26, 26, 26, 0.95) 0%, rgba(45, 45, 45, 0.9) 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 0.8rem 0;
        border-left: 4px solid #FFDD00;
        color: white;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .event-card:hover {
        transform: translateX(5px);
        box-shadow: 0 12px 35px rgba(255, 221, 0, 0.3);
    }
    
    .tech-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        border: 1px solid rgba(255, 221, 0, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .tech-card:hover {
        border-color: rgba(255, 221, 0, 0.6);
        box-shadow: 0 12px 35px rgba(255, 221, 0, 0.2);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
    }
    
    .stSelectbox > div > div {
        background: rgba(26, 26, 26, 0.9);
        border: 1px solid rgba(255, 221, 0, 0.3);
        border-radius: 8px;
        color: white;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #FFDD00 0%, #FFB800 100%);
        color: #1a1a1a;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 221, 0, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 221, 0, 0.4);
    }
    
    .animated-bg {
        animation: pulse 4s ease-in-out infinite alternate;
    }
    
    @keyframes pulse {
        0% { opacity: 0.8; }
        100% { opacity: 1; }
    }

</style>
""", unsafe_allow_html=True)

# Dados simulados para demonstração
def load_sample_data():
    # OKRs por diretoria
    okrs_data = {
        'Diretoria': ['RH', 'Marketing', 'Tecnologia', 'Product Manager', 'Governança e Operações', 'Presidência'],
        'OKRs_Total': [5, 4, 6, 3, 4, 2],
        'OKRs_Concluidos': [3, 2, 4, 2, 3, 1],
        'Progresso': [60, 50, 67, 67, 75, 50]
    }
    
    # Eventos próximos
    eventos_data = {
        'Evento': ['Reunião de Diretoria', 'Workshop Python', 'FGV Datathon', 'Halloween FEA.dev', 'Desafio Itaú Asset'],
        'Data': ['2025-06-15', '2025-06-20', '2025-07-01', '2025-10-31', '2025-08-15'],
        'Tipo': ['Reunião', 'Capacitação', 'Competição', 'Social', 'Competição'],
        'Status': ['Confirmado', 'Inscrições Abertas', 'Planejamento', 'Planejamento', 'Inscrições Abertas']
    }
    
    # Newsletters
    newsletters_data = {
        'Título': ['Newsletter #15 - Junho 2025', 'Newsletter #14 - Maio 2025', 'Newsletter #13 - Abril 2025'],
        'Data': ['2025-06-01', '2025-05-01', '2025-04-01'],
        'Resumo': ['Resultados do 1º semestre, novos projetos em andamento', 'Recap dos eventos de maio, próximos desafios', 'Mudanças na estrutura organizacional']
    }
    
    # Squads ativos
    squads_data = {
        'Squad': ['Data Science Aplicada', 'Web Development', 'Mobile Solutions', 'AI Research'],
        'Projeto': ['Análise Preditiva Mercado', 'Portal FEA.dev 2.0', 'App Mobile FEA.dev', 'Chatbot Inteligente'],
        'PO': ['Ana Silva', 'Carlos Santos', 'Maria Oliveira', 'João Pereira'],
        'Membros': [8, 6, 5, 4],
        'Status': ['Em Andamento', 'Em Andamento', 'Planejamento', 'Pesquisa']
    }
    
    return okrs_data, eventos_data, newsletters_data, squads_data

# Sidebar - Navegação principal
def sidebar_navigation():
    st.sidebar.markdown("""
    <div style='text-align: center; padding: 2rem 1rem; background: linear-gradient(135deg, rgba(255,221,0,0.1) 0%, rgba(255,221,0,0.05) 100%); border-radius: 15px; margin-bottom: 1.5rem; border: 1px solid rgba(255,221,0,0.3);'>
        <div style='font-size: 3rem; margin-bottom: 0.5rem;'>
            <svg width="60" height="60" viewBox="0 0 100 100" style="filter: drop-shadow(0 4px 8px rgba(255,221,0,0.3));">
                <defs>
                    <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#FFDD00;stop-opacity:1" />
                        <stop offset="100%" style="stop-color:#FFB800;stop-opacity:1" />
                    </linearGradient>
                </defs>
                <path d="M20 20 L60 35 L20 80 Z" fill="url(#logoGrad)" opacity="0.9"/>
                <path d="M40 45 L80 25 L80 70 Z" fill="url(#logoGrad)" opacity="0.7"/>
            </svg>
        </div>
        <h2 style='color: #FFDD00; margin: 0; font-weight: 700; text-shadow: 0 2px 4px rgba(0,0,0,0.3);'>FEA.dev GO!</h2>
        <p style='color: rgba(255,221,0,0.8); margin: 0; font-size: 0.9em; font-weight: 500;'>Governança & Operações</p>
        <div style='width: 40px; height: 2px; background: linear-gradient(90deg, #FFDD00, transparent); margin: 0.5rem auto;'></div>
    </div>
    """, unsafe_allow_html=True)
    
    menu_options = {
        "🏠 Dashboard": "dashboard",
        "📊 Governança": "governanca", 
        "⚙️ Operações": "operacoes",
        "📞 Contatos": "contatos",
        "❓ Suporte": "suporte"
    }
    
    st.sidebar.markdown("### 🧭 Navegação")
    selected = st.sidebar.radio("Navegação Principal", list(menu_options.keys()), label_visibility="collapsed")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"""
    <div style='padding: 1rem; background: rgba(26,26,26,0.5); border-radius: 10px; border: 1px solid rgba(255,221,0,0.2);'>
        <h4 style='color: #FFDD00; margin: 0 0 0.5rem 0;'>📡 Sistema</h4>
        <div style='display: flex; align-items: center; margin-bottom: 0.3rem;'>
            <div style='width: 8px; height: 8px; background: #00ff00; border-radius: 50%; margin-right: 0.5rem; animation: pulse 2s infinite;'></div>
            <span style='color: white; font-size: 0.8em;'>Status: Online</span>
        </div>
        <div style='color: rgba(255,255,255,0.7); font-size: 0.7em;'>Última atualização: {datetime.now().strftime('%H:%M:%S')}</div>
    </div>
    """, unsafe_allow_html=True)
    
    return menu_options[selected]

# Dashboard Principal
def show_dashboard():
    st.markdown("""
    <div class="main-header animated-bg">
        <div style='position: relative; z-index: 2;'>
            <h1 style='font-size: 3rem; font-weight: 700; margin-bottom: 0.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
                🚀 Bem-vindos ao FEA.dev GO!
            </h1>
            <p style='font-size: 1.2rem; opacity: 0.9; font-weight: 400;'>
                Central de Governança e Operações da FEA.dev
            </p>
            <div style='width: 100px; height: 3px; background: linear-gradient(90deg, #FFDD00, #FFB800); margin: 1rem auto; border-radius: 2px;'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>📈</div>
            <h2 style='font-size: 2.5rem; margin: 0.5rem 0; font-weight: 700; color: #FFDD00;'>68%</h2>
            <p style='margin: 0; opacity: 0.9; font-weight: 500;'>Progresso Geral</p>
            <p style='margin: 0; opacity: 0.7; font-size: 0.8em;'>OKRs 2025</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>📅</div>
            <h2 style='font-size: 2.5rem; margin: 0.5rem 0; font-weight: 700; color: #FFDD00;'>5</h2>
            <p style='margin: 0; opacity: 0.9; font-weight: 500;'>Próximos Eventos</p>
            <p style='margin: 0; opacity: 0.7; font-size: 0.8em;'>30 dias</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>📝</div>
            <h2 style='font-size: 2.5rem; margin: 0.5rem 0; font-weight: 700; color: #FFDD00;'>15</h2>
            <p style='margin: 0; opacity: 0.9; font-weight: 500;'>Newsletters</p>
            <p style='margin: 0; opacity: 0.7; font-size: 0.8em;'>Publicadas 2025</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>👥</div>
            <h2 style='font-size: 2.5rem; margin: 0.5rem 0; font-weight: 700; color: #FFDD00;'>4</h2>
            <p style='margin: 0; opacity: 0.9; font-weight: 500;'>Squads Ativos</p>
            <p style='margin: 0; opacity: 0.7; font-size: 0.8em;'>Em desenvolvimento</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("## 🌟 Destaques Recentes")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📊 Progresso dos OKRs por Diretoria")
        okrs_data, _, _, _ = load_sample_data()
        df_okrs = pd.DataFrame(okrs_data)
        
        fig = px.bar(df_okrs, x='Diretoria', y='Progresso', 
                     title='Progresso dos OKRs (%)',
                     color='Progresso',
                     color_continuous_scale=[[0, '#FFB800'], [1, '#FFDD00']])
        
        fig.update_layout(
            showlegend=False, height=400, plot_bgcolor='rgba(26,26,26,0.9)',
            paper_bgcolor='rgba(26,26,26,0.9)', font_color='white',
            title_font_color='#FFDD00', title_font_size=16,
            xaxis=dict(gridcolor='rgba(255,221,0,0.2)'),
            yaxis=dict(gridcolor='rgba(255,221,0,0.2)'))
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card">
            <h4 style='color: #FFDD00; margin-bottom: 1rem;'>📰 Última Newsletter</h4>
            <h5 style='margin-bottom: 0.5rem;'>Newsletter #15 - Junho 2025</h5>
            <p style='opacity: 0.8; font-size: 0.9em; margin-bottom: 1rem;'>
                Resultados do 1º semestre e novos projetos em andamento
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        dias_restantes = (datetime(2025, 6, 15) - datetime.now()).days
        st.markdown(f"""
        <div class="tech-card" style='margin-top: 1rem;'>
            <h4 style='color: #FFDD00; margin-bottom: 1rem;'>📅 Próximo Evento</h4>
            <h5 style='margin-bottom: 0.5rem;'>Reunião de Diretoria</h5>
            <p style='opacity: 0.8; margin-bottom: 0.5rem;'>📅 15 de Junho, 2025</p>
            <div style='background: rgba(255,221,0,0.1); padding: 0.5rem; border-radius: 6px; text-align: center; margin-bottom: 1rem;'>
                <span style='color: #FFDD00; font-weight: 600;'>⏰ Faltam {dias_restantes} dias</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Seção Governança
def show_governanca():
    st.markdown("# 📊 Governança")
    
    tabs = st.tabs(["📰 Newsletters", "📋 Relatórios RD", "🎯 OKRs", "📅 Calendário"])
    
    with tabs[0]:
        st.markdown("## 📰 Newsletters e Comunicados")
        
        col1, col2 = st.columns(2)
        with col1:
            year_filter = st.selectbox("Ano", [2025, 2024, 2023])
        with col2:
            month_filter = st.selectbox("Mês", ["Todos", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"])
        
        _, _, newsletters_data, _ = load_sample_data()
        df_newsletters = pd.DataFrame(newsletters_data)
        
        # --- CÓDIGO CORRIGIDO E INTEGRADO ---
        for idx, newsletter in df_newsletters.iterrows():
            with st.expander(f"📄 {newsletter['Título']} - {newsletter['Data']}", expanded=(idx == 0)):
                st.write(f"**Resumo:** {newsletter['Resumo']}")
                
                if idx == 0:
                    st.markdown("""
                    <div style='background: rgba(26,26,26,0.1); padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 3px solid #FFDD00;'>
                        <h5>📊 Destaques desta edição:</h5>
                        <ul style='margin: 0;'>
                            <li>✅ 68% dos OKRs cumpridos no semestre</li>
                            <li>🚀 3 novos projetos iniciados</li>
                            <li>👥 Expansão de 2 squads técnicos</li>
                            <li>🎯 Meta de 500 membros atingida</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
                b_col1, b_col2, b_col3 = st.columns(3)
                with b_col1:
                    if st.button("📖 Ler Online", key=f"read_{idx}"):
                        st.success(f"Abrindo a newsletter: {newsletter['Título']}")
                with b_col2:
                    if st.button("⬇️ Download PDF", key=f"download_{idx}"):
                        st.info(f"Iniciando download de: {newsletter['Título']}")
        # --- FIM DO CÓDIGO CORRIGIDO ---

    with tabs[1]:
        st.markdown("## 📋 Relatórios das Reuniões de Diretoria")
        search_term = st.text_input("🔍 Buscar por tópico", placeholder="Ex: OKRs, orçamento, eventos...")
        relatorios = [
            {"data": "2025-06-01", "temas": "OKRs Q2, Planejamento Halloween, Orçamento Eventos"},
            {"data": "2025-05-15", "temas": "Resultados FGV Datathon, Reestruturação Squads"},
            {"data": "2025-05-01", "temas": "Aprovação Novos Projetos, Feedback Comunidade"}
        ]
        for i, relatorio in enumerate(relatorios):
            with st.expander(f"📊 RD {relatorio['data']}"):
                st.write(f"**Temas Abordados:** {relatorio['temas']}")
                st.button("📄 Ver Relatório Completo", key=f"relatorio_{i}")
    
    with tabs[2]:
        st.markdown("## 🎯 Acompanhamento de OKRs")
        okrs_data, _, _, _ = load_sample_data()
        df_okrs = pd.DataFrame(okrs_data)
        
        col1, col2 = st.columns(2)
        with col1:
            total_okrs = df_okrs['OKRs_Total'].sum()
            completed_okrs = df_okrs['OKRs_Concluidos'].sum()
            labels = ['Concluídos', 'Em Andamento']
            values = [completed_okrs, total_okrs - completed_okrs]
            
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
            fig.update_traces(hoverinfo='label+percent', textinfo='value+percent', marker=dict(colors=['#FFDD00', '#2d2d2d']))
            fig.update_layout(title="Status Geral dos OKRs", height=400, paper_bgcolor='rgba(0,0,0,0)', font_color='white')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 📊 Detalhes por Diretoria")
            for idx, row in df_okrs.iterrows():
                progress_color = "🟢" if row['Progresso'] >= 70 else "🟡" if row['Progresso'] >= 50 else "🔴"
                st.markdown(f"""
                <div class="okr-card">
                    <strong>{progress_color} {row['Diretoria']}</strong><br>
                    Progresso: {row['Progresso']}% ({row['OKRs_Concluidos']}/{row['OKRs_Total']} OKRs)
                </div>
                """, unsafe_allow_html=True)
    
    with tabs[3]:
        st.markdown("## 📅 Calendário da Entidade")
        _, eventos_data, _, _ = load_sample_data()
        df_eventos = pd.DataFrame(eventos_data)
        
        st.markdown("### 📅 Próximos Eventos")
        for idx, evento in df_eventos.iterrows():
            status_color = "🟢" if evento['Status'] == 'Confirmado' else "🟡"
            st.markdown(f"""
            <div class="event-card">
                <strong>{status_color} {evento['Evento']}</strong><br>
                📅 {evento['Data']} | 🏷️ {evento['Tipo']} | Status: {evento['Status']}
            </div>
            """, unsafe_allow_html=True)

# Seção Operações
def show_operacoes():
    st.markdown("# ⚙️ Operações")
    
    tabs = st.tabs(["🏢 Reserva de Espaços", "🎉 Eventos", "👥 Squads"])
    
    with tabs[0]:
        st.markdown("## 🏢 Reserva de Espaços")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### 📝 Nova Reserva")
            with st.form("reserva_form"):
                nome = st.text_input("Nome do Solicitante")
                espaco = st.selectbox("Espaço", ["Sala de Reunião A", "Sala de Reunião B", "Auditório", "Laboratório"])
                data = st.date_input("Data")
                hora_inicio = st.time_input("Hora Início")
                hora_fim = st.time_input("Hora Fim")
                motivo = st.text_area("Motivo da Reserva")
                if st.form_submit_button("📋 Solicitar Reserva"):
                    st.success("✅ Solicitação enviada! Aguarde aprovação.")
        with col2:
            st.markdown("### 📅 Espaços Ocupados")
            ocupacao_data = {
                'Espaço': ['Sala A', 'Sala B', 'Auditório', 'Laboratório'],
                'Hoje': ['14:00-16:00', 'Livre', '09:00-12:00', 'Livre'],
                'Amanhã': ['10:00-12:00', '14:00-17:00', 'Livre', '13:00-15:00']
            }
            df_ocupacao = pd.DataFrame(ocupacao_data)
            st.dataframe(df_ocupacao, use_container_width=True)
            st.info("💡 **Regras de Reserva:**\n- Antecedência mínima: 24h\n- Duração máxima: 4h\n- Confirmação em até 2h")
            
    with tabs[1]:
        st.markdown("## 🎉 Eventos Pontuais")
        st.markdown("### 📸 Galeria - Eventos Passados")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://via.placeholder.com/300x200/FFDD00/000000?text=Halloween+2024", caption="Halloween 2024")
        with col2:
            st.image("https://via.placeholder.com/300x200/FFB800/000000?text=Sitio+Verao+2024", caption="Sítio Verão 2024")
        with col3:
            st.image("https://via.placeholder.com/300x200/FFDD00/000000?text=Confrat+2024", caption="Confraternização 2024")

    with tabs[2]:
        st.markdown("## 👥 Squads e Grupos de Trabalho")
        _, _, _, squads_data = load_sample_data()
        df_squads = pd.DataFrame(squads_data)
        for idx, squad in df_squads.iterrows():
            with st.expander(f"🚀 {squad['Squad']} - {squad['Status']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Projeto:** {squad['Projeto']}")
                    st.write(f"**Product Owner:** {squad['PO']}")
                    st.write(f"**Membros:** {squad['Membros']} pessoas")
                with col2:
                    status_color = "🟢" if squad['Status'] == 'Em Andamento' else "🟡"
                    st.write(f"**Status:** {status_color} {squad['Status']}")
                    st.button("🔗 Acessar Trello", key=f"trello_{idx}")
                    st.button("📋 Ver Notion", key=f"notion_{idx}")

# --- BLOCO PRINCIPAL PARA EXECUTAR O APP ---
if 'page' not in st.session_state:
    st.session_state.page = "dashboard"

# Captura a seleção da página da sidebar
# st.session_state.page = sidebar_navigation() -> Causa loop com st.rerun
page_selection = sidebar_navigation()

# Renderiza a página selecionada
if page_selection == "dashboard":
    show_dashboard()
elif page_selection == "governanca":
    show_governanca()
elif page_selection == "operacoes":
    show_operacoes()
elif page_selection == "contatos":
    st.title("📞 Contatos")
    st.info("Página de Contatos em construção.")
elif page_selection == "suporte":
    st.title("❓ Suporte")
    st.info("Página de Suporte em construção.")