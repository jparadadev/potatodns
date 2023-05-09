from inputparams.ParamDefinition import ParamDefinition

DESTINY = 'destiny'
INTERFACE = 'interface'


def _get_params_definitions() -> list[ParamDefinition]:
    return [
        ParamDefinition(DESTINY, 'dst', str, '127.0.0.1', 'Default destiny for DNS packets.'),
        ParamDefinition(INTERFACE, 'I', str, 'en0', 'Default interface to sniff.'),
    ]
