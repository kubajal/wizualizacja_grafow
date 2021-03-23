from wizualizacje import *

def rysuj_graf(graf = {}):

  # zmiana slownika na NetworkX
  G = nx.DiGraph()
  wezly_zrodla = set(graf.keys())
  wezly_cele = set([w for lista in list(graf.values()) for w in lista]) # flattening
  if(not set.issubset(wezly_cele, wezly_zrodla)):
    raise Exception("Błąd. Węzły docelowe nie są podzbiorem wszystkich węzłów.")
  for zrodlo in wezly_zrodla:
    G.add_node(zrodlo)
  for zrodlo in wezly_zrodla:
    for cel in graf[zrodlo]:
      G.add_edge(zrodlo, cel)

  # uklad grafu & rysowanie
  pos = nx.spectral_layout(G)
  nx.draw_networkx(G, pos)
  plt.show()
  return G
