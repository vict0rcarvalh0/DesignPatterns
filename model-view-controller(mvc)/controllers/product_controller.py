from tornado.web import RequestHandler
from models.product_model import Product

# Classe para renderizar a página inicial
class Index(RequestHandler):

    # Método para apresentar os produtos cadastrados no model em uma view
    def get(self):
        products = Product.get_products()
        self.render("index.html", products=products)

# Classe para renderizar a página de cadastro de produtos
class New(RequestHandler):

    # Método para apresentar o formulário de cadastro de produtos
    def get(self):
        self.render('new.html')

    # Método para receber os dados do formulário e salvar no model
    def post(self):
        name = self.get_argument('name', None)
        price = self.get_argument('price', None)

        product = Product(name=name, price=price)
        product.save()

        self.redirect('/')

# Classe para renderizar a página de edição de produtos
class Update(RequestHandler):

    # Método para apresentar o formulário de edição de produtos
    def get(self, id, status):
        product = Product.get_product_by_id(id)
        product.status = status
        product.update()

        self.redirect('/')

# Classe para renderizar a página de exclusão de produtos
class Delete(RequestHandler):

    # Método para apresentar o formulário de exclusão de produtos
    def get(self, id):
        product = Product.get_product_by_id(id)
        product.delete()

        self.redirect('/')