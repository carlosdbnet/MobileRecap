-- MobCap DB Schema Dump
-- Generated automatically

-- Table: ATIVIDADE
CREATE TABLE IF NOT EXISTS public."ATIVIDADE" (
    "ID" integer NOT NULL,
    "CODATIV" character(5) NOT NULL,
    "DESCRICAO" character(50),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "ATIVIDADE_pkey" PRIMARY KEY ("ID")
);

-- Table: BALANCO
CREATE TABLE IF NOT EXISTS public."BALANCO" (
    "ID" integer NOT NULL,
    "CODEMP" character(3) NOT NULL,
    "NUMLOTE" integer NOT NULL,
    "DESCRICAO" character varying(80),
    "DATABAL" timestamp without time zone,
    "STATUS" character(1),
    "VTOTENT" numeric,
    "VTOTSAI" numeric,
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "BALANCO_pkey" PRIMARY KEY ("ID")
);

-- Table: BALANCO_PRODUTO
CREATE TABLE IF NOT EXISTS public."BALANCO_PRODUTO" (
    "ID" integer NOT NULL,
    "ID_LOTE" integer NOT NULL,
    "ID_PRODUTO" integer NOT NULL,
    "CODPROD" character(20),
    "QUANT" numeric NOT NULL,
    "VUNIT" numeric NOT NULL,
    "VTOTAL" numeric NOT NULL,
    "SINAL" character(1),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "BALANCO_PRODUTO_pkey" PRIMARY KEY ("ID")
);

-- Table: BANCO
CREATE TABLE IF NOT EXISTS public."BANCO" (
    "ID" integer NOT NULL,
    "CODBAN" character(4) NOT NULL,
    "FANTASIA" character(20),
    "RAZAOSOCIAL" character(50),
    "ENDERECO" character(100),
    "CEP" character(9),
    "CIDADE" character(60),
    "UF" character(2),
    "CONTATO" character(20),
    "FONE" character(17),
    "CNPJ" character varying(18),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "BANCO_pkey" PRIMARY KEY ("ID")
);

-- Table: BONUS
CREATE TABLE IF NOT EXISTS public."BONUS" (
    "ID" integer NOT NULL,
    "CODBON" character(3) NOT NULL,
    "DESCRICAO" character(30),
    "DATAINI" timestamp without time zone,
    "DATAVAL" timestamp without time zone,
    "VALOR" numeric NOT NULL,
    "TIPO" character(1),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "BONUS_pkey" PRIMARY KEY ("ID")
);

-- Table: CIDADE
CREATE TABLE IF NOT EXISTS public."CIDADE" (
    "ID" integer NOT NULL,
    "NOME" character(100) NOT NULL,
    "ESTADO" character(2),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "CODIBGE" character varying(7),
    "ATIVO" character(1),
    CONSTRAINT "CIDADE_pkey" PRIMARY KEY ("ID")
);

-- Table: COMISSAO
CREATE TABLE IF NOT EXISTS public."COMISSAO" (
    "ID" integer NOT NULL,
    "TIPO" character(10) NOT NULL,
    "CODIGO" character varying(20) NOT NULL,
    "PCOMISS" numeric NOT NULL,
    "PDESCTO1" numeric NOT NULL,
    "PCOMFXA1" numeric NOT NULL,
    "PDESCTO2" numeric NOT NULL,
    "PCOMFXA2" numeric NOT NULL,
    "PDESCTO3" numeric NOT NULL,
    "PCOMFXA3" numeric NOT NULL,
    "PDESCTO4" numeric NOT NULL,
    "PCOMFXA4" numeric NOT NULL,
    CONSTRAINT "COMISSAO_pkey" PRIMARY KEY ("ID")
);

-- Table: CONTATO
CREATE TABLE IF NOT EXISTS public."CONTATO" (
    "ID" integer NOT NULL,
    "CPFCNPJ" character(18) NOT NULL,
    "PESSOA" character(1),
    "TIPODOC" character(3),
    "RG" character(14),
    "UFRG" character(2),
    "INSCRICAO" character(14),
    "INSCMUNICIPIO" character varying(10),
    "CONTRIBUINTE" character(1),
    "CONSUMIDOR" character(1),
    "NOME" character varying(50),
    "RAZAOSOCIAL" character varying(100),
    "RUA" character varying(60),
    "NUMCASA" character varying(5),
    "COMPLEMENTO" character varying(20),
    "BAIRRO" character varying(30),
    "CXPOSTAL" character(6),
    "CEP" character(9),
    "CIDADE" character(60),
    "UF" character(2),
    "FONERES" character(17),
    "FONECOM" character(17),
    "CONTATO_COM" character(30),
    "CELULAR_COM" character(17),
    "CONTATO_FIN" character(30),
    "CELULAR_FIN" character(17),
    "EMAIL" character(100),
    "EMAILNFE" character varying(100),
    "SITE" character(80),
    "DATANASCTO" timestamp without time zone,
    "NOMEPAI" character(40),
    "NOMEMAE" character(40),
    "NOMECONJUGE" character(40),
    "RGCONJUGE" character(14),
    "NASCTOCONJUGE" timestamp without time zone,
    "SEXO" character(1),
    "ECIVIL" character(1),
    "CODPAIS" character varying(5),
    "NOMEPAIS" character varying(50),
    "DATAPRICOMPRA" timestamp without time zone,
    "DATAULTCOMPRA" timestamp without time zone,
    "NUMCOMPRA" integer NOT NULL,
    "VALPRICOMPRA" numeric NOT NULL,
    "VALMAICOMPRA" numeric NOT NULL,
    "VALULTCOMPRA" numeric NOT NULL,
    "LIMICREDITO" numeric NOT NULL,
    "PRAZOMAX" integer,
    "DIAFAT" integer NOT NULL,
    "DATACAD" timestamp without time zone,
    "DATASPC" timestamp without time zone,
    "CONCEITO" character(10),
    "CODTRANSP" character(5),
    "CODATIV" character(5),
    "CODVEN" character(10),
    "CODREG" character(5),
    "CODBAN" character(4),
    "NUMAGE" character(4),
    "CODGRU" character(5),
    "OBS" text,
    "REF_SPC" text,
    "REF_FIN" text,
    "REF_COM" text,
    "REF_PROD" text,
    "FLAGCLIENTE" character(1),
    "FLAGFORNECEDOR" character(1),
    "FLAGTRANSPOTADOR" character(1),
    "FLAGCOLABORADOR" character(1),
    "FLAGVENDEDOR" character(1),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    "ID_CIDADE" integer,
    "ID_AREA" integer,
    "ID_REGIAO" integer,
    "ID_VENDEDOR" integer,
    "ID_ATIVIDADE" integer,
    "ID_CLIENTE_OLIST" integer,
    CONSTRAINT "CONTATO_pkey" PRIMARY KEY ("ID")
);

