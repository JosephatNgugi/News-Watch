class News:
    """
    News class to define News Article objects
    """
    
    def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt, content):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        
class Sources:
    def __init__(self,id,name,description,url,category,country,language):
        '''
        Sources Class to define News Sources objects
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language
