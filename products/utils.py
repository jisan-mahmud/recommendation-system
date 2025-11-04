from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from products.models import Product

def get_similar_products(product_id, top_n=10):
    products = list(Product.objects.all())
    descriptions = [p.description for p in products]

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    target_product = Product.objects.get(id=product_id)
    
    target_index = next(i for i, p in enumerate(products) if p.id == target_product.id)
    
    cosine_sim = cosine_similarity(tfidf_matrix[target_index], tfidf_matrix).flatten()

    similar_indices = cosine_sim.argsort()[::-1] 
    similar_indices = [i for i in similar_indices if i != target_index][:top_n]

    similar_products = [products[i] for i in similar_indices]
    

    return similar_products