-- Table: CONTATO_EMAIL
CREATE TABLE IF NOT EXISTS public."CONTATO_EMAIL" (
    "ID" integer NOT NULL,
    "ID_CONTATO" integer NOT NULL,
    "TIPO" character varying(50) NOT NULL,
    "EMAIL" character varying(100) NOT NULL,
    "ATIVO" character(1),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "CONTATO_EMAIL_pkey" PRIMARY KEY ("ID")
);

-- Table: CONTATO_ENDERECO
CREATE TABLE IF NOT EXISTS public."CONTATO_ENDERECO" (
    "ID" integer NOT NULL,
    "ID_CONTATO" integer NOT NULL,
    "TIPO" character(1),
    "RUA" character varying(80),
    "NUMCASA" character varying(5),
    "COMPLEMENTO" character varying(20),
    "BAIRRO" character varying(60),
    "CEP" character varying(9),
    "CIDADE" character(60),
    "UF" character(2),
    "FONE" character(17),
    "FAX" character(17),
    "CELULAR" character(17),
    "CXPOSTAL" character(6),
    "CONTATO" character(20),
    "E_MAIL" character varying(80),
    "INSCRICAO" character(14),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "CONTATO_ENDERECO_pkey" PRIMARY KEY ("ID")
);

-- Table: CONTATO_INFO
CREATE TABLE IF NOT EXISTS public."CONTATO_INFO" (
    "ID" integer NOT NULL,
    "ID_CONTATO" integer NOT NULL,
    "DATAINF" timestamp without time zone NOT NULL,
    "TIPO" character varying(50),
    "DESCRICAO" bytea,
    "ATIVO" character(1),
    "USERCAD" character(10),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "CONTATO_INFO_pkey" PRIMARY KEY ("ID")
);

-- Table: CONTRATO
CREATE TABLE IF NOT EXISTS public."CONTRATO" (
    "ID" integer NOT NULL,
    "CODEMP" character(3) NOT NULL,
    "NUMCTR" integer NOT NULL,
    "CPFCGC" character(18) NOT NULL,
    "CODVEN" character(5),
    "CODPLANO" integer NOT NULL,
    "DATACON" timestamp without time zone,
    "DATAVEN" timestamp without time zone,
    "QUANT" integer NOT NULL,
    "VALOR" numeric NOT NULL,
    "TEXTO" text,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "CONTRATO_pkey" PRIMARY KEY ("ID")
);

-- Table: DEPTO
CREATE TABLE IF NOT EXISTS public."DEPTO" (
    "ID" integer NOT NULL,
    "CODDEP" character varying(10) NOT NULL,
    "DESCRICAO" character varying(50),
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "DEPTO_pkey" PRIMARY KEY ("ID")
);

-- Table: DESENHO
CREATE TABLE IF NOT EXISTS public."DESENHO" (
    "ID" integer NOT NULL,
    "CODIGO" character varying(10) NOT NULL,
    "DESCRICAO" character varying(50),
    "TIPO" character(1),
    "LARGURA" character varying(3),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "DESENHO_pkey" PRIMARY KEY ("ID")
);

-- Table: DESPVENDEDOR
CREATE TABLE IF NOT EXISTS public."DESPVENDEDOR" (
    "ID" integer NOT NULL,
    "ID_VENDEDOR" integer NOT NULL,
    "ID_VEICULO" integer NOT NULL,
    "DESCRICAO" character varying(200),
    "CODVEN" character varying(10),
    "PLACA" character varying(10),
    "DATA" timestamp without time zone,
    "TIPO" character varying(10),
    "QLITRO" numeric,
    "VLITRO" numeric,
    "VRTOT" numeric,
    "KMANTER" integer,
    "KMATUAL" integer,
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "DESPVENDEDOR_pkey" PRIMARY KEY ("ID")
);

-- Table: EMPRESA
CREATE TABLE IF NOT EXISTS public."EMPRESA" (
    "ID" integer NOT NULL,
    "CODEMP" character(3) NOT NULL,
    "CNPJ" character(18),
    "NOMEFANTASIA" character varying(50),
    "RAZAOSOCIAL" character varying(100),
    "ENDERECO" character(60),
    "NUMCASA" character(10),
    "BAIRRO" character(30),
    "CEP" character(9),
    "CIDADE" character(60),
    "UF" character(2),
    "INSCRICAO" character(15),
    "TELEFONE" character(17),
    "CXPOSTAL" character(6),
    "EMAIL" character(80),
    "INSCMUNICIPIO" character(12),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    "IDCLIENT" character varying(255),
    "IDSECRET" character varying(255),
    "CODAUTH2" character varying(255),
    "TOKEN" character varying(8000),
    CONSTRAINT "EMPRESA_pkey" PRIMARY KEY ("ID")
);

-- Table: ESTADO
CREATE TABLE IF NOT EXISTS public."ESTADO" (
    "ID" integer NOT NULL,
    "SIGLA" character(2) NOT NULL,
    "NOME" character(30) NOT NULL,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "ESTADO_pkey" PRIMARY KEY ("ID")
);

-- Table: EXPEDICAO
CREATE TABLE IF NOT EXISTS public."EXPEDICAO" (
    "ID" integer NOT NULL,
    "ID_PNEU" integer NOT NULL,
    "ID_OS" integer NOT NULL,
    "DATA" timestamp without time zone,
    "HORA" character(2),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "EXPEDICAO_pkey" PRIMARY KEY ("ID")
);

-- Table: FABRICA
CREATE TABLE IF NOT EXISTS public."FABRICA" (
    "ID" integer NOT NULL,
    "CODFAB" character(5) NOT NULL,
    "DESCRICAO" character(50),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "FABRICA_pkey" PRIMARY KEY ("ID")
);

-- Table: FAIXACOM
CREATE TABLE IF NOT EXISTS public."FAIXACOM" (
    "ID" integer NOT NULL,
    "TIPO" character(10) NOT NULL,
    "GRUCOM" character varying(10) NOT NULL,
    "CODIGO" character varying(20) NOT NULL,
    "PLANTA" character(1) NOT NULL,
    "PCOM0" numeric,
    "PDES1" numeric,
    "PCOM1" numeric,
    "PDES2" numeric,
    "PCOM2" numeric,
    "PDES3" numeric,
    "PCOM3" numeric,
    "PDES4" numeric,
    "PCOM4" numeric,
    "PDES5" numeric,
    "PCOM5" numeric,
    "PCOM9" numeric,
    "ATIVO" character(1),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "FAIXACOM_pkey" PRIMARY KEY ("ID")
);

-- Table: FALHA
CREATE TABLE IF NOT EXISTS public."FALHA" (
    "ID" integer NOT NULL,
    "CODFALHA" integer NOT NULL,
    "DESCRICAO" character varying(50),
    "OBSERVACAO" character varying(250),
    "CODSET" character varying(10),
    "MSG_EMAIL" character varying(250),
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "FALHA_pkey" PRIMARY KEY ("ID")
);

