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
    TABLE_NAME_ALARM = "fat_alarme"

    # COLUNAS DA TABELA DE ALARME
    ALARM_ID = "id"
    ALARM_DATE = "data"
    ALARM_CORRECTION_DATE = "data_correcao"
    ALARM_CORRECTION_STATUS = "status_correcao"
    ALARM_SEVERITY = "severidade"
    ALARM_INDICATOR_TYPE = "tipo_indicador"
    ALARM_INDICATOR_NAME = "desc_nome_indicador"
    ALARM_INDICATOR_VERSION = "versao_numero_indicador"
    ALARM_CURRENT_VALUE = "valor_corrente"
    ALARM_PREVIOUS_VALUE = "valor_anterior"
    ALARM_IES_NAME = "nome_ies"
    ALARM_IES_RADICAL_CNPJ = "radical_cnpj_ies"
    ALARM_IES_CNPJ = "cnpj_ies"
    ALARM_IES_LATITUDE = "latitude_ies"
    ALARM_IES_LONGITUDE = "longitude_ies"
    ALARM_IES_CITY = "cidade_ies"
    ALARM_IES_STATE = "estado_ies"
    ALARM_IES_ADDRESS = "endereco_ies"
    ALARM_IES_GROUP = "grupo_mantenedor_ies"
    ALARM_IES_SEDE = "ies_sede"
    ALARM_IES_SEDE_NAME = "nome_sede_ies"
    ALARM_COURSE_NAME = "nome_curso"
    ALARM_COURSE_AREA = "area_curso"
    ALARM_COURSE_WORKLOAD = "carga_horaria_curso"

    # NOME DA TABELA DE PREENCHIMENTO DO CENSO
    TABLE_NAME_PREENCHIMENTO_CENSO = "fat_preenchimento_censo"

    PREENCHIMENTO_CENSO_ID = "id"
    PREENCHIMENTO_CENSO_DATE = "data_preenchimento"
    PREENCHIMENTO_CENSO_IES = "id_ies_fk"
    PREENCHIMENTO_CENSO_COURSE = "id_curso_fk"

    TABLE_NAME_RENOVACAO_AUTOMATICA = "fat_renovacao_automatica"

    RENOVACAO_AUTOMATICA_ID = "id"
    RENOVACAO_AUTOMATICA_DATE_RENOVACAO = "data_renovacao"
    RENOVACAO_AUTOMATICA_DATE_VENCIMENTO = "data_vencimento"
    RENOVACAO_AUTOMATICA_SEQUENTIAL_TYPE = "sequencial_de_tipo"
    RENOVACAO_AUTOMATICA_IES = "id_ies_fk"
    RENOVACAO_AUTOMATICA_COURSE = "id_curso_fk"
