from flask_openapi3 import Tag

# Tags para organizar a documentação
customer_tag = Tag(name="Customer", description="Operações relacionadas a clientes")
zipcode_tag = Tag(name="ZipCode", description="Operações para busca de CEP")

