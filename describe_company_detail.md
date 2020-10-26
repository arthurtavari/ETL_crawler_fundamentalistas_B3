#### A tabela company_detail contém informações e indicadores fundamentalistas de todas as empresas listadas na bolsa de valores (B3). 

Nome | Coluna | Descrição
------------ | ------------- | ------------ 
Papel | papel | Código da Ação |
Tipo | tipo | ON = Ordinária, PN = Preferencial, PNA = Pref. tipo A
Empresa | empresa | Nome comercial da empresa
Setor | setor | Classificação setorial
Subsetor | sub_setor | Classificação por segmento de atuação
Valor de mercado | valor_de_mercado | Valor de mercado da empresa, calculado multiplicando o preço da ação pelo número total de ações
Valor da firma | valor_da_firma | Valor da firma (Enterprise Value) é calculado somando o valor de mercado da empresa a sua dívida líquida
Último balanço | ultimo_balanco | Data do último balanço divulgado pela empresa que consta no nosso banco de dados. Todos os indicadores são calculados considerando os últimos 12 meses finalizados na data deste balanço
Número de ações | numero_de_acoes | Número total de ações, somadas todas as espécies: ON, PN
Última cotação | ultima_cotacao | Data do último pregão em  que o ativo foi negociado
P/L | pl | Preço da ação dividido pelo lucro por ação. O P/L é o número de anos que se levaria para reaver o capital aplicado na compra de uma ação, através do recebimento do lucro gerado pela empresa, considerando que esses lucros permaneçam constantes
P/VP | p_vp | Preço da ação dividido pelo Valor Patrimonial por ação. Informa quanto o mercado está disposto a pagar sobre o Patrimônio Líquido da empresa
PSR | psr | Price Sales Ratio: Preço da ação dividido pela Receita Líquida por ação
Div. Yield | div_yeld | Dividend Yield: Dividendo pago por ação dividido pelo preço da ação. É o rendimento gerado para o dono da ação pelo pagamento de dividendos
P/Ativo | p_ativo | Preço da ação dividido pelos Ativos totais por ação
P/Cap. Giro | p_cap_giro | Preço da ação dividido pelo capital de giro por ação. Capital de giro é o Ativo Circulante menos Passivo Circulante
P/EBIT | p_ebit | Preço da ação dividido pelo EBIT por ação. EBIT é o Lucro antes dos Impostos e Despesas Financeiras. É uma boa aproximação do lucro operacional da empresa
P/Ativ Circ Liq | p_ativo_circ_liq | Preço da ação dividido pelos Ativos Circulantes Líquidos por ação. Ativo Circ. Líq. é obtido subtraindo os ativos circulantes pelas dívidas de curto e longo prazo, ou seja, após o pagamento de todas as dívidas, quanto sobraria dos ativos mais líquidos da empresa (caixa, estoque, etc)
EV / EBITDA | ev_ebit | Valor da Firma (Enterprise Value dividido pelo EBITDA
EV / EBITDA | ev_ebitda | Valor da Firma (Enterprise Value dividido pelo EBITDA
Marg. EBIT | mrg_ebit | EBIT dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o pagamento dos custos dos produtos/serviços vendidos, das despesas com vendas, gerais e administrativas
Marg. Líquida | mrg_liq | Lucro Líquido dividido pela Receita Líquida
Liquidez Corr | liq_corr | Ativo Circulante dividido pelo Passivo Circulante: Reflete a capacidade de pagamento da empresa no curto prazo
Roic | roic | Retorno sobre o Capital Investido: Calculado dividindo-se o EBIT por (Ativos - Fornecedores - Caixa). Informa o retorno que a empresa consegue sobre o capital total aplicadoo
Roe | roe | Retorno sobre o Patrimônio Líquido: Lucro líquido dividido pelo Patrimônio Líquido
Patrim. Líq | patrim_liq | O patrimônio líquido representa os valores que os sócios ou acionistas têm na empresa em um determinado momento. No balanço patrimonial, a diferença entre o valor dos ativos e dos passivos e resultado de exercícios futuros representa o PL (Patrimônio Líquido), que é o valor contábil devido pela pessoa jurídica aos sócios ou acionistas
Div Br/ Patrim | div_brut_patrim | Dívida Bruta total (Dívida+Debêntures) dividido pelo Patrimônio Líquido
Cres. Rec (5a) | cresc_rec_5a | Crescimento da Receita Líquida nos últimos 5 anos
