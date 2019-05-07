#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors

db = pymysql.connect(
    host = 'localhost',
    user = 'user',
    password = 'password',
    db = 'sucupirafilter',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = db.cursor()

sql = 'select area_avaliacao.id as aa_id, area_avaliacao.nome as aa_nome, area_avaliacao.codigo as aa_codigo, '
sql += 'area_conhecimento.id as ac_id, area_conhecimento.nome as ac_nome, area_conhecimento.codigo as ac_codigo, '
sql += 'area_conhecimento.area_avaliacao_id as ac_area_avaliacao_id, programa.id as p_id, programa.nome as p_nome, '
sql += 'programa.codigo as p_codigo, programa.uf as p_uf, programa.area_conhecimento_id as p_area_conhecimento_id, '
sql += 'programa.instituicao_id as p_instituicao_id, instituicao.id as i_id, instituicao.nome i_nome, '
sql += 'instituicao.codigo i_codigo, instituicao.acronimo as i_acronimo, instituicao.endereco as i_endereco, '
sql += 'instituicao.distrito as i_distrito, instituicao.cidade as i_cidade, instituicao.estado as i_estado, '
sql += 'instituicao.tipo as i_tipo, instituicao.cep as i_cep, instituicao.caixa_postal as i_caixa_postal, '
sql += 'instituicao.url as i_url, instituicao.coordenandas as i_coordenandas, curso.id as c_id, curso.nome as c_nome, '
sql += 'curso.situacao as c_situacao, curso.nivel as c_nivel, curso.nota_curso as c_nota_curso, '
sql += 'curso.data_recomendacao as c_data_recomendacao, curso.data_inicio as c_data_inicio, '
sql += 'curso.programa_id as c_programa_id from curso inner join programa on curso.programa_id = programa.id '
sql += 'inner join instituicao on programa.instituicao_id = instituicao.id inner join area_conhecimento '
sql += 'on programa.area_conhecimento_id = area_conhecimento.id inner join area_avaliacao '
sql += 'on area_conhecimento.area_avaliacao_id = area_avaliacao.id'

cursor.execute(sql)
result = cursor.fetchall()

linhaTitulo = '(area_avaliacao) id;(area_avaliacao) nome;(area_avaliacao) codigo;'
linhaTitulo += '(area_conhecimento) id;(area_conhecimento) nome;(area_conhecimento) codigo;(area_conhecimento) area_avaliacao_id;'
linhaTitulo += '(programa) id;(programa) nome;(programa) codigo;(programa) uf;(programa) area_conhecimento_id;(programa) instituicao_id;'
linhaTitulo += '(instituicao) id;(instituicao) nome;(instituicao) codigo;(instituicao) acronimo;(instituicao) endereco;'
linhaTitulo += '(instituicao) distrito;(instituicao) cidade;(instituicao) estado;(instituicao) tipo;(instituicao) cep;'
linhaTitulo += '(instituicao) caixa_postal;(instituicao) url;(instituicao) coordenadas;'
linhaTitulo += '(curso) id;(curso) nome;(curso) situacao;(curso) nivel;(curso) nota_curso;(curso) data_recomendacao;'
linhaTitulo += '(curso) data_inicio;(curso) programa_id'

print(linhaTitulo)

for res in result:

    linha = ''
    linha += str(res['aa_id']) + ';'
    linha += str(res['aa_nome']) + ';'
    linha += str(res['aa_codigo']) + ';'
    linha += str(res['ac_id']) + ';'
    linha += str(res['ac_nome']) + ';'
    linha += str(res['ac_codigo']) + ';'
    linha += str(res['ac_area_avaliacao_id']) + ';'
    linha += str(res['p_id']) + ';'
    linha += str(res['p_nome']) + ';'
    linha += str(res['p_codigo']) + ';'
    linha += str(res['p_uf']) + ';'
    linha += str(res['p_area_conhecimento_id']) + ';'
    linha += str(res['p_instituicao_id']) + ';'
    linha += str(res['i_id']) + ';'
    linha += str(res['i_nome']) + ';'
    linha += str(res['i_codigo']) + ';'
    linha += str(res['i_acronimo']) + ';'
    linha += str(res['i_endereco']) + ';'
    linha += str(res['i_distrito']) + ';'
    linha += str(res['i_cidade']) + ';'
    linha += str(res['i_estado']) + ';'
    linha += str(res['i_tipo']) + ';'
    linha += str(res['i_cep']) + ';'
    linha += str(res['i_caixa_postal']) + ';'
    linha += str(res['i_url']) + ';'
    linha += str(res['i_coordenandas']) + ';'
    linha += str(res['c_id']) + ';'
    linha += str(res['c_nome']) + ';'
    linha += str(res['c_situacao']) + ';'
    linha += str(res['c_nivel']) + ';'
    linha += str(res['c_nota_curso']) + ';'
    linha += str(res['c_data_recomendacao']) + ';'
    linha += str(res['c_data_inicio']) + ';'
    linha += str(res['c_programa_id'])

    print(linha)

