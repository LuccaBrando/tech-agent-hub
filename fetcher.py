import feedparser

RSS_FEEDS = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "Ars Technica": "https://feeds.arstechnica.com/arstechnica/index",
    "Wired": "https://www.wired.com/feed/rss"
}

def fetch_tech_news(limit_per_source=4):
    """
    Coleta as notícias mais recentes de múltiplos portais de tecnologia americanos.
    """
    news_list = []
    
    # Loop que passa por cada portal
    for source_name, url in RSS_FEEDS.items():
        print(f"Coletando dados de: {source_name}...")
        feed = feedparser.parse(url)
        
        if not feed.entries:
            print(f"  [!] Nenhuma notícia encontrada ou falha ao acessar o feed da {source_name}.")
            continue
            
        # Pega as últimas notícias
        for entry in feed.entries[:limit_per_source]:
            news_data = {
                "source": source_name,
                "title": entry.title,
                "link": entry.link,
                "published": entry.get("published", "Data não disponível"),
                "summary": entry.summary if 'summary' in entry else "Sem sumário disponível."
            }
            news_list.append(news_data)
            
    return news_list

if __name__ == "__main__":
    top_news = fetch_tech_news(limit_per_source=4)
    
    print(f"\n--- Coletadas {len(top_news)} notícias no total ---\n")
    for idx, news in enumerate(top_news, 1):
        print(f"[{idx}] [{news['source']}] {news['title']}")
        print(f"Link: {news['link']}")
        print("-" * 40)