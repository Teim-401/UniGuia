import telebot 
from telebot import types
import logging

# Configurar logs para reducir mensajes en la terminal
logging.basicConfig(level=logging.CRITICAL)

# Conexión con nuestro BOT
TOKEN = '7567218231:AAF15mvlHY_8WDEQhPeLQeUjOzhLxAEnMvs'  
bot = telebot.TeleBot(TOKEN)  

# Creación de comandos simples como '/Start' y '/Help' 
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '🎓 Bienvenido al Bot de Pensum de la Universidad de Oriente 📖\n\nHola! Soy tu asistente para obtener información sobre los pensum de diferentes carreras universitarias.')

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """🤖 *Ayuda - Comandos disponibles* 📌

*/start* → Inicia el bot y recibe un mensaje de bienvenida.  
*/help* → Muestra esta lista de comandos y cómo usarlos.  
*/pensum* → Selecciona tu carrera y recibe el pensum en PDF.  

📩 Escríbeme y te asistiré con cualquier duda. 🚀"""
    
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")

# Menú de selección de carrera
@bot.message_handler(commands=['pensum'])
def send_career_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)

    carreras = [
        "Ingeniería Civil", "Ingeniería de Petróleo", "Ingeniería de Sistemas",
        "Ingeniería Eléctrica", "Ingeniería en Computación", "Ingeniería Industrial",
        "Ingeniería Mecánica", "Ingeniería Química", "Arquitectura", "Medicina",
        "Contaduría Pública", "Turismo", "Tecnología en Fabricación Mecánica",
        "Tecnología Electrónica", "Administración de Empresas"
    ]

    for carrera in carreras:
        markup.add(types.KeyboardButton(carrera))

    bot.send_message(message.chat.id, "Selecciona tu carrera:", reply_markup=markup)

# Diccionario con descripciones breves de cada carrera
descripciones_carreras = {
    "Ingeniería Civil": "Diseño y construcción de infraestructuras como edificios y puentes.",
    "Ingeniería de Petróleo": "Exploración y extracción de hidrocarburos para la producción de energía.",
    "Ingeniería de Sistemas": "Desarrollo de software, estructura de datos y tecnología informática.",
    "Ingeniería Eléctrica": "Estudio y aplicación de sistemas eléctricos y generación de energía.",
    "Ingeniería en Computación": "Diseño y desarrollo de hardware, redes y programación avanzada.",
    "Ingeniería Industrial": "Optimización de procesos y mejora de productividad en empresas.",
    "Ingeniería Mecánica": "Diseño y desarrollo de maquinaria, motores y procesos mecánicos.",
    "Ingeniería Química": "Aplicación de procesos químicos en la producción industrial.",
    "Arquitectura": "Diseño y planificación de espacios funcionales y estéticos.",
    "Medicina": "Diagnóstico y tratamiento de enfermedades en el ámbito de la salud.",
    "Contaduría Pública": "Gestión financiera y administración económica en empresas.",
    "Turismo": "Planificación y promoción de actividades turísticas.",
    "Tecnología en Fabricación Mecánica": "Procesos avanzados en manufactura y producción mecánica.",
    "Tecnología Electrónica": "Diseño y desarrollo de dispositivos electrónicos.",
    "Administración de Empresas": "Gestión de negocios, planificación estratégica y liderazgo organizacional."
}

# Diccionario con los archivos PDF correspondientes
pensums_pdf = {
    "Ingeniería Civil": "pensum_civil.pdf",
    "Ingeniería de Petróleo": "pensum_petroleo.pdf",
    "Ingeniería de Sistemas": "pensum_sistemas.pdf",
    "Ingeniería Eléctrica": "pensum_electrica.pdf",
    "Ingeniería en Computación": "pensum_computacion.pdf",
    "Ingeniería Industrial": "pensum_industrial.pdf",
    "Ingeniería Mecánica": "pensum_mecanica.pdf",
    "Ingeniería Química": "pensum_quimica.pdf",
    "Arquitectura": "pensum_arquitectura.pdf",
    "Medicina": "pensum_medicina.pdf",
    "Contaduría Pública": "pensum_contaduria.pdf",
    "Turismo": "pensum_turismo.pdf",
    "Tecnología en Fabricación Mecánica": "pensum_fabricacion.pdf",
    "Tecnología Electrónica": "pensum_electronica.pdf",
    "Administración de Empresas": "pensum_administracion.pdf"
}

