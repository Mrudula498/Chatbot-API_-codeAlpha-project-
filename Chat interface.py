st.header("A simple Chat Bot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

inputText=st.text_input("Input: ",key="input")
submitButton=st.button("Get Instant answers")

if submitButton and inputText:
    output=get_gemini_response(inputText)
    st.session_state['chat_history'].append(("You", inputText))
    st.subheader("The Response is")
    for outputChunk in output:
        st.write(outputChunk.text)
        st.session_state['chat_history'].append(("Bot", outputChunk.text))

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
