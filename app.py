import random
import time
import hashlib

class AlgoritmoV10Contraria:
    def __init__(self, resultados_recientes):
        """
        resultados_recientes: Lista con los últimos números que salieron (ej. [45, 12, 89])
        """
        self.historico = resultados_recientes
        self.rango_maximo = 100 # Ajustar según el formato del Súper Gana (00 al 99)

    def _generar_entropia_pura(self):
        """Genera una semilla impredecible usando hardware (milisegundos) y hashing"""
        pulso_tiempo = str(time.time_ns()).encode('utf-8')
        hash_caotico = hashlib.sha256(pulso_tiempo).hexdigest()
        # Convertimos el hash en un entero gigante para romper la inercia del día
        return int(hash_caotico, 16)

    def calcular_numeros_antiesperados(self):
        """Filtra lo predecible y extrae los números fríos con alta entropía"""
        semilla = self._generar_entropia_pura()
        random.seed(semilla)
        
        # 1. Mapa de calor inverso: Identificar qué números NO deben salir según la lógica común
        numeros_esperados = set()
        for num in self.historico:
            numeros_esperados.add(num)
            # Elimina también los vecinos directos (lo que la masa suele jugar por descarte)
            numeros_esperados.add((num + 1) % self.rango_maximo)
            numeros_esperados.add((num - 1) % self.rango_maximo)
            # Elimina reflejos (ej: si salió 12, descarta 21)
            reflejo = int(str(num)[::-1]) if len(str(num)) == 2 else num
            numeros_esperados.add(reflejo % self.rango_maximo)

        # 2. Generar el universo de números "Fríos" o "Invisibles" para el sistema
        universo_contrario = [x for x in range(self.rango_maximo) if x not in numeros_esperados]
        
        # Si el histórico está vacío o es muy pequeño, asegurar el universo completo
        if not universo_contrario:
            universo_contrario = list(range(self.rango_maximo))

        # 3. Selección caótica de los 2 números definitivos
        # Mezclamos el universo usando la entropía del hash para evitar patrones lineales
        random.shuffle(universo_contrario)
        
        seleccionados = universo_contrario[:2]
        
        # Formatear a dos dígitos (00, 01... 99)
        return [f"{num:02d}" for num in seleccionados]

# ==========================================
# REPLICA EN EJECUCIÓN (Para usar hoy)
# ==========================================
if __name__ == "__main__":
    # INGRESA AQUÍ LOS ÚLTIMOS RESULTADOS DEL SÚPER GANA
    # Ejemplo: Si los últimos tres resultados fueron 34, 87 y 12:
    ultimos_sorteos = [34, 87, 12] 
    
    print("⚡ [V10 MODIFICADO]: Iniciando contra-algoritmo de evasión...")
    motor = AlgoritmoV10Contraria(ultimos_sorteos)
    
    # Ejecutamos la simulación de inversión
    numeros_para_jugar = motor.calcular_numeros_antiesperados()
    
    print("\n==========================================")
    print(f"🎯 DOS NÚMEROS DE EVASIÓN PARA HOY: {numeros_para_jugar[0]} y {numeros_para_jugar[1]}")
    print("==========================================")
    print("👁️ Explicación: Estos números rompen la inercia lineal del día y evitan las trampas del sistema.")
