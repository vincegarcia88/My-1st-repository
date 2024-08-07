<mxfile host="app.diagrams.net" modified="2024-07-15T09:17:17.717Z" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" etag="KyDsvYCB9W4LO9FRudtL" version="24.6.4" type="github">
  <diagram name="Página-1" id="Kp1El3cVsVaoHsX5JYvA">
    <mxGraphModel dx="794" dy="454" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="hrsnVplvnM6waeOL_aCX-1" value="Exercício Prático n.º 1 – Base de Dados Empresa Importação&lt;div&gt;&amp;nbsp; &lt;br&gt;Uma empresa de importação efectua as suas compras através de contratos. &lt;br&gt;Cada contrato (identificado por um número) é assinado com um dado fornecedor e diz respeito a &lt;br&gt;várias mercadorias (identificadas por um código e com um nome). Do contrato consta também a &lt;br&gt;data da assinatura, o prazo de validade, a moeda e o valor. É fixado no contrato o preço unitário &lt;br&gt;de compra de cada mercadoria, a quantidade comprada especificada numa unidade de medida &lt;br&gt;que é sempre a mesma para cada mercadoria independentemente do contrato.&lt;div&gt;&lt;br&gt;&lt;/div&gt;&lt;div&gt;&amp;nbsp; &lt;br&gt;É necessário manter informação sobre os fornecedores (nome, endereço, telefone e fax) que são &lt;br&gt;identificados por um código. As mercadorias envolvidas num contrato são todas enviadas num &lt;br&gt;único transporte (identificado por um número). Para cada transporte é necessário conhecer o tipo &lt;br&gt;de transporte, a data de partida e a data de chegada.&lt;/div&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;&lt;div&gt;&amp;nbsp; &lt;br&gt;1. Faça o Modelo ER para o problema apresentado &lt;br&gt;2. Faça o Diagrama ER do Modelo criado na pergunta anterior &lt;br&gt;3. Converta o Modelo ER para o Modelo Relacional &lt;br&gt;4. Crie o Diagrama de Modelo Relacional&lt;/div&gt;&lt;/div&gt;" style="text;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="20" width="730" height="290" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-3" value="Endereço" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="70" y="390" width="180" height="210" as="geometry">
            <mxRectangle x="70" y="390" width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-4" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-3">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-5" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-4">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-6" value="IdEndereço" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-4">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-7" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-3">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-8" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-7">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-9" value="Rua" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-7">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-10" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-3">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-11" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-10">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-12" value="NumeroPorta" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-10">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-13" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-3">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-14" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-13">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-15" value="CodigoPostal" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-13">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-33" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-3">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-34" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-33">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-35" value="Cidade" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-33">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-36" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-3">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-37" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-36">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-38" value="&lt;u&gt;CódigoFornecedor&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-36">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-19" value="Transporte&lt;span style=&quot;white-space: pre;&quot;&gt;&#x9;&lt;/span&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="324" y="410" width="180" height="150" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-20" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-19">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-21" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-20">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-22" value="IdTransporte&lt;span style=&quot;white-space: pre;&quot;&gt;&#x9;&lt;/span&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-20">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-23" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-19">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-24" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-23">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-25" value="TipoTransporte" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-23">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-26" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-19">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-27" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-26">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-28" value="DataPartidaTransporte" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-26">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-29" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-19">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-30" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-29">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-31" value="DataChegadaTransporte" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-29">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-39" value="Mercadoria" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="410" width="180" height="210" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-40" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-39">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-41" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-40">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-42" value="CódigoMercadoria" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-40">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-43" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-39">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-44" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-43">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-45" value="NomeMercadoria" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-43">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-46" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-39">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-47" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-46">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-48" value="UnidadeMedida" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-46">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-49" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-39">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-50" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-49">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-51" value="PreçoUnitário" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-49">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-55" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-39">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-56" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-55">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-57" value="&lt;u&gt;IdTransporte&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-55">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-58" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-39">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-59" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-58">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-60" value="&lt;u&gt;CódigoFornecedor&lt;span style=&quot;white-space: pre;&quot;&gt;&#x9;&lt;/span&gt;&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-58">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-61" value="Fornecedor" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="340" y="690" width="180" height="90" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-62" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-61">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-63" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-62">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-64" value="CódigoFornecedor" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-62">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-65" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-61">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-66" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-65">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-67" value="Nome" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-65">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-74" value="Telefones" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="70" y="690" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-75" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-74">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-76" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-75">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-77" value="IdTelefone" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-75">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-78" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-74">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-79" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-78">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-80" value="Telefone" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-78">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-81" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-74">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-82" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-81">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-83" value="&lt;u&gt;CódigoFornecedor&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-81">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-87" value="QuantidadesMercadoriaContrato" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="590" y="820" width="200" height="120" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-88" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-87">
          <mxGeometry y="30" width="200" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-89" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-88">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-90" value="QuantidadesContrato" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-88">
          <mxGeometry x="30" width="170" height="30" as="geometry">
            <mxRectangle width="170" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-91" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-87">
          <mxGeometry y="60" width="200" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-92" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-91">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-93" value="&lt;u&gt;NúmeroContrato&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-91">
          <mxGeometry x="30" width="170" height="30" as="geometry">
            <mxRectangle width="170" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-94" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-87">
          <mxGeometry y="90" width="200" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-95" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-94">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-96" value="&lt;u&gt;CódigoMercadoria&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-94">
          <mxGeometry x="30" width="170" height="30" as="geometry">
            <mxRectangle width="170" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-100" value="Contrato" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="340" y="900" width="180" height="210" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-101" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-100">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-102" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-101">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-103" value="NúmeroContrato" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-101">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-104" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-100">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-105" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-104">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-106" value="MoedaContrato" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-104">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-107" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-100">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-108" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-107">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-109" value="Valor" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-107">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-110" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-100">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-111" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-110">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-112" value="DataContrato" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-110">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-113" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-100">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-114" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-113">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-115" value="ValidadeContrato" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-113">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-116" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-100">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-117" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-116">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-118" value="&lt;u&gt;CódigoFornecedor&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-116">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-119" value="Fax" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="860" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-120" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-119">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-121" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-120">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-122" value="Id_Fax" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-120">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-123" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-119">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-124" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-123">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-125" value="Fax" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-123">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-126" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-119">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-127" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-126">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-128" value="&lt;u&gt;CódigoFornecedor&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" vertex="1" parent="hrsnVplvnM6waeOL_aCX-126">
          <mxGeometry x="30" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-132" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToMany;endFill=1;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" target="hrsnVplvnM6waeOL_aCX-62">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="260" y="960" as="sourcePoint" />
            <mxPoint x="360" y="860" as="targetPoint" />
            <Array as="points">
              <mxPoint x="240" y="950" />
              <mxPoint x="240" y="860" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-133" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToMany;endFill=1;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" target="hrsnVplvnM6waeOL_aCX-62">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="250" y="800" as="sourcePoint" />
            <mxPoint x="350" y="700" as="targetPoint" />
            <Array as="points">
              <mxPoint x="340" y="710" />
              <mxPoint x="330" y="720" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-135" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToMany;endFill=1;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" target="hrsnVplvnM6waeOL_aCX-62">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="250" y="585" as="sourcePoint" />
            <mxPoint x="330" y="610" as="targetPoint" />
            <Array as="points">
              <mxPoint x="160" y="515" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-139" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToMany;endFill=1;rounded=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;elbow=vertical;" edge="1" parent="1" target="hrsnVplvnM6waeOL_aCX-40">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="790" y="920" as="sourcePoint" />
            <mxPoint x="810" y="450" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-140" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToMany;endFill=1;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" target="hrsnVplvnM6waeOL_aCX-58">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="520" y="740" as="sourcePoint" />
            <mxPoint x="620" y="640" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-142" value="" style="edgeStyle=orthogonalEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToMany;endFill=1;rounded=0;elbow=vertical;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="hrsnVplvnM6waeOL_aCX-55" target="hrsnVplvnM6waeOL_aCX-20">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="730" y="630" as="sourcePoint" />
            <mxPoint x="830" y="530" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-145" value="1" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeWidth=2;fontFamily=Tahoma;spacingBottom=4;spacingRight=2;strokeColor=#d3d3d3;" vertex="1" parent="1">
          <mxGeometry x="310" y="700" width="20" height="20" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-148" value="1" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeWidth=2;fontFamily=Tahoma;spacingBottom=4;spacingRight=2;strokeColor=#d3d3d3;" vertex="1" parent="1">
          <mxGeometry x="530" y="700" width="20" height="20" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-152" value="1" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeWidth=2;fontFamily=Tahoma;spacingBottom=4;spacingRight=2;strokeColor=#d3d3d3;" vertex="1" parent="1">
          <mxGeometry x="530" y="940" width="20" height="20" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-155" value="1" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeWidth=2;fontFamily=Tahoma;spacingBottom=4;spacingRight=2;strokeColor=#d3d3d3;" vertex="1" parent="1">
          <mxGeometry x="510" y="430" width="20" height="20" as="geometry" />
        </mxCell>
        <mxCell id="hrsnVplvnM6waeOL_aCX-156" value="1" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeWidth=2;fontFamily=Tahoma;spacingBottom=4;spacingRight=2;strokeColor=#d3d3d3;" vertex="1" parent="1">
          <mxGeometry x="770" y="430" width="20" height="20" as="geometry" />
        </mxCell>
        <UserObject label="N" placeholders="1" name="Variable" id="hrsnVplvnM6waeOL_aCX-158">
          <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" vertex="1" parent="1">
            <mxGeometry x="220" y="560" width="80" height="20" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="N" placeholders="1" name="Variable" id="hrsnVplvnM6waeOL_aCX-159">
          <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" vertex="1" parent="1">
            <mxGeometry x="290" y="1080" width="80" height="20" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="N" placeholders="1" name="Variable" id="hrsnVplvnM6waeOL_aCX-160">
          <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" vertex="1" parent="1">
            <mxGeometry x="230" y="940" width="80" height="20" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="N" placeholders="1" name="Variable" id="hrsnVplvnM6waeOL_aCX-161">
          <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" vertex="1" parent="1">
            <mxGeometry x="540" y="850" width="80" height="20" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="N" placeholders="1" name="Variable" id="hrsnVplvnM6waeOL_aCX-162">
          <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" vertex="1" parent="1">
            <mxGeometry x="760" y="880" width="80" height="20" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="N" placeholders="1" name="Variable" id="hrsnVplvnM6waeOL_aCX-163">
          <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" vertex="1" parent="1">
            <mxGeometry x="220" y="780" width="80" height="20" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="N" placeholders="1" name="Variable" id="hrsnVplvnM6waeOL_aCX-164">
          <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" vertex="1" parent="1">
            <mxGeometry x="530" y="610" width="80" height="20" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="N" placeholders="1" name="Variable" id="hrsnVplvnM6waeOL_aCX-165">
          <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" vertex="1" parent="1">
            <mxGeometry x="530" y="560" width="80" height="20" as="geometry" />
          </mxCell>
        </UserObject>
        <mxCell id="hrsnVplvnM6waeOL_aCX-167" value="" style="fontSize=12;html=1;endArrow=ERzeroToMany;endFill=1;rounded=0;edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="340" y="1097" as="sourcePoint" />
            <mxPoint x="340" y="730" as="targetPoint" />
            <Array as="points">
              <mxPoint x="330" y="1097" />
              <mxPoint x="330" y="730" />
            </Array>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>