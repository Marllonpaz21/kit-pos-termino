import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Kit Pós-Término 💔", layout="centered")

# Estilo personalizado com HTML e CSS
st.markdown("""
    <style>
        body {
            background-image: url('https://i.pinimg.com/originals/84/0e/b8/840eb83a07cfbfb841c06f1e43539c12.jpg');
            background-size: cover;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 12px;
            font-family: 'Arial', sans-serif;
        }
        h1, h2, h3 {
            color: #c62828;
        }
        .block-container {
            padding: 2rem 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# GIF de abertura
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTYwMzhkYmRiZjdmMjZjN2Q5MzY5ZTc2OGZhNWM1ZmY2YjZjNTQzMiZjdD1n/wP1Kz8P1VxkZ2/giphy.gif")

# Título e subtítulo
st.title("💔 Kit de Reorganização de Vida Após um Pé na Bunda")
st.markdown("<h4>🌈 Porque a vida continua — e você também!</h4>", unsafe_allow_html=True)

# -------------------------
# Frase motivacional
# -------------------------
st.markdown("<h2>🧠 Frase motivacional do dia</h2>", unsafe_allow_html=True)
frases = [
    "Você não perdeu um amor, perdeu quem não te amava de verdade.",
    "Se valorize! Você é o prêmio. 🏆",
    "Cada término é uma chance de recomeçar mais forte.",
    "Um dia vai doer menos. E outro dia, nem vai doer mais.",
    "Não corra atrás de quem não ficaria por você.",
    "Sua paz vale mais que qualquer relacionamento tóxico.",
    "Você é incrível mesmo que alguém tenha sido cego demais pra ver isso."
]

if st.button("✨ Me inspira aí"):
    st.success(random.choice(frases))

# -------------------------
# Checklist emocional
# -------------------------
st.markdown("<h2>✅ Checklist de Primeiros Socorros Emocionais</h2>", unsafe_allow_html=True)
check1 = st.checkbox("🛌 Dormiu bem?")
check2 = st.checkbox("💧 Bebeu água hoje?")
check3 = st.checkbox("🚫 Bloqueou a pessoa?")
check4 = st.checkbox("🙈 Evitou stalkear?")

if check1 and check2 and check3 and check4:
    st.balloons()
    st.success("Você tá se cuidando direitinho. Orgulho de você 💛")
else:
    st.info("Não tem problema... faz o possível por hoje 🧲")

# -------------------------
# Tarefa do dia
# -------------------------
st.markdown("<h2>📋 Tarefa do Dia</h2>", unsafe_allow_html=True)
tarefas = [
    "🛎️ Arrume sua cama ouvindo uma música animada.",
    "☁️ Saia pra caminhar 10 minutos e observe as nuvens.",
    "📝 Escreva 3 coisas que você ama em você.",
    "🚫 Bloqueie o ex — você merece paz mental.",
    "🎨 Faça algo que te fazia feliz antes desse relacionamento.",
    "📹 Grave um vídeo dizendo o quanto você merece ser feliz.",
]

if st.button("🎯 Nova missão"):
    st.info(random.choice(tarefas))

# -------------------------
# Playlist
# -------------------------
st.markdown("<h2>🎷 Escolha sua vibe de hoje</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("😭 Quero chorar"):
        st.markdown("[Ouvir no Spotify](https://open.spotify.com/playlist/37i9dQZF1DWX83CujKHHOn)")

with col2:
    if st.button("🚀 Quero superar logo"):
        st.markdown("[Ouvir no Spotify](https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0)")

# -------------------------
# Diário terapêutico
# -------------------------
st.markdown("<h2>📓 Diário Terapêutico</h2>", unsafe_allow_html=True)

diario = st.text_area("💬 Escreve o que você tá sentindo hoje (ninguém vai ler, é só pra você)")

if st.button("💌 Salvar no coração"):
    if diario.strip() == "":
        st.warning("Escreve um pouquinho, vai te fazer bem 💭")
    else:
        st.success("Prontinho! Às vezes desabafar já alivia bastante.")

# -------------------------
# Botão "Falar com um amigo"
# -------------------------
st.markdown("<h2>📞 Falar com um amigo</h2>", unsafe_allow_html=True)

mensagem = "Oi, tô precisando conversar. Tem um tempinho?"
url_whatsapp = f"https://wa.me/?text={mensagem.replace(' ', '%20')}"

if st.button("💬 Enviar no WhatsApp"):
    st.markdown(f"[Abrir conversa no WhatsApp]({url_whatsapp})", unsafe_allow_html=True)

# -------------------------
# Mensagem final
# -------------------------
st.markdown("---")
st.markdown("💬 <i>Você não é o que aconteceu com você. Você é o que você faz com isso.</i>", unsafe_allow_html=True)
st.caption("Feito com carinho pra quem precisa se reconstruir. Você vai ficar bem. 💛")
