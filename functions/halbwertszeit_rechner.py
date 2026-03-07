import math
def verbleibende_menge(N0, T_half, t):
   """
   Berechnet die verbleibende Menge eines radioaktiven Stoffes nach der Zeit t.
   Parameter:
   N0 : float : Anfangsmenge
   T_half : float : Halbwertszeit
   t : float : verstrichene Zeit
   Rückgabe:
   float : verbleibende Menge
   """
   return N0 * (0.5) ** (t / T_half)

def berechne_halbwertszeit(N0, N, t):
   """
   Berechnet die Halbwertszeit basierend auf Anfangs- und Endmenge und verstrichener Zeit.
   Parameter:
   N0 : float : Anfangsmenge
   N : float : Endmenge nach Zeit t
   t : float : verstrichene Zeit
   Rückgabe:
   float : Halbwertszeit
   """
   if N <= 0 or N >= N0:
       raise ValueError("Endmenge muss zwischen 0 und Anfangsmenge liegen!")
   return t / math.log2(N0 / N)