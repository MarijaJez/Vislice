% rebase('base.tpl', title="Vislice")

Geslo: {{geslo}}</br>
Nepravilni ugibi: {{nepravilni}}</br>
<img src="/img/{{obesenost}}.jpg" alt="obesanje">
% if stanje != model.ZMAGA and stanje != model.PORAZ:
<form action="" method="post">
    <input name="crka" autofocus> <input type="submit" value="Ugibaj">
</form>
% elif stanje == model.ZMAGA:
Bravo, zmagali ste! Ali bi radi igrali še enkrat?
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
% elif stanje == model.PORAZ:
O, ne, obešeni ste. Pravilno geslo je bilo {{celo_geslo}}.
 Ali želite igrati še enkrat?
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
% end