# Manejo de la selección de carrera para enviar Pensum con descripción breve y opción de solicitar más información
@bot.message_handler(func=lambda message: message.text in descripciones_carreras.keys())
def send_selected_info_or_pensum(message):
    carrera = message.text
    descripcion = descripciones_carreras.get(carrera, "Descripción no disponible.")

    # Enviar descripción breve con la opción de solicitar más detalles
    bot.send_message(message.chat.id, f"📌 *{carrera}*\n{descripcion}\n\n🔍 Usa `/info_carrera {carrera}` para más detalles.", parse_mode="Markdown")

    # Enviar el PDF si existe
    pdf_file = pensums_pdf.get(carrera)
    if pdf_file:
        try:
            bot.send_document(message.chat.id, open(pdf_file, "rb"))
        except FileNotFoundError:
            bot.send_message(message.chat.id, f"Aún no tengo el pensum de {carrera}. ¡Pronto lo agregaré!")

# Diccionario con información detallada de cada carrera
explicaciones_carreras = {
    "Ingeniería Civil": "La carrera de Ingeniería Civil en la Universidad de Oriente (UDO) forma profesionales para planificar, diseñar, construir, supervisar y mantener infraestructuras esenciales para la sociedad (edificios, puentes, carreteras, etc.). El plan de estudios abarca Ciencias Básicas (Matemáticas, Física, Química), Mecánica de Sólidos y Estructuras, Hidráulica y Sanitaria, Vías Terrestres, Gerencia de la Construcción y otras áreas como Dibujo Técnico y Legislación. Es importante revisar el plan específico de cada núcleo de la UDO. Para tener éxito en esta carrera, se recomiendan aptitudes como el interés por las ciencias exactas, capacidad de análisis y resolución de problemas, pensamiento lógico, visión espacial, atención al detalle, habilidad para el trabajo en equipo, responsabilidad, interés por el desarrollo y la adaptabilidad. Estudiar Ingeniería Civil en la UDO ofrece una sólida formación para contribuir al desarrollo a través de la infraestructura.",
    "Ingeniería de Petróleo": "La carrera de Ingeniería en Petróleo en la UDO forma profesionales para planificar, diseñar, operar y optimizar procesos de exploración, perforación, producción, transporte y almacenamiento de hidrocarburos. Combina geología, física, química, termodinámica y mecánica de fluidos. El plan de estudios incluye Ciencias Básicas, Geociencias, Ingeniería de Perforación, Producción y Yacimientos, Ingeniería de Gas Natural, Economía y Evaluación de Proyectos, Seguridad, Ambiente y Salud. Es crucial revisar el plan específico del Núcleo de Anzoátegui. Se recomiendan aptitudes como una sólida base en ciencias exactas, capacidad de análisis y resolución de problemas complejos, pensamiento lógico, interés por la tecnología, habilidad para trabajar con modelos y en equipo, atención al detalle, conciencia sobre seguridad y ambiente, adaptabilidad e interés por la geología. Estudiar Ingeniería en Petróleo en la UDO ofrece oportunidades en una industria energética clave.",
    "Ingeniería de Sistemas": "Ingeniería en Sistemas en la UDO (Puerto La Cruz) te forma para diseñar, desarrollar, implementar y gestionar sistemas informáticos complejos. Aprenderás sobre programación avanzada, estructuras de datos, algoritmos, bases de datos, redes, sistemas operativos, inteligencia artificial, ingeniería de software y gestión de proyectos tecnológicos. La formación combina teoría, prácticas de laboratorio y desarrollo de proyectos de ingeniería.",
    "Ingeniería Eléctrica": "La Ingeniería Eléctrica en la UDO (Núcleo de Anzoátegui) forma profesionales para diseñar, desarrollar, operar y mantener sistemas eléctricos y electrónicos, abarcando generación, transmisión y distribución de energía, máquinas eléctricas, electrónica de potencia, control automático, comunicaciones y más, con una posible orientación hacia el sector energético regional. El plan de estudios incluye Ciencias Básicas (Matemáticas, Física, Circuitos), Análisis de Circuitos, Electromagnetismo, Máquinas Eléctricas, Electrónica, Electrónica de Potencia, Sistemas de Control y Potencia, Comunicaciones, Procesamiento de Señales e Instrumentación. Es crucial revisar el plan de estudios específico del departamento. Se recomiendan aptitudes como una sólida base en ciencias exactas, razonamiento lógico y analítico, resolución de problemas técnicos, pensamiento abstracto, atención al detalle, curiosidad tecnológica, habilidad para el trabajo en equipo, responsabilidad, capacidad de aprendizaje continuo y habilidades de comunicación. Estudiar Ingeniería Eléctrica en la UDO en esta región ofrece amplias oportunidades en el sector energético, la industria petrolera y petroquímica, y otras áreas tecnológicas.",
    "Ingeniería en Computación": "La Ingeniería en Computación en la UDO (Núcleo de Anzoátegui) forma profesionales para diseñar, desarrollar, implementar y mantener sistemas computacionales, abarcando hardware y software, incluyendo arquitectura de computadoras, sistemas operativos, redes, sistemas embebidos, IA y más. El plan de estudios incluye Ciencias Básicas (Matemáticas, Física, Lógica), Fundamentos de Programación, Arquitectura de Computadoras, Sistemas Operativos, Redes, Electrónica Digital, Sistemas Embebidos, Inteligencia Artificial y Diseño Digital. Es crucial revisar el plan de estudios específico del departamento. Se recomiendan aptitudes como una sólida base en ciencias exactas, razonamiento lógico y analítico, pensamiento abstracto, atención al detalle, curiosidad tecnológica, habilidad para la resolución de problemas técnicos, habilidad para el trabajo en equipo, paciencia, capacidad de adaptación e interés por la innovación. Estudiar Ingeniería en Computación en la UDO en esta región ofrece amplias oportunidades en el diseño de hardware y software, IA, robótica, sistemas embebidos, seguridad informática y otras áreas tecnológicas en crecimiento.",
    "Ingeniería Industrial": "La Ingeniería Industrial en la UDO (Núcleo de Anzoátegui) forma profesionales para diseñar, implementar, optimizar y gestionar sistemas productivos y de servicios, con una visión integral de las organizaciones para mejorar la eficiencia, productividad, calidad y rentabilidad. El plan de estudios abarca Ciencias Básicas (Matemáticas, Estadística, Investigación de Operaciones), Ciencias de la Ingeniería (Mecánica, Termodinámica, Electricidad), Gestión de la Producción y Operaciones, Estudio del Trabajo y Ergonomía, Gestión de la Calidad, Ingeniería Económica, Investigación de Operaciones, Gestión de Recursos Humanos, Seguridad Industrial y otras áreas complementarias. Es crucial revisar el plan de estudios específico del departamento. Se recomiendan aptitudes como el razonamiento lógico y analítico, pensamiento sistémico, capacidad de organización y planificación, habilidad para la toma de decisiones, habilidades de comunicación, liderazgo, interés por la eficiencia y productividad, adaptabilidad, habilidad para trabajar con datos y visión estratégica. Estudiar Ingeniería Industrial en la UDO en esta región ofrece amplias oportunidades en diversos sectores industriales y de servicios que buscan optimizar sus operaciones.",
    "Ingeniería Mecánica": "Ingeniería Mecánica en la UDO (Puerto La Cruz) te forma para diseñar, desarrollar, analizar, fabricar y mantener sistemas mecánicos. Aprenderás sobre termodinámica, mecánica de fluidos, mecánica de sólidos, diseño mecánico, materiales de ingeniería, procesos de manufactura, control y automatización. La formación combina teoría, prácticas de laboratorio y proyectos de diseño e ingeniería",
    "Ingeniería Química": "La Ingeniería Química en la UDO (Núcleo de Anzoátegui) formas profesionales para diseñar, desarrollar, optimizar y operar procesos industriales que transforman materias primas en productos útiles, con un enfoque significativo en la industria petrolera y petroquímica de la región. El plan de estudios abarca Ciencias Básicas (Matemáticas, Física, Química), Termodinámica Química, Mecánica de Fluidos, Transferencia de Calor y Masa, Operaciones Unitarias, Cinética Química y Diseño de Reactores, Control de Procesos, Ingeniería de las Reacciones Químicas, Diseño de Plantas Químicas, Química Industrial, Seguridad Industrial y Protección Ambiental. Es crucial revisar el plan de estudios específico del departamento. Se recomiendan aptitudes como una sólida base en ciencias exactas, capacidad de análisis y síntesis, pensamiento lógico y sistemático, habilidad para la resolución de problemas prácticos, atención al detalle, curiosidad por los procesos industriales, habilidad para el trabajo en equipo, conciencia sobre seguridad y ambiente, adaptabilidad y habilidades de comunicación. Estudiar Ingeniería Química en la UDO en esta región ofrece excelentes oportunidades en la industria energética y otras áreas relacionadas. MECÁNICA La Ingeniería Mecánica en la UDO (Núcleo de Anzoátegui) forma profesionales para diseñar, desarrollar, fabricar, operar y mantener sistemas mecánicos en diversas industrias. El plan de estudios abarca Ciencias Básicas (Matemáticas, Física, Química), Mecánica de Sólidos y Fluidos, Diseño Mecánico (CAD, FEA), Termodinámica y Transferencia de Calor, Ciencia de los Materiales, Manufactura, Control, Sistemas de Fluidos y Gestión del Mantenimiento. Es crucial revisar el plan de estudios específico del departamento. Se recomiendan aptitudes como la inclinación hacia ciencias exactas, razonamiento lógico y analítico, resolución de problemas prácticos, pensamiento espacial, atención al detalle, curiosidad por el funcionamiento de las cosas, habilidad para el trabajo en equipo, creatividad, habilidades de comunicación e interés por la tecnología y la manufactura. En el contexto industrial de Puerto La Cruz, esta carrera ofrece amplias oportunidades laborales.",
    "Arquitectura": "La Licenciatura en Arquitectura de la UDO forma profesionales para proyectar, diseñar, construir y gestionar espacios habitables que respondan a las necesidades sociales, culturales, económicas y ambientales. El plan de estudios abarca Diseño Arquitectónico, Teoría e Historia de la Arquitectura y el Urbanismo, Tecnología de la Construcción, Expresión Gráfica y Digital, Estructuras, Instalaciones, Urbanismo, Legislación, Gestión de Proyectos y Diseño Bioclimático. La formación es teórico-práctica, con énfasis en talleres de diseño y desarrollo de habilidades como creatividad, visión espacial, representación gráfica, análisis, resolución de problemas y comunicación. Se recomiendan aptitudes como interés por el diseño y el arte, habilidad para el dibujo, visión espacial, creatividad, capacidad de observación, habilidades matemáticas y físicas básicas, capacidad de análisis, habilidades de comunicación, interés por la historia y la cultura, conciencia ambiental, paciencia y perseverancia. Esta licenciatura ofrece la oportunidad de contribuir al desarrollo del entorno construido en la región oriental de Venezuela. Es importante verificar la oferta específica del campus de interés.",
    "Medicina": "La Licenciatura en Medicina en la UDO (Núcleo de Anzoátegui, Barcelona) forma médicos generales integrales con sólida base científica, humanística y ética, capacitados para la promoción, prevención, diagnóstico, tratamiento y rehabilitación de la salud a nivel individual, familiar y comunitario. El plan de estudios es extenso y riguroso, abarcando Ciencias Básicas, Ciencias Clínicas, Salud Pública, Bioética, Semiología y Diagnóstico. La formación es teórico-práctica, con laboratorios y rotaciones clínicas en hospitales como el Dr. Luis Razetti. Se desarrollan habilidades como pensamiento crítico, comunicación, empatía, responsabilidad y aprendizaje continuo. La carrera dura seis años, incluyendo el internado rotatorio. Se recomiendan aptitudes como vocación de servicio, sólida base en ciencias, capacidad de estudio, paciencia, habilidad para la observación, estabilidad emocional, trabajo en equipo, curiosidad científica e integridad ética. Estudiar Medicina en la UDO en este núcleo ofrece una formación comprometida con la salud de la comunidad y es una carrera exigente pero gratificante.",
    "Contaduría Pública": "La Licenciatura en Contaduría Pública en la UDO forma profesionales con conocimientos en contabilidad, finanzas, tributación y auditoría, capacitados para analizar la información financiera de organizaciones públicas y privadas bajo las leyes venezolanas. El plan de estudios ofrece una formación integral con enfoque teórico-práctico, cubriendo áreas como contabilidad general y de costos, finanzas, derecho mercantil y tributario (IVA, ISLR), auditoría, sistemas de información contable y ética profesional. Se busca desarrollar habilidades de análisis, atención al detalle, organización, comunicación y pensamiento crítico, adaptándose al contexto venezolano. Se recomiendan aptitudes como habilidad numérica y lógica, precisión, capacidad de análisis e interpretación, organización, integridad, responsabilidad, habilidades de comunicación, pensamiento crítico, adaptabilidad e interés por la tecnología. La carrera es ideal para quienes se interesan por los números, el análisis financiero y la transparencia en la gestión empresarial en Venezuela.",
    "Turismo": "La Licenciatura en Turismo de la UDO forma profesionales para planificar, gestionar, desarrollar y promover la actividad turística de manera sostenible, aprovechando los recursos naturales y culturales de la región. El plan de estudios abarca Introducción al Turismo, Geografía Turística (con énfasis en Venezuela y la región oriental), Patrimonio Turístico y Cultural, Planificación y Desarrollo Turístico, Gestión de Empresas Turísticas, Marketing Turístico, Legislación Turística, Servicios Turísticos, Turismo Sostenible e Idioma Extranjero. Se enfoca en el contexto local y busca desarrollar habilidades prácticas como comunicación, trabajo en equipo y creatividad. Se recomiendan aptitudes como la pasión por viajar, habilidades de comunicación interpersonal, vocación de servicio, capacidad de organización, flexibilidad, creatividad, conciencia cultural, interés por la geografía e historia, habilidad para los idiomas y conciencia ambiental. Esta licenciatura ofrece oportunidades en el sector turístico en crecimiento de la región oriental de Venezuela.",
    "Tecnología en Fabricación Mecánica": "El TSU en Fabricación Mecánica de la UDO forma técnicos capacitados para planificar, ejecutar, supervisar y controlar procesos de fabricación de piezas mecánicas utilizando diversas técnicas y máquinas-herramienta. El plan de estudios se centra en Dibujo Técnico Mecánico, Metrología Dimensional, Procesos de Fabricación (torneado, fresado, soldadura, etc.), Máquinas-Herramienta (convencionales y CNC básicas), Selección de Materiales, Tratamientos Térmicos, Automatización Básica, Seguridad Industrial, Mantenimiento Mecánico Básico y Control de Calidad. La formación tiene un fuerte énfasis práctico con prácticas profesionales en industrias de la región. El programa suele durar de dos a tres años y proporciona una inserción laboral rápida a nivel técnico. Se recomiendan aptitudes como interés por máquinas y procesos de fabricación, habilidad para el dibujo técnico y la visualización espacial, destreza manual, atención al detalle, capacidad para seguir instrucciones, habilidad para resolver problemas técnicos, conciencia de seguridad, interés por la tecnología CNC, capacidad de trabajo en equipo y responsabilidad con la calidad y productividad.",
    "Tecnología Electrónica": "El TSU en Tecnología Electrónica de la UDO forma técnicos capacitados para instalar, mantener, reparar y operar sistemas y equipos electrónicos en diversas áreas industriales y de servicios. El plan de estudios se centra en Electricidad y Magnetismo, Electrónica Analógica y Digital, Instrumentación Electrónica, Comunicaciones Electrónicas, Control Electrónico (introducción), Mantenimiento de Equipos Electrónicos, Instalaciones Eléctricas (básicas), Seguridad Eléctrica e Informática Aplicada a la Electrónica. La formación tiene un fuerte énfasis práctico con prácticas profesionales en industrias, empresas de telecomunicaciones y centros de servicio técnico de la región. El programa suele durar de dos a tres años y proporciona una inserción laboral rápida a nivel técnico. Se recomiendan aptitudes como interés por la electrónica y los equipos electrónicos, habilidad para el razonamiento lógico y la resolución de problemas técnicos, atención al detalle, destreza manual, capacidad para seguir diagramas, interés por la tecnología, paciencia, conciencia de seguridad eléctrica, habilidad para el manejo de instrumentos de medición y capacidad de trabajo en equipo.",
    "Administración de Empresas": "La Licenciatura en Administración de Empresas en la UDO forma profesionales para gestionar organizaciones de manera eficiente y eficaz. El plan de estudios abarca áreas como contabilidad, finanzas, mercadeo, recursos humanos, producción, economía, derecho, informática, administración estratégica y emprendimiento, combinando teoría y práctica. Se busca desarrollar habilidades como liderazgo, comunicación, trabajo en equipo, resolución de problemas y pensamiento crítico, adaptándose al entorno venezolano. Se recomiendan aptitudes como interés por los negocios, habilidad numérica y analítica, organización, comunicación efectiva, liderazgo, trabajo en equipo, pensamiento crítico, adaptabilidad, ética e interés por la tecnología, aunque la carrera también ayuda a desarrollarlas. En resumen, la carrera busca formar profesionales integrales y adaptables al mundo empresarial."
}



# Explicación detallada con el comando /info_carrera NombreDeLaCarrera
@bot.message_handler(commands=['info_carrera'])
def send_detailed_info(message):
    carrera = message.text.replace("/info_carrera ", "")
    info = explicaciones_carreras.get(carrera, "Aún no hay información detallada para esta carrera.")
    
    bot.send_message(message.chat.id, info, parse_mode="Markdown")

# Mantener el bot activo
if __name__ == "__main__":
    bot.polling(none_stop=True, skip_pending=True)
