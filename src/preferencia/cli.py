# preferencia/cli.py
import typer, yaml, pathlib
from preferencia.pipeline import run_full_pipeline

cli = typer.Typer(help="PreferencIA command-line interface")

@cli.command()
def run(
# um único comando – sem sub-comandos
# def main(
    config: pathlib.Path = typer.Option(
        ..., 
        exists=True, 
        help="YAML config"
    )
):
    """
    Executa todo o fluxo (pré-processamento + treino + recomendação)
    definido no arquivo de configuração.
    """
    cfg = yaml.safe_load(config.read_text())
    run_full_pipeline(cfg)

if __name__ == "__main__":
    # cli()
    
    # Typer gera automaticamente --help/-h
    typer.run(main)