-- Table: FICHA_TECNICA
CREATE TABLE IF NOT EXISTS public."FICHA_TECNICA" (
    "ID" integer NOT NULL,
    "ID_SERVICO" integer NOT NULL,
    "ID_FICHAPADRAO" integer NOT NULL,
    "CODTABSERV" character varying(30) NOT NULL,
    "CODPROD" character(20) NOT NULL,
    "QUANTMP" numeric,
    "VALOR" numeric,
    "FATOR" numeric,
    "ORDEM" integer NOT NULL,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "FICHA_TECNICA_pkey" PRIMARY KEY ("ID")
);

-- Table: FICHJA_PADRAO
CREATE TABLE IF NOT EXISTS public."FICHJA_PADRAO" (
    "ID" integer NOT NULL,
    "CODTABSERV" character varying(30) NOT NULL,
    "PISO" character(3) NOT NULL,
    "CODPROD" character(20) NOT NULL,
    "QUANTMP" numeric,
    "VALOR" numeric,
    "FATOR" numeric,
    "ORDEM" integer NOT NULL,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "FICHJA_PADRAO_pkey" PRIMARY KEY ("ID")
);

-- Table: GARANTIA
CREATE TABLE IF NOT EXISTS public."GARANTIA" (
    "ID" integer NOT NULL,
    "ID_PNEU" integer NOT NULL,
    "NUMLAUDO" integer NOT NULL,
    "DATASOL" timestamp without time zone NOT NULL,
    "CODEMP" character varying(3) NOT NULL,
    "NUMOS" integer NOT NULL,
    "SEQOS" integer NOT NULL,
    "CPFCNPJ" character(18),
    "CODREG" character(3),
    "CODVEN" character(5),
    "CODSERVICO" character(5),
    "MEDIDA" character(10),
    "DESENHO" character(6),
    "CODSERV" character(3),
    "MARCA" character(5),
    "DOT" character varying(15),
    "NUMSERIE" character(20),
    "NUMFOGO" character(10),
    "DORIGINAL" character(6),
    "VALOR" numeric NOT NULL,
    "BORRACHA" character(2),
    "CARCACA" character(1),
    "QREFORMA" integer NOT NULL,
    "PLACA" character varying(9),
    "USO" character(5),
    "GARANTIA" character varying(1),
    "CODRESP" character(5),
    "ESTADO" character(1),
    "DEFEITO" character(4),
    "CAUSA" character(4),
    "DATAPROD" timestamp without time zone,
    "DATAEXA" timestamp without time zone,
    "RESPGARA" character(5),
    "LAUDO" character varying(1),
    "MOTIVO" character(4),
    "TIPOREPO" character(1),
    "PERCDESG" numeric NOT NULL,
    "PERCREPO" numeric NOT NULL,
    "PERCREFOR" numeric NOT NULL,
    "SERVREPO" character(3),
    "VALREP" numeric NOT NULL,
    "PISO" character varying(10),
    "NOTAREP" integer,
    "STATREP" character(1),
    "DATAREP" timestamp without time zone,
    "QREMANE" numeric,
    "ALEGACAO" bytea,
    "EXAMINADOR" character varying(30),
    "LAUDOFAB" integer NOT NULL,
    "PROFUNDIDADE" numeric,
    "SERIENF" character(3),
    "NUMNOTA" integer NOT NULL,
    "DATAFAT" timestamp without time zone,
    "USEREXA" character(10),
    "DATARESUL" timestamp without time zone,
    "PCOMSERV" numeric,
    "OBS2" bytea,
    "DATABXA" timestamp without time zone,
    "DOCBXA" character varying(20),
    "STATUS" character(1),
    "OBS" bytea,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "GARANTIA_pkey" PRIMARY KEY ("ID")
);

-- Table: GRUPO_CONTATO
CREATE TABLE IF NOT EXISTS public."GRUPO_CONTATO" (
    "ID" integer NOT NULL,
    "CODGRU" character(5) NOT NULL,
    "DESCRICAO" character(20),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "GRUPO_CONTATO_pkey" PRIMARY KEY ("ID")
);

-- Table: GRUPO_PRODUTO
CREATE TABLE IF NOT EXISTS public."GRUPO_PRODUTO" (
    "ID" integer NOT NULL,
    "CODGRU" character(5) NOT NULL,
    "DESCRICAO" character(30),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "GRUPO_PRODUTO_pkey" PRIMARY KEY ("ID")
);

-- Table: LOGERRO
CREATE TABLE IF NOT EXISTS public."LOGERRO" (
    "ID" integer NOT NULL,
    "MENSAGEM" text,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "LOGERRO_pkey" PRIMARY KEY ("ID")
);

-- Table: LOGSIS
CREATE TABLE IF NOT EXISTS public."LOGSIS" (
    "ID" integer NOT NULL,
    "MENSAGEM" text,
    "DATALAN" timestamp without time zone NOT NULL,
    "USERLAN" character(10),
    CONSTRAINT "LOGSIS_pkey" PRIMARY KEY ("ID")
);

-- Table: MAQUINA
CREATE TABLE IF NOT EXISTS public."MAQUINA" (
    "ID" integer NOT NULL,
    "CODMAQ" integer NOT NULL,
    "DESCRICAO" character varying(50),
    "ATIVO" character(1),
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "MAQUINA_pkey" PRIMARY KEY ("ID")
);

-- Table: MARCA
CREATE TABLE IF NOT EXISTS public."MARCA" (
    "ID" integer NOT NULL,
    "CODIGO" character(5) NOT NULL,
    "DESCRICAO" character(50) NOT NULL,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "MARCA_pkey" PRIMARY KEY ("ID")
);

-- Table: MEDIDA
CREATE TABLE IF NOT EXISTS public."MEDIDA" (
    "ID" integer NOT NULL,
    "CODIGO" character(15) NOT NULL,
    "DESCRICAO" character(50),
    "TIPO" character(5),
    "DATACAD" timestamp without time zone,
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "MEDIDA_pkey" PRIMARY KEY ("ID")
);

-- Table: MOBOS
CREATE TABLE IF NOT EXISTS public."MOBOS" (
    "ID" integer NOT NULL,
    "CODVEN" character(5) NOT NULL,
    "NUMMOB" integer NOT NULL,
    "DATAOS" timestamp without time zone,
    "CPFCGC" character varying(18),
    "INSCRICAO" character(14),
    "NOME" character varying(100),
    "RUA" character varying(80),
    "NUMCASA" character varying(5),
    "COMPLEMENTO" character varying(20),
    "BAIRRO" character varying(60),
    "CEP" character varying(9),
    "CIDADE" character(60),
    "UF" character(2),
    "FONE" character(17),
    "CELULAR" character(17),
    "CONTATO" character(20),
    "E_MAIL" character varying(80),
    "VTOTAL" numeric NOT NULL,
    "QPNEU" integer NOT NULL,
    "MSGMOB" text,
    "CODEMP" character(3),
    "NUMOS" integer,
    "STATUS" character(1),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "MOBOS_pkey" PRIMARY KEY ("ID")
);

