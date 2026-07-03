import requests
from django.conf import settings

class TMDBService:
    BASE_URL = "https://api.themoviedb.org/3"
    
    @classmethod
    def _get_headers(cls):
        return {
            "Authorization": f"Bearer {settings.TMDB_API_KEY}",
            "accept": "application/json"
        }

    @classmethod
    def search_movies(cls, query: str, language: str = "pt-BR"):
        """Busca filmes pelo título no TMDB"""
        url = f"{cls.BASE_URL}/search/movie"
        params = {
            "query": query,
            "language": language,
            "include_adult": "false"
        }
        
        try:
            response = requests.get(url, headers=cls._get_headers(), params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return {"results": [], "error": "Erro ao conectar com o TMDB"}