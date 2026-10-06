# Busca espacial em alto desempenho

Caminho mínimo em grade com implementações Python e Rust.

**Status: MVP de pesquisa, v0.1.0.** Estudo de caso independente inspirado
em desafios dos setores relacionados à trajetória do autor (Saneamento · Indústria).
Não representa entrega contratada, resultado real ou endosso dessas organizações.
Todos os exemplos desta versão são sintéticos e reproduzíveis.

## Executar

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e .
python -m spatialsearch.demo --size 30 --seed 7
python -m unittest discover -s tests -v
```

## Implementado

A* e Dijkstra em grade com obstáculos, benchmark determinístico e execução paralela por processos; crate Rust com A* e testes unitários; CLI Rust em protocolo stdin/stdout e adapter Python para comparação.

## Próximas etapas

Bindings PyO3; benchmarks maiores e perfil de memória; aceleração não é presumida.

## Rust

```bash
cargo test --manifest-path rust/Cargo.toml
cargo build --release --manifest-path rust/Cargo.toml
python -m spatialsearch.demo --rust-binary rust/target/release/spatial-search
```

No Windows, o binário usa o sufixo `.exe`.

## Reprodutibilidade e avaliação

A demonstração grava `artifacts/report.json`, com parâmetros e métricas.
Resultados de dados sintéticos validam o fluxo; não demonstram desempenho em produção.
Use a mesma semente e orçamento computacional para comparar abordagens.
Consulte `docs/design.md` para decisões e limitações.

## Contribuição

Abra uma issue com objetivo e critério de aceite. Entregue mudanças pequenas,
revisadas e acompanhadas de testes de comportamento. Não inclua dados de clientes,
credenciais ou resultados sem proveniência. Licença MIT para código e dados sintéticos próprios.
