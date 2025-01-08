from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Produto

def listar_produtos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all().values('id', 'nome', 'descricao', 'preco', 'quantidade_em_estoque')
        return JsonResponse(list(produtos), safe=False)
    
@csrf_exempt
def criar_produto(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        try:
            produto = Produto.objects.create(
                nome=dados['nome'],
                descricao=dados['descricao'],
                preco=dados['preco'],
                quantidade_em_estoque=dados['quantidade_em_estoque']
            )
            return JsonResponse({'message': 'Produto criado!', 'id': produto.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def editar_produto(request, id):
    if request.method == 'PUT':
        try:
            produto = Produto.objects.get(id=id)
            dados = json.loads(request.body)
            produto.nome = dados.get('nome', produto.nome)
            produto.descricao = dados.get('descricao', produto.descricao)
            produto.preco = dados.get('preco', produto.preco)
            produto.quantidade_em_estoque = dados.get('quantidade_em_estoque', produto.quantidade_em_estoque)
            produto.save()
            return JsonResponse({'message': 'Produto atualizado!'})
        except Produto.DoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
@csrf_exempt
def deletar_produto(request, id):
    if request.method == 'DELETE':
        try:
            produto = Produto.objects.get(id=id)
            produto.delete()
            return JsonResponse({'message': 'Produto deletado!'})
        except Produto.DoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)