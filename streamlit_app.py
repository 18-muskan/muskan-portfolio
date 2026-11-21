import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Muskan Ejaz – AI Engineer", layout="wide", initial_sidebar_state="collapsed")
st.markdown(
    "<style>header,footer,#MainMenu{visibility:hidden}"
    ".block-container{padding:0!important;max-width:100%!important}</style>",
    unsafe_allow_html=True,
)

root = Path(__file__).parent
page = root / "index.html"
if not page.exists():
    found = sorted(root.rglob("*.html"))
    page = found[0] if found else None

if page is None:
    st.error("Koi .html file nahi mili. Repository mein ye files hain:")
    st.write(sorted(str(p.relative_to(root)) for p in root.rglob("*") if p.is_file() and ".git" not in p.parts))
else:
    components.html(page.read_text(encoding="utf-8"), height=900, scrolling=True)
