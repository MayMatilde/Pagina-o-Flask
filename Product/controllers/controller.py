from flask import Blueprint, render_template, request #manteve-se
from models.model import produtos

#manteve-se
arraso = Blueprint('arraso', __name__, template_folder='templates')
#diferente
@arraso.route('/') #uma rota normal 
def page1(): #uma função normal
    page = request.args.get('page', 1, type=int) #está lidando com a lista
    per_page = 3 #por 3 páginas
    star= (page -1) * per_page
    end = star + per_page
    total_pages = (len(produtos) + per_page - 1) //per_page
    produtos_on_page = produtos[star:end]
    return render_template(template_name_or_list='page1.html', produtos_on_page=produtos_on_page, total_pages=total_pages, page=page)
 

  

