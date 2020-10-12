qntQuadros = 4
listaprocessamento = [ 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

faltaPagina = 0
q= []

for i in listaprocessamento:
    if i not in q:
        if(len(q) == qntQuadros): 
            q.remove(q[0]) 
            q.append(i)
        else: 
            q.append(i) 
  
        faltaPagina +=1
    else: 
          
        q.remove(i) 
  
        q.append(i) 
        
print("Quantidade de Faltas de pagina: ""{}".format(faltaPagina)) 