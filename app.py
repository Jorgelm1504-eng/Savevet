import streamlit as st

col1, col2 = st.columns([1, 3])  # proporção: 1 parte logo, 3 partes título

with col1:
    st.image("logo.jpg", width=120)

with col2:
    st.markdown("<h1 style='margin-bottom:0; font-size:35px;'>Savevet - Centro Veterinário</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: gray; margin-top:0;font-size:25px;'>💡 Cálculo de Conta de Luz</h3>", unsafe_allow_html=True)
    
st.markdown("---")  # cria uma linha horizontal em toda a largura da coluna

# Entradas do usuário
consumo_total = st.number_input("Digite o consumo total em kWh:", min_value=0, step=1)
consumo_outra = st.number_input("Digite o consumo do Banho&Tosa em kWh:", min_value=0, step=1)
valor_total = st.number_input("Digite o valor total da conta de luz em R$:", min_value=0.0, step=0.01)
st.markdown("<h2 style='color: gray; margin-top:0;font-size:15px;font-style: italic;text-align: right;'>by Metric - IA e Automações </h2>", unsafe_allow_html=True)

# Botão para calcular
if st.button("Calcular"):
    if consumo_total > 0:
        # Cálculos
        valor_kwh = valor_total / consumo_total
        valor_outra = consumo_outra * valor_kwh

        # Exibição dos resultados
        st.subheader("🔹 Resultado")
        st.write(f"Valor de 1 kWh: **R$ {valor_kwh:.2f}**")
        st.write(f"Consumo do Banho&Tosa: **{int (consumo_outra)}kWh**")
        st.write(f"Valor que o Banho&Tosa deve pagar: **R$ {valor_outra:.2f}**")
    else:
        st.warning("⚠️ O consumo total deve ser maior que zero.")
