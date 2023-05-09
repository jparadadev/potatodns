import argparse

from inputparams.allowed_params import get_params_definitions


def extract_params() -> dict:
    parser = argparse.ArgumentParser()
    for param in get_params_definitions():
        parser.add_argument(
            f'-{param.short_name}',
            f'--{param.name}',
            type=param.type,
            default=param.default,
            help=param.help,
        )

    params = vars(parser.parse_args())
    return params
