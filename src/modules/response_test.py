"""funció get_response_test()"""
def get_response_test() -> None:
	"""
	En el mode test no fem servir cap api. Retorna una simulació d'un resum

	Arguments: -

	Returns:
	str: el resum i l'esquema del video transcrit
	"""
	content = """

# **Resumen**

En el video, José Luis Cava, analista financiero, aborda dos preguntas clave: qué se necesita para ser rentable en bolsa y si las acciones de inteligencia artificial han alcanzado su techo tras recientes ventas significativas. Cava argumenta que la venta masiva de acciones no necesariamente indica un techo en las cotizaciones de la inteligencia artificial, ya que los "insiders" no siempre toman decisiones acertadas sobre el futuro del mercado. Respecto a ser un especulador exitoso, Cava resalta la importancia de defenderse de la degradación monetaria invirtiendo en fondos indexados, y señala que, debido a la situación económica actual, la especulación se presenta como una necesidad para los jóvenes.

Cava enfatiza que para especular con éxito, es crucial tener autoconfianza y una mentalidad de superación, sugiriendo que aquellos que creen en sí mismos son más propensos a triunfar en la bolsa. También explica que la especulación efectiva requiere práctica y aprendizaje continuo, idealmente bajo la guía de un mentor, y destaca la importancia de poseer un "truco" o sistema de especulación, aunque sea imperfecto. Este truco debe ser refinado y adaptado mediante repetición y experiencia práctica, y subraya que la autocorrección y el ajuste constante son fundamentales.

Cava también menciona la necesidad de equilibrar entre buscar grandes ganancias esporádicas y realizar operaciones pequeñas que generen beneficios recurrentes. Recomienda controlar las pérdidas desde el inicio y hacer muchas operaciones para alcanzar la rentabilidad. El proceso de convertirse en rentable, según Cava, puede tomar entre dos a tres años, dependiendo de la dedicación y la frecuencia con la que se opera. Además, insiste en que la especulación debe adaptarse a cambios macroeconómicos, como las políticas monetarias de los bancos centrales, para aprovechar el flujo de liquidez en los mercados. Finaliza animando a los espectadores a conocer más sobre las condiciones del mercado y enfatiza la importancia de comenzar a especular sin demora para desarrollar la experiencia necesaria en el entorno financiero actual.

# **Esquema**

- **Venta de acciones de inteligencia artificial**

  - La venta masiva no indica necesariamente un techo en las cotizaciones.
  - Insiders no siempre aciertan.

- **Ser un especulador exitoso**

  - **Importancia de la autoconfianza y mentalidad de superación.**
  - **Defenderse de la degradación monetaria** mediante inversión en fondos indexados.

- **Desarrollo de habilidades para la especulación**

  - Conseguir un "truco" o sistema de especulación, aunque no sea perfecto.
  - Aprender de mentores y refinar el truco mediante repetición.
  - Equilibrar entre grandes ganancias esporádicas y beneficios recurrentes.

- **Estrategias para la operativa en bolsa**

  - Hacer muchas operaciones para aprender y adaptarse.
  - Controlar pérdidas desde el inicio.
  - Rentabilidad en dos a tres años.

- **Adaptación a cambios macroeconómicos**

  - Comprender políticas monetarias y flujos de liquidez.
  - Iniciar la especulación sin demora para ganar experiencia.

- **Conclusión**

  - Especular es esencial para jóvenes en la situación económica actual.
  - Aumentar conocimientos y dedicación para éxito en mercados.
"""

	return content
