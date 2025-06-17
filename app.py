## Testing streamlit live deployment

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Streamlit Feature Showcase",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("✨ Streamlit Feature Showcase")
st.write("This application demonstrates a wide range of Streamlit's core features for building interactive web apps.")

# --- Sidebar Elements ---
st.sidebar.header("Navigation & Controls")

# Radio buttons for page selection
page = st.sidebar.radio(
    "Choose a Section:",
    ["Text & Media", "Input Widgets", "Data Display & Charts", "Layout & Status", "Session State & Caching"]
)

st.sidebar.info("Explore different sections to see Streamlit's capabilities!")

# --- Section 1: Text & Media ---
if page == "Text & Media":
    st.header("1. Text & Media Elements")
    st.subheader("Displaying various types of text and media.")

    st.write("This is a simple text output using `st.write()`.")
    st.markdown("---") # Horizontal line

    st.markdown("""
    ### Markdown Support
    You can use **Markdown** to format text.
    - **Bold Text**
    - *Italic Text*
    - `Code snippets`
    - Links: [Streamlit Docs](https://docs.streamlit.io/)
    """)

    st.code("""
import streamlit as st
st.write("Hello, Streamlit!")
    """, language="python")

    st.latex(r"""
    E=mc^2
    """)

    st.caption("This is a small caption for some extra information.")

    st.subheader("Images, Audio, and Video")
    st.image("https://www.streamlit.io/images/brand/streamlit-logo-light.svg", caption="Streamlit Logo", width=200)

    # Example of an audio file (replace with a real path if you have one)
    # st.audio("audio_file.mp3", format="audio/mp3")

    # Example of a video file (replace with a real path if you have one)
    # st.video("video_file.mp4")

# --- Section 2: Input Widgets ---
elif page == "Input Widgets":
    st.header("2. Input Widgets")
    st.subheader("Collecting user input with interactive widgets.")

    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}!")

    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=30)
    st.write(f"You are {age} years old.")

    options = ["Option A", "Option B", "Option C"]
    selected_option = st.selectbox("Select an option:", options)
    st.write(f"You selected: {selected_option}")

    multi_options = ["Apple", "Banana", "Cherry", "Date"]
    selected_fruits = st.multiselect("Select your favorite fruits:", multi_options, default=["Apple", "Cherry"])
    st.write("Your favorite fruits are:", ", ".join(selected_fruits))

    agree = st.checkbox("I agree to the terms and conditions.")
    if agree:
        st.success("You agreed!")
    else:
        st.warning("Please agree to proceed.")

    gender = st.radio("Select your gender:", ["Male", "Female", "Other"])
    st.write(f"You identified as: {gender}")

    slider_value = st.slider("Select a value on the slider:", 0, 100, 50)
    st.write(f"Slider value: {slider_value}")

    button_clicked = st.button("Click Me!")
    if button_clicked:
        st.write("Button was clicked!")

    file_uploader = st.file_uploader("Upload a file:", type=["csv", "txt", "png"])
    if file_uploader is not None:
        st.write("File uploaded successfully!")
        st.write(f"File name: {file_uploader.name}")
        st.write(f"File type: {file_uploader.type}")

    date_input = st.date_input("Select a date:")
    st.write(f"Selected date: {date_input}")

    time_input = st.time_input("Select a time:")
    st.write(f"Selected time: {time_input}")

# --- Section 3: Data Display & Charts ---
elif page == "Data Display & Charts":
    st.header("3. Data Display & Charts")
    st.subheader("Visualizing data with tables and various chart types.")

    st.write("### Pandas DataFrame")
    data = {'Col1': np.random.rand(10),
            'Col2': np.random.randint(1, 100, 10),
            'Col3': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']}
    df = pd.DataFrame(data)
    st.dataframe(df) # Interactive dataframe

    st.write("### Static Table")
    st.table(df.head()) # Static table display

    st.write("### Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "25 °C", "1 °C")
    col2.metric("Humidity", "60%", "-2%")
    col3.metric("Wind Speed", "15 km/h", "5%")

    st.write("### Charts")

    st.subheader("Line Chart")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)

    st.subheader("Area Chart")
    st.area_chart(chart_data)

    st.subheader("Bar Chart")
    st.bar_chart(chart_data)

    st.subheader("Matplotlib/Seaborn Chart")
    # Generate some random data for a histogram
    np.random.seed(42)
    data_hist = np.random.normal(0, 1, 1000)

    fig, ax = plt.subplots()
    sns.histplot(data_hist, kde=True, ax=ax)
    ax.set_title("Distribution of Random Data")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    st.subheader("Map Chart")
    # Some random data for a map
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [28.6, 77.2], # Centered around Delhi for illustration
        columns=['lat', 'lon']
    )
    st.map(map_data)

# --- Section 4: Layout & Status ---
elif page == "Layout & Status":
    st.header("4. Layout & Status Elements")
    st.subheader("Organizing your app and showing real-time feedback.")

    st.write("### Columns Layout")
    col1, col2 = st.columns(2)
    with col1:
        st.write("This is in the first column.")
        st.button("Column 1 Button")
    with col2:
        st.write("This is in the second column.")
        st.checkbox("Column 2 Checkbox")

    st.write("---")

    st.write("### Expander")
    with st.expander("Click to see more information"):
        st.write("This content is hidden by default and expands when clicked.")
        st.info("You can put any Streamlit element inside an expander.")

    st.write("---")

    st.write("### Tabs")
    tab1, tab2, tab3 = st.tabs(["Tab A", "Tab B", "Tab C"])
    with tab1:
        st.header("Content for Tab A")
        st.write("This is the content of the first tab.")
    with tab2:
        st.header("Content for Tab B")
        st.write("This is the content of the second tab. Different content!")
    with tab3:
        st.header("Content for Tab C")
        st.success("You found the hidden success message!")

    st.write("---")

    st.write("### Status Messages & Progress")
    st.success("This is a success message!")
    st.info("This is an informational message.")
    st.warning("This is a warning message.")
    st.error("This is an error message!")
    st.exception(ZeroDivisionError("Division by zero!")) # Display an exception

    st.write("### Progress Bar")
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    my_bar.empty() # Remove the progress bar after completion
    st.success("Operation complete!")

    st.write("### Spinner")
    with st.spinner('Waiting for data to load...'):
        time.sleep(2)
    st.success('Data loaded!')

# --- Section 5: Session State & Caching ---
elif page == "Session State & Caching":
    st.header("5. Session State & Caching")
    st.subheader("Managing application state and optimizing performance.")

    st.write("### Session State")
    st.info("Session State allows you to preserve variable values across reruns.")

    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    st.write(f"Current counter value: {st.session_state.counter}")

    if st.button("Increment Counter"):
        st.session_state.counter += 1
        st.experimental_rerun() # Rerun the app to update the display immediately

    st.write("---")

    st.write("### Caching (`st.cache_data` and `st.cache_resource`)")
    st.info("Caching prevents Streamlit from re-running expensive computations on every rerun if inputs haven't changed.")

    # st.cache_data for data transformations and functions returning data
    @st.cache_data
    def load_heavy_data():
        st.write("Loading heavy data (this runs only once or when inputs change)...")
        time.sleep(3) # Simulate a heavy computation
        data = pd.DataFrame({
            'col1': np.random.randn(1000),
            'col2': np.random.randint(0, 100, 1000)
        })
        return data

    cached_df = load_heavy_data()
    st.write("Heavy data loaded and cached:")
    st.dataframe(cached_df.head())

    # st.cache_resource for objects that should be shared across all users (e.g., ML models, database connections)
    @st.cache_resource
    def load_ml_model():
        st.write("Loading ML model (this runs only once across all sessions)...")
        time.sleep(2)
        # In a real scenario, this would load a pre-trained model
        class SimpleModel:
            def predict(self, x):
                return x * 2
        return SimpleModel()

    model = load_ml_model()
    st.write(f"Model prediction for 5: {model.predict(5)}")

    st.write("Try interacting with other widgets. The cached functions won't re-run unless their inputs change!")

st.sidebar.markdown("---")
st.sidebar.markdown("Built with ❤️ by Streamlit Enthusiast")