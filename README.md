# 🌱 Sustainability Sentiment Analysis

## 📌 Project Overview
This project analyzes sentiment trends in Reddit discussions related to **sustainability**. By scraping posts from relevant subreddits, the project categorizes sentiment as **Positive, Neutral, or Negative** using **Natural Language Processing (NLP)** techniques.

## 🔍 Features
- **Scrape Reddit posts** from sustainability-related subreddits
- **Sentiment classification** using VADER (optimized for social media text)
- **Trend analysis** to track sentiment changes over time
- **Keyword analysis** with word clouds to identify key discussion themes
- **Engagement analysis** (measuring sentiment vs. post upvotes)
- **Data visualization** (bar charts, pie charts, sentiment over time graphs)

## 📂 Project Structure
```
📦 sustainability-sentiment-analysis
├── .gitignore            
├── .env                  
├── main.py               
├── sentiment_analysis.py   
├── requirements.txt       
├── README.md             
└── reddit_posts.csv     
```

## 🚀 Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/rvznr/sustainability-sentiment-analysis.git
cd sustainability-sentiment-analysis
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Set Up Reddit API Credentials**
1. Create a `.env` file in the project directory:
   ```bash
   touch .env
   ```
2. Add your **Reddit API credentials**:
   ```
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USER_AGENT=your_user_agent
   ```

### 4️⃣ **Run the Scraper**
```bash
python main.py
```
- Enter the subreddit name (e.g., `sustainability`)
- Optionally enter a keyword filter
- Specify the number of posts to scrape

### 5️⃣ **Run Sentiment Analysis**
```bash
python sentiment_analysis.py
```
- Generates **bar chart**, **pie chart**, **trend graphs**, and **word clouds**.

## 📊 Example Outputs
### **Sentiment Distribution**
![Sentiment Distribution](path/to/sentiment_distribution.png)

### **Sentiment Trends Over Time**
![Sentiment Trends](path/to/sentiment_trends.png)

### **Word Cloud (Positive Sentiment)**
![Positive Word Cloud](path/to/positive_wordcloud.png)

### **Word Cloud (Negative Sentiment)**
![Negative Word Cloud](path/to/negative_wordcloud.png)

### **Upvotes vs. Sentiment**
![Upvotes by Sentiment](path/to/upvotes_sentiment.png)

## 📈 Key Findings
- **Neutral sentiment dominates (54.4%)**, indicating discussions are largely informative.
- **Positive sentiment (33.3%)** is higher than negative (12.4%), reflecting optimism.
- **Common positive topics**: renewable energy, solar power, sustainability projects.
- **Common negative topics**: waste, greenwashing, climate policies.
- **Highly upvoted posts tend to be neutral**, suggesting informative content is valued.

## 🌟 Future Improvements
- **Expand to more subreddits** (`r/climatechange`, `r/environment`, etc.)
- **Use machine learning models** (e.g., BERT) for advanced sentiment classification.
- **Analyze top-upvoted posts** for deeper insights into viral sustainability discussions.
- **Automate trend reporting** with scheduled data collection.

## 👥 Contributors
- **@rvznr** (Project Creator)

## 📜 License
This project is open-source and available under the **MIT License**.

---
🚀 **Feel free to contribute or provide feedback!** Happy coding! 🌱