-- Table: MOBPNEU
CREATE TABLE IF NOT EXISTS public."MOBPNEU" (
    "ID" integer NOT NULL,
    "ID_MOBOS" integer NOT NULL,
    "CODVEN" character(5) NOT NULL,
    "NUMMOB" integer NOT NULL,
    "SEQMOB" integer NOT NULL,
    "CODTABSERV" character varying(20),
    "CODSERV" character varying(10),
    "MEDIDA" character varying(10),
    "DEXECUTAR" character varying(12),
    "PISO" character varying(10),
    "QREFORMA" integer NOT NULL,
    "VALOR" numeric NOT NULL,
    "MARCA" character(2),
    "NUMSERIE" character(20),
    "NUMFOGO" character varying(10),
    "DOT" character varying(15),
    "DORIGINAL" character varying(12),
    "USO" character(5),
    "GARANTIA" character varying(1),
    "OBS" character varying(80),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "MOBPNEU_pkey" PRIMARY KEY ("ID")
);

-- Table: NOTAFISCAL
CREATE TABLE IF NOT EXISTS public."NOTAFISCAL" (
    "ID" integer NOT NULL,
    "ID_CONTATO" integer NOT NULL,
    "ID_TRANSPO" integer NOT NULL,
    "CODEMP" character(3) NOT NULL,
    "CNPJEMP" character(18),
    "NUMFAT" character(10),
    "SERIENF" character(3),
    "NUMNOTA" integer NOT NULL,
    "CPFCNPJ" character(18),
    "ENDENT" integer NOT NULL,
    "ENDCOB" integer NOT NULL,
    "TIPOCLI" character(1),
    "TIPOFAT" integer NOT NULL,
    "DATAEMI" timestamp without time zone,
    "DATAMOV" timestamp without time zone,
    "CODMSG" integer NOT NULL,
    "PLANOPAG" integer NOT NULL,
    "CODREG" character(3),
    "CODVEN" character(5),
    "CODBAN" character(4),
    "NUMAGE" character(4),
    "CODTRANSP" character(5),
    "CGCTRANSP" character(18),
    "NUMCONHEC" integer NOT NULL,
    "VALFRETE" numeric NOT NULL,
    "VICMFRETE" numeric NOT NULL,
    "VALPROD" numeric NOT NULL,
    "VALSERV" numeric NOT NULL,
    "VTABPROD" numeric NOT NULL,
    "VTABSERV" numeric NOT NULL,
    "VDESCTO" numeric NOT NULL,
    "VALLIVR" numeric NOT NULL,
    "TOTALFAT" numeric NOT NULL,
    "BASEISS" numeric NOT NULL,
    "BASEIPI" numeric NOT NULL,
    "VISENTO" numeric NOT NULL,
    "VOUTRAS" numeric NOT NULL,
    "VRICM" numeric NOT NULL,
    "VRIPI" numeric NOT NULL,
    "VRISS" numeric NOT NULL,
    "VCUSTOCTB" numeric NOT NULL,
    "VCUSTOGER" numeric NOT NULL,
    "VIR" numeric NOT NULL,
    "VPIS" numeric NOT NULL,
    "VCOFIN" numeric NOT NULL,
    "VVISTA" numeric NOT NULL,
    "VPRAZO" numeric NOT NULL,
    "VBONUS" numeric NOT NULL,
    "VCARCA" numeric NOT NULL,
    "VLAUDO" numeric NOT NULL,
    "VREQUI" numeric NOT NULL,
    "CNPJREQ" character(18),
    "PZMEDIO" numeric NOT NULL,
    "ALIQISS" numeric NOT NULL,
    "PCOMSERV" numeric NOT NULL,
    "PCOMPROD" numeric NOT NULL,
    "QTMERC" integer NOT NULL,
    "ESPECIE" character(10),
    "MARCA" character(10),
    "NUMIDENT" character(6),
    "PESOBRU" numeric NOT NULL,
    "PESOLIQ" numeric NOT NULL,
    "STATUS" character(1),
    "MSG_NF" text,
    "OBS_FAT" text,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "CANHOTO" character(1),
    "DATADIG" timestamp without time zone,
    "CONSUMIDOR" character(1),
    "CONTRIB" character(1),
    "DHIST" character(3),
    "DOCORIGEM" integer,
    "DTORIGEM" timestamp without time zone,
    "NFORIGEM" integer,
    "SEORIGEM" character(3),
    "STATNFE" character(3),
    "TIPOFRETE" character(1),
    "UFDEST" character(2),
    "UFORIG" character(2),
    "VALNOTA" numeric,
    "MOTIVOLIB" text,
    "USERLIB" character varying(10),
    "DATALIB" timestamp without time zone,
    "NUMCTR" integer,
    "NUMOS" integer,
    "TIPODIV" character(2),
    "CHAVENFE" character varying(44),
    "SERIERPS" character(3),
    "NUMRPS" integer,
    "LOTERPS" integer,
    "PROTOCOLO" character varying(20),
    "VDESCNF" numeric,
    "DATACANHOTO" timestamp without time zone,
    "CODVERIF" character varying(50),
    "STATLIB" character(1),
    "CODHIST" character varying(10),
    "PRODUTO" character varying(4),
    "ID_OS_OLIST" integer,
    CONSTRAINT "NOTAFISCAL_pkey" PRIMARY KEY ("ID")
);

-- Table: NOTA_PARCELA
CREATE TABLE IF NOT EXISTS public."NOTA_PARCELA" (
    "ID" integer NOT NULL,
    "ID_NOTA" integer NOT NULL,
    "CODEMP" character(3) NOT NULL,
    "TIPODOCTO" character(3) NOT NULL,
    "NUMDOCTO" character(15) NOT NULL,
    "NUMFAT" character(10),
    "EMISSAO" timestamp without time zone,
    "VENCTO" timestamp without time zone,
    "VRFAT" numeric NOT NULL,
    "VALOR" numeric NOT NULL,
    "VPAGO" numeric NOT NULL,
    "VALDOCTO" numeric,
    "VTERC" numeric NOT NULL,
    "VBONUS" numeric NOT NULL,
    "CPFCNPJ" character(18),
    "CODVEN" character(5),
    "CODBAN" character(4),
    "NUMAGE" character(4),
    "CODOPER" integer NOT NULL,
    "CODCLASS" character(20),
    "CODREP" character(5),
    "CODREG" character(3),
    "PERCCOM" numeric NOT NULL,
    "VCOMISS" numeric NOT NULL,
    "ENDCOB" integer NOT NULL,
    "CODCOB" character(5),
    "STATFAT" character(1),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "SERIENF" character(3),
    "NUMNOTA" integer,
    "BANCOCH" character varying(3),
    "AGENCIACH" character varying(4),
    "CONTACH" character varying(10),
    "NUMCHEQUE" character varying(20),
    "CPFCNPJCH" character(18),
    "EMITENTECH" character varying(80),
    "DATAEMICH" timestamp without time zone,
    CONSTRAINT "NOTA_PARCELA_pkey" PRIMARY KEY ("ID")
);

