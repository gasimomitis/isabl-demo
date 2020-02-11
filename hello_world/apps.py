from os.path import join

from isabl_cli import AbstractApplication
from isabl_cli import options


class HelloWorldApp(AbstractApplication):

    NAME = "HELLO WORLD"
    VERSION = "1.0.0"
    SPECIES = "HUMAN"
    ASSEMBLY = "GRCh37"

    cli_options = [options.TARGETS]

    application_description = "An App to show case different Isabl functionalities."
    application_url = "https://docs.isabl.io/writing-applications"

    def get_command(self, analysis, *args):
        for experiment in analysis.targets:
            return f"echo '{experiment.sample.identifier} {experiment.technique.slug}'"

    def validate_experiments(self, targets, references):
        assert len(targets) == 1, "Only one target experiment per analysis"

