Algoritmo "semnome"
// O departamento de Educa��o F�sica deseja informatizar este setor e colocou
// � disposi��o os seguintes dados de 40 alunos:

// Matr�cula, sexo (M,F), altura (cm) e status f�sico
// (1 - bom, 2 - regular, 3 - mau)

// Estes dados dever�o ser lidos atrav�s de uma unidade de entrada qualquer.

// Calcular e imprimir:
// a) A quantidade de alunos do sexo feminino com altura superior a 170 cm.
// b) A % de alunos do sexo masculino (em rela��o ao total do sexo masculino)
// cujo status f�sico seja bom.

Var
// Se��o de Declara��es das vari�veis 
    matricula, sexo, statusFisico: caractere
    altura, percMascBom: real
    i, feminino170, mascTotal, qtdeMascBom: inteiro

inicio
// Inicializa as vari�veis
    i := 0
    feminino170 := 0
    mascTotal := 0
    qtdeMascBom := 0

// Estrutura de repeti��o
    enquanto (i < 2) faca
        escreva("Digite a matr�cula do aluno: ")
        leia(matricula)
        escreva("Digite o sexo do aluno (M/F): ")
        leia(sexo)
        escreva("Digite a altura do aluno (cm): ")
        leia(altura)
        escreva("Digite o status f�sico do aluno ((1) Bom, (2) Regular, (3) Mau): ")
        leia(statusFisico)

// Verificar a quantidade de alunas do sexo feminino
// com altura superior a 170 cm
        se (sexo = "F") entao
            se (altura > 170) entao
                feminino170 := feminino170 + 1
            fimse
        fimse

// Alunos do sexo masculino com status f�sico bom
        se (sexo = "M") entao
            mascTotal := mascTotal + 1
            se (statusFisico = "1") entao
                qtdeMascBom := qtdeMascBom + 1
            fimse
        fimse

        i := i + 1
    fimenquanto
    
// Porcentagem de alunos do sexo masculino com status bom
    se (mascTotal > 0) entao
        percMascBom := (qtdeMascBom / mascTotal) * 100
    senao
        percMascBom := 0
    fimse

// Exibir os resultados
    escreval("Quantidade de alunas do sexo feminino com altura superior a 170 cm:",feminino170)
    escreval("Porcentagem de alunos do sexo masculino com status f�sico bom:",percMascBom:0:2, "%")

fimalgoritmo
