import streamlit as st
import pandas as pd
import os
from io import BytesIO
import random
from dotenv import load_dotenv
import google.generativeai as gen_ai


# Load environment variables
load_dotenv('.env')

# Function to get a random motivational quote


def get_random_quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "Your limitation—it's only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
    ]
    return random.choice(quotes)


# Set up App Configuration
st.set_page_config(
    page_title='Data Sweeper - Mind Growth Village', layout='wide', page_icon='🌿')

# Sidebar Navigation # Add a logo (replace URL)
st.sidebar.title("📂 Mind Growth")

page = st.sidebar.radio("Go to:", [
    "🏠 Home",
    "🤖 AI Chatbot",
    "📂 Data Sweeper",
    "📝 To-Do List",
    "ℹ️ About"
])

# # Home Page
# if page == "Home":
#     # Custom CSS for a stylish navbar
#     st.markdown("""
#         <style>
#             .navbar {
#                 background-color: #4CAF50;
#                 padding: 10px;
#                 text-align: center;
#                 border-radius: 10px;
#             }
#             .navbar a {
#                 color: white;
#                 text-decoration: none;
#                 font-size: 18px;
#                 padding: 14px 20px;
#                 display: inline-block;
#             }
#             .navbar a:hover {
#                 background-color: #45a049;
#                 border-radius: 5px;
#             }
#             .quote {
#                 font-size: 22px;
#                 font-style: italic;
#                 text-align: center;
#                 color: #333;
#                 margin-top: 20px;
#             }
#             .quote-author {
#                 font-size: 18px;
#                 text-align: center;
#                 color: #555;
#             }
#         </style>
#     """, unsafe_allow_html=True)


#     # Homepage Content
#     st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌱 Welcome to MindGrowth Village 🚀</h1>", unsafe_allow_html=True)

#     st.write("### 🔥 Unleash Your Full Potential with a Growth Mindset!")
#     st.write("At **MindGrowth Village**, we believe in continuous learning and self-improvement. Whether you’re looking for daily motivation, challenges, or success stories, you’ve come to the right place.")

#     st.write("---")

#      # Motivational Quotes
#     quotes = [
#         ("Your only limit is your mind.", "Anonymous"),
#         ("Challenges are what make life interesting. Overcoming them is what makes life meaningful.", "Joshua J. Marine"),
#         ("Growth and comfort do not coexist.", "Ginni Rometty"),
#         ("Do not be embarrassed by your failures, learn from them and start again.", "Richard Branson"),
#         ("Believe you can and you’re halfway there.", "Theodore Roosevelt")
#     ]
#     selected_quote, author = random.choice(quotes)

#     st.markdown(f"<p class='quote'>“{selected_quote}”</p>", unsafe_allow_html=True)
#     st.markdown(f"<p class='quote-author'>- {author}</p>", unsafe_allow_html=True)


#     # Challenge of the Day
#     st.subheader("💡 Challenge of the Day")
#     daily_challenge = random.choice([
#         "Write down 3 things you are grateful for.",
#         "Try something new today, even if it scares you.",
#         "Spend 30 minutes learning a new skill.",
#         "Reflect on a past mistake and write what you learned from it.",
#         "Say positive affirmations to yourself in the mirror for 2 minutes."
#     ])

#     st.write(f"👉 **{daily_challenge}**")
#     if st.button("I Accept the Challenge!"):
#         st.success("Great! Stay committed to your growth journey. 💪")

#     st.write("---")


#     # CTA Button
#     st.markdown("<h3 style='text-align: center;'>🚀 Are You Ready to Grow?</h3>", unsafe_allow_html=True)
#     if st.button("Join the MindGrowth Challenge!"):
#         st.success("You're on your way to an amazing transformation! 🎉")
#         st.image("https://miro.medium.com/v2/resize:fit:1100/format:webp/1*aFtggN7wbeBIKCN5i3kTdw.png", width=200)  # Replace with an actual banner image

