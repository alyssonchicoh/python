create table dim_ies (
	id int auto_increment primary key,
	nome varchar(500) not null,
	cnpj varchar(255),
	radical_cnpj varchar(255),
	cidade varchar(255),
	estado varchar(255),
	endereco varchar(255),
	latitude varchar(255),
	longitude varchar(255),
	ies_sede boolean,
	nome_sede varchar(255)
);

create table dim_curso (
	id int auto_increment primary key,
	nome varchar(255),
	area varchar(255),
	carga_horaria int,
	id_ies_fk int,
	foreign key (id_ies_fk)
		references dim_ies(id)

);


create table fat_preenchimento_censo(
	id int auto_increment primary key,
	data_preenchimento date, 
	id_ies_fk int,
	id_curso_fk int,
	foreign key (id_ies_fk)
		references dim_ies(id),
	foreign key (id_curso_fk)
		references dim_curso(id)
	
);


create table fat_renovacao_automatica(
	id int auto_increment primary key,
	data_renovacao date, 
	data_vencimento int,
	sequencial_de_tipo int,
	id_ies_fk int,
	id_curso_fk int,
	foreign key (id_ies_fk)
		references dim_ies(id),
	foreign key (id_curso_fk)
		references dim_curso(id)
	
);

# VALOR_CORRENTE
# VALOR_ANTERIOR

create table fat_alarme(
	id int auto_increment primary key,
	data date,
	data_correcao date,
	status_correcao varchar(255),
	severidade varchar(255),
	tipo_indicador varchar(255),
	desc_nome_indicador varchar(255),
	versao_numero_indicador varchar(255),
	nome_ies varchar(255),
	radical_cnpj_ies varchar(255),
	cnpj_ies varchar(255),
	latitude_ies varchar(255),
	longitude_ies varchar(255),
	cidade_ies varchar(255),
	estado_ies varchar(255),
	endereco_ies varchar(255),
	grupo_mantenedor_ies varchar(255),
	ies_sede varchar(255),
	nome_sede_ies varchar(255),
	nome_curso varchar(255),
	area_curso varchar(255),
	carga_horaria_curso varchar(255)	
);

