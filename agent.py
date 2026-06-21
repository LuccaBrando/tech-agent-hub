import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from fetcher import fetch_tech_news


load_dotenv()

def generate_linkedin_posts():
    # Coleta as notícias mais recentes do fetcher
    print("Buscando notícias...")
    news_data = fetch_tech_news()
    
    if not news_data:
        print("Sem dados para processar.")
        return
    
    # Formata as notícias em uma única string
    formatted_context = ""
    for idx, item in enumerate(news_data, 1):
        formatted_context += f"--- News #{idx} ---\n"
        formatted_context += f"Title: {item['title']}\n"
        formatted_context += f"Summary: {item['summary']}\n\n"

    
    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are an expert AI Research Engineer, jornalist and Venture Capital Tech Analyst writing for a sophisticated US tech audience on LinkedIn.\n\n"
            "Your task is to review the latest tech news provided and output a highly structured, analytical breakdown in TWO parts:\n\n"
            
            "--- PART 1: [LINKEDIN POST - ENGLISH] ---\n"
            "Structure the post exactly like this:\n"
            "1. THE HEADLINES: Cite the core breaking news from the list with brief, punchy engineering/business context.\n (10 lines minimun)"
            "2. MARKET OUTLOOK & IMPACT: Provide a deep technical and macroeconomic conclusion. How does this shift the market? Why does it matter to developers/investors?\n"
            "3. NEXT STEPS: What should tech leaders or engineers do next? What are the upcoming trends to watch based on this?\n"
            "4. HASHTAGS: Include high-intent tech/AI hashtags.\n\n"
            
            "--- PART 2: [LINKEDIN POST - PORTUGUESE] ---\n"
            "Rewrite and localize the entire breakdown above for the Brazilian tech ecosystem. "
            "Maintain the same analytical depth, structure (Notícias, Conclusão de Mercado, Próximos Passos), "
            "but adapt the tone to be natural, engaging, and culturally relevant for Brazilian professionals.\n\n"
            "Do not use robotic, literal translations."
        )),
        ("user", "Here are the latest tech updates:\n\n{context}")
    ])

    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

    
    chain = prompt | llm

    print("IA processando e gerando os posts personalizados...")
    response = chain.invoke({"context": formatted_context})
    
   
    print("\n================ RESULTADO DO AGENTE ================\n")
    print(response.content)

if __name__ == "__main__":
    
    if not os.getenv("GROQ_API_KEY"):
        print("Adicione sua GROQ_API_KEY no arquivo .env antes de rodar.")
    else:
        generate_linkedin_posts()