if page == "🏠 Home":
    # Custom CSS for a stylish navbar
    st.markdown("""
        <style>
            .navbar {
                background-color: #4CAF50;
                padding: 10px;
                text-align: center;
                border-radius: 10px;
            }
            .navbar a {
                color: white;
                text-decoration: none;
                font-size: 18px;
                padding: 14px 20px;
                display: inline-block;
            }
            .navbar a:hover {
                background-color: #45a049;
                border-radius: 5px;
            }
            .quote {
                font-size: 22px;
                font-style: italic;
                text-align: center;
                color: #333;
                margin-top: 20px;
            }
            .quote-author {
                font-size: 18px;
                text-align: center;
                color: #555;
            }
        </style>
    """, unsafe_allow_html=True)

    # Homepage Content
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌱 Welcome to MindGrowth Village 🚀</h1>",
                unsafe_allow_html=True)

    st.write("### 🔥 Unleash Your Full Potential with a Growth Mindset!")
    st.write("At **MindGrowth Village**, we believe in continuous learning and self-improvement. Whether you’re looking for daily motivation, challenges, or success stories, you’ve come to the right place.")

    st.write("---")

    # Motivational Quotes
    quotes = [
        ("Your only limit is your mind.", "Anonymous"),
        ("Challenges are what make life interesting. Overcoming them is what makes life meaningful.", "Joshua J. Marine"),
        ("Growth and comfort do not coexist.", "Ginni Rometty"),
        ("Do not be embarrassed by your failures, learn from them and start again.",
         "Richard Branson"),
        ("Believe you can and you’re halfway there.", "Theodore Roosevelt")
    ]
    selected_quote, author = random.choice(quotes)

    st.markdown(
        f"<p class='quote'>“{selected_quote}”</p>", unsafe_allow_html=True)
    st.markdown(
        f"<p class='quote-author'>- {author}</p>", unsafe_allow_html=True)

    # Challenge of the Day
    st.subheader("💡 Challenge of the Day")
    daily_challenge = random.choice([
        "Write down 3 things you are grateful for.",
        "Try something new today, even if it scares you.",
        "Spend 30 minutes learning a new skill.",
        "Reflect on a past mistake and write what you learned from it.",
        "Say positive affirmations to yourself in the mirror for 2 minutes."
    ])

    st.write(f"👉 **{daily_challenge}**")
    if st.button("I Accept the Challenge! ✅"):
        st.success("Great! Stay committed to your growth journey. 💪")

    st.write("---")

    # Additional Growth Mindset Section
    st.subheader("🌟 Why Growth Mindset Matters?")
    st.write(
        "A growth mindset helps you embrace challenges, learn from criticism, and persist despite setbacks. "
        "It’s the key to unlocking your potential and achieving success in all areas of life. "
        "Keep pushing forward and believe in yourself! 🚀"
    )

    # CTA Button
    st.markdown("<h3 style='text-align: center;'>🚀 Are You Ready to Grow?</h3>",
                unsafe_allow_html=True)
    if st.button("Join the MindGrowth Challenge!",):
        st.success("You're on your way to an amazing transformation! 🎉")
        # Replace with an actual banner image
        st.image(
            "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*aFtggN7wbeBIKCN5i3kTdw.png", width=200)