-- Table: NOTA_SERVICO
CREATE TABLE IF NOT EXISTS public."NOTA_SERVICO" (
    "ID" integer NOT NULL,
    "ID_NOTA" integer NOT NULL,
    "CODEMP" character(3) NOT NULL,
    "ID_ORIGEM" character(3) NOT NULL,
    "ID_NUMERO" integer NOT NULL,
    "ID_SEQLAN" integer NOT NULL,
    "CODSERV" character(15),
    "DESCRICAO" character(255),
    "CODSIT" character(3),
    "ALIQDESC" numeric NOT NULL,
    "ALIQICM" numeric NOT NULL,
    "BASEICM" numeric NOT NULL,
    "VISENTO" numeric NOT NULL,
    "VOUTRAS" numeric NOT NULL,
    "QUANT" numeric NOT NULL,
    "VRTAB" numeric NOT NULL,
    "VDESC" numeric NOT NULL,
    "VALOR" numeric NOT NULL,
    "VRTOT" numeric NOT NULL,
    "VRICM" numeric NOT NULL,
    "VRISS" numeric NOT NULL,
    "DATALAN" timestamp without time zone,
    "CODCFO" character(5),
    "BASEISS" numeric,
    "VDESCNF" numeric,
    "PCOMSERV" numeric,
    CONSTRAINT "NOTA_SERVICO_pkey" PRIMARY KEY ("ID")
);

-- Table: OPERADOR
CREATE TABLE IF NOT EXISTS public."OPERADOR" (
    "ID" integer NOT NULL,
    "CODFUN" character(20) NOT NULL,
    "NOME" character(80),
    "CARGO" character varying(10),
    "CODSET" character varying(10),
    "CODDEP" character varying(10),
    "QMETA" integer,
    "VALOR" numeric,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    "ID_DEPTO" integer NOT NULL,
    "ID_SETOR" integer NOT NULL,
    CONSTRAINT "OPERADOR_pkey" PRIMARY KEY ("ID")
);

-- Table: ORCAM
CREATE TABLE IF NOT EXISTS public."ORCAM" (
    "ID" integer NOT NULL,
    "NUMORC" integer NOT NULL,
    "CPFCNPJ" character(18) NOT NULL,
    "NOME" character(100),
    "RUA" character(80),
    "COMPLEMENTO" character(30),
    "BAIRRO" character(30),
    "CXPOSTAL" character(6),
    "CEP" character(9),
    "CIDADE" character(60),
    "UF" character(2),
    "FONERES" character(17),
    "FONECOM" character(17),
    "FAX" character(17),
    "CONTATO" character(30),
    "CELULAR" character(17),
    "EMAIL1" character varying(80),
    "EMAIL2" character varying(80),
    "DATAORC" timestamp without time zone,
    "VDESCTO" numeric,
    "VALORC" numeric,
    "CODVEN" character(5),
    "VALIDADE" character varying(50),
    "CONDICAO" text,
    "OBS" text,
    "NOMERESP" character varying(50),
    "FONERESP" character varying(50),
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "ORCAM_pkey" PRIMARY KEY ("ID")
);

-- Table: ORCITEM
CREATE TABLE IF NOT EXISTS public."ORCITEM" (
    "ID" integer NOT NULL,
    "ID_ORC" integer NOT NULL,
    "NUMOS" integer NOT NULL,
    "SEQOS" integer NOT NULL,
    "MEDIDA" character varying(20),
    "MARCA" character varying(10),
    "SERVICO" character varying(10),
    "DESENHO" character varying(20),
    "NUMFOGO" character varying(10),
    "DOT" character varying(5),
    "DESCRICAO" character varying(150),
    "QUANT" numeric,
    "VALOR" numeric,
    "VRTOT" numeric,
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "ORCITEM_pkey" PRIMARY KEY ("ID")
);

-- Table: OS
CREATE TABLE IF NOT EXISTS public."OS" (
    "ID" integer NOT NULL,
    "CODEMP" character(3) NOT NULL,
    "NUMOS" integer NOT NULL,
    "TIPOFAT" integer NOT NULL,
    "NUMCTR" integer NOT NULL,
    "CPFCGC" character(18),
    "ENDENT" integer NOT NULL,
    "ENDCOB" integer NOT NULL,
    "DIASPRE" integer NOT NULL,
    "DATAOS" timestamp without time zone,
    "DATAPRE" timestamp without time zone,
    "DATAFAT" timestamp without time zone,
    "DATAENT" timestamp without time zone,
    "NOTAENT" integer,
    "FRETE" character(1),
    "CODTRANSP" character(5),
    "UNIPRO" character(3),
    "CODVEN" character(5),
    "CODBAN" character(4),
    "NUMAGE" character(4),
    "CODCFO" character(5),
    "CODMSG" integer NOT NULL,
    "CODPLANO" integer NOT NULL,
    "VALPROD" numeric NOT NULL,
    "VALSERV" numeric NOT NULL,
    "VALLIVR" numeric NOT NULL,
    "VBONUS" numeric NOT NULL,
    "VCARCA" numeric NOT NULL,
    "VCONV" numeric NOT NULL,
    "VREQUI" numeric NOT NULL,
    "VALFRETE" numeric NOT NULL,
    "TOTALFAT" numeric NOT NULL,
    "VDESCPROD" numeric NOT NULL,
    "VDESCSERV" numeric NOT NULL,
    "QBONUS" integer NOT NULL,
    "PDESCPROD" numeric NOT NULL,
    "PDESCSERV" numeric NOT NULL,
    "PCOMSERV" numeric NOT NULL,
    "PCOMPROD" numeric NOT NULL,
    "PLACA" character varying(9),
    "CARCACA" character(1),
    "CGCREQ" character(18),
    "ACABADO" character(1),
    "MSG_NF" text,
    "OBS_FAT" text,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "DOCORIGEM" integer,
    "STATLIB" character(1),
    "DATALIB" timestamp without time zone,
    "USERLIB" character(10),
    "SENHALIB" character(15),
    "MOTIVOLIB" text,
    "SERIENT" character varying(3),
    "EMITNFE" character(1),
    "STATNFE" character(1),
    "NUMMOB" integer,
    "SOMENTEPAR" character(1),
    "MUDARDESENHO" character varying(50),
    "FORMAPG" character varying(10),
    "UNIFAT" character(3),
    "DATADIG" timestamp without time zone,
    "USERETIQ" character varying(10),
    "BORRACHEIRO" character varying(100),
    "VSERV" numeric,
    "PLANTA" character(1),
    "STATUS" character(1),
    CONSTRAINT "OS_pkey" PRIMARY KEY ("ID")
);

