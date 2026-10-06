# Decisões de engenharia

## Escopo
Caminho mínimo em grade com implementações Python e Rust. O cenário é um benchmark sintético independente.

## Entregas atuais
A* e Dijkstra em grade com obstáculos, benchmark determinístico e execução paralela por processos; crate Rust com A* e testes unitários; CLI Rust em protocolo stdin/stdout e adapter Python para comparação.

## Evolução
bindings PyO3; benchmarks maiores e perfil de memória; aceleração não é presumida.

## Qualidade e colaboração
CI executa testes de comportamento. Revisões devem conferir contratos de entrada,
invariantes, divisão de dados e métricas. Evoluções de infraestrutura exigem avaliação
de custo, autorização e observabilidade. Não há recursos cloud provisionados.

## Limitações
Validar a hipótese com dados públicos licenciados ou dados autorizados antes de uso
operacional. Relatar baseline, várias sementes, intervalos de incerteza, consumo
de recursos e resultados negativos. O backlog não constitui funcionalidade implementada.
