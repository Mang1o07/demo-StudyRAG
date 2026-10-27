"""StudyRAG · demo online. Avvio: streamlit run streamlit_app.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

try:
    from views import main
except Exception as e:
    import streamlit as st
    st.error(f"Errore di import: {type(e).__name__}: {e}")
    st.write("Cartella dell'app:", HERE)
    for root, dirs, files in os.walk(HERE):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
        st.text(f"{os.path.relpath(root, HERE)}: {sorted(files)}")
else:
    main.run()
