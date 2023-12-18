import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)
from services.poke_service import RequestSender

def main():
    st.title('CBR POKEMON')

    # Create a navigation menu
    page = st.sidebar.selectbox("Go to", ["Home", "Attributes Form"])

    if page == "Home":
        display_home()
    elif page == "Attributes Form":
        display_attributes_form()

def display_home():
    # Set page title
    st.title("QUEM É ESSE POKÉMON!??")

    # Display a picture
    st.image("img/pokemons image.png", caption="Pokemon Image", use_column_width=True)

    # Write a description
    st.write("""
        Bem vindo ao mundo Pokémon! Somos pesquisadores Pokémon assim como você e desenvolvemos o nosso sistema para que
        você consiga inferir qual Pokémon mais se adequa aos parâmetros referenciados! 

        ...

        Eu escolho você!!!
    """)

def display_attributes_form():
    with st.form(key='attributes_form'):
        st.write("Preencha o formulário com os atributos:")

        total = st.slider("Total", min_value=0, max_value=800, step=1)
        hp = st.slider("HP", min_value=0, max_value=255, step=1)
        attack = st.slider("Attack", min_value=0, max_value=255, step=1)
        defense = st.slider("Defense", min_value=0, max_value=255, step=1)
        sp_atk = st.slider("Sp_Atk", min_value=0, max_value=255, step=1)
        sp_def = st.slider("Sp_Def", min_value=0, max_value=255, step=1)
        speed = st.slider("Speed", min_value=0, max_value=255, step=1)
        generation = st.slider("Generation", min_value=1, max_value=6, step=1)
        is_legendary = st.checkbox("Is Legendary?")
        has_gender = st.checkbox("Has Gender?")
        pr_male = st.slider("Probability of Being Male", min_value=0.0, max_value=1.0, step=0.125)
        has_mega_evolution = st.checkbox("Has Mega Evolution?")
        height_m = st.slider("Height (m)", min_value=0.0, max_value=10.0, step=0.1)
        weight_kg = st.slider("Weight (kg)", min_value=0.0, max_value=1000.0, step=1.0)
        catch_rate = st.slider("Catch Rate", min_value=3, max_value=255, step=1)

        submit_button = st.form_submit_button('Submit')

        if submit_button:
            # Process the form data here
            attributes = {
                'Total': total, 'HP': hp, 'Attack': attack, 'Defense': defense,
                'Sp_Atk': sp_atk, 'Sp_Def': sp_def, 'Speed': speed,
                'Generation': generation, 'isLegendary': is_legendary,
                'hasGender': has_gender, 'Pr_Male': pr_male,
                'hasMegaEvolution': has_mega_evolution,
                'Height_m': height_m, 'Weight_kg': weight_kg,
                'Catch_Rate': catch_rate
            }
            
            request = RequestSender('http://127.0.0.1:5000')
            response = (dict(request.send_request(attributes)['Name']).values()).mapping
            response = list(response.values())
            st.markdown(f"<h4 style='color: blue;'>O pokémon que se adequa aos dados é {response[0]}</h1>", unsafe_allow_html=True)

            google_link = f'[Clique aqui e saiba mais sobre {response[0]}](https://www.google.com/search?q={response[0]})'
            st.markdown(google_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
