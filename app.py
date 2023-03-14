# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc 
from home_page import run_home_page
from eda_app import run_eda
from ml_app import run_ml

html_temp = """
		<div style="background-color:#FF0000;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Black Friday Sales App</h1>
		<h4 style="color:white;text-align:center;">Happy Thanksgiving</h4>
		</div>
		"""

def main():
	stc.html(html_temp)
	menu = ["Home","EDA","ML","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		run_home_page()
		pass
	elif choice == "EDA":
		run_eda()
	elif choice == "ML":
		run_ml()
	else:
		st.subheader("About")
		st.info("Built with Streamlit")
		st.header("Great things in business are never done by one person.They're done by a team of people")
		


if __name__ == '__main__':                                          
	main()