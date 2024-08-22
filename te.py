class Te:
    duracion = 365 # Dias
    # Incorporacion de constructor
    def __init__(self, sabor, formato):
        self.sabor = sabor
        self.formato = formato

   
    
    @staticmethod
    def retorna_tiempo_y_recomendacion(sabor):
        """
        Retorna el tiempo de preparación y la recomendación de consumo 
        en función del sabor seleccionado.

        Args:
            sabor (int): El número correspondiente al sabor del té.
                - 1: Sabor 1
                - 2: Sabor 2
                - 3: Sabor 3

        Returns:
            tuple: Un par (tiempo_preparacion, recomendacion_consumo)
                - tiempo_preparacion (int): El tiempo en minutos que tarda en prepararse el té.
                - recomendacion_consumo (str): La recomendación de cuándo consumir el té.

        Ejemplos:
            >>> retorna_tiempo_y_recomendacion(1)
            (3, 'Al desayunar')

            >>> retorna_tiempo_y_recomendacion(2)
            (5, 'Al medio día')

            >>> retorna_tiempo_y_recomendacion(4)
            (0, 'Sabor no válido')
        """
        if sabor == 1:
            return (
                3,
                "Al desayunar",
            )
        elif sabor == 2:
            return (
                5,
                "Al medio día",
            )
        elif sabor == 3:
            return (
                6,
                "Al atardecer",
            )
        else:
            return 0, "Sabor no válido"


    @staticmethod
    def retorna_precio(formato):
        """
        Retorna el precio correspondiente al formato seleccionado.

        Args:
            formato (int): El formato del té en gramos.
                - 300: Formato de 300 gramos.
                - 500: Formato de 500 gramos.

        Returns:
            int: El precio en moneda local para el formato especificado.
                - 3000 si el formato es de 300 gramos.
                - 5000 si el formato es de 500 gramos.
                - 0 si el formato no es válido.

        Ejemplos:
            >>> retorna_precio(300)
            3000

            >>> retorna_precio(500)
            5000

            >>> retorna_precio(100)
            0
        """
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        else:
            return 0



#duración
#retorno da error