-- Table: PARAMETRO
CREATE TABLE IF NOT EXISTS public."PARAMETRO" (
    "ID" integer NOT NULL,
    "CODPARAM" character(20) NOT NULL,
    "DESCRICAO" character varying(100),
    "VALOR" numeric,
    "REFERENCIA" character varying(50),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "PARAMETRO_pkey" PRIMARY KEY ("ID")
);

-- Table: PLANOPAG
CREATE TABLE IF NOT EXISTS public."PLANOPAG" (
    "ID" integer NOT NULL,
    "CODPLANO" integer NOT NULL,
    "FORMAPAG" character(60),
    "NUMPARC" integer NOT NULL,
    "ACRESCIMO" numeric NOT NULL,
    "DESCONTO" numeric NOT NULL,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    "DATACAD" timestamp without time zone,
    "MOBILE" character(1),
    CONSTRAINT "PLANOPAG_pkey" PRIMARY KEY ("ID")
);

-- Table: PNEU
CREATE TABLE IF NOT EXISTS public."PNEU" (
    "ID" integer NOT NULL,
    "ID_OS" integer NOT NULL,
    "ID_NOTA" integer NOT NULL,
    "ID_CONTATO" integer NOT NULL,
    "CODEMP" character varying(3) NOT NULL,
    "NUMOS" integer NOT NULL,
    "SEQOS" integer NOT NULL,
    "CODBARRA" character varying(15),
    "NUMNOTA" integer NOT NULL,
    "CPFCNPJ" character(18),
    "NUMCTR" integer NOT NULL,
    "CODBON" character(3),
    "DATAOS" timestamp without time zone,
    "DATAPRE" timestamp without time zone,
    "DATAPRO" timestamp without time zone,
    "DATAFAT" timestamp without time zone,
    "MEDIDA" character varying(10),
    "DESENHO" character varying(12),
    "TIPOSERV" character varying(5),
    "PISO" character varying(10),
    "CODSERVICO" character varying(30),
    "MARCA" character(3),
    "NUMSERIE" character(20),
    "NUMFOGO" character varying(10),
    "DOT" character varying(15),
    "PLACA" character varying(9),
    "DORIGINAL" character varying(12),
    "QREFORMA" integer NOT NULL,
    "QUANT" integer NOT NULL,
    "VALOR" numeric NOT NULL,
    "VRTOT" numeric NOT NULL,
    "VTABSRV" numeric NOT NULL,
    "PDESCTO" numeric NOT NULL,
    "VCARCA" numeric NOT NULL,
    "VCUSTMP" numeric NOT NULL,
    "VCUSTODESP" numeric NOT NULL,
    "CAUSAREC" character varying(11) NOT NULL,
    "USO" character(5),
    "GARANTIA" character varying(1),
    "CODRESP" character(5),
    "ESTADO" character(2),
    "PRAZO" numeric NOT NULL,
    "STATPRO" character varying(1),
    "STATFAT" character varying(1),
    "OBS" character varying(80),
    "VALNFE" numeric,
    "CODCARCACA" character varying(20),
    "CODACABADO" character varying(20),
    "REFMASTER" character(1),
    "DOTSRV" character varying(15),
    "DATAEXP" timestamp without time zone,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ID_LAUDO" character(3),
    "ID_EXPED" integer,
    "ID_MEDIDA" integer NOT NULL,
    "ID_DESENHO" integer NOT NULL,
    "ID_MARCA" integer NOT NULL,
    CONSTRAINT "PNEU_pkey" PRIMARY KEY ("ID")
);

-- Table: PNEU_FALHA
CREATE TABLE IF NOT EXISTS public."PNEU_FALHA" (
    "ID" integer NOT NULL,
    "ID_PNEU" integer NOT NULL,
    "CODEMP" character varying(10) NOT NULL,
    "NUMOS" integer NOT NULL,
    "SEQOS" integer NOT NULL,
    "CODFALHA" integer NOT NULL,
    "CODSET" character varying(10) NOT NULL,
    "CODFUN" character varying(10) NOT NULL,
    "MOTIVO" character varying(255),
    "DATA" timestamp without time zone,
    "VALOR" numeric,
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "PNEU_FALHA_pkey" PRIMARY KEY ("ID")
);

-- Table: PNEU_MPRIMA
CREATE TABLE IF NOT EXISTS public."PNEU_MPRIMA" (
    "ID" integer NOT NULL,
    "ID_PNEU" integer NOT NULL,
    "ID_PRODUTO" integer NOT NULL,
    "QUANT" numeric,
    "VALOR" numeric,
    "VTOTAL" numeric,
    "CODEMP" character varying(10) NOT NULL,
    "NUMOS" integer NOT NULL,
    "SEQOS" integer NOT NULL,
    "SEQSRV" integer NOT NULL,
    "CODPROD" character varying(20) NOT NULL,
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "PNEU_MPRIMA_pkey" PRIMARY KEY ("ID")
);

-- Table: PNEU_SERVICO
CREATE TABLE IF NOT EXISTS public."PNEU_SERVICO" (
    "ID" integer NOT NULL,
    "ID_PNEU" integer NOT NULL,
    "ID_SERVICO" integer NOT NULL,
    "ID_NOTA" integer NOT NULL,
    "CODEMP" character varying(3) NOT NULL,
    "NUMOS" integer NOT NULL,
    "SEQOS" integer NOT NULL,
    "SEQSRV" integer NOT NULL,
    "CODSERVICO" character varying(30) NOT NULL,
    "PISO" character varying(3) NOT NULL,
    "QUANT" integer NOT NULL,
    "VALOR" numeric NOT NULL,
    "VRTOT" numeric NOT NULL,
    "VRTAB" numeric NOT NULL,
    "PZMEDIO" numeric NOT NULL,
    "PDESCTO" numeric NOT NULL,
    "PCOMISS" numeric NOT NULL,
    "CUSTOCTB" numeric NOT NULL,
    "CUSTOGER" numeric NOT NULL,
    "NUMTAB" character varying(10),
    "STATPRO" character(1),
    "DATAPRO" timestamp without time zone,
    "DATAFAT" timestamp without time zone,
    "SERIENF" character varying(5),
    "NUMNOTA" integer,
    "CPFCGC" character varying(18),
    "UNIPRO" character(3),
    "MEDIDA" character varying(20),
    "DESENHO" character varying(20),
    "TIPOSERV" character varying(5),
    "CODVEN" character varying(5),
    "CODREG" character varying(5),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "PNEU_SERVICO_pkey" PRIMARY KEY ("ID")
);

-- Table: PRECOCLI
CREATE TABLE IF NOT EXISTS public."PRECOCLI" (
    "ID" integer NOT NULL,
    "CPFCGC" character(18) NOT NULL,
    "CODEMP" character(3) NOT NULL,
    "NUMCTR" integer NOT NULL,
    "NUMTAB" character(18),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    "PCOM1" numeric,
    "PCOM2" numeric,
    "PCOM3" numeric,
    "PCOM4" numeric,
    "PCOM5" numeric,
    CONSTRAINT "PRECOCLI_pkey" PRIMARY KEY ("ID")
);

