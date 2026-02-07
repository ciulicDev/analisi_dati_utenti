import json

with open('utenti.json') as f:
    utenti=json.load(f)

attivi =[u for u in utenti if u['attivo']]
totale_attivi=len(attivi)
media_eta=sum(u['eta'] for u in attivi)/totale_attivi

with open('report.txt','w') as f:
    f.write(f'Totale utenti attivi: {totale_attivi}\n')
    f.write(f'Media età utenti attivi: {media_eta:.1f}\n\n')
    f.write(f'lista utenti attivi:\n')
    for u in attivi:
        f.write(f'-{u['nome']},{u['eta']} anni\n')

print(f"Report generato! Totale utenti attivi: {totale_attivi}")