# Upload & Process Data Page
elif page == "📂 Data Sweeper":
    st.balloons()
    # Custom CSS for a visually appealing UI
    st.markdown("""
        <style>
            .main-title {
                text-align: center;
                font-size: 32px;
                color: #4CAF50;
                font-weight: bold;
            }
            .subheader {
                text-align: center;
                font-size: 20px;
                color: #555;
                margin-bottom: 10px;
            }
            .section-title {
                font-size: 22px;
                font-weight: bold;
                color: #4CAF50;
                margin-top: 20px;
            }
            .upload-box {
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                border: 2px dashed #4CAF50;
                margin-bottom: 20px;
            }
            .file-info {
                color: #333;
                font-size: 16px;
            }
            .divider {
                border-bottom: 2px solid #ddd;
                margin: 20px 0;
            }
            .highlight {
                background-color: #ffeb3b;
                padding: 5px;
                border-radius: 5px;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title Section
    st.markdown("<h1 class='main-title'>🚀 Welcome to Data Sweeper</h1>",
                unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Transform Your Data with Ease!</p>",
                unsafe_allow_html=True)

    st.write("""
    Data Sweeper is a powerful yet simple tool that helps you **clean, analyze, and convert CSV & Excel files effortlessly.**  
    Designed as part of the **Mind Growth Village** initiative, this tool enhances your **data-handling skills** while providing a seamless experience.
    """)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # 📌 Why Use Data Sweeper?
    st.markdown("<h2 class='section-title'>💡 Why Use Data Sweeper?</h2>",
                unsafe_allow_html=True)
    st.write("""
    ✔ **Save Time** – Automate data cleaning and processing.  
    ✔ **Reduce Errors** – Ensure accurate, structured data.  
    ✔ **Easy to Use** – Just upload your file and let the magic happen.  
    ✔ **Improve Productivity** – Focus on analysis, not formatting.  
    """)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # 🛠️ How It Works?
    st.markdown("<h2 class='section-title'>📌 How It Works?</h2>",
                unsafe_allow_html=True)
    st.write("""
    1️⃣ **Upload your CSV or Excel file**  
    2️⃣ **Data Sweeper processes it instantly**  
    3️⃣ **Preview the cleaned data**  
    4️⃣ **Download the processed file** – Done! 🚀  
    """)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # 📊 Upload & Process Data Section
    st.markdown("<h2 class='main-title'>📊 Upload & Process Your Data</h2>",
                unsafe_allow_html=True)

    upload_files = st.file_uploader(" 📂 Upload your files (CSV or Excel):", type=[
                                    "csv", "xlsx"], accept_multiple_files=True)

    if upload_files:
        for file in upload_files:
            files_ext = os.path.splitext(file.name)[-1].lower()
            df = None

            if files_ext == '.csv':
                df = pd.read_csv(file)
            elif files_ext == '.xlsx':
                df = pd.read_excel(file)
            else:
                st.error(f'Unsupported file type: {files_ext}')
                continue

            # Display File Info
            st.subheader(f"📁 File: {file.name}")
            st.write(f"**File Size:** {file.size/1024:.2f} KB")
            st.write("🔍 **Data Preview:**")
            st.dataframe(df.head())

            # Data Cleaning Options
            st.subheader("🛠 Data Cleaning Options")
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("✅ Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=('number')).columns
                    df[numeric_cols] = df[numeric_cols].fillna(
                        df[numeric_cols].mean())
                    st.success("✅ Missing Values Filled!")

            # Column Selection
            st.subheader("🔄 Select Columns to Keep")
            columns = st.multiselect(
                f"Choose columns for {file.name}", df.columns, default=df.columns)
            df = df[columns]

            # Data Visualization
            st.subheader("📊 Data Visualization")
            if st.checkbox(f"Show Visualizations for {file.name}"):
                st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

            # File Conversion
            st.subheader("🔄 Convert Your File")
            conversion_type = st.radio(f"Convert {file.name} to:", [
                                       'CSV', 'Excel'], key=file.name)
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                file_name = file.name.replace(
                    files_ext, '.csv' if conversion_type == 'CSV' else '.xlsx')
                mime_type = 'text/csv' if conversion_type == 'CSV' else 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                df.to_csv(buffer, index=False)
                buffer.seek(0)

                # Download Button
                st.download_button(
                    label=f"⬇️ Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )

            st.success("🎉 All Files Processed Successfully!")

tasks = []
if page == "📝 To-Do List":
    st.title("📝 To-Do List")
    new_task = st.text_input("Add a task:")
    if st.button("Add Task") and new_task:
        tasks.append(new_task)

    if tasks:
        for i, task in enumerate(tasks):
            st.checkbox(task, key=i)

    st.write("🔜 More features coming soon! Stay tuned for updates.")

# Chat Bot
elif page == '🤖 AI Chatbot':

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    # Set up Google Gemini-Pro AI model
    gen_ai.configure(api_key=GOOGLE_API_KEY)
    model = gen_ai.GenerativeModel('gemini-pro')

    # Function to translate roles between Gemini-Pro and Streamlit terminology
    def translate_role_for_streamlit(user_role):
        if user_role == "model":
            return "assistant"
        else:
            return user_role

    # Initialize chat session in Streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # 🎨 Custom Page Styling
    st.markdown("""
        <style>
            .title {
                text-align: center;
                font-size: 34px;
                font-weight: bold;
                color: #4CAF50;
            }
            .subtitle {
                text-align: center;
                font-size: 18px;
                color: #555;
            }
            .chat-container {
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                border: 2px solid #4CAF50;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    # 🌟 Enhanced Title and Subtitle
    st.markdown("<h1 class='title'>🤖 Gemini AI - Your Smart Assistant</h1>",
                unsafe_allow_html=True)
    st.markdown("""
        <p class='subtitle'>
            Welcome to <b>Gemini AI ChatBot</b>!  
            Ask anything, explore knowledge, or get assistance with coding, writing, and more.  
            🚀 Powered by <b>Google Gemini-Pro AI</b> for intelligent conversations.  
        </p>
    """, unsafe_allow_html=True)

    # Display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input field for user's message
    user_prompt = st.chat_input("Type your question or request...")
    if user_prompt:
        # Add user's message to chat and display it
        st.chat_message("user").markdown(user_prompt)

        # Send user's message to Gemini-Pro and get the response
        gemini_response = st.session_state.chat_session.send_message(
            user_prompt)

        # Display Gemini-Pro's response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

    # 🌱 Extra Motivation Section
    st.divider()


# About Page
elif page == "ℹ️ About":
    st.title("📢 About Data Sweeper")
    st.write("Data Sweeper is part of the **Mind Growth Village** initiative, designed to empower individuals with data processing skills. With a focus on efficiency and ease, this tool simplifies data cleaning, visualization, and file conversions.")
    st.subheader("💡 Features:")
    st.write("✅ Upload multiple CSV & Excel files")
    st.write("✅ Clean data by removing duplicates & filling missing values")
    st.write("✅ Select specific columns for conversion")
    st.write("✅ Visualize data with built-in charts")
    st.write("✅ Convert files between CSV & Excel formats")

    st.title("📢 About AI Chatbot")
    st.write("The AI Chatbot, powered by **Google Gemini-Pro AI**, is designed to assist you with intelligent conversations. Whether you need help with coding, writing, or general inquiries, the chatbot is here to provide accurate and helpful responses.")
    st.subheader("💡 Features:")
    st.write("✅ Intelligent conversations powered by Google Gemini-Pro AI")
    st.write("✅ Assistance with coding, writing, and general inquiries")
    st.write("✅ Easy-to-use chat interface")

    st.title("📢 About To-Do List")
    st.write("The To-Do List feature helps you keep track of your tasks and stay organized. Easily add, view, and manage your tasks to ensure you stay productive.")
    st.subheader("💡 Features:")
    st.write("✅ Add new tasks")
    st.write("✅ View and manage existing tasks")
    st.write("✅ Simple and intuitive interface")

    st.write("🔜 More features coming soon! Stay tuned for updates.")
    st.write(
        "\nDeveloped with ❤️ by Kulsoom Adnan for the Mind Growth Village community!")
