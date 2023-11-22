from database import _execute

class Product:

    def __init__(self, name, price, id = None):
        self.id = id
        self.name = name
        self.price = price
        self.status = 1 # Ativo = 1 / Inativo = 0

        # Se a tabela de produtos não existir, cria ela
        query = "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, status NUMERIC)"
        _execute(query)
    
    # Método para salvar todos os produtos
    def save(self):
        query = f"INSERT INTO products (name, price, status) VALUES ('{self.name}', {float(self.price)}, {self.status})"
        
        # Executa a query
        _execute(query)
    
    # Método para atualizar o status de um produto
    def update(self):
        query = "UPDATE products SET status = ? WHERE id = ?"
        _execute(query, (self.status, self.id,))

    # Método para deletar um objeto(produto)
    def delete(self):
        query = "DELETE FROM products WHERE id = ?"
        _execute(query, (self.id,))
    
    # Método estático para dar um get all nos produtos
    @staticmethod
    def get_products():
        query = "SELECT * FROM products"
        products = _execute(query)

        return products

    # Método estático para dar um get em um produto específico
    @staticmethod
    def get_product_by_id(id):
        query = f"SELECT id, name, price FROM products WHERE id={int(id)}"
        product = _execute(query)[0]

        # Criando um objeto do tipo produto
        product = Product(id=product[0], name=product[1], price=product[2])

        # Retorna o objeto com os dados do produto
        return product