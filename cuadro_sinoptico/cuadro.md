# Actividad: Cuadro Sinóptico de Metodologías Ágiles

```mermaid
graph LR
    %% Nodo Principal
    A[METODOLOGÍAS ÁGILES] ---> B(Scrum)
    A ---> C(Extreme Programming - XP)
    A ---> D(Lean Software Development)
    A ---> E(SAFe - Scaled Agile Framework)
    A ---> F(Crystal)

    %% Scrum Branches
    B --- B1[Propósito Principal] --> B1a(Maximizar valor mediante entrega temprana e incrementos funcionales.)
    B --- B2[Características Clave] --> B2a(Proceso iterativo en sprints cortos y fijos.)
    B --- B3[Roles] --> B3a(Product Owner, Scrum Master, Equipo de Desarrollo.)
    B --- B4[Artefactos] --> B4a(Product Backlog, Sprint Backlog, Incremento.)
    B --- B5[Prácticas] --> B5a(Sprint Planning, Daily, Review, Retrospective.)
    B --- B6[Proyectos] --> B6a(Requisitos cambiantes, equipos pequeños.)
    B --- B7[Ventajas] --> B7a(Flexibilidad, transparencia, mejora continua.)
    B --- B8[Limitaciones] --> B8a(Depende de equipos maduros y autoorganizados.)

    %% XP Branches
    C --- C1[Propósito Principal] --> C1a(Alta calidad constante y excelencia técnica.)
    C --- C2[Características Clave] --> C2a(Desarrollo iterativo y comunicación constante.)
    C --- C3[Roles] --> C3a(Desarrollador, Cliente, Probador, Tracker, Coach.)
    C --- C4[Artefactos] --> C4a(Historias de usuario, Plan de lanzamiento, Código.)
    C --- C5[Prácticas] --> C5a(Pair Programming, TDD, Integración Continua.)
    C --- C6[Proyectos] --> C6a(Requisitos volátiles y alta exigencia técnica.)
    C --- C7[Ventajas] --> C7a(Alta calidad de código, respuesta rápida.)
    C --- C8[Limitaciones] --> C8a(Rígida en ingeniería, foco excesivo en código.)

    %% Lean Branches
    D --- D1[Propósito Principal] --> D1a(Minimizar desperdicio y maximizar valor.)
    D --- D2[Características Clave] --> D2a(Eliminar desperdicio, calidad integrada.)
    D --- D3[Roles] --> D3a(Equipos multifuncionales sin roles rígidos.)
    D --- D4[Artefactos] --> D4a(Tableros Kanban visuales.)
    D --- D5[Prácticas] --> D5a(Value Stream Mapping, Pull Systems.)
    D --- D6[Proyectos] --> D6a(Optimización de procesos y eficiencia operativa.)
    D --- D7[Ventajas] --> D7a(Reducción de costos, entrega rápida.)
    D --- D8[Limitaciones] --> D8a(Requiere cambio cultural profundo.)

    %% SAFe Branches
    E --- E1[Propósito Principal] --> E1a(Escalar agilidad a nivel organizacional.)
    E --- E2[Características Clave] --> E2a(Sincronización de múltiples equipos.)
    E --- E3[Roles] --> E3a(RTE, STE, Product Management a escala.)
    E --- E4[Artefactos] --> E4a(Program Backlog, Features, Enablers.)
    E --- E5[Prácticas] --> E5a(PI Planning, Agile Release Trains.)
    E --- E6[Proyectos] --> E6a(Grandes corporativos con cientos de desarrolladores.)
    E --- E7[Ventajas] --> E7a(Alineación estratégica y gobernanza global.)
    E --- E8[Limitaciones] --> E8a(Alta complejidad y burocracia técnica.)

    %% Crystal Branches
    F --- F1[Propósito Principal] --> F1a(Priorizar personas sobre procesos.)
    F --- F2[Características Clave] --> F2a(Adaptabilidad según tamaño y criticidad.)
    F --- F3[Roles] --> F3a(Varía por color ej. Crystal Clear.)
    F --- F4[Artefactos] --> F4a(Documentación mínima, código probado.)
    F --- F5[Prácticas] --> F5a(Comunicación osmótica, entrega frecuente.)
    F --- F6[Proyectos] --> F6a(Enfoque en factor humano y comunicación.)
    F --- F7[Ventajas] --> F7a(Ligera, flexible y centrada en el talento.)
    F --- F8[Limitaciones] --> F8a(Falta de estructura para equipos novatos.)