-- Table: PRECOCOM
CREATE TABLE IF NOT EXISTS public."PRECOCOM" (
    "ID" integer NOT NULL,
    "NUMTAB" character varying(10) NOT NULL,
    "ID_SERVICO" integer NOT NULL,
    "PCOM0" numeric,
    "PDES1" numeric,
    "PCOM1" numeric,
    "PDES2" numeric,
    "PCOM2" numeric,
    "PDES3" numeric,
    "PCOM3" numeric,
    "PDES4" numeric,
    "PCOM4" numeric,
    "PDES5" numeric,
    "PCOM5" numeric,
    "PCOM9" numeric,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "PRECOCOM_pkey" PRIMARY KEY ("ID")
);

-- Table: PRECOTAB
CREATE TABLE IF NOT EXISTS public."PRECOTAB" (
    "ID" integer NOT NULL,
    "NUMTAB" character varying(20) NOT NULL,
    "DESCRICAO" character varying(100),
    "INIVALIDADE" timestamp without time zone,
    "FIMVALIDADE" timestamp without time zone,
    "MSG" text,
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "PRECOTAB_pkey" PRIMARY KEY ("ID")
);

-- Table: PRECO_SERVICO
CREATE TABLE IF NOT EXISTS public."PRECO_SERVICO" (
    "ID" integer NOT NULL,
    "ID_TABPRECO" integer NOT NULL,
    "NUMTAB" character varying(20) NOT NULL,
    "SEQTAB" integer NOT NULL,
    "CODSERVICO" character varying(30) NOT NULL,
    "TIPOSERV" character varying(5) NOT NULL,
    "MEDIDA" character varying(20) NOT NULL,
    "DESENHO" character varying(20) NOT NULL,
    "PISO" character varying(5) NOT NULL,
    "VALOR" numeric,
    "MINIMO" numeric,
    "CODGRU" character varying(10),
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    "DATACAD" timestamp without time zone,
    CONSTRAINT "PRECO_SERVICO_pkey" PRIMARY KEY ("ID")
);

-- Table: PRODUCAO
CREATE TABLE IF NOT EXISTS public."PRODUCAO" (
    "ID" integer NOT NULL,
    "ID_PNEU" integer NOT NULL,
    "ID_SETOR" integer NOT NULL,
    "CODBARRA" character varying(30) NOT NULL,
    "CODRETRAB" integer NOT NULL,
    "CODEMP" character varying(10) NOT NULL,
    "NUMOS" integer NOT NULL,
    "SEQOS" integer NOT NULL,
    "CODSET" character varying(10) NOT NULL,
    "CODFUN" character varying(10),
    "SEQFAB" integer,
    "STATUS" character(1),
    "TIPOSERV" character varying(5),
    "DESENHO" character varying(20),
    "PISO" character(3),
    "CODMAQ" integer,
    "DATAINI" timestamp without time zone,
    "DATAFIM" timestamp without time zone,
    "DATAPRO" timestamp without time zone,
    "TEMPO" numeric,
    "ESTADO" character(1),
    "GARANTIA" character(1),
    "MASTER" character(1),
    "CODRESP" character varying(5),
    "CAUSAREC" character varying(11),
    "RESULTADO" character(1),
    "RAIO" numeric,
    "PERIMETRO" numeric,
    "CODCARCACA" character varying(20),
    "CODACABADO" character varying(20),
    "ENVELOPE" integer,
    "INNLOP" integer,
    "SACOAR" integer,
    "PROTETOR" integer,
    "BICO" integer,
    "CICLO" integer,
    "ESTCARCA" character varying(5),
    "TEXTURA" character(1),
    "VALTRAB" numeric,
    "OBS" character varying(100),
    "PROXSET" character varying(10),
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "PRODUCAO_pkey" PRIMARY KEY ("ID")
);

-- Table: PRODUTO
CREATE TABLE IF NOT EXISTS public."PRODUTO" (
    "ID" integer NOT NULL,
    "CODPROD" character(20) NOT NULL,
    "CODATUAL" character(20),
    "CODANTER" character(20),
    "NUMFAB" character(20),
    "DESCRICAO" character(100),
    "CODGRU" character(5),
    "CODSUB" character(5),
    "CODFAB" character(5),
    "UNIDADE" character(2),
    "EMBALAG" character(10),
    "QVOLUME" numeric NOT NULL,
    "PESOBRU" numeric NOT NULL,
    "PESOLIQ" numeric NOT NULL,
    "PCOMPRA" timestamp without time zone,
    "UCOMPRA" timestamp without time zone,
    "PVENDA" timestamp without time zone,
    "UVENDA" timestamp without time zone,
    "UATPRECO" timestamp without time zone,
    "GRUDESCTO" character varying(1),
    "PRECOVEN" numeric NOT NULL,
    "PRECOREP" numeric NOT NULL,
    "ABCDEM" character(1),
    "ABCVAL" character(1),
    "CLASSEICM" character varying(10),
    "CODCEST" character varying(8),
    "CODGTIN" character varying(14),
    "IMAGEM" character(100),
    "DESTINO" character(1),
    "TIPO" character(1),
    "ATIVO" character(1),
    "DATACAD" timestamp without time zone,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "DATASUB" timestamp without time zone,
    "DATAPRO" timestamp without time zone,
    "DATAVAL" timestamp without time zone,
    "PROMOCAO" character(1),
    "PRECOPRO" numeric NOT NULL,
    "MARGEM" numeric NOT NULL,
    "MINIMO" numeric NOT NULL,
    "MAXIMO" numeric NOT NULL,
    "CODNCM" character varying(8),
    "PESOMT" numeric,
    "CODTABSERV" character varying(30),
    "IPICENQ" character varying(3),
    "ID_PRODUTO_OLIST" integer,
    CONSTRAINT "PRODUTO_pkey" PRIMARY KEY ("ID")
);

-- Table: REGIAO
CREATE TABLE IF NOT EXISTS public."REGIAO" (
    "ID" integer NOT NULL,
    "CODREG" character(3) NOT NULL,
    "NOME" character(50),
    "ID_AREA" integer,
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "DATACAD" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "REGIAO_pkey" PRIMARY KEY ("ID")
);

-- Table: SERVICO
CREATE TABLE IF NOT EXISTS public."SERVICO" (
    "ID" integer NOT NULL,
    "ID_TIPOSERV" integer NOT NULL,
    "ID_MEDIDA" integer NOT NULL,
    "ID_DESENHO" integer NOT NULL,
    "CODSERVICO" character varying(30) NOT NULL,
    "DESCRICAO" character varying(100),
    "MEDIDA" character varying(20),
    "DESENHO" character varying(20),
    "TIPOSERV" character varying(5),
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "SERVICO_pkey" PRIMARY KEY ("ID")
);

