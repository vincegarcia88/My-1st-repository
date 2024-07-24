Algoritmo "semnome"
// O departamento de Educação Física deseja informatizar este setor e colocou
// à disposição os seguintes dados de 40 alunos:

// Matrícula, sexo (M,F), altura (cm) e status físico
// (1 - bom, 2 - regular, 3 - mau)

// Estes dados deverão ser lidos através de uma unidade de entrada qualquer.

// Calcular e imprimir:
// a) A quantidade de alunos do sexo feminino com altura superior a 170 cm.
// b) A % de alunos do sexo masculino (em relação ao total do sexo masculino)
// cujo status físico seja bom.

Var
// Seção de Declarações das variáveis 
    matricula, sexo, statusFisico: caractere
    altura, percMascBom: real
    i, feminino170, mascTotal, qtdeMascBom: inteiro

inicio
// Inicializa as variáveis
    i := 0
    feminino170 := 0
    mascTotal := 0
    qtdeMascBom := 0

// Estrutura de repetição
    enquanto (i < 2) faca
        escreva("Digite a matrícula do aluno: ")
        leia(matricula)
        escreva("Digite o sexo do aluno (M/F): ")
        leia(sexo)
        escreva("Digite a altura do aluno (cm): ")
        leia(altura)
        escreva("Digite o status físico do aluno ((1) Bom, (2) Regular, (3) Mau): ")
        leia(statusFisico)

// Verificar a quantidade de alunas do sexo feminino
// com altura superior a 170 cm
        se (sexo = "F") entao
            se (altura > 170) entao
                feminino170 := feminino170 + 1
            fimse
        fimse

// Alunos do sexo masculino com status físico bom
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
    escreval("Porcentagem de alunos do sexo masculino com status físico bom:",percMascBom:0:2, "%")

fimalgoritmo
