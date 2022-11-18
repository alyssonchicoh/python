class DBUtil:

    # TABELA DE IES
    TABLE_NAME_IES = "dim_ies"

    # COLUNAS DA TABELA DE IES
    IES_ID = "id"
    IES_NAME = "nome"
    IES_CNPJ = "cnpj"
    IES_RADICAL_CNPJ = "radical_cnpj"
    IES_CITY = "cidade"
    IES_STATE = "estado"
    IES_ADDRESS = "endereco"
    IES_LATITUDE = "latitude"
    IES_LONGITUDE = "longitude"
    IES_HEAD_OFFICE = "ies_sede"
    IES_HEAD_OFFICE_NAME = "nome_sede"

    # NOME DA TABELA DE CURSO
    TABLE_NAME_CURSO = "dim_curso"

    # COLUNAS DA TABELA DE COURSE
    COURSE_ID = "id"
    COURSE_NAME = "nome"
    COURSE_AREA = "area"
    COURSE_WORKLOAD = "carga_horaria"
    COURSE_ID_IES_FK = "id_ies_fk"

    # NOME DA TABELA DE ALARME
    TABLE_NAME_ALARME = "fat_alarme"

    # COLUNAS DA TABELA DE ALARME
    ALARM_ID = "id"
    ALARM_DATE = "date"
    ALARM_CORRECTION_DATE = "correction_date"
    ALARM_CORRECTION_STATUS = ""
    ALARM_SEVERITY = ""
    ALARM_INDICATOR_TYPE = ""
    ALARM_INDICATOR_NAME = ""
    ALARM_INDICATOR_VERSION = ""
    ALARM_IES_NAME = ""
    ALARM_IES_RADICAL_CNPJ = ""
    ALARM_IES_CNPJ = ""
    ALARM_IES_LATITUDE = ""
    ALARM_IES_LONGITUDE = ""
    ALARM_IES_CITY = ""
    ALARM_IES_STATE = ""
    ALARM_IES_ADDRESS = ""
    ALARM_IES_GROUP = ""
    ALARM_IES_SEDE = ""
    ALARM_COURSE_NAME = ""
    ALARM_COURSE_NAME = ""
    ALARM_COURSE_AREA = ""
    ALARM_COURSE_WORKLOAD = ""

    # NOME DA TABELA DE PREENCHIMENTO DO CENSO
    TABLE_NAME_PREENCHIMENTO_CENSO = "fat_preenchimento_censo"

    PREENCHIMENTO_CENSO_ID = "id"
    PREENCHIMENTO_CENSO_DATE = "data_preenchimento"
    PREENCHIMENTO_CENSO_IES = "id_ies_fk"
    PREENCHIMENTO_CENSO_COURSE = "id_curso_fk"

    TABLE_NAME_RENOVACAO_AUTOMATICA = "fat_renovacao_automatica"
