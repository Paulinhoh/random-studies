from rich import print
from rich.table import Table

tabela = Table(title='Exemplo', show_footer=True, show_header=True, header_style='bold')

tabela.add_column('Nome', justify='right', style='red')
tabela.add_column('Preço', justify='center', style='blue')

tabela.add_row('Lapis', 'R$1,50')
tabela.add_row('Borracha', '[green]R$5,00[/]')

print(tabela)
