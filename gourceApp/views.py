from django.shortcuts import render, redirect
from . forms import *
from django.conf import settings
from . models import Arvore
from . models import Gource
import os

# Arrumar home para setar hierarquia da árvore:
def index(request):
    if request.method == 'POST':
        form = HierarquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gourceApp/cadastroDados.html')
    else:
        form = HierarquiaForm(request.POST)
        context = {
            'form' : form
        }
        return render( request, 'gourceApp/index.html', context)

# Cadastro de dados para a árvore
def cadastroDados(request):

    form = DadosForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
#        form = DadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_dados')
    else:
#        form = DadosForm()
        #context = {
        #    'form' : form
        #}
        return render(request, 'gourceApp/cadastroDados.html', {'form':form})

# Configurações do Gource
def cadastroGource(request):

    form = DadosGource(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cadastro_gource')
    else:
       form = DadosGource()
       context = {
           'form' : form
       }
       return render(request, 'gourceApp/cadastroGource.html', context)


# Processamento dos dados do banco e geração do vídeo
def showvideo(request):
    dados = Arvore.objects.values('nome', 'escola', 'serie', 'cidade')
    gourceconf = Gource.objects.values('titulo', 'cor', 'fonte', 'elasticidade')

    list_result = [entry for entry in dados]  # converts ValuesQuerySet into Python list
    list_result2 = [entry for entry in gourceconf]

    contents = eval(str(list_result))
    contentsconf = eval(str(list_result2))

    f = open("media/tabela_temp", "w")
    for i in range(0,len(contents)):
        f.write(contents[i]['nome'] + "," + contents[i]['escola'] + "," + contents[i]['cidade'] + "," + contents[i]['serie'])
        f.write("\n")
    f.close()

    #executa o script para criar log do gource
    os.system("media/geralog.sh")

    #executa o programa
    cor = contentsconf[len(contentsconf) -1 ]['cor']
    os.system('gource -1280x720 --hide date -o media/gource.ppm -i 0 --title "' + contentsconf[len(contentsconf) -1 ]['titulo'] + ' " --font-size '+ str(contentsconf[len(contentsconf) -1 ]['fonte']) +' -b ' + cor[1:] + ' -e '+str(contentsconf[len(contentsconf) -1]['elasticidade'])+' --max-user-speed 500 -a 1 --highlight-users media/tabela --date-format "%d.%m.%Y" --bloom-multiplier 0.5 --bloom-intensity 0.5 -s 4')
    os.system('ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i media/gource.ppm -vcodec libx264 -preset ultrafast -crf 1 -threads 0 -bf 0 media/gource.mp4')

    return render(request, 'gourceApp/videoGerado.html', {'media': settings.MEDIA_ROOT})