-- Table: SETOR
CREATE TABLE IF NOT EXISTS public."SETOR" (
    "ID" integer NOT NULL,
    "CODSET" character varying(10) NOT NULL,
    "DESCRICAO" character varying(50),
    "SEQUENCIA" integer,
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    "TEMPOMEDIO" integer,
    "TEMPOMINIMO" integer,
    "QMETA" integer,
    "ATIVO" character(1),
    "PROXSETOR" character varying(50),
    "SOPASSAGEM" character(1),
    "EXAINICIAL" character(1),
    "EXAFINAL" character(1),
    "FALHA" character(1),
    "AVALIACAO" character(1),
    "CONSUMOMP" character(1),
    "EXPEDICAO" character(1),
    "SUPERVISAO" character(1),
    CONSTRAINT "SETOR_pkey" PRIMARY KEY ("ID")
);

-- Table: SUBGRUPO
CREATE TABLE IF NOT EXISTS public."SUBGRUPO" (
    "ID" integer NOT NULL,
    "CODSUB" character(10) NOT NULL,
    "DESCRICAO" character(30),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "SUBGRUPO_pkey" PRIMARY KEY ("ID")
);

-- Table: TABGERAL
CREATE TABLE IF NOT EXISTS public."TABGERAL" (
    "ID" integer NOT NULL,
    "TIPO" character(3) NOT NULL,
    "CODIGO" character(5) NOT NULL,
    "DESCRICAO" character(50),
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "TABGERAL_pkey" PRIMARY KEY ("ID")
);

-- Table: TIPODOCTO
CREATE TABLE IF NOT EXISTS public."TIPODOCTO" (
    "ID" integer NOT NULL,
    "CODIGO" character(5) NOT NULL,
    "DESCRICAO" character(30),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "TIPODOCTO_pkey" PRIMARY KEY ("ID")
);

-- Table: TIPOOPERACAO
CREATE TABLE IF NOT EXISTS public."TIPOOPERACAO" (
    "ID" integer NOT NULL,
    "CODIGO" integer NOT NULL,
    "SINAL" character(1),
    "DESCRICAO" character(50),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "TIPOOPERACAO_pkey" PRIMARY KEY ("ID")
);

-- Table: TRANSPORTADORA
CREATE TABLE IF NOT EXISTS public."TRANSPORTADORA" (
    "ID" integer NOT NULL,
    "CODIGO" character(10) NOT NULL,
    "NOME" character(50),
    "ENDERECO" character(60),
    "CEP" character(9),
    "CIDADE" character(60),
    "UF" character(2),
    "FONE" character(17),
    "FAX" character(17),
    "CPFCNPJ" character varying(18),
    "INSCRICAO" character(15),
    "PLACAVEIC" character(10),
    "UFPLACA" character(2),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "TRANSPORTADORA_pkey" PRIMARY KEY ("ID")
);

-- Table: USUARIO
CREATE TABLE IF NOT EXISTS public."USUARIO" (
    "ID" integer NOT NULL,
    "CODIGO" character(20) NOT NULL,
    "NOME" character(50),
    "SENHA" character(100),
    "FUNCAO" character(1),
    "GRUPO" character varying(100),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "CODEMP" character(3),
    "ATIVO" character(1),
    "CODVEN" character varying(10),
    "CODFUN" character varying(10),
    "CODSET" character varying(10),
    CONSTRAINT "USUARIO_pkey" PRIMARY KEY ("ID")
);

-- Table: USUARIO_PERMISSAO
CREATE TABLE IF NOT EXISTS public."USUARIO_PERMISSAO" (
    "ID" integer NOT NULL,
    "ID_USUARIO" integer NOT NULL,
    "ROTINA" character varying(100),
    "EXECUTAR" character(1),
    "INCLUIR" character(1),
    "ALTERAR" character(1),
    "EXCLUIR" character(1),
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    CONSTRAINT "USUARIO_PERMISSAO_pkey" PRIMARY KEY ("ID")
);

-- Table: VEICULO
CREATE TABLE IF NOT EXISTS public."VEICULO" (
    "ID" integer NOT NULL,
    "PLACA" character varying(10) NOT NULL,
    "DESCRICAO" character varying(50),
    "CODVEN" character varying(10),
    "GRUPO" character varying(10),
    "TIPO" character(1),
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    "COMB" character varying(10),
    "PLAQUETA" integer,
    "ATIVO" character(1),
    "DATACAD" timestamp without time zone,
    "UF" character(2),
    "CODMOD" character varying(20),
    "RENAVAM" character varying(20),
    "CHASSI" character varying(20),
    "ANO" character varying(5),
    "ALIENADO" character(1),
    "BANCOFIN" character varying(50),
    "SINISTRO" character(1),
    "SEGURADORA" character varying(30),
    "ANTT" character varying(10),
    CONSTRAINT "VEICULO_pkey" PRIMARY KEY ("ID")
);

-- Table: VENDEDOR
CREATE TABLE IF NOT EXISTS public."VENDEDOR" (
    "ID" integer NOT NULL,
    "CODVEN" character(10) NOT NULL,
    "APELIDO" character(50),
    "NOME" character(100),
    "ENDERECO" character(60),
    "CEP" character(9),
    "CIDADE" character(60),
    "UF" character(2),
    "FONE" character(17),
    "FAX" character(17),
    "CPFCNPJ" character(18),
    "INSCRICAO" character(15),
    "CARGO" character(10),
    "CODAREA" character(5),
    "CODREG" character(5),
    "USERLAN" character(10),
    "DATALAN" timestamp without time zone,
    "ATIVO" character(1),
    "VINCULO" character varying(10),
    "ID_AREA" integer,
    "ID_REGIAO" integer,
    "ID_VENDEDOR_OLIST" integer,
    CONSTRAINT "VENDEDOR_pkey" PRIMARY KEY ("ID")
);

-- Table: VENDEDOR_META
CREATE TABLE IF NOT EXISTS public."VENDEDOR_META" (
    "ID" integer NOT NULL,
    "CODVEN" character varying(10) NOT NULL,
    "ANO" integer NOT NULL,
    "MES" integer NOT NULL,
    "VMETAFAT" numeric,
    "VFATREAL" numeric,
    "VMETACOMB" numeric,
    "VCOMBREAL" numeric,
    "USERLAN" character varying(10),
    "DATALAN" timestamp without time zone,
    CONSTRAINT "VENDEDOR_META_pkey" PRIMARY KEY ("ID")
);

-- Table: area
CREATE TABLE IF NOT EXISTS public."area" (
    "id" integer NOT NULL,
    "codigo" character varying(5),
    "descricao" character varying(80),
    "ativo" boolean DEFAULT true,
    "userlan" character varying(20),
    "datalan" timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "area_pkey" PRIMARY KEY ("id")
);

