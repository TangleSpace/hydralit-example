mkdir -p ~/.streamlit/
echo "
[general]n
email = "c6lculus8ntr0py@gmail.com"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=falsen
port = $PORTn
" > ~/.streamlit/config.toml