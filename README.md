# 🎫 AI-Powered Support Ticket Assistant

An AI-powered analytics system that enables users to query support ticket data using natural language and automatically detect operational anomalies.

The application uses a Large Language Model (LLM) to convert user questions into SQL queries, executes them on a SQLite database, and presents the results through an interactive Streamlit dashboard.

---

## 🚀 Features

### 🤖 Natural Language to SQL

Ask questions in plain English such as:

- How many open tickets are there?
- How many critical tickets are there?
- Which agent has the lowest average customer rating?
- What is the average customer rating for Technical tickets?
- How many unresolved tickets are there?

The system automatically:

1. Converts the question into SQL using a Groq-hosted LLM.
2. Executes the SQL query on a SQLite database.
3. Displays the generated SQL and query results.

---

### 🚨 Anomaly Detection

The application identifies key operational issues:

#### Unresolved High/Critical Tickets
Tickets where:
- Priority = High or Critical
- Status ≠ Resolved

#### Resolution Time Anomalies
Tickets with unusually high resolution times.

#### Low Rated Tickets
Tickets with customer ratings ≤ 2.

---

### 📊 Interactive Dashboard

Built using Streamlit:

- AI Query Assistant
- SQL Visualization
- Query Results Table
- Anomaly Detection Dashboard

---

# 📸 Application Screenshots

## Dashboard

The main dashboard provides access to both AI Query Assistant and Anomaly Detection modules.

![alt text](dashboard.png)

---

## Natural Language Query Example

Users can ask questions in plain English and the system automatically generates SQL.

**Question:** How many open tickets are there?

![alt text](open-tickets.png)

**Result:** 111 Open Tickets

---

## Agent Performance Analysis

Identify agents with lower customer satisfaction ratings.

**Question:** Which agent has the lowest average customer rating?

!![alt text](critical-tickets.png)

**Result:** AGT-08 → Average Rating: 3.48

---

## Anomaly Detection Dashboard

The system automatically highlights operational anomalies and ticket risks.

![alt text](agent-rating.png)

![alt text](technical-rating.png)

![alt text](anomaly-detection.png)

**Summary Results:**

| Anomaly Type | Count |
|-------------|--------|
| Unresolved High/Critical Tickets | 80 |
| Resolution Time Anomalies | 17 |
| Low Rated Tickets | 47 |

---

# 🏗️ Architecture

```text
User Question
      │
      ▼
Groq LLM
(Natural Language → SQL)
      │
      ▼
Generated SQL
      │
      ▼
SQLite Database
      │
      ▼
Query Results
      │
      ▼
Streamlit Dashboard
```

---

# 📂 Project Structure

```text
ai-ticket-assistant/
│
├── app/
│   ├── __init__.py
│   ├── anomaly_detector.py
│   ├── data_loader.py
│   ├── database.py
│   ├── llm_service.py
│   ├── main.py
│   └── query_engine.py
│
├── data/
│   └── support_tickets.csv
│
├── notebooks/
│   └── explore_data.py
│
├── tests/
│   ├── test_anomaly_detector.py
│   ├── test_groq.py
│   ├── test_query_engine.py
│   └── test_sql_generation.py
│
├── ui/
│   └── streamlit_app.py
│
├── screenshots/
│   ├── dashboard.png
│   ├── open-tickets.png
│   ├── agent-rating.png
│   └── anomaly-detection.png
│
├── tickets.db
├── requirements.txt
├── .env
└── README.md
```

---

# 🛠️ Technologies Used

### Programming Language
- Python

### Database
- SQLite

### Data Processing
- Pandas

### AI / LLM
- Groq API
- GPT-OSS-20B

### Frontend
- Streamlit

### Environment Management
- Python Virtual Environment
- python-dotenv

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-ticket-assistant.git
cd ai-ticket-assistant
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Running the Application

Launch the Streamlit dashboard:

```bash
streamlit run ui/streamlit_app.py
```

Open:

```text
http://localhost:8501
```

---

# 🧪 Sample Queries

### Open Tickets

```sql
SELECT COUNT(*)
FROM tickets
WHERE status='Open';
```

Result:

```text
111
```

---

### Critical Tickets

```sql
SELECT COUNT(*)
FROM tickets
WHERE priority='Critical';
```

Result:

```text
55
```

---

### Lowest Rated Agent

```sql
SELECT agent_id,
AVG(customer_rating) AS avg_rating
FROM tickets
GROUP BY agent_id
ORDER BY avg_rating ASC
LIMIT 1;
```

Result:

```text
AGT-08 → 3.48
```

---

### Technical Ticket Rating

```sql
SELECT AVG(customer_rating)
FROM tickets
WHERE category='Technical';
```

Result:

```text
3.74
```

---

### Unresolved Tickets

```sql
SELECT COUNT(*)
FROM tickets
WHERE status <> 'Resolved';
```

Result:

```text
173
```

---

# 🚨 Anomaly Detection Results

| Anomaly Type | Count |
|-------------|--------|
| Unresolved High/Critical Tickets | 80 |
| Resolution Time Anomalies | 17 |
| Low Rated Tickets | 47 |

---

# 🔮 Future Enhancements

- Query History
- Download Results as CSV
- Interactive Visualizations
- Agent Performance Dashboard
- Multi-table Support
- User Authentication
- RAG-based Ticket Search
- Advanced Analytics

---

# 👨‍💻 Author

**Balaji Rithesh G**

AI Engineer | Generative AI 

GitHub: https://github.com/your-github-username

LinkedIn: https://www.linkedin.com/in/your-linkedin-profile

---

# 📄 License

This project is intended for educational, learning, and portfolio purposes.
