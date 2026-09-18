import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

import streamlit as st

from app.llm_service import generate_sql
from app.query_engine import execute_query

from app.anomaly_detector import (
    get_unresolved_high_priority,
    get_resolution_time_anomalies,
    get_low_rated_tickets
)

st.set_page_config(
    page_title="AI Ticket Assistant",
    page_icon="🎫",
    layout="wide"
)

st.title("🎫 AI-Powered Support Ticket Assistant")
st.markdown(
    "Ask questions about support tickets and detect anomalies using AI."
)

tab1, tab2 = st.tabs(
    ["🤖 AI Query Assistant", "🚨 Anomaly Detection"]
)

# ==================================================
# TAB 1
# ==================================================

with tab1:

    st.subheader("Ask Questions in Natural Language")

    question = st.text_input(
        "Example: How many open tickets are there?"
    )

    if st.button("Generate Answer"):

        if question:

            sql = generate_sql(question)

            result = execute_query(sql)

            st.success("Query Executed Successfully")

            st.subheader("Generated SQL")

            st.code(sql, language="sql")

            st.subheader("Result")

            st.dataframe(result, use_container_width=True)

# ==================================================
# TAB 2
# ==================================================

with tab2:

    unresolved = get_unresolved_high_priority()

    resolution = get_resolution_time_anomalies()

    low_rated = get_low_rated_tickets()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Unresolved High/Critical",
            len(unresolved)
        )

    with col2:
        st.metric(
            "Resolution Anomalies",
            len(resolution)
        )

    with col3:
        st.metric(
            "Low Rated Tickets",
            len(low_rated)
        )

    st.divider()

    st.subheader("Unresolved High Priority Tickets")

    st.dataframe(
        unresolved.head(10),
        use_container_width=True
    )

    st.subheader("Resolution Time Anomalies")

    st.dataframe(
        resolution.head(10),
        use_container_width=True
    )

    st.subheader("Low Rated Tickets")

    st.dataframe(
        low_rated.head(10),
        use_container_width=True
    )