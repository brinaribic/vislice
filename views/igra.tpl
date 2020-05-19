% import model

<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>
  
  <h2> {{ igra.pravilni_del_gesla() }} </h2>

  Nepravilni ugibi: <b> {{ igra.nepravilni_ugibi() }} </b>

  Stopnja obešenosti: <b> {{ igra.stevilo_napak() }} </b>

  % if stanje == model.ZMAGA:

  <h3> čestitam. uspelo ti je. </h3>

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
  
  % if stanje == model.PORAZ:

  <h3> Ni ti usepelo. </h3>

  Pravilno geslo je bilo: <b> {{ igra.geslo }} </b>

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % else:

  <form action="/igra/{{id_igre}}/" method="post">
    Črka: <input type="text" name ="crka">
    <button type="submit">Ugibaj</button>
  </form>

  % end

</body>

</html>