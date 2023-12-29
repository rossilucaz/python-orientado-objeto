class Programa:
    
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0 

    @property   
    def likes(self):
        return self._likes
    
    
    def dar_like(self):
        self._likes += 1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title() 
        
    def __str__(self):
        return f'Nome: {self.nome}\nAno: {self.ano}\nLikes: {self.likes}'

class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
              
            
    def __str__(self):
         return f'\nNome: {self.nome}\nAno: {self.ano}\nDuração: {self.duracao}\nLikes: {self.likes}'
        
        
class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
                
    def __str__(self):
         return f'\nNome: {self.nome}\nAno: {self.ano}\nTemporadas: {self.temporadas}\nLikes: {self.likes}'
     
class Playlist:
    
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas
        
    
    def __getitem__(self, item):
        return self.programas[item]
        
    @property
    def listagem(self):
        return self.programas
    
    
    def __len__(self):
        return len(self.programas)
